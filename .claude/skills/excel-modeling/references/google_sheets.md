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

## Measured conversions
None yet. The first time a model goes to Sheets, run the checks above and log the results here, with the date and the feature list from `xl.py features`.
