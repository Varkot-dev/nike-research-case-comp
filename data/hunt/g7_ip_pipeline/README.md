# G7: IP pipeline (trademarks and patents), Nike vs seven peers

Question: are Nike's trademark and patent filings (leading indicators of launches) thin ahead of FY28? Result and tables: `research_notes/Smoking gun hunt/G7_ip_pipeline.md`. Verdict: no smoking gun.

Sources (anonymous, no key, no email): USPTO Trademark Search backend (`tmsearch.uspto.gov`, index loaded 2026-10-01) and USPTO Patent Public Search (`ppubs.uspto.gov`, to 2026-10-13).

Run order: `g7_tm_pull.py`, `g7_tm_analyze.py`, `g7_pat_pull.py` (about 20 minutes), `g7_pat_analyze.py`, `g7_pooled_share.py`, `g7_pat_verify.py`. Helpers: `tmlib.py`, `pplib.py`. Raw pulls: `tm_raw_*.jsonl`, `pat_raw_*.jsonl`, `pat_fwcpc_*.json`.

Key outputs: `g7_tm_annual_counts.csv`, `g7_tm_same_period_jan_sep.csv`, `g7_tm_nike_share.csv`, `g7_tm_change_2024_26_vs_2017_19.csv`, `g7_tm_abandon_cancel.csv`, `g7_nike_tm_abandoned_2024_26_detail.csv`, `g7_tm_leadlag_first_use.csv`, `g7_pat_annual_by_pub_year.csv`, `g7_pat_annual_by_filing_year.csv`, `g7_pat_nike_share.csv`, `g7_pat_change_2024_26_vs_2017_19.csv`, `g7_pooled_share_2017_19_vs_2024_26.csv`, `g7_nike_ip_intensity.csv`, `g7_pat_verify_counts.csv`.

Caveats: counts are documents, not products; 2026 trademark window ends Sep 30; 2025 to 2026 design filings are not yet public; EU, Hague, PCT, Lens and PatentsView were blocked (routes in the note).
