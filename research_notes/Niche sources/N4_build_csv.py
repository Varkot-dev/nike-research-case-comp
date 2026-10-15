"""N4: build data/niche/N4_subsidiary_accounts.csv from the extracted statutory accounts.

Korea (Nike Korea LLC, Converse Korea LLC): parsed from the DART audit-report text saved in data/niche/N4_raw/
(fetched from dart.fss.or.kr viewer; amounts in KRW; filings are for fiscal years ending 31 May).
UK, Netherlands, Australia: values typed in from the OCR text / ATO workbooks listed in the source column
(OCR text for the UK/NL files is saved beside the Korea text; ATO workbooks are on data.gov.au).
Run: python3 -I "research_notes/Niche sources/N4_build_csv.py"   (from the repo root)
"""
import csv, json, os, re

RAW = "data/niche/N4_raw"
OUT = "data/niche/N4_subsidiary_accounts.csv"
rows = []


def add(entity, fy, metric, value, unit, source, tag, note=""):
    if value is None:
        return
    rows.append(dict(entity=entity, fiscal_year=fy, metric=metric, value=value, unit=unit,
                     source=source, tag=tag, note=note))


# ---------- Korea ----------
LABELS = [("revenue", r"매\s*출\s*액"), ("cogs", r"매\s*출\s*원\s*가"), ("gross_profit", r"매\s*출\s*총\s*이\s*익"),
          ("sga", r"판매비와\s*관리비"), ("operating_profit", r"영\s*업\s*이\s*익|영\s*업\s*손\s*실|영\s*업\s*이\s*익\(손\s*실\)"),
          ("net_income", r"당\s*기\s*순\s*이\s*익|당\s*기\s*순\s*손\s*실|당\s*기\s*순\s*이\s*익\(손\s*실\)"),
          ("cash", r"현금및현금성자산"), ("receivables", r"매출채권"), ("inventory", r"재\s*고\s*자\s*산"),
          ("returns_asset", r"반품제품회수권"), ("returns_provision", r"반품충당부채"),
          ("early_pay_discount_provision", r"매출할인충당부채"), ("trade_payables", r"매입채무"),
          ("total_assets", r"자\s*산\s*총\s*계"), ("total_liabilities", r"부\s*채\s*총\s*계"),
          ("equity", r"자\s*본\s*총\s*계"), ("operating_cash_flow", r"영업활동으로\s*인한\s*현금흐름")]


def nums(lines, i):
    out = []
    for l in lines[i + 1:i + 6]:
        l = l.strip()
        if re.fullmatch(r"\(?-?[\d,]+\)?", l) and re.search(r"\d", l):
            out.append(int(l.replace(",", "").replace("(", "-").replace(")", "")))
        else:
            break
    return out


def parse_year(path):
    L = open(path, encoding="utf8").read().split("\n")
    d = {}
    for k, p in LABELS:
        for i, l in enumerate(L):
            if re.match(r"^\s*(Ⅰ\.|[0-9]\.)?\s*(" + p + r")(\(주석[^)]*\))?\s*$", l):
                n = nums(L, i)
                if len(n) >= 2:
                    d[k] = n[0]
                    break
    return d


def sgn(label, v):
    return v


def korea(entity, prefix, years, src_tpl):
    for y in years:
        fy = f"FY{y}"
        path = f"{RAW}/{prefix}_FY{y}.txt"
        d = parse_year(path)
        txt = re.sub(r"\n\s*", " / ", open(path, encoding="utf8").read())
        # losses are printed unsigned under 영업손실 / 당기순손실 captions
        if re.search(r"영\s*업\s*손\s*실", txt) and not re.search(r"영\s*업\s*이\s*익\(손\s*실\)", txt) and "operating_profit" in d and d["operating_profit"] > 0:
            m = re.search(r"영\s*업\s*손\s*실[^/]*/ *([\d,]+)", txt)
            if m and int(m.group(1).replace(",", "")) == d["operating_profit"]:
                d["operating_profit"] = -d["operating_profit"]
        if re.search(r"당\s*기\s*순\s*손\s*실", txt):
            m = re.search(r"당\s*기\s*순\s*손\s*실[^/]*/ *([\d,]+)", txt)
            if m:
                d["net_income"] = -int(m.group(1).replace(",", ""))
        for k, v in d.items():
            add(entity, fy, k, round(v / 1e9, 3), "KRW bn", src_tpl.format(fy=fy), "OPENED")
        if entity.startswith("Nike Korea"):
            def g(p, i=1):
                m = re.search(p, txt)
                if not m:
                    return None
                t = m.group(i).replace(",", "").replace("(", "-").replace(")", "")
                return int(t) if re.fullmatch(r"-?\d+", t) else None
            purch = g(r"당기상품매입액[^/]*/ *([\d,]+)")
            tp = g(r"이전가격조정금액[^/]*/ *([\(\)\d,\-]+)")
            if fy == "FY22":
                tp = -34226408  # FY22 purchases included a transfer price gain; amount shown only as the FY23 report comparative
            allow = g(r"상품 */ *[\d,]+ */ *[\d,]+ */ *평가손실충당금 */ *\(?([\d,]+)\)?")
            m = re.search(r"반품충당부채 */ *([\d,]+) */ *([\d,]+) */ *\(([\d,]+)\) */ *([\d,]+)", txt)
            for name, v in (("goods_purchases", purch), ("transfer_price_adjustment_in_cogs", tp or 0), ("inventory_valuation_allowance", allow)):
                if v is not None:
                    add(entity, fy, name, round(v / 1e6, 3), "KRW bn", src_tpl.format(fy=fy), "OPENED", "note on cost of sales / inventories (KRW thousand in filing)")
            if m:
                add(entity, fy, "returns_provision_charge", round(int(m.group(2).replace(",", "")) / 1e6, 3), "KRW bn", src_tpl.format(fy=fy), "OPENED", "provision rollforward, increase")
                add(entity, fy, "returns_provision_usage", round(int(m.group(3).replace(",", "")) / 1e6, 3), "KRW bn", src_tpl.format(fy=fy), "OPENED", "provision rollforward, decrease")
            # NGT purchases of goods (Singapore branch)
            mm = re.search(r"Global Trading BV Singapore Branch */ *[-\d,]+ */ *[\d,\-]+ */ *[-\d,]* */ *([\d,]+) */", txt, re.I)
    return


korea("Nike Korea LLC", "nike_korea", range(21, 27), "DART audit report, Nike Korea LLC, {fy} (rcpNo in note)")
korea("Converse Korea LLC", "converse_korea", range(21, 27), "DART audit report, Converse Korea LLC, {fy} (rcpNo in note)")

# related-party goods purchases from NIKE Global Trading BV Singapore Branch (KRW bn, OPENED, note on related parties)
NGT = {"FY21": 1125.898, "FY22": 1304.789, "FY23": 1817.568, "FY24": 1388.481, "FY25": 1442.109, "FY26": 1325.539}
for fy, v in NGT.items():
    add("Nike Korea LLC", fy, "goods_purchases_from_NGT_Singapore", v, "KRW bn", "DART audit report related-party note", "OPENED")

# ---------- Australia (ATO Corporate Tax Transparency, data.gov.au) ----------
AU = {"2014-15": (367332190, 9919035, 2975710), "2015-16": (463397922, 13699320, 4109796),
      "2016-17": (496703079, 12659549, 3797865), "2017-18": (515979370, 9631385, 2889416),
      "2018-19": (571801609, 14143559, 4243068), "2019-20": (517704093, 32575012, 9772504),
      "2020-21": (722918137, 9127256, 2738177), "2021-22": (705868119, 29958185, 8987456),
      "2022-23": (944349169, 42920548, 12876164), "2023-24": (924873389, 32202142, 9660643),
      "2024-25": (893961111, 21626729, 6488019)}
for yr, (ti, tx, tp) in AU.items():
    s = f"ATO Report of Entity Tax Information {yr} (data.gov.au), NIKE AUSTRALIA PTY LTD ABN 99055141743"
    add("Nike Australia Pty Ltd", yr, "total_income", round(ti / 1e6, 3), "AUD m", s, "OPENED", "income year; includes all income, not only sales")
    add("Nike Australia Pty Ltd", yr, "taxable_income", round(tx / 1e6, 3), "AUD m", s, "OPENED")
    add("Nike Australia Pty Ltd", yr, "tax_payable", round(tp / 1e6, 3), "AUD m", s, "OPENED")

# ---------- UK ----------
S = "Companies House 01887016 FY21 accounts (OCR)"
for fy, rev, op, ni, na, emp in (("FY21", 63.342, 20.096, 15.565, 110.986, 260), ("FY20", 79.773, 19.522, 17.091, 92.148, 279)):
    add("Nike (UK) Limited", fy, "revenue", rev, "GBP m", S, "OPENED", "commission on UK and Ireland sales plus cost reimbursement")
    add("Nike (UK) Limited", fy, "operating_profit", op, "GBP m", S, "OPENED")
    add("Nike (UK) Limited", fy, "net_income", ni, "GBP m", S, "OPENED")
    add("Nike (UK) Limited", fy, "net_assets", na, "GBP m", S, "OPENED")
    add("Nike (UK) Limited", fy, "headcount_avg", emp, "people", S, "OPENED")
add("Nike (UK) Limited", "FY21", "going_concern_note", "basis other than going concern; trade and net assets to move to another Nike company at book value and company to be liquidated", "text", S, "OPENED", "dissolved 4 Jun 2024")
for fy, rev, op, ni, inv, emp, stores in (("FY25", 3.443, 0.107, -0.030, 0.226, 28, 1), ("FY24", 3.881, 0.492, 0.131, 0.249, 24, 3), ("FY23", 7.345, 0.402, None, 0.282, 51, 3)):
    s = "Companies House 10584502 FY25/FY24 accounts (OCR)"
    add("Converse Retail (UK) Limited", fy, "revenue", rev, "GBP m", s, "OPENED", "Wembley, Mansfield, Cheshire Oaks outlets; two closed FY23/FY24")
    add("Converse Retail (UK) Limited", fy, "operating_profit", op, "GBP m", s, "OPENED")
    add("Converse Retail (UK) Limited", fy, "net_income", ni, "GBP m", s, "OPENED")
    add("Converse Retail (UK) Limited", fy, "inventory", inv, "GBP m", s, "OPENED")
    add("Converse Retail (UK) Limited", fy, "headcount_avg", emp, "people", s, "OPENED")
    add("Converse Retail (UK) Limited", fy, "stores_operated", stores, "stores", s, "OPENED")
add("Converse Retail (UK) Limited", "FY25", "inventory_impairment_expensed", 0.029, "GBP m", "Companies House 10584502 FY25 note 11", "OPENED")
add("Converse Retail (UK) Limited", "FY24", "inventory_impairment_expensed", 0.057, "GBP m", "Companies House 10584502 FY24 note", "OPENED")

# ---------- Netherlands / EMEA (Companies House overseas company filings) ----------
S = "Companies House FC019114 FY25 and FY24 accounts (OCR); FY23 column from FY24 accounts; FY22 from the FY22 accounts (OCR; NEON merged in on 1 May 2022 with carryover accounting from 1 Jun 2021, so FY22 is the first like-for-like year)"
NR = {  # EUR m, company accounts
    "FY25": dict(revenue=10977.288, gross_profit=2494.984, operating_profit=-36.047, net_income=426.136, inventory=1288.450,
                 inventory_finished=972.004, inventory_in_transit=316.446, trade_receivables=904.540, bad_debt_reserve=11.7,
                 rev_netherlands=1009.873, rev_rest_emea=9807.682, rev_other=159.733, trade_revenue=10800.611,
                 headcount_avg=9155, equity=3560.606, cost_of_inventories_expensed=5481.5),
    "FY24": dict(revenue=12354.814, gross_profit=2805.321, operating_profit=-324.213, net_income=94.196, inventory=1225.882,
                 inventory_finished=1049.568, inventory_in_transit=176.314, trade_receivables=715.265, bad_debt_reserve=2.8,
                 rev_netherlands=1051.410, rev_rest_emea=11100.087, rev_other=203.317, trade_revenue=12152.998,
                 headcount_avg=9489, equity=3127.313, cost_of_inventories_expensed=6165.8),
    "FY22": dict(revenue=10710.506, gross_profit=2807.720, operating_profit=318.170, net_income=902.681, inventory=1174.055,
                 trade_receivables=917.940, rev_netherlands=834.649, rev_rest_emea=9521.644, rev_other=354.213,
                 trade_revenue=10439.524, headcount_avg=7239),
    "FY23": dict(revenue=12702.932, gross_profit=3192.034, operating_profit=423.611, net_income=778.015, inventory=1536.337,
                 inventory_finished=1139.413, inventory_in_transit=396.924, trade_receivables=746.637, bad_debt_reserve=5.7,
                 rev_netherlands=924.431, rev_rest_emea=11548.653, rev_other=229.848, trade_revenue=12493.986,
                 headcount_avg=9193, equity=3417.048),
}
for fy, d in NR.items():
    for k, v in d.items():
        add("Nike Retail B.V. (EMEA)", fy, k, v, "people" if k == "headcount_avg" else "EUR m", S, "OPENED")
S = "Companies House FC032565 FY24 accounts of parent Nike Flight B.V. under Art. 2:403 (OCR)"
for fy, d in {"FY24": dict(revenue=20986.876, gross_profit=933.265, operating_profit=111.901, net_income=250.303, inventory=1806.772, receivables=2546.087, cash=6276.889),
              "FY23": dict(revenue=21839.607, gross_profit=1107.594, operating_profit=72.826, net_income=135.551, inventory=1679.630, receivables=2768.990, cash=5448.120)}.items():
    for k, v in d.items():
        add("Nike Flight B.V. consolidated (NTC and NGT sourcing hub; filed via Nike 360 Holding B.V.)", fy, k, v, "USD m", S, "OPENED")

# optional extra rows appended by hand-edited file (OCR of older NRBV years)
EXTRA = "research_notes/Niche sources/N4_extra_rows.csv"
if os.path.exists(EXTRA):
    for r in csv.DictReader(open(EXTRA)):
        rows.append(r)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="", encoding="utf8") as f:
    w = csv.DictWriter(f, fieldnames=["entity", "fiscal_year", "metric", "value", "unit", "source", "tag", "note"])
    w.writeheader()
    w.writerows(rows)
print(len(rows), "rows ->", OUT)
