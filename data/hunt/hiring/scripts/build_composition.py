"""Composition of Nike open postings over time (function and geography), from:
 - cc_job_objects.csv (Common Crawl archived listing pages; old site 2019 to early 2025, new site 2025 to Sep 2026)
 - live_postings_workday_2026-10-14.csv (live Workday census, all 1,303 Nike postings)
Outputs composition_by_period.csv. Usage: python3 build_composition.py"""
import pandas as pd, re
j = pd.read_csv("cc_job_objects.csv", low_memory=False).drop_duplicates(["crawl", "req_id"])
j["date"] = pd.to_datetime(j.timestamp.astype(str).str[:8])
# old-site pages: keep only job objects from pages whose URL carries no search filter (filtered pages over-sample one function/location)
lc = pd.read_csv("cc_listing_counts.csv")[["crawl", "timestamp", "url"]].drop_duplicates(["crawl", "timestamp"])
lc["url_filtered"] = lc.url.str.contains(r"jsCat|jsLocation|jsKeywords|jsBrand|jsPosition|internships|filter%5B|filter\[|keyword=", regex=True)
j = j.merge(lc[["crawl", "timestamp", "url_filtered"]], on=["crawl", "timestamp"], how="left")
j = j[~j.url_filtered.fillna(False)]
def bucket_new(fam, cat_cf):
    f = str(fam)
    if cat_cf == "Retail" or f in ("Stores", "Retail Stores", "Stores General"): return "retail_store"
    if re.search(r"Software|Technology|Data|Information Security|Technical Product|UX/UI|Machine|Cloud|Engineering Management|Platform", f): return "tech_data"
    if re.search(r"Product|Design|Material|Color|Innovation|Manufacturing Eng|Testing|Footwear|Apparel", f): return "product_design"
    if re.search(r"Account Management|Sales|Merchandis|Omni Channel|E-Commerce|Business Development|Demand Planning|Marketplace|Wholesale|Customer", f): return "sales_merch"
    if re.search(r"Marketing|Communications|Creative|Brand|Entertainment|Consumer", f): return "marketing"
    return "ops_support"
def bucket_old(cat):
    c = str(cat)
    if c == "Retail Stores": return "retail_store"
    if c in ("Technology", "Digital", "Data & Analytics"): return "tech_data"
    if c in ("Design", "Product Creation, Development & Management", "Advanced Innovation", "Air Manufacturing Innovation", "Manufacturing & Engineering"): return "product_design"
    if c in ("Sales", "Merchandising", "Planning", "Retail Corporate", "Customer Service"): return "sales_merch"
    if c in ("Marketing", "Communications", "Sports Marketing"): return "marketing"
    if c == "Internships": return "internship"
    return "ops_support"
j["bucket"] = [bucket_new(f, c) if s == "new" else bucket_old(k) for s, f, c, k in zip(j.site, j.job_family, j.job_category_cf, j.category)]
j["country_std"] = j.country.replace({"Mainland China": "China", "China Mainland": "China", "United States of America": "United States"})
j["period"] = j.date.dt.year.astype(str) + "H" + ((j.date.dt.month > 6) + 1).astype(str)
j.loc[j.date >= "2026-07-01", "period"] = "2026Q3"
live = pd.read_csv("live_postings_workday_2026-10-14.csv"); live = live[live.company == "Nike"].copy()
wmap = {"Technology": "tech_data", "Analytics": "tech_data", "Product Development Group": "product_design", "Design": "product_design", "Manufacturing": "product_design", "Quality": "product_design",
        "Sales": "sales_merch", "Merchandising": "sales_merch", "Marketing": "marketing", "Retail Stores": "retail_store"}
live["bucket"] = live.category.fillna("").map(lambda c: wmap.get(c.split(";")[0], "ops_support"))
live["country_std"] = live.country.replace({"China Mainland": "China", "United States of America": "United States"})
live["period"] = "2026-10-14 live census"; live["site"] = "live_workday"
snap = pd.read_csv("raw/repo_careers_corporate_2026-10-13.csv")
snap["bucket"] = [bucket_new(f, "Corporate") for f in snap.job_family]
snap["country_std"] = snap.country.replace({"Mainland China": "China"}); snap["period"] = "2026-10-13 careers corporate census"; snap["site"] = "new_census_corporate_only"
cols = ["period", "site", "bucket", "country_std"]
allj = pd.concat([j[cols], live[cols], snap[cols]])
out = []
for (p, s), g in allj.groupby(["period", "site"]):
    corp = g[~g.bucket.isin(["retail_store", "internship"])]
    ret = g[g.bucket == "retail_store"]
    row = {"period": p, "source": s, "n_postings_sampled": len(g), "retail_share_pct": round(100 * len(ret) / len(g), 1), "n_corporate": len(corp)}
    for b in ["tech_data", "product_design", "sales_merch", "marketing", "ops_support"]:
        row[f"corp_{b}_pct"] = round(100 * (corp.bucket == b).mean(), 1) if len(corp) else None
    for c in ["United States", "China", "India"]:
        row[f"corp_{c.replace(' ', '_')}_pct"] = round(100 * (corp.country_std == c).mean(), 1) if len(corp) else None
    row["retail_China_pct"] = round(100 * (ret.country_std == "China").mean(), 1) if len(ret) else None
    row["all_China_pct"] = round(100 * (g.country_std == "China").mean(), 1)
    row["corp_tech_in_India_pct"] = round(100 * (corp[corp.bucket == "tech_data"].country_std == "India").mean(), 1) if (corp.bucket == "tech_data").any() else None
    out.append(row)
o = pd.DataFrame(out).sort_values(["source", "period"])
o.to_csv("composition_by_period.csv", index=False)
j.to_csv("cc_job_objects_bucketed.csv", index=False)
pd.set_option("display.width", 250); print(o.to_string(index=False))
