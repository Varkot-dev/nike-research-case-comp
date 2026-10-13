---
name: excel-modeling
description: Build, edit, audit and verify financial models in Excel (.xlsx) and Google Sheets the way a sell-side or Wharton-trained modeler would, editing workbooks surgically instead of regenerating them. Use whenever a task touches a spreadsheet model; examples are a DCF, LBO, three-statement or operating model, scenario or sensitivity tables, changing an input or formula in an existing workbook, adding a row or year, checking a model for errors, explaining where a number comes from, or putting a model into Google Sheets.
---

# Excel and Sheets modeling

Three ideas run through this skill:
1. **Edit, don't rebuild.** An existing workbook is changed at the XML level, cell by cell, so charts, sparklines, formats, comments and the user's own edits survive byte for byte.
2. **Nothing ships unverified.** LibreOffice recalculates a throwaway copy, then the audit, the diff and the checks prove that the change did what was intended and only that.
3. **Models are consistent by construction.** New models come from a declarative builder where each row has one formula template, so the classic errors (a mid-row plug, a typed number in a formula, a broken copy-across) cannot happen.

Tools: `scripts/xl.py` (CLI), `scripts/xlcore.py` (library), `scripts/model_builder.py` (new models). Tests: `python3 tests/test_xl.py` (about 3 minutes; proves insert and patch against LibreOffice). References: `references/modeling_standards.md` (layout, formatting, checks, scenarios, circularity, valuation review), `references/formulas.md` (portable formulas and patterns), `references/fidelity.md` (what each save path destroys, measured), `references/google_sheets.md`.

In the commands below, `XL` means `python3 .claude/skills/excel-modeling/scripts/xl.py`.

## Step 0: route the request

| The request is... | Path |
|---|---|
| A new model | **Build** (B) |
| A change to a workbook that a repo script generates (its header names the script, or `scripts/*_xlsx.py` writes it) | Edit the script and regenerate (repo rule: regenerate, don't hand-edit). Then use `XL diff old new` to confirm only the intended cells moved. |
| A change to a workbook a person owns or edited (uploaded, from Drive, or edited in Excel) | **Patch** (P). Never regenerate it, which would destroy their edits. |
| "Is this right?", "check the model", "why is X this number?" | **Audit and trace** (A) |
| "What if X?", sensitivity, scenario comparison | `XL sensitivity` (S) |
| Google Sheets in any form | Read `references/google_sheets.md` first: Sheets cannot be edited in place from here. |

## Step 1: map before touching anything (every path)
```
XL features model.xlsx     # risky parts: sparklines, dynamic arrays, data tables, macros, pivots, external links; recommended engine
XL map model.xlsx [--sheet S] [--max-rows 120]   # per row: label, formula pattern, inputs, live values from a fresh recalc
```
Read the map, not the raw cells. It costs a few hundred lines instead of thousands, and it shows the conventions to match: timeline row, label column, input colour, units column and sheet order. **An existing file's conventions beat every rule in this skill.**

Never save a workbook with openpyxl unless `features` shows none of: sparklines, dynamic arrays, x14 extensions, slicers, data tables, form controls or macros. Even then openpyxl wipes every cached value (fidelity.md), so `xl.py patch` is the default engine for any existing file.

## P: patch an existing workbook
1. Write the ops as JSON. Address cells by A1 address, by `{"row": "<label>", "col": "<header>"}`, or (builder models) by `{"key": "<row key>", "col": "FY2028E"}`. Labels and keys survive row insertions; A1 addresses do not.
```json
[
 {"op": "set",   "sheet": "Inputs", "cell": {"key": "wacc"}, "value": 0.095},
 {"op": "set",   "sheet": "Model",  "cell": "D14", "formula": "=C14*(1+D13)", "style_like": "C14"},
 {"op": "fill",  "sheet": "Model",  "src": "D14", "range": "E14:J14"},
 {"op": "insert_rows", "sheet": "Model", "at": 12, "n": 1, "copy_from": 11},
 {"op": "insert_cols", "sheet": "Model", "at": "H", "n": 1, "copy_from": "G"},
 {"op": "style", "sheet": "Model", "range": "C20:J20", "like": "C19"},
 {"op": "name",  "name": "Circ", "ref": "Inputs!$C$30"},
 {"op": "iterate", "on": true}
]
```
2. Run `XL patch model.xlsx ops.json --out model_v2.xlsx --refresh-cache`. It edits only the target XML, expands shared formulas before touching them, refuses to write inside a multi-cell array, drops `calcChain.xml` (a stale chain makes Excel "repair" the file), sets `fullCalcOnLoad`, recalculates a copy, reports errors and the values of the cells it wrote, and with `--refresh-cache` writes fresh cached values so previews, pandas and GitHub show real numbers.
3. Run `XL diff model.xlsx model_v2.xlsx --expect "Inputs!C17,Model!D14:J14"`. `unexpected_input_or_formula_changes` must be empty.
4. Run `XL audit model_v2.xlsx`. No new issues compared with the audit of the original. Inherited issues are reported to the user, not silently fixed.

**Inserting rows or columns** rewrites every reference the way Excel does: formulas on all sheets, defined names, chart series, conditional formats, validations, merged cells, tables, drawings, comments, sparklines and pivot sources. It matches LibreOffice's own insert on every test case, and handles sparklines better than LibreOffice. Insert **inside** a block that a SUM covers (above the last item), not directly under it, otherwise the total will not include the new row (Excel behaves the same). `copy_from` copies styles and translated formulas from a neighbouring row. Deleting rows is not supported: blank the row and tell the user, or ask them to delete it in Excel.

## B: build a new model
Write a repo script (`scripts/<name>_xlsx.py`) that uses `model_builder`. `scripts/jordan_valuation_xlsx.py` is the worked example: scenario switch, timing rows, margin ramp, corkscrew-free DCF, checks, and a proof block that flips every scenario and matches the Python model's CSVs to the cent.
```python
m = Model(OUT, "Title", ["FY2027E", ...], description="...")
inp = m.list_sheet("Inputs"); inp.switch("case", "Active scenario", ["Bear", "Base", "Bull"], "Base")
inp.scalar("j26", "Jordan revenue FY2026", J26, "$m", "FY2026 Form 10-K p. 32")   # input, blue, with source
inp.scenario("g", "Terminal growth", "%", {"Bear": .01, "Base": .025, "Bull": .03}, "ASSUMPTION")
md = m.timeline_sheet("Model")
md.scenario_rows("growth", "Revenue growth", "%", {"Bear": [...], ...})                # case rows + live CHOOSE row
md.row("rev", "Revenue", "$m", "={rev[-1]}*(1+{growth})", first="={Inputs.j26}*(1+{growth})")
val = m.list_sheet("Valuation"); val.calc("ev", "DCF value", "$m", "={pv_fcf}+{pv_tv}")  # formula scalar
m.check("Value = PV(FCF) + PV(TV)", "={Valuation.ev}-SUM({Model.pv@all})-{Valuation.pv_tv}")
print(m.save())   # writes, recalculates, caches values, returns verify status
```
Template tokens: `{key}` same column, `{key[-1]}` prior period, `{Sheet.key}` cross-sheet, `{key@FY2031E}` one fixed period, `{key@all}` the whole period range, plus `{col}`, `{period}` and `{idx}`. Unknown keys and look-backs before the first period raise errors at build time, not as `#REF!` later. Every row gets a defined name `k_<Sheet>_<key>` so later patches find it by key.

Then: `XL audit` must be empty, the master check must be 1 in every scenario (loop over them with `xlcore.LOSession`, as the Jordan script does), and if a Python model exists, prove that the workbook reproduces its outputs.

## A: audit and trace
```
XL audit model.xlsx         # JSON: errors, inconsistent rows, plugs, literals in formulas, refs to blanks,
                            # bare new functions (#NAME? risk), volatile, whole-column, IFERROR, circularity,
                            # SUM ranges that skip a line item, colour-convention breaks, % stored as 5 not 0.05
XL trace model.xlsx "Valuation!C10" --depth 3          # precedents with live values and row labels
XL trace model.xlsx "Inputs!C17" --dependents          # what an input drives
XL verify model.xlsx --cells "Valuation!C10,Checks!D7"
```
Each audit finding is a claim to check by reading the cell, not an automatic fix. To explain a number, trace it and give the dollar or basis-point decomposition the repo's CLAUDE.md requires, never a narrative.

## S: sensitivities and scenarios
`XL sensitivity model.xlsx "Valuation!C10" --row "Inputs!C17=0.08,0.09,0.10,0.11" --col "Inputs!E21=0.08,0.11,0.14"` recalculates the full model at every grid point through LibreOffice (about 2 seconds for a 3x3 grid). `--write "Outputs!B30" --out new.xlsx` lays the verified grid into the workbook as a labelled static block. Use it in place of Excel data tables, which LibreOffice cannot evaluate (fidelity.md); if the user specifically wants a live data table, explain that trade-off first.

## Gotchas that bite (all verified here; details in references/fidelity.md)
- openpyxl save: drops sparklines and dynamic-array metadata, and blanks **every** cached value. `data_only=True` plus save destroys every formula. Use openpyxl only to read.
- LibreOffice re-save rewrites custom number formats and kills dynamic arrays. Only ever recalculate a **copy** (`xlcore.lo_recalc_copy`), never deliver its output.
- `soffice --convert-to` alone does not recalculate; `lo_recalc_copy` sets the recalc-on-load profile flag.
- This LibreOffice (24.2) cannot evaluate XLOOKUP, XMATCH, FILTER, SORT, UNIQUE or SEQUENCE, and returns `#N/A` for `[@Col]` structured references. Use INDEX/MATCH and plain ranges (formulas.md).
- LibreOffice has no boolean type. Write checks as `IF(cond,1,0)`.
- Shared formulas (`t="shared"`): editing the master cell without expanding first silently changes every dependent. `xl.py` expands automatically.
- After any formula edit, drop `calcChain.xml` and set `fullCalcOnLoad`. `xl.py` does both.
- Iterative calculation converges only to `iterateDelta`, so check tolerances must exceed it. Without iteration, a circular model shows `#VALUE!` in LibreOffice.
- Excel data-table input cells must be on the same sheet as the table.
- Sheet names with spaces need quotes in references (`'Model Calc'!B2`). `xlcore.quote_sheet` handles this.
- Percentages are stored as fractions; years are text headers; never round inside calculations, only in number formats.

## Repo rules that apply to every workbook
- Every hard-coded input carries its source in the note column, in the house citation format (`FY2026 Form 10-K p. 32`, `market data, ... (Oct 13, 2026)`, `ASSUMPTION`). Pull filing numbers from `data/nike_filing_facts.csv`, never typed from memory (nike-report-update skill).
- No em-dashes or en-dashes in labels, notes or sheet names.
- The workbook, its generating script and any finding it produces are committed and pushed in the same session (CLAUDE.md).
- When a measured behaviour here turns out wrong, or a new one is found (for example after a Google Sheets conversion), update `references/fidelity.md` or `google_sheets.md` and add a test, so the skill keeps learning.
