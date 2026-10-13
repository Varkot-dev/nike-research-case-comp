# Prior art: what other projects do, and what this skill took from them

Surveyed Oct 13, 2026. Star counts are GitHub search API values from that day. Each source marked "opened" was read directly; the key claims behind adopted rules were re-checked on the source page before use (the "verified" column).

## Where this skill stands
No project found combines these four things:
1. XML-level patching with workbook-wide reference rewriting, proven against LibreOffice's own insert on a real Excel model: 0 differences across 9,225 values (fidelity.md).
2. Two-engine verification: LibreOffice, plus the `formulas` package via `xl.py crosscheck`.
3. A rule-labelled audit.
4. A builder that makes inconsistent rows impossible.

Some projects have features this skill does not:
- Excel MCP servers can create native pivots and 16 chart types.
- sbroenne/mcp-server-excel drives real Excel through COM, so it can evaluate data tables and Goal Seek. That needs Windows.

## Projects and what was adopted

| Project | What it does well | Adopted here | Verified |
|---|---|---|---|
| anthropics/skills, xlsx skill (180,908 stars) https://github.com/anthropics/skills | LibreOffice recalc with JSON error summary; external-link guard; `_xlfn.` function rules; lowercase-on-parse-failure tell | Recalc moved to a COPY (theirs rewrites in place); external-link guard on `--refresh-cache`; "LibreOffice could not parse" detection in `verify` | read in full in this environment (/mnt/skills/public/xlsx) |
| anthropics/financial-services, financial-analysis skills (39,698 stars) https://github.com/anthropics/financial-services | dcf-model: odd-sized sensitivity grids whose centre equals the model, no Data Tables, a "Source:" comment on every hardcode; audit-xls: report table plus Clean/Minor/Major rating, report-first; 3-statement: master check, scenario hierarchy | `grid_assertions` (odd size, centre = base, distinct, monotonic); builder writes a "Source:" comment on every input; audit rating and table; `scenarios --order` hierarchy check; report-first rule in SKILL.md | dcf-model SKILL.md quotes re-checked on the raw file |
| petehottelet/spreadsheet-auditor (9 stars) https://github.com/petehottelet/spreadsheet-auditor | Rule IDs (LIVE_ERROR, BROKEN_REFERENCE, TOTAL_MISMATCH, IFERROR_MASK, LITERAL_CONSTANT); labels for mode (DET/HEUR) and confidence (Defect, Likely defect, Review, Info); annotated workbook copy; SARIF; `--fail-on` | Finding schema (id, severity, confidence, mode, fix); `--annotate` REVIEW copy; `--suppress`; `--fail-on` exit 2 | README re-checked |
| PerfectXL Risk Finder library https://www.perfectxl.com/learning-center/risk-finder-library/ | 54 inspections with thresholds | Hardcoded-number exclusions (0, 1, 10% to 100%; factors 2, 4, 7, 12, 24, 30, 31, 52, 53, 60, 100, 365, 1000, 3600 in * or /); approximate lookups; double count; formula interrupted by other formula, data or blank (other formula and data only when they cover 20% or less of the run); complexity (length 200 or more, 8 or more distinct operations, nesting of 5 or more, 10 or more references); invisible values | thresholds quoted from the page |
| ExceLint (Barowy, Berger, Zorn, OOPSLA 2018) https://arxiv.org/pdf/1901.11100 | Reference-vector fingerprints and entropy-based rectangular regions | Simplified form: a cell whose relative (R1C1) shape differs from two agreeing neighbours, checked along both rows and columns | paper (via research agent) |
| Microsoft Inquire, via O'Beirne, EuSpRIG 2013 https://arxiv.org/pdf/1401.7586 | Unused inputs, formulas referencing hidden cells or text, numbers stored as text | UNUSED_INPUT (scoped to input-styled cells), HIDDEN_CELL_REFERENCED, REF_TO_TEXT (arithmetic operands only), NUMBER_STORED_AS_TEXT | paper (via research agent) |
| Hermans et al., formula smells, TUD-SERG-2013-022 | Multiple operations, multiple references, conditional complexity, long calculation chain, duplicated formulas | COMPLEX_FORMULA and NESTED_IF (PerfectXL thresholds). Not yet: calculation-chain length, duplicated subtrees | paper (via research agent) |
| vinci1it2000/formulas (501 stars) https://github.com/vinci1it2000/formulas | Pure-Python Excel engine; circular support; compile a workbook to a function | `xl.py crosscheck`: second-engine agreement check. Measured: 131 of 131 on the Jordan workbook; 1,222 of 1,231 on Damodaran's model (9 explained: 2 dates where `formulas` ignores the 1904 date system, 7 unconverged circular cells) | installed and run here |
| haris-musa/excel-mcp-server (4,235 stars) https://github.com/haris-musa/excel-mcp-server | 44 tools including chart (16 types), pivot, slicer, sparkline creation; `describe_workbook` first; evaluator reports `uncalculated` cells with a reason | `map` and `features` as the mandatory first step (already present); `read` with citation URI; crosscheck reports cells the second engine could not evaluate | README (via research agent) |
| knowledgestack/excel-parser https://github.com/knowledgestack/excel-parser | Chunks with `file.xlsx#Sheet!A1:F18` source URIs and dependency summaries | `xl.py read` prints the same URI form | README (via research agent) |
| lianghsun/open-sheet https://github.com/lianghsun/open-sheet | Named-cell model authoring; CI recalcs in LibreOffice and diffs against its own evaluator | Same pattern: builder keys plus LibreOffice plus a second engine | README (via research agent) |
| jeremylongshore/excel-analyst-pro-skill-md https://github.com/jeremylongshore/excel-analyst-pro-skill-md | Never call a formula "verified" before a recalc and reopen; edit a copy by default | Stated in SKILL.md rules | README (via research agent) |
| andreworia/claude-excel-skills https://github.com/andreworia/claude-excel-skills | Assumption registry and sensitivity tornado skills | `xl.py tornado`; builder source comments act as the registry | README only |

## Not adopted (and why)
- **Native Excel 2016 waterfall and funnel charts (chartex):** they do not render in LibreOffice or convert to Sheets. Stacked series with an invisible base render everywhere.
- **Excel Data Tables:** they cannot be verified here (fidelity.md). anthropics/financial-services bans them for the same reason.
- **SARIF output:** JSON findings plus `--fail-on` covers the CI use. Add SARIF if a GitHub code-scanning integration is wanted.
- **Full ExceLint entropy partitioning:** the two-neighbour rule catches the same lone-cell errors at a fraction of the code. Revisit if block-level errors (a wrong rectangle of formulas) show up in practice.
- **COM automation of real Excel:** not available on Linux.
