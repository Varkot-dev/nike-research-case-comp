---
name: nike-report-update
description: Rules and steps for changing anything in this Nike research repo (REPORT.md, DEEP_DIVE_DENTON_EWING.md, research_notes, charts, data). Use whenever editing a number, table, chart or claim in the report, adding a new quarter's results, or preparing commits for this repo.
---

# Updating the Nike report

## House rules
- **Every financial number cites a filing and printed page**, written like `(FY26 10-K p. 32)`, `(Q1 FY27 10-Q p. 25)`, `(Q4 FY26 release p. 1)`, `(2026 proxy p. 56)`, `(8-K filed Oct 1, 2026, p. 2)`. The value must exist in `data/nike_filing_facts.csv` or on the cited page. Never type a number from memory.
- **Non-filing facts carry a label:** *market data* (Yahoo Finance, `data/nke_daily_prices.csv`), *Nike release* (an opened about.nike.com or investors.nike.com page), *secondary* (an opened news or aggregator page), *my arithmetic*, *my inference*. If a claim cannot be verified on an opened page or in a filing, remove it and list the removal in REPORT.md Section 13.
- **No generic explanations.** Never write statements like "fewer people want the shoes," "demand is weak" or "the bright spot." Every "why" is decomposed into data: units versus ASP, channel, region, gross margin bridge in bps, cost deleverage as a share of revenue, and a dollar bridge or sensitivity. If the filings cannot separate two causes, say so. See `CLAUDE.md`.
- **Check derived claims against the data before writing them.** A chart title or sentence like "down 38%" or "closed at $X that day" must be computed from the files, not estimated.
- **No em-dashes or en-dashes anywhere**, including quoted filing text (replace with a hyphen). Professional tone. Check with `python3 -c "import pathlib;[print(f) for f in pathlib.Path('.').rglob('*') if f.suffix in ('.md','.py','.csv') and '.git' not in f.parts and any(c in f.read_text() for c in (chr(8212),chr(8211)))]"` (prints any file containing U+2014 or U+2013)
- Charts: one y-axis per panel (no dual axes), the fixed palette in `scripts/make_charts.py`, a source note on every chart. `v()` raises on a missing fact by design; do not bypass it with hard-coded numbers.

## Data flow (regenerate, don't hand-edit)
1. `data/nike_filing_facts.csv` is the source of truth for filing numbers (built by the `sec-filing-research` skill).
2. `python3 scripts/build_data_pack.py` regenerates `research_notes/04_financial_data_pack.md`. Edit the script, not the generated file.
3. `pip install matplotlib numpy && python3 scripts/make_charts.py` regenerates every chart in `charts/`.
4. `data/people_events.csv` drives the exits charts; every row needs a source and a `verified_against` value.
5. Then update the prose in REPORT.md and the deep dive, with citations.

## Adding a new quarter
Download the new 10-Q and earnings exhibit, extract and verify (sec-filing-research), merge the facts, extend `QTRS` and the Greater China period list in `make_charts.py` and the period lists in `build_data_pack.py`, regenerate, then update REPORT.md Sections 1, 5 and 6 and the "what changed" list in Section 13.

## Before committing
- Re-run both scripts and look at the changed charts (open the PNGs).
- Spot-check five or more citations you touched against the facts CSV.
- Commit in purposeful slices (data, generated notes, charts, prose), each with a message that says what changed and why.
- **Publish every finding as a pull request.** Commit on the session branch, push it, open a PR into the default branch `claude/wonderful-franklin-u31n4e`, and merge it when it is safe. Safe means: no merge conflict, only research content changed (notes, data, charts, scripts), no secrets or personal contact details, the em-dash check passes, and any regenerated files were rebuilt by their scripts. If any check fails, leave the PR open and tell the user why.
- Do not push straight to `claude/wonderful-franklin-u31n4e`; it changes only through merged PRs. Other `claude/*` branches belong to other sessions; do not merge or rewrite them without the user's say-so.
