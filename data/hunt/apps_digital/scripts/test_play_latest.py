"""Latest-window test: same calendar window this year vs last year, per app, and an implied NIKE Digital growth from the FY23+ calibration fit."""
import glob, pandas as pd, numpy as np
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
W = {"Q4FY26 Mar-May": ("03-01", "06-01", 2026), "Q1FY27 Jun-Aug": ("06-01", "09-01", 2026), "Q2FY27 to date Sep1-Oct12": ("09-01", "10-13", 2026),
     "Jul-Sep 2026": ("07-01", "10-01", 2026), "Sep 2026": ("09-01", "10-01", 2026)}
out = []
for f in sorted(glob.glob(f"{BASE}/raw/play_reviews/*.csv.gz")):
    app, loc = f.split("/")[-1][:-7].split("__")
    d = pd.read_csv(f, parse_dates=["at"])
    for name, (a, b, y) in W.items():
        n1 = ((d["at"] >= f"{y}-{a}") & (d["at"] < f"{y}-{b}")).sum()
        n0 = ((d["at"] >= f"{y-1}-{a}") & (d["at"] < f"{y-1}-{b}")).sum()
        s1 = d[(d["at"] >= f"{y}-{a}") & (d["at"] < f"{y}-{b}")].score.mean()
        out.append([app, loc, name, n0, n1, (n1 / n0 - 1) * 100 if n0 else np.nan, s1])
o = pd.DataFrame(out, columns=["app", "locale", "window", "n_last_year", "n_this_year", "yoy_pct", "avg_stars_this_year"])
o.to_csv(f"{BASE}/test_play_latest.csv", index=False)
print(o.pivot_table(index=["app", "locale"], columns="window", values="yoy_pct").round(0).to_string())
cal = pd.read_csv(f"{BASE}/test_play_calibration.csv")
c = cal[(cal.fq >= "FY2023Q1") & cal.nike_app_us_yoy.notna()]
c = c[c.fq != "FY2027Q1"]
b, a = np.polyfit(c.nike_app_us_yoy, c.nike_brand_digital_yoy_pct, 1)
res = c.nike_brand_digital_yoy_pct - (a + b * c.nike_app_us_yoy)
print("fit FY23Q1-FY26Q4 (holdout FY27Q1): digital = %.1f + %.2f*reviews_yoy, resid sd %.1f, n=%d" % (a, b, res.std(), len(c)))
for name in ["Q1FY27 Jun-Aug", "Q2FY27 to date Sep1-Oct12"]:
    v = o[(o.app == "nike_app") & (o.locale == "en_us") & (o.window == name)].yoy_pct.iloc[0]
    print(name, "Nike app US review YoY %.1f -> implied digital %.1f%%" % (v, a + b * v))
