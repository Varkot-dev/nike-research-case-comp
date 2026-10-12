# SEC filing pipeline

How `data/nike_filing_facts.csv` was built (Oct 12, 2026). Run from a scratch directory, not inside the repo.

1. `dl.py <dir>` and `dl2.py <dir>`: download Nike's filing index from data.sec.gov (`<dir>/sub.json`) and then every 10-K (FY2019 to FY2026), 10-Q (Q1 FY2024 onward), earnings 8-K with Exhibit 99.1, the 2026 DEF 14A, and the 2024 to 2026 leadership and restructuring 8-Ks. Set `SEC_USER_AGENT="Your Name your@email"` first; the SEC requires a contact in the User-Agent. First fetch the index with `curl -A "$SEC_USER_AGENT" -o <dir>/sub.json https://data.sec.gov/submissions/CIK0000320187.json`.
2. `topages.py <outdir> <files...>`: convert each HTML filing to text split on its page breaks, with the printed page number detected from the footer and tables rendered as `|`-separated rows.
3. Readers (`INSTRUCTIONS.md`, `CLAIMS.md`): each filing was read in full and every data point extracted with its page and a verbatim quote.
4. `merge.py <dir>`: merge the extracts and check that every value appears on the cited page of the cited filing.
5. `canon.py <dir> <outdir>`: choose one value per metric and period, preferring the filing that first reported it; report cross-source conflicts.
6. `relocate.py <dir> <csv>`: re-cite annual and balance-sheet values to the period's own 10-K or 10-Q where the same table row and value are found there.
7. `xbrl.py <companyfacts.json> <out.csv>`: independent cross-check against SEC XBRL company facts.
