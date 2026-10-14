# peers_reported: Nike vs athletic peers, company-reported quarterly data (2019 to Oct 2026)

Pulled 2026-10-14. All sources are free and public. No logins. SEC requests used a generic research User-Agent (no personal data) with 0.25 to 0.5 s sleeps; HKEX and IR sites used 0.5 to 1 s sleeps.

## Tidy outputs (this folder)

| File | What it is |
|---|---|
| `panel_region_quarterly.csv` | One row per company x reported region x calendar quarter: local-currency revenue, reported yoy, constant-currency yoy where the company prints it, source. 14 companies, 2017 to 2026Q3. |
| `panel_growth_comparable.csv` | Region growth on a comparable basis: constant currency when printed, otherwise reported revenue translated into the region's home currency (USD for North America, EUR for Europe/EMEA, CNY for China) with ECB monthly averages. Adds Vans regional cc growth and China domestic brands' retail sell-through. |
| `panel_company_quarterly.csv` | Company level: revenue, gross profit, gross margin, inventory, revenue yoy, inventory yoy, inventory-minus-sales gap, GM yoy bps. |
| `sec_regional_quarterly.csv` | SEC XBRL segment and geography revenue, discrete quarters (Q4 derived as annual minus 9-month YTD). |
| `sec_quarterly_financials_raw.csv` | SEC companyfacts quarterly revenue, gross profit, inventory (companyfacts lags for some filers; the instance-based panel above is preferred). |
| `adidas_quarterly_extract.csv`, `puma_quarterly_extract.csv`, `asics_quarterly_extract.csv`, `asics_ytd_regional_tanshin.csv`, `on_quarterly_extract.csv`, `deckers_release_extract.csv`, `vf_vans_regional_growth.csv` | Per-company parses with file and line references. |
| `china_peers_sellthrough_quarterly.csv` | HKEX quarterly operational updates: ANTA brand, FILA, Anta other brands, Li Ning overall platform, Xtep core brand, Saucony China retail sell-through growth (word ranges mapped to midpoints), plus Xtep retail discount rate and channel inventory turnover (months). 2017 to 2026Q2. |
| `test_gap_by_region_quarter.csv`, `test_T1_summary.json` | T1: Nike minus peer-median growth by region and quarter. |
| `test_T2_inventory_gm_latest.csv`, `test_T2_summary.json`, `test_T2b_gm_gap.csv` | T2: inventory growth minus sales growth, and gross-margin change vs peers. |
| `test_T3_nike_share_by_region.csv`, `test_T3_summary.json` | T3: Nike share of combined peer-set revenue by region, and yoy change in share. |
| `test_T4_china.csv` | T4: Nike Greater China vs foreign peers in China and domestic brands' sell-through, with Xtep discount and channel inventory. |

Calendar mapping: a fiscal quarter is assigned to the calendar quarter that contains its midpoint. Nike Jun-Aug = CQ3, Mar-May = CQ2, Dec-Feb = CQ1; Lululemon May-Jul = CQ2. So Nike's quarter runs about one month ahead of peers' calendar quarter. Nike CQ3 2026 (Jun-Aug) has no peer counterpart yet (adidas, Puma, On, Deckers, Anta report late Oct to mid Nov).

## Sources (URLs) and method

1. SEC EDGAR (scripts 01 to 04, 08, 09, 15)
   - `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` and `https://data.sec.gov/submissions/CIK##########.json` for Nike 320187, Deckers 910521, Lululemon 1397187, VF 103379, Under Armour 1336917, Skechers 1065837, On 1858985, Crocs 1334036, Amer Sports 1988894, Birkenstock 1977102, Columbia 1050797, DICK'S 1089063. Raw JSON in `raw/sec_companyfacts/`.
   - XBRL instance documents (`*_htm.xml`) for every 10-Q, 10-K and XBRL 6-K filed since 2019-03 (about 300 files, 226 MB, kept in the session scratchpad, not the repo). Parsed into `raw/sec_xbrl_dimensional_facts.csv` (every revenue, gross profit, cost of sales, inventory and segment fact with its dimension members). Manifest of URLs: scratchpad `xbrl/manifest.tsv` (re-create with script 03).
   - Earnings-release exhibits (8-K Item 2.02 Ex. 99.1; 6-K Ex. 99.1 for On, Amer, Birkenstock) saved as text in `raw/releases_<company>/`; first line of each file is the source URL.
2. adidas IR, `https://www.adidas-group.com/en/investors/financial-reports` (links to res.cloudinary.com PDFs): quarterly results releases 2017 to Q2 2026 and financial supplements; pdftotext output in `raw/adidas_text/` (PDFs kept in scratchpad).
3. Puma IR, `https://about.puma.com/en/investor-relations/financial-publications`: quarterly statements and press releases 2019 to Q2 2026, text in `raw/puma_text/`.
4. ASICS IR, `https://corp.asics.com/en/investor_relations/library/financial_summary` and `.../financial_data`: fact-sheet workbooks FY2021, FY2022, FY2023, FY2024 (`raw/asics/*.xlsx`, quarterly regional sales 2020 to 2024 and gross profit 2023 to 2024) and Japan-GAAP summary statements Q1 2025 to Q2 2026 (`raw/asics_text/`, `_index.txt` maps ids to URLs). 2025 to 2026 quarters are YTD differenced.
5. HKEXnews title-search JSON endpoint `https://www1.hkexnews.hk/search/titleSearchServlet.do` (stock ids: Anta 16111, Li Ning 7647, Xtep 23896, 361 Degrees 34919, Topsports 1000010460, Pou Sheng 23491). Operational updates and results announcements as text in `raw/hkex_text/` (`_manifest.tsv`; some titles wrap onto a second line).
6. ECB Data API, `https://data-api.ecb.europa.eu/service/data/EXR/M.USD+CHF+JPY+CNY.EUR.SP00.A?startPeriod=2018-01&format=csvdata` (`raw/fx/ecb_monthly_eur_rates.csv`).
7. Nike constant-currency regional growth: taken from the repo's `data/nike_filing_facts.csv` (already verified against filings); Nike levels from XBRL.
8. adidas Q3 2025 regional: that release's regional table is an image. Levels (Europe EUR 2.32bn, North America EUR 1.29bn, Greater China EUR 947m) and adidas-brand cc growth (+12%, +8%, +10%, against a prior-year base that excludes Yeezy) come from press coverage found by web search (worldfootwear.com, retail-insight-network.com). Tagged SNIPPET in `source_type`.
9. VF Q2 to Q4 2025 Vans growth (global only) typed from the slide-format release narrative (bullets quoted in script 14).

Re-run order: 01, 02, 03 (needs a scratch dir), 04, 05, 06, 07, 08, 09, 10 (needs a scratch dir), 11, 12, 13, 14, 15, 16, 17, 18, 19. Always run Python with `-I`.

## Known gaps and caveats

- Peer regions are not identical: Puma "Americas" and On "Americas" include Latin America; adidas "Europe" excludes Emerging Markets; Deckers only splits US vs international; Lululemon is apparel; Columbia and Crocs are outdoor or casual. T1 uses medians to limit the effect of any one definition.
- Reported growth for non-cc reporters is translated with average monthly ECB rates. That approximates constant currency but differs from company cc figures (hedging, invoicing currency).
- ASICS 2019 quarterly regions are missing (no fact sheet for FY2019/FY2020 on the site); ASICS 2026 tanshin restates 2025 regions, so 2025 to 2026 yoy uses same-vintage prior-year columns.
- Lululemon US and Canada quarterly XBRL facts are missing for 2021 to 2022, so Lululemon is only in the 2023Q2+ share set.
- On regional data start 2021Q3 (IPO); before 2022 On is set to zero in share calculations (On was under CHF 0.3bn in 2019). On's 2021 to 2022 regions were North America/Europe/APAC/ROW, later EMEA/Americas/APAC.
- Skechers stops at CQ2 2025 (taken private). Amer Sports starts 2023 (IPO).
- VF "Active" XBRL series is distorted by segment changes; Vans uses release growth tables instead (no Vans levels).
- Deckers HOKA: XBRL HOKA segment before 2024 is wholesale only; the panel uses release figures for HOKA.
- CQ2 2026 gross margins at Nike (USD 986m IEEPA credit), Under Armour, Lululemon, Columbia, Amer and others include tariff refunds. Nike ex-credit GM for Mar-May 2026 is about 40.2% (my arithmetic), roughly flat yoy. Use CQ1 2026 and Nike CQ3 2026 for clean GM comparisons.
- China domestic brands report retail sell-through as word ranges (for example "low-single-digit decline"); midpoints are my mapping (low single digit 2.5, mid 5, high 8, low teens 12, and so on). They measure retail sales, not company revenue.
- All of this is sell-in (company revenue), not consumer sell-through, except the China domestic series. It cannot by itself separate channel fill from consumer demand.
- Blocked or failed: FRED fredgraph CSV (HTTP/2 stream errors via proxy; ECB used instead); adidas Q3 2025 investor deck (image-only PDF, no text); some 2025 VF slide releases lack the Vans region table.
