---
name: verify-non-sec-claims
description: Verify people, layoff, strategy, index and analyst claims that SEC filings do not cover, using pages that can actually be opened. Use when checking executive moves, Nike announcements, layoff counts, WARN notices, analyst ratings or price targets, or any news-sourced claim in this repo.
---

# Verifying claims outside SEC filings

1. **Try a filing first.** Executive appointments, departures, pay terms and restructuring charges usually appear in 8-K Item 5.02 or 2.05 and the proxy. Use the `sec-filing-research` skill if they do.
2. **Then Nike's own pages:** the leadership roster at about.nike.com/en/company, profiles under about.nike.com/en/company/people/<name>, newsroom releases under about.nike.com/en/newsroom/releases/, and investors.nike.com press releases. These are company statements: good for titles and dates, not independent evidence of performance.
3. **Then opened news pages.** As of Oct 2026 these were reachable through the proxy: retaildive.com, wwd.com, fortune.com, marketingdive.com, fashionunited.com, talkbusiness.net, technode.com, dailytidings.com, stockanalysis.com, marketbeat.com, en.wikipedia.org, and state WARN notices (for example tn.gov). These were blocked: cnbc.com, bloomberg.com, reuters.com, businesswire.com, businessoffashion.com, macrotrends.net, spglobal.com. Re-test with `curl -sS -o /dev/null -w '%{http_code}' -A "Mozilla/5.0" URL`, since access changes.
4. **Record what you actually opened.** Note the URL and a short verbatim quote. A search-result snippet is not verification: mark it "snippet only" or leave the claim out.
5. **Layoffs:** filings give charges, not headcounts. Use WARN notices for counts where they exist, and say which state and site they cover.
6. **Analyst data:** always give the aggregator, the analyst count and the as-of date. Aggregators disagree, so never present one aggregator's split as "consensus" without naming it.
7. **Market prices:** pull from the Yahoo Finance chart API (`https://query1.finance.yahoo.com/v8/finance/chart/NKE?period1=...&period2=...&interval=1d`). Save to `data/`, label as market data, and compute every price claim ("13-year low", "% from peak") from that file.
8. Fold the results into REPORT.md with the labels from the `nike-report-update` skill, and list corrections in Section 13.
