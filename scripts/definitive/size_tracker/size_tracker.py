#!/usr/bin/env python3
"""size_tracker.py: per-retailer, per-size stock and price for a list of Nike/Jordan style codes.

Usage:
  python3 -I size_tracker.py --input shoes.csv --out OUTDIR [--retailers nike,footlocker,champs,finishline]
      [--raw RAWDIR] [--asof YYYY-MM-DD] [--delay 2.5]

Input CSV columns (header required): style_code,name,release_date,retail_usd,gender,group
  style_code  e.g. IQ5495-005 (required)
  gender      men | women (selects the size grid; default men)
  group       free label, e.g. jordan_retro / control

Outputs (appended with a run timestamp, so repeat runs build a time series):
  OUTDIR/size_rows.csv     one row per retailer x style x size
  OUTDIR/size_summary.csv  one row per retailer x style with DERIVED metrics
  OUTDIR/fetch_log.jsonl   every request (url, status, utc time, raw file)

Sources (public pages only, no login):
  nike        https://api.nike.com/product_feed/threads/v3/?filter=marketplace(US)&filter=language(en)
              &filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.styleColor(<code>)
              skus[] map gtin -> nikeSize; availableGtins[] gives available + level (HIGH/MEDIUM/LOW/OOS).
              A size is counted in stock only when merchProduct.status == ACTIVE: on 2026-10-13 INACTIVE products
              (for example IR0914-400, HV0823-101) returned HTTP 404 on nike.com while their gtins still showed HIGH.
              A commerceStartDate in the future also means not buyable yet (CK9246-200 showed "Coming Soon").
  footlocker  https://www.footlocker.com/product/~/<flsku>.html  (flsku = style code without dash, first char dropped)
              embedded "sizes":[...] with inventory.inventoryAvailable and price.salePrice/listPrice.
              Falls back to https://www.footlocker.com/search?query=<code> to discover the sku.
  champs      same platform and URL scheme on www.champssports.com
  finishline  https://www.finishline.com/ (JD Sports US). Blocked by the site's bot wall on 2026-10-13
              (HTTP 403 "Your Access Has Been Denied"); kept so a future run records the status.
Foot Locker and Champs return 403 to python requests, so every retailer fetch uses curl.
"""
import argparse, csv, datetime as dt, hashlib, json, os, re, subprocess, sys, time, urllib.parse

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
NIKE_CHANNEL = "d9a5bc42-4b9c-4976-858a-f159cf99c647"  # Nike.com
GRID = {"men": [x / 2 for x in range(14, 27)],          # 7.0 .. 13.0 = 13 sizes
        "women": [x / 2 for x in range(12, 23)]}        # 6.0 .. 11.0 = 11 sizes
CORE = {"men": [9.0, 9.5, 10.0, 10.5, 11.0], "women": [7.5, 8.0, 8.5, 9.0]}

_last = {}


def fetch(url, rawdir, log, delay, accept="text/html,application/json;q=0.9,*/*;q=0.8", extra=None):
    host = urllib.parse.urlparse(url).netloc
    w = _last.get(host, 0) + delay - time.time()
    if w > 0:
        time.sleep(w)
    os.makedirs(rawdir, exist_ok=True)
    fn = os.path.join(rawdir, hashlib.sha1((url + str(time.time())).encode()).hexdigest()[:16] + ".raw")
    cmd = ["curl", "-s", "-L", "--compressed", "--max-time", "90", "-A", UA,
           "-H", "Accept-Language: en-US,en;q=0.9", "-H", "Accept: " + accept, "-o", fn, "-w", "%{http_code}"]
    for h in (extra or []):
        cmd += ["-H", h]
    cmd.append(url)
    try:
        st = int(subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout.strip() or 0)
    except Exception:
        st = 0
    _last[host] = time.time()
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log.write(json.dumps({"utc": ts, "url": url, "status": st, "file": fn}) + "\n"); log.flush()
    body = open(fn, encoding="utf-8", errors="ignore").read() if os.path.exists(fn) else ""
    return st, body, ts


def fnum(s):
    m = re.search(r"\d+(\.\d+)?", str(s))
    return float(m.group(0)) if m else None


# ---------------- Nike ----------------
def nike(code, rawdir, log, delay):
    url = ("https://api.nike.com/product_feed/threads/v3/?filter=marketplace(US)&filter=language(en)"
           f"&filter=channelId({NIKE_CHANNEL})&filter=productInfo.merchProduct.styleColor({code})")
    st, body, ts = fetch(url, rawdir, log, delay, accept="application/json",
                         extra=["nike-api-caller-id: com.nike.commerce.nikedotcom.web"])
    res = {"url": url, "status": st, "utc": ts, "listed": False, "sizes": [], "price": None, "full": None, "pdp": ""}
    if st != 200:
        return res
    try:
        d = json.loads(body)
    except Exception:
        return res
    for o in d.get("objects", []):
        for pi in o.get("productInfo", []):
            mp = pi.get("merchProduct", {})
            if mp.get("styleColor") != code:
                continue
            res["listed"] = True
            res["status_nike"] = mp.get("status")
            res["start"] = (mp.get("commerceStartDate") or "")[:10]
            res["price"] = pi.get("merchPrice", {}).get("currentPrice")
            res["full"] = pi.get("merchPrice", {}).get("fullPrice")
            slug = pi.get("productContent", {}).get("slug", "")
            res["pdp"] = f"https://www.nike.com/t/{slug}/{code}" if slug else ""
            avail = {g["gtin"]: g for g in pi.get("availableGtins", [])}
            for s in pi.get("skus", []):
                g = avail.get(s.get("gtin"), {})
                loc = (s.get("countrySpecifications") or [{}])[0].get("localizedSize", "")
                res["sizes"].append({"size_label": s.get("nikeSize"), "localized": loc,
                                     # a size counts only if the product is for sale on nike.com (merch status ACTIVE;
                                     # INACTIVE/HOLD products return 404 on the PDP even when gtin levels are HIGH)
                                     "in_stock": bool(g.get("available")) and g.get("level") != "OOS" and mp.get("status") == "ACTIVE"
                                                 and (mp.get("commerceStartDate") or "") <= dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
                                     "level": g.get("level", "NOT_LISTED"), "price": res["price"]})
            return res
    return res


# ---------------- Foot Locker / Champs ----------------
FL_HOST = {"footlocker": "https://www.footlocker.com", "champs": "https://www.champssports.com"}


def fl_sizes(body, sku):
    dec = json.JSONDecoder()
    for m in re.finditer(r'"sizes":\[', body):
        try:
            arr, _ = dec.raw_decode(body[m.end() - 1:])
        except Exception:
            continue
        if arr and isinstance(arr[0], dict) and "inventory" in arr[0] and str(arr[0].get("id", "")).startswith(sku + "_"):
            return arr
    return None


def footlocker(code, retailer, rawdir, log, delay):
    base = FL_HOST[retailer]
    sku = code.replace("-", "")[1:]
    url = f"{base}/product/~/{sku}.html"
    st, body, ts = fetch(url, rawdir, log, delay)
    arr = fl_sizes(body, sku) if st == 200 else None
    if arr is None and st == 200:  # sku rule failed: discover via search
        surl = f"{base}/search?query={urllib.parse.quote(code)}"
        st2, sbody, _ = fetch(surl, rawdir, log, delay)
        cands = set(re.findall(r'"sku":"([A-Z0-9]{6,12})"', sbody))
        tail = code.replace("-", "")
        hit = [c for c in cands if tail.endswith(c) or c.endswith(tail[-8:])]
        if hit:
            sku = hit[0]
            url = f"{base}/product/~/{sku}.html"
            st, body, ts = fetch(url, rawdir, log, delay)
            arr = fl_sizes(body, sku) if st == 200 else None
    res = {"url": url, "status": st, "utc": ts, "listed": arr is not None, "sizes": [], "price": None, "full": None}
    if st == 403 or "Access Denied" in body[:3000]:
        res["blocked"] = True
    for s in arr or []:
        inv = s.get("inventory") or {}
        pr = s.get("price") or {}
        res["sizes"].append({"size_label": s.get("size"), "localized": s.get("dualSize", ""),
                             "in_stock": bool(inv.get("inventoryAvailable")) and bool(s.get("active")),
                             "level": "", "price": pr.get("salePrice")})
        if pr.get("salePrice") is not None:
            res["price"] = pr.get("salePrice") if res["price"] is None else min(res["price"], pr.get("salePrice"))
            res["full"] = pr.get("listPrice")
    return res


def finishline(code, rawdir, log, delay):
    url = f"https://www.finishline.com/search?q={urllib.parse.quote(code)}"
    st, body, ts = fetch(url, rawdir, log, delay)
    return {"url": url, "status": st, "utc": ts, "listed": False, "sizes": [], "price": None, "full": None,
            "blocked": st == 403 or "Access Has Been Denied" in body}


# ---------------- metrics ----------------
def men_size(lbl, loc, gender):
    """numeric size on the shoe's own grid (men's US for men/unisex, women's US for women)."""
    if gender == "women":
        m = re.search(r"W\s*(\d+(\.\d+)?)", loc or "")
        if m:
            return float(m.group(1))
    else:
        m = re.search(r"M\s*(\d+(\.\d+)?)", loc or "")
        if m:
            return float(m.group(1))
    return fnum(lbl)


def summarize(r, shoe, retailer, asof):
    g = shoe.get("gender") or "men"
    grid, core = GRID.get(g, GRID["men"]), CORE.get(g, CORE["men"])
    stock = {}
    for s in r["sizes"]:
        v = men_size(s["size_label"], s["localized"], g)
        if v is not None:
            stock[v] = stock.get(v, False) or s["in_stock"]
    n_in = sum(1 for x in grid if stock.get(x))
    core_in = sum(1 for x in core if stock.get(x))
    retail = fnum(shoe.get("retail_usd")) or (float(r["full"]) if r.get("full") else None)
    try:
        days = (dt.date.fromisoformat(asof) - dt.date.fromisoformat(shoe.get("release_date") or r.get("start"))).days
    except Exception:
        days = ""
    instock_prices = [s["price"] for s in r["sizes"] if s["in_stock"] and s["price"] is not None]
    price = min(instock_prices) if instock_prices else r.get("price")
    return {
        "asof": asof, "retailer": retailer, "style_code": shoe["style_code"], "name": shoe.get("name", ""),
        "group": shoe.get("group", ""), "gender_grid": g, "release_date": shoe.get("release_date", ""),
        "days_since_release_DERIVED": days, "http_status": r["status"],
        "blocked": r.get("blocked", False), "listed": r["listed"],
        "sizes_listed_total": len(r["sizes"]), "sizes_in_stock_total": sum(1 for s in r["sizes"] if s["in_stock"]),
        "grid_sizes": len(grid), "grid_in_stock": n_in if r["listed"] else "",
        "share_grid_in_stock_DERIVED": round(n_in / len(grid), 3) if r["listed"] else "",
        "core_in_stock": f"{core_in}/{len(core)}" if r["listed"] else "",
        "core_all_available_DERIVED": (core_in == len(core)) if r["listed"] else "",
        "in_stock_grid_sizes": " ".join(f"{x:g}" for x in grid if stock.get(x)) if r["listed"] else "",
        "price_low_in_stock": price, "retailer_full_price": r.get("full"), "retail_usd": retail,
        "price_vs_retail_DERIVED": round(price / retail - 1, 3) if (price and retail and r["listed"]) else "",
        "nike_commerce_start": r.get("start", ""), "nike_merch_status": r.get("status_nike", ""),
        "nike_feed_sizes_with_stock_any_status": sum(1 for s in r["sizes"] if s["level"] not in ("OOS", "NOT_LISTED", "")),
        "url": r.get("pdp") or r["url"], "fetched_utc": r["utc"],
        "label": "VERIFIED (retailer page/JSON opened); metrics DERIVED" if r["listed"] else
                 ("BLOCKED" if r.get("blocked") else "NOT LISTED / NOT FOUND (page opened)"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--raw", default=None)
    ap.add_argument("--retailers", default="nike,footlocker,champs")
    ap.add_argument("--asof", default=dt.date.today().isoformat())
    ap.add_argument("--delay", type=float, default=2.5)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    raw = a.raw or os.path.join(a.out, "raw")
    shoes = [r for r in csv.DictReader(open(a.input)) if r.get("style_code")]
    log = open(os.path.join(a.out, "fetch_log.jsonl"), "a")
    rows_p, sum_p = os.path.join(a.out, "size_rows.csv"), os.path.join(a.out, "size_summary.csv")
    rw = sw = None
    rf = open(rows_p, "a", newline=""); sf = open(sum_p, "a", newline="")
    new_r, new_s = os.path.getsize(rows_p) == 0, os.path.getsize(sum_p) == 0
    rets = a.retailers.split(",")
    fl_block = False
    for i, shoe in enumerate(shoes):
        code = shoe["style_code"].strip().upper()
        shoe["style_code"] = code
        for ret in rets:
            if ret == "nike":
                r = nike(code, os.path.join(raw, "nike"), log, a.delay)
            elif ret in FL_HOST:
                r = footlocker(code, ret, os.path.join(raw, ret), log, a.delay)
            elif ret == "finishline":
                if fl_block:
                    continue
                r = finishline(code, os.path.join(raw, "finishline"), log, a.delay)
                fl_block = r.get("blocked", False)  # stop hammering a bot wall after the first refusal
            else:
                continue
            for s in r["sizes"]:
                row = {"asof": a.asof, "fetched_utc": r["utc"], "retailer": ret, "style_code": code,
                       "size_label": s["size_label"], "localized_size": s["localized"], "in_stock": s["in_stock"],
                       "nike_level": s["level"], "price": s["price"], "url": r.get("pdp") or r["url"]}
                if rw is None:
                    rw = csv.DictWriter(rf, fieldnames=list(row))
                    if new_r: rw.writeheader()
                rw.writerow(row)
            srow = summarize(r, shoe, ret, a.asof)
            if sw is None:
                sw = csv.DictWriter(sf, fieldnames=list(srow))
                if new_s: sw.writeheader()
            sw.writerow(srow); sf.flush(); rf.flush()
            print(f"[{i+1}/{len(shoes)}] {ret:10s} {code} st={r['status']} listed={r['listed']} "
                  f"grid={srow['grid_in_stock']}/{srow['grid_sizes']} core={srow['core_in_stock']} price={srow['price_low_in_stock']}",
                  flush=True)


if __name__ == "__main__":
    main()
