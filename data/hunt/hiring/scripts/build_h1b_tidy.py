"""Clean h1b_lca_rows.csv into deduplicated LCA rows and a quarterly count table.
Usage: python3 build_h1b_tidy.py (from data/hunt/hiring)"""
import pandas as pd, re
d = pd.read_csv("h1b_lca_rows.csv")
d["submit"] = pd.to_datetime(d.submit_date, errors="coerce", format="%m/%d/%Y")
d = d.dropna(subset=["submit"])
d["employer"] = d.employer.str.upper().str.strip()
def firm(e):
    if e.startswith("NIKE"): return "Nike"
    if e.startswith("CONVERSE"): return "Converse (Nike)"
    if "ADIDAS" in e or "REEBOK" in e: return "adidas"
    if "DECKERS" in e: return "Deckers"
    if "LULULEMON" in e: return "lululemon"
    if "UNDER ARMOUR" in e: return "Under Armour"
    if e.startswith("VF ") or "VF CORPORATION" in e or e.startswith("VF OUTDOOR"): return "VF"
    if "SKECHERS" in e: return "Skechers"
    if "NEW BALANCE" in e: return "New Balance"
    if "FOOT LOCKER" in e: return "Foot Locker"
    if e.startswith("ON ") or "ON RUNNING" in e: return "On"
    return None
d["firm"] = d.employer.map(firm)
d = d.dropna(subset=["firm"])
d = d.drop_duplicates(subset=["employer", "job_title", "base_salary", "location", "submit_date", "start_date"])
t = d.job_title.str.upper()
d["role_group"] = "other"
d.loc[t.str.contains(r"SOFTWARE|DATA|ENGINEER|DEVELOPER|ARCHITECT|ANALYTIC|MACHINE LEARNING|CLOUD|TECHNOLOG|DEVOPS|SECURITY|SCIENTIST|PLATFORM|QA|SRE"), "role_group"] = "tech_data"
d.loc[t.str.contains(r"DESIGN|PRODUCT DEVELOP|PRODUCT CREATION|MATERIAL|DEVELOPER, FOOTWEAR|FOOTWEAR|APPAREL|INNOVATION|COLOR|PATTERN|BIOMECH")
      & ~t.str.contains(r"SOFTWARE|DATA"), "role_group"] = "product_design_innovation"
d.loc[t.str.contains(r"MERCHAND|PLANNER|PLANNING|SALES|MARKETING|BRAND|CONSUMER|ACCOUNT"), "role_group"] = "commercial_merch_marketing"
d["quarter"] = d.submit.dt.to_period("Q").astype(str)
d["year"] = d.submit.dt.year
d.drop(columns=["search_key", "search_year"]).sort_values(["firm", "submit"]).to_csv("h1b_lca_clean.csv", index=False)
q = d.groupby(["firm", "quarter"]).size().unstack(0).fillna(0).astype(int)
q.to_csv("h1b_lca_quarterly_by_firm.csv")
r = d[d.firm == "Nike"].groupby(["quarter", "role_group"]).size().unstack(1).fillna(0).astype(int)
r.to_csv("h1b_lca_quarterly_nike_by_role.csv")
print(q.tail(28).to_string()); print(r.tail(28).to_string())
