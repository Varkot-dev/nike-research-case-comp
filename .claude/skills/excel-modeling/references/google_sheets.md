# Google Sheets

## What the tools in this environment can and cannot do
The Google Drive connector (`mcp__Google_Drive__*`) offers:
- `create_file`: upload content. An `.xlsx` uploaded with `contentMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` is **converted to a native Google Sheet by default** (`disableConversionToGoogleType: true` keeps it as an .xlsx in Drive).
- `download_file_content`: export a native Sheet as `.xlsx` (`exportMimeType` set to the xlsx MIME type), returned as base64.
- `read_file_content`: a text rendering for a quick read, including comments.
- `update_file`: **title and folder only.** There is no cell-level write and no content replacement.

So there is **no in-place edit of a native Google Sheet** from here. Every change produces a new Sheet, which gets a new link and loses the old file's sharing, comments and version history. Plan around that:

| Situation | Do this |
|---|---|
| New model the user wants in Sheets | Build the .xlsx (model_builder), verify, `--refresh-cache`, upload with conversion, then run the post-upload checks below. Keep the .xlsx in the repo as the source of truth. |
| User edited a Sheet and wants changes | Export it to .xlsx (`download_file_content`), `xl.py map` and `diff` it against the repo copy to absorb their edits, `patch`, verify, then upload as a NEW Sheet named with a version suffix (for example "Jordan valuation v3"). Tell the user the link changed and the old one still holds their comments. Never trash their original. |
| A small edit to a live Sheet that other people use | Give the user the exact cells and formulas to paste (the `diff` output is that list). Ask before replacing a shared file. |
| A Drive-hosted .xlsx (not converted) | Download it, patch it, and re-upload with `disableConversionToGoogleType: true` as a new file. Same caution about links. |

`google-workspace` (an anthropic skill) covers Docs, Sheets and Slides editing tools when they are connected. Check whether it offers cell-level Sheets writes before falling back to the new-file route.

## Design for Sheets from the start
- Sheets supports XLOOKUP, LET, LAMBDA, FILTER, SORT, UNIQUE and SEQUENCE natively (https://support.google.com/docs/table/25273, via research agent), but our verifier (LibreOffice 24.2) does not. Stick to the portable set in formulas.md, so the file verified here is the file the user gets.
- Native Sheets limit: 20 million cells or 100MB; cells over 50,000 characters are dropped on conversion (https://support.google.com/drive/answer/37603).
- Not supported after conversion (https://support.google.com/docs/answer/6055139): macros, links to other spreadsheets, and protection (locked and hidden cells become editable and visible). Do not rely on sheet protection to guard inputs.
- Excel What-If data tables have no Sheets equivalent. Ship sensitivities as a static grid from `xl.py sensitivity --write`, labelled with the command that rebuilds it.
- Iterative calculation is a per-spreadsheet setting in Sheets (File > Settings > Calculation > Iterative calculation; https://workspaceupdates.googleblog.com/2016/12/new-iterative-calculation-settings-and.html). Whether conversion carries over Excel's `iterate` flag is unverified, so tell the user to switch it on if the model has a circularity, or remove the circularity (modeling_standards.md section 6).
- Named ranges in Sheets allow letters, digits and underscores only. model_builder's `k_<Sheet>_<key>` names follow that rule on purpose.
- Sheets dates count from 1899-12-30 (Excel from 1900-01-01 with the 1900 leap-year bug); they agree from March 1900 onward.

## Post-upload checks (the conversion is a black box: verify it)
1. `download_file_content` the new Sheet as .xlsx into the scratchpad.
2. `xl.py verify` on the export: zero errors.
3. `xl.py diff original.xlsx export.xlsx --values` and look for:
   - formulas Sheets rewrote (it adds or strips function prefixes);
   - values that moved (a function that computes differently);
   - lost rows or named ranges.
4. Compare the headline outputs (master check, valuation per share) between the two files.
5. Record what changed in this file's "Measured conversions" section below, so the knowledge compounds.

## Measured conversions (Oct 13, 2026, Google Drive connector)

Method: upload a small .xlsx with `create_file` (conversion to a native Sheet is the default), then read what Sheets computed with `read_file_content`. Probe workbook: `tests/gsheets_lite.py` (3.8 KB; every probe row carries an expected value). Real model: the Jordan valuation with its charts and comments stripped (10.8 KB).

**Verified: these survive conversion and compute the same numbers**

| Feature | Result |
|---|---|
| Defined name (`=B2*(1+Growth)`) | Works: 1,050 |
| Cross-sheet SUMIFS, INDEX/MATCH, SUMPRODUCT | Match |
| `_xlfn.XLOOKUP`, `_xlfn.IFS`, `_xlfn.TEXTJOIN`, `_xlfn.MAXIFS` | Match, including XLOOKUP, which LibreOffice 24.2 cannot evaluate |
| Legacy CSE array `{=SUM(A*2)}` | Matches (200) |
| EOMONTH and date serials | Same serial, same date (46,053 shows 1/31/2026), so the epochs agree |
| XNPV(rate, values, dates) | Matches LibreOffice (4.13223) |
| Number formats `0.0%_);(0.0%);"-"_)`, `0.0"x"`, `$#,##0.00_);($#,##0.00);"-"_)` | Preserved: 5.0%, 12.5x, ($1,234.50) |
| Text year `FY2027E` | Stays text |
| Array constant inside MATCH (`MATCH(C5,{"Bear","Base","Bull"},0)`), CHOOSE, MAX, AND-style checks | Match |
| Jordan model, full chain (scenario switch, margin ramp, DCF, checks, cover) | Matches the local calculation: DCF $5,639m, $3.79 per share, 10.7% of price, terminal share 78.1%, all five checks and the master check pass, the Cover reads "OK: all checks pass" |

**Verified: these break or change silently**

| Feature | Result | What to do |
|---|---|---|
| Iterative calculation flag (`calcPr iterate="1"`) | Not carried over: interest on average debt shows `#REF!` (circular dependency) | Turn it on in Sheets (File > Settings > Calculation), or avoid circularity (modeling_standards.md section 6) |
| Excel What-If data table (`t="dataTable"`) | Flattened to the cached values, with no error and no recalculation: the grid showed its cached zeros | Never ship a data table to Sheets. Use `xl.py sensitivity --write` (static, labelled) or formula grids |
| Dynamic array stored as `_xlfn._xlws.SORT(...)` | `#NAME?`. Google reads `_xlfn.XLOOKUP` but not the `_xlfn._xlws.` prefix. Caveat: the probe wrote it as a legacy array with no `cm` metadata, so a file saved by real Excel may behave differently | Avoid SORT, FILTER and UNIQUE in files headed for Sheets, or rewrite them as Sheets-native formulas after upload |

**Not verified (the Drive connector cannot see structure)**

Data validation lists, conditional formats, frozen panes, sparklines, charts, cell notes, structured table references, font colours and fills. `read_file_content` returns values only, and `download_file_content` returns the whole export as base64 inside the reply, which cannot be diffed without retyping it. With a Sheets editor connector, `get_spreadsheet` with `includeGridData` would settle all of these.

**Practical limits of uploading**
- The file travels inside the call as base64 text, and long payloads get corrupted in transit. A 17 KB payload failed ("Invalid conversion requested"), a 6.6 KB one failed ("Request contains an invalid argument"), while 2.1 KB, 5.1 KB and 14.5 KB payloads converted. A rejected upload means a damaged copy, not an unsupported feature. Keep the payload small and retry.
- To test a model, strip what the connector cannot verify anyway (theme, docProps, comments, charts) and compare the computed values.
- Every test upload creates a new file in the user's Drive. Link them, say what they are, and offer to trash them. Never trash without being asked.
