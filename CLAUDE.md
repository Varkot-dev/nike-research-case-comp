# Nike research repo: standing instructions

## Every explanation must be financial and data driven
This repo supports a stock pitch. Never explain a result with a generic, consumer-sentiment or common-sense statement such as "fewer people want the shoes," "the brand lost its cool," "demand is weak," "it's a bright spot," or "this is the swing factor." Those statements are not acceptable in notes, the report, chart titles or chat replies.

Instead, every "why" must be decomposed into measurable drivers, with a source or labelled arithmetic for each:
- **Revenue:** split into units versus price (ASP), channel (Direct versus wholesale), geography, and currency, using the figures Nike reports.
- **Margin:** gross margin bridge items in basis points (Nike's own bridge), then costs below gross profit as a share of revenue (deleverage).
- **Profit:** a dollar bridge (volume, rate, opex), and a sensitivity where it helps the thesis (for example, "EBIT would be $X higher at the FY2024 margin").
- **Ranking claims** ("largest," "only," "best"): compute them across every segment from the data before writing them, including any one-time items.
- If filings cannot separate two causes (for example, deliberate supply cuts versus lower sell-through), say exactly that, instead of filling the gap with a qualitative guess.
- Management and analyst opinions may be quoted verbatim as evidence, labelled as opinion, but never used as the explanation on their own.

## Go down the rabbit hole
- For every "why," list every plausible explanation, then test each one against data until all but one are ruled out. Write down the alternatives that were ruled out and the evidence that ruled them out.
- If more than one explanation still survives, keep digging: other filings, peers, retailers, suppliers, third-party data. If the data truly cannot separate them, say exactly which explanations remain and what data would decide between them.
- Parallelize heavy research with subagents (the user has approved launching many when needed). Every agent result is verified against its source before it enters the repo.

## Always push what you learn
- Every finding goes into the repo (data, research_notes, and REPORT.md when it changes the pitch), is committed and pushed to GitHub in the same session. Nothing learned stays only in chat or scratch files.

## Other rules
Follow `.claude/skills/nike-report-update/SKILL.md` (citations, labels, no em-dashes or en-dashes, regenerate rather than hand-edit) and `.claude/skills/sec-filing-research/SKILL.md`. For any spreadsheet model (build, edit, audit, sensitivity, Google Sheets) follow `.claude/skills/excel-modeling/SKILL.md`: patch existing workbooks surgically with its `xl.py`, never rebuild a workbook a person has edited. **Downloads:** fetch Nike filings from the investors.nike.com mirror (see the sec-filing-research skill), not www.sec.gov. Never put the user's email address in an HTTP request (for example a SEC User-Agent) unless the user explicitly provides it for that purpose.
