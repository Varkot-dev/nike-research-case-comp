"""Retry Wayback fetches that failed (http 000) in fl_history_summary.csv; writes fl_history_summary_final.csv.
usage: python3 -I fl_history_retry.py <fl_history_dir> <input_csv>"""
import csv, os, sys, time, datetime as dt, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import size_tracker as T
d, inp = sys.argv[1], sys.argv[2]
shoes = {r["style_code"]: r for r in csv.DictReader(open(inp))}
for r in csv.DictReader(open(os.path.join(os.path.dirname(inp), "hist_input.csv"))):
    shoes.setdefault(r["style_code"], r)
rows = list(csv.DictReader(open(os.path.join(d, "fl_history_summary.csv"))))
out = []
for row in rows:
    if row["http_status"] == "200":
        out.append(row); continue
    code = row["style_code"]; sku = code.replace("-", "")[1:]
    fn = os.path.join(d, "raw", f"{sku}_{row['capture_ts_requested']}.html")
    st = "000"
    for a in range(3):
        time.sleep(8)
        p = subprocess.run(["curl", "-s", "-L", "--compressed", "--max-time", "60", "-A", T.UA, "-o", fn, "-w", "%{http_code} %{url_effective}", row["url"]],
                           capture_output=True, text=True)
        st, eff = (p.stdout.split(" ", 1) + [""])[:2]
        if st == "200":
            break
    body = open(fn, encoding="utf-8", errors="ignore").read() if os.path.exists(fn) else ""
    arr = T.fl_sizes(body, sku) if st == "200" else None
    served = eff.split("/web/")[1].split("id_")[0] if "/web/" in eff else row["capture_ts_requested"]
    r = {"url": row["url"], "status": st, "utc": served, "listed": arr is not None, "sizes": [], "price": None, "full": None}
    for z in arr or []:
        inv = z.get("inventory") or {}; pr = z.get("price") or {}
        r["sizes"].append({"size_label": z.get("size"), "localized": z.get("dualSize", ""),
                           "in_stock": bool(inv.get("inventoryAvailable")) and bool(z.get("active")), "level": "", "price": pr.get("salePrice")})
        if pr.get("listPrice") is not None: r["full"] = pr.get("listPrice")
    sd = dt.datetime.strptime(served[:8], "%Y%m%d").date().isoformat()
    s = T.summarize(r, dict(shoes[code], style_code=code), "footlocker_wayback", sd)
    new = {"window": row["window"], "capture_ts_requested": row["capture_ts_requested"], "capture_ts_served": served,
           "capture_http": row["capture_http"], **s,
           "label": "VERIFIED (Wayback capture of retailer page opened); metrics DERIVED" if arr else "capture fetch failed or no size data"}
    out.append({k: new.get(k, "") for k in rows[0].keys()})
    print(code, row["window"], st, s["grid_in_stock"], s["core_in_stock"], s["price_low_in_stock"], flush=True)
w = csv.DictWriter(open(os.path.join(d, "fl_history_summary_final.csv"), "w", newline=""), fieldnames=list(rows[0].keys()))
w.writeheader(); w.writerows(out)
