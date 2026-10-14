# Nike earnings call transcripts, Q1 FY21 to Q1 FY27

Official NIKE, Inc. call transcripts (PDF) from the Nike investor site (investors.nike.com asset store). All 25 quarters were downloaded on 2026-10-13 (OPENED). No quarter was missing, so no mirror fill was needed.

Each `Q?FY??.txt` file is `pdftotext` output of the official PDF, with page breaks kept as `=== PAGE n ===` lines so a quote can be cited by PDF page. Em and en dashes are replaced with hyphens (repo house rule); nothing else is edited. The Q1 FY24 PDF carries a "remarks as prepared" cover note but contains the full Q&A. Elliott Hill became CEO on Oct 14, 2024, so Q2 FY25 is the first Hill call; Dave Denton replaced Matt Friend as CFO for Q1 FY27.

Rebuild: `python3 -I data/hunt/earnings_calls/scripts/01_extract_transcripts.py <folder with t_<db id>.pdf> data/hunt/earnings_calls/transcripts`

| Quarter | Call date | CEO | CFO on call | PDF pages | Words | Nike db id | Source URL (OPENED 2026-10-13) |
|---|---|---|---|---|---|---|---|
| Q1FY21 | 2020-09-22 | Donahoe | Friend | 13 | 9,033 | 9384 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9384/webcast_transcript/NIKE-Inc.-Q1FY21-OFFICIAL-Transcript-with-QA.pdf |
| Q2FY21 | 2020-12-18 | Donahoe | Friend | 13 | 9,355 | 9385 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9385/webcast_transcript/NIKE-Inc.-Q2FY21-OFFICIAL-Transcript-with-QA.pdf |
| Q3FY21 | 2021-03-18 | Donahoe | Friend | 16 | 9,330 | 9386 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9386/webcast_transcript/NIKE-Inc.-Q3FY21-OFFICIAL-Transcript-with-Q-A.pdf |
| Q4FY21 | 2021-06-24 | Donahoe | Friend | 21 | 8,349 | 9387 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9387/webcast_transcript/NIKE-Inc.-Q4FY21-OFFICIAL-Transcript-with-QA-FINAL.pdf |
| Q1FY22 | 2021-09-23 | Donahoe | Friend | 15 | 8,929 | 9388 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9388/webcast_transcript/FY-2022-Q1-Earnings-Release-Conference-Call-OFFICIAL-Transcipt-FINAL.pdf |
| Q2FY22 | 2021-12-20 | Donahoe | Friend | 28 | 8,615 | 9389 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9389/webcast_transcript/FY-2022-Q2-Earnings-Release-Conference-Call-OFFICIAL-TRANSCRIPT-FINAL-%281%29.pdf |
| Q3FY22 | 2022-03-21 | Donahoe | Friend | 31 | 9,176 | 9390 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9390/webcast_transcript/FY-2022-Q3-Earnings-Release-Conference-Call-OFFICIAL-TRANSCRIPT-FINAL.pdf |
| Q4FY22 | 2022-06-27 | Donahoe | Friend | 29 | 9,119 | 9391 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9391/webcast_transcript/NIKE-Inc.-Q4FY22-OFFICIAL-Transcript-FINAL.pdf |
| Q1FY23 | 2022-09-29 | Donahoe | Friend | 30 | 9,351 | 9392 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9392/webcast_transcript/NIKE-Inc.-Q1FY23-OFFICIAL-Transcript-FINAL.pdf |
| Q2FY23 | 2022-12-20 | Donahoe | Friend | 28 | 9,032 | 9393 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9393/webcast_transcript/NIKE-Inc.-Q2FY23-OFFICIAL-Transcript-FINAL.pdf |
| Q3FY23 | 2023-03-21 | Donahoe | Friend | 27 | 8,819 | 9394 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9394/webcast_transcript/NIKE-Inc-Q3FY23-OFFICIAL-Transcript-FINAL.pdf |
| Q4FY23 | 2023-06-29 | Donahoe | Friend | 28 | 8,914 | 9395 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9395/webcast_transcript/NIKE-Inc-Q4FY23-OFFICIAL-Transcript.pdf |
| Q1FY24 | 2023-09-28 | Donahoe | Friend | 25 | 9,351 | 9396 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9396/webcast_transcript/NIKE-Inc-Q1FY24-OFFICIAL-Transcript.pdf |
| Q2FY24 | 2023-12-21 | Donahoe | Friend | 26 | 8,785 | 9397 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9397/webcast_transcript/NIKE-Inc-Q2FY24-OFFICIAL-Transcript_FINAL.pdf |
| Q3FY24 | 2024-03-21 | Donahoe | Friend | 29 | 8,793 | 9398 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9398/webcast_transcript/NIKE-Inc-Q3FY24-OFFICIAL-Transcript-FINAL.pdf |
| Q4FY24 | 2024-06-27 | Donahoe | Friend | 30 | 9,460 | 9399 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9399/webcast_transcript/NIKE-Inc-Q4FY24-OFFICIAL-Transcript_FINAL.pdf |
| Q1FY25 | 2024-10-01 | Donahoe | Friend | 20 | 7,095 | 9400 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9400/webcast_transcript/NIKE-Inc-Q1FY25-OFFICIAL-Transcript_-FINAL.pdf |
| Q2FY25 | 2024-12-19 | Hill | Friend | 29 | 9,502 | 9401 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9401/webcast_transcript/NIKE-Inc-Q2FY25-OFFICIAL-Transcript_-FINAL.pdf |
| Q3FY25 | 2025-03-20 | Hill | Friend | 30 | 9,404 | 9402 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9402/webcast_transcript/NIKE-Inc-Q3FY25-OFFICIAL-Transcript_-FINAL.pdf |
| Q4FY25 | 2025-06-26 | Hill | Friend | 27 | 8,747 | 9403 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9403/webcast_transcript/NIKE-Inc-Q4FY25-OFFICIAL-Transcript_-FINAL.pdf |
| Q1FY26 | 2025-09-30 | Hill | Friend | 26 | 8,799 | 9404 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9404/webcast_transcript/NIKE-Inc-Q1FY26-OFFICIAL-Transcript_-FINAL.pdf |
| Q2FY26 | 2025-12-18 | Hill | Friend | 28 | 9,025 | 9405 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9405/webcast_transcript/NIKE-Inc-Q2FY26-OFFICIAL-Transcript_-FINAL.pdf |
| Q3FY26 | 2026-03-31 | Hill | Friend | 26 | 8,680 | 9406 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9406/webcast_transcript/NIKE-Inc-Q3FY26-OFFICIAL-Transcript.pdf |
| Q4FY26 | 2026-06-30 | Hill | Friend | 25 | 8,836 | 9540 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9540/webcast_transcript/NIKE-Inc-Q4FY26-OFFICIAL-Transcript_-FINAL.pdf |
| Q1FY27 | 2026-10-01 | Hill | Denton | 25 | 8,239 | 9591 | https://investors.nike.com/_assets/_5c5e7dfb9b8f3a4f8235c64466d81cf9/nike/db/938/9591/webcast_transcript/NIKE+Inc.+Q1FY27+OFFICIAL+Transcript_+FINAL.pdf |

## Other files in data/hunt/earnings_calls (run in this order, each with `python3 -I` from the repo root or this folder)

| Script | Output | What it does |
|---|---|---|
| 01_extract_transcripts.py | transcripts/*.txt | PDF to text with page markers |
| 02_parse_turns.py | turns.csv | Speaker turns, prepared vs Q&A, role, page, words |
| 03_language_trends.py | language_trends.csv, tone_index.csv | Term counts per 10,000 words by section and by CEO or CFO |
| 04_promise_candidates.py | promise_candidates.csv | Every management sentence pairing a forward verb with a date (451 rows, raw) |
| 05_guidance.py | guidance_specificity.csv, guidance_scorecard.csv | Hand-coded guidance detail by call; next-quarter guide vs reported actual (actuals from data/nike_filing_facts.csv) |
| 06_qa_analysis.py | qa_pairs.csv, qa_topics_by_quarter.csv | Analyst question topics, answer length, numeric specificity, deflections |
| 07_fy28_clues.py | fy28_clues.csv | Every FY28-or-later, long-term and Investor Day sentence since Q3 FY24 |
| 08_promise_tracker.py | promise_tracker.csv, promise_events.csv | 27 curated promises and 83 dated statements, every quote verified word for word |
| 09_peer_mentions.py | peers/peer_calls_summary.csv, peers/peer_nike_mentions.csv, peers/text/*.txt | Nike mentions in 14 DICK'S and Academy calls 2024 to 2026 (Motley Fool pages in peers/peer_urls.txt, downloaded 2026-10-14, OPENED); tone hand-coded |
| pagefind.py | (helper) | Finds the PDF page of a quoted sentence |
