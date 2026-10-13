"""Combine 2026-10-13 runs into one per-shoe table (DERIVED). usage: python3 -I analyze.py <sizes_dir>"""
import csv, sys, os, statistics as S
d = sys.argv[1]
fl = [r for r in csv.DictReader(open(os.path.join(d, "data/run_20261013/size_summary.csv"))) if r["retailer"] in ("footlocker", "champs")]
nk = list(csv.DictReader(open(os.path.join(d, "data/run_20261013_nike_v2/size_summary.csv"))))
for r in nk:  # same rule as the patched tracker: future commerce start = not buyable yet
    if r["nike_commerce_start"] and r["nike_commerce_start"] > r["asof"] and r["listed"] == "True":
        r.update(grid_in_stock="0", share_grid_in_stock_DERIVED="0.0", core_in_stock="0/" + r["core_in_stock"].split("/")[-1],
                 core_all_available_DERIVED="False", in_stock_grid_sizes="", price_vs_retail_DERIVED="",
                 label=r["label"] + "; commerceStartDate in future, not buyable")
allr = nk + fl
out = os.path.join(d, "data/size_runs_combined_20261013.csv")
keys = list(nk[0].keys())
w = csv.DictWriter(open(out, "w", newline=""), fieldnames=keys, extrasaction="ignore"); w.writeheader(); w.writerows(allr)
by = {}
for r in allr:
    by.setdefault(r["style_code"], {})[r["retailer"]] = r
rows = []
for code, m in by.items():
    base = m.get("nike") or next(iter(m.values()))
    def g(ret, k):
        x = m.get(ret)
        return x[k] if x and x["listed"] == "True" else ""
    best = max([float(g(x, "share_grid_in_stock_DERIVED")) for x in ("nike", "footlocker", "champs") if g(x, "share_grid_in_stock_DERIVED") != ""] or [-1])
    disc = [float(g(x, "price_vs_retail_DERIVED")) for x in ("nike", "footlocker", "champs") if g(x, "price_vs_retail_DERIVED") not in ("",)]
    rows.append(dict(style_code=code, name=base["name"], group=base["group"], gender=base["gender_grid"], release=base["release_date"],
                     days=base["days_since_release_DERIVED"], nike_status=m.get("nike", {}).get("nike_merch_status", ""),
                     nike_start=m.get("nike", {}).get("nike_commerce_start", ""),
                     nike_share=g("nike", "share_grid_in_stock_DERIVED"), nike_core=g("nike", "core_in_stock"),
                     fl_share=g("footlocker", "share_grid_in_stock_DERIVED"), fl_core=g("footlocker", "core_in_stock"),
                     fl_price_vs_retail=g("footlocker", "price_vs_retail_DERIVED"),
                     ch_share=g("champs", "share_grid_in_stock_DERIVED"), ch_core=g("champs", "core_in_stock"),
                     ch_price_vs_retail=g("champs", "price_vs_retail_DERIVED"),
                     max_share_any_retailer_DERIVED=best if best >= 0 else "",
                     min_price_vs_retail_any_DERIVED=min(disc) if disc else "",
                     retail=base["retail_usd"]))
rows.sort(key=lambda r: (r["group"], r["release"]))
o2 = os.path.join(d, "data/size_runs_per_shoe_20261013.csv")
w = csv.DictWriter(open(o2, "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows:
    print(r["group"][:4], r["release"], str(r["days"]).rjust(4), r["style_code"], r["name"][:34].ljust(34), r["nike_status"][:4],
          "N", r["nike_share"] or "-", r["nike_core"] or "-", "| FL", r["fl_share"] or "-", r["fl_core"] or "-", r["fl_price_vs_retail"] or "-",
          "| CH", r["ch_share"] or "-", r["ch_core"] or "-", r["ch_price_vs_retail"] or "-")
