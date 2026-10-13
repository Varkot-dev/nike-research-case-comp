#!/usr/bin/env python3
"""fl_history.py: Foot Locker size runs from Wayback captures at about 30 and 90 days after release.

usage: python3 -I fl_history.py --input shoes.csv --out OUTDIR [--host footlocker.com]
Input columns: style_code,name,release_date,retail_usd,gender
For each style: CDX lookup of https://www.footlocker.com/product/~/<flsku>.html (flsku = style code without dash,
first char dropped), then the capture closest to release+30 d (window 18 to 50 d) and release+90 d (window 65 to 130 d).
Captures with HTTP 302 are followed (Wayback serves the redirect target's nearest capture); the capture actually served
is recorded. Parsing reuses size_tracker.fl_sizes / summarize. Polite: 7 s between web.archive.org requests.
"""
import argparse, csv, datetime as dt, json, os, subprocess, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import size_tracker as T

UA = T.UA
WIN = {"d30": (18, 50, 30), "d90": (65, 130, 90)}
_last = [0.0]


def curl(url, out=None, maxt=90):
    w = _last[0] + 7 - time.time()
    if w > 0:
        time.sleep(w)
    cmd = ["curl", "-s", "-L", "--compressed", "--max-time", str(maxt), "-A", UA, "-w", "%{http_code} %{url_effective}"]
    if out:
        cmd += ["-o", out]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=maxt + 30)
    _last[0] = time.time()
    if out:
        st, eff = (p.stdout.split(" ", 1) + [""])[:2]
        return st, eff, None
    body, tail = p.stdout[:-60], p.stdout
    i = p.stdout.rfind(" http")
    j = p.stdout[:i].rfind("\n") if i > 0 else -1
    return None, None, p.stdout


def cdx(host, sku):
    q = urllib.parse.urlencode({"url": f"{host}/product/~/{sku}.html", "output": "json", "from": "2024", "to": "2026",
                                "limit": "500"})
    for a in range(2):
        _, _, out = curl("https://web.archive.org/cdx/search/cdx?" + q, maxt=40)
        txt = out.rsplit("]", 1)[0] + "]" if "]" in out else ""
        try:
            j = json.loads(txt) if txt.strip() else []
            return [dict(zip(j[0], r)) for r in j[1:]] if j else []
        except Exception:
            time.sleep(15)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--host", default="footlocker.com")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True); raw = os.path.join(a.out, "raw"); os.makedirs(raw, exist_ok=True)
    shoes = list(csv.DictReader(open(a.input)))
    sp = os.path.join(a.out, "fl_history_summary.csv"); new = not os.path.exists(sp)
    sf = open(sp, "a", newline=""); sw = None
    lg = open(os.path.join(a.out, "fl_history_log.jsonl"), "a")
    for i, s in enumerate(shoes):
        code = s["style_code"].strip().upper(); sku = code.replace("-", "")[1:]
        rel = dt.date.fromisoformat(s["release_date"])
        caps = cdx(a.host, sku)
        lg.write(json.dumps({"style_code": code, "sku": sku, "cdx_n": None if caps is None else len(caps)}) + "\n"); lg.flush()
        print(f"[{i+1}/{len(shoes)}] {code} cdx={None if caps is None else len(caps)}", flush=True)
        if not caps:
            continue
        for tag, (lo, hi, tgt) in WIN.items():
            best = None
            for c in caps:
                if c.get("statuscode") not in ("200", "302"):
                    continue
                d = (dt.datetime.strptime(c["timestamp"][:8], "%Y%m%d").date() - rel).days
                if lo <= d <= hi and (best is None or abs(d - tgt) < abs(best[0] - tgt)):
                    best = (d, c)
            if not best:
                continue
            d, c = best
            fn = os.path.join(raw, f"{sku}_{c['timestamp']}.html")
            url = f"https://web.archive.org/web/{c['timestamp']}id_/{c['original']}"
            st, eff, _ = curl(url, out=fn)
            body = open(fn, encoding="utf-8", errors="ignore").read() if os.path.exists(fn) else ""
            arr = T.fl_sizes(body, sku) if st == "200" else None
            served_ts = eff.split("/web/")[1].split("id_")[0] if "/web/" in (eff or "") else c["timestamp"]
            r = {"url": url, "status": st, "utc": served_ts, "listed": arr is not None, "sizes": [], "price": None, "full": None}
            for z in arr or []:
                inv = z.get("inventory") or {}; pr = z.get("price") or {}
                r["sizes"].append({"size_label": z.get("size"), "localized": z.get("dualSize", ""),
                                   "in_stock": bool(inv.get("inventoryAvailable")) and bool(z.get("active")),
                                   "level": "", "price": pr.get("salePrice")})
                if pr.get("listPrice") is not None:
                    r["full"] = pr.get("listPrice")
            served_date = dt.datetime.strptime(served_ts[:8], "%Y%m%d").date().isoformat()
            row = T.summarize(r, dict(s, style_code=code), "footlocker_wayback", served_date)
            row = {"window": tag, "capture_ts_requested": c["timestamp"], "capture_ts_served": served_ts,
                   "capture_http": c.get("statuscode"), **row,
                   "label": "VERIFIED (Wayback capture of retailer page opened); metrics DERIVED" if arr else "capture has no size data"}
            if sw is None:
                sw = csv.DictWriter(sf, fieldnames=list(row))
                if new: sw.writeheader()
            sw.writerow(row); sf.flush()
            print(f"    {tag} d={row['days_since_release_DERIVED']} st={st} grid={row['grid_in_stock']}/13 core={row['core_in_stock']} price={row['price_low_in_stock']}", flush=True)


if __name__ == "__main__":
    main()
