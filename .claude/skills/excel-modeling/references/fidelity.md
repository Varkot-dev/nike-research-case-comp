# What survives an edit: measured, not assumed

Everything on this page was produced in this environment (openpyxl 3.1.5, LibreOffice 24.2.7, lxml 6.1). Re-run any of it before relying on it after a library upgrade:

- `python3 tests/fidelity_lab.py` rebuilds the round-trip table below.
- `python3 tests/test_xl.py` re-proves the insert-rows, insert-cols and patch behaviour against LibreOffice.

## Round trip by save path

| feature | original | openpyxl load+save | LibreOffice re-save | xl.py patch |
|---|---|---|---|---|
| chart | kept | kept (re-serialised, formatting may change) | kept | kept, byte-identical |
| sparkline | kept | **LOST** | kept | kept |
| table (ListObject) | kept | kept | kept | kept |
| comment | kept | kept | kept | kept |
| defined name | kept | kept | kept | kept |
| data validation | kept | kept | kept | kept |
| conditional format | kept | kept | kept | kept |
| freeze panes | kept | kept | kept | kept |
| dynamic array metadata | kept | **LOST** (spill becomes a legacy CSE array) | **LOST** | kept |
| cached formula values | kept | **LOST** (every formula written with an empty `<v>`) | kept (recomputed) | kept (edited cells cleared; `--refresh-cache` rewrites all) |
| custom number format kept verbatim | kept | kept | **LOST** (rewritten as `\$#,##0;"($"#,##0\);\-`) | kept |

A one-cell `xl.py patch` changes exactly two zip parts: that sheet's XML and `xl/workbook.xml`, which gets the `fullCalcOnLoad` flag. Every other part is byte-identical; `tests/test_xl.py` asserts this.

## Other verified behaviours

| Behaviour | Evidence |
|---|---|
| openpyxl prints `Sparkline Group extension is not supported and will be removed` on load. | fidelity lab output |
| LibreOffice 24.2 cannot evaluate `_xlfn._xlws.SORT` and writes it back lowercased with `#NAME?`. | lab, `rt_lo.xlsx` H1 |
| LibreOffice returns `#N/A` for a structured reference `Tbl[[#This Row],[V]]` inside a table. | lab, `rt_lo.xlsx` C6 |
| `soffice --convert-to` does NOT recalculate an xlsx by default; cached values pass through unchanged. `xlcore.lo_recalc_copy` fixes this by writing `OOXMLRecalcMode=0` into a throwaway profile. | lab: plain convert kept xlsxwriter's 0s; the profile run computed 1050, 1102.5 and so on |
| LibreOffice's own Insert Rows does not update sparkline ranges (stays `B2:F2` at `G2`). `xl.py` does (`B2:G2` at `H2`), which is what Excel does. | `tests/test_xl.py` working files |
| Inserting a column immediately right of a formatted block: Excel and LibreOffice grow conditional-format and validation ranges into it ("format same as left"). `xl.py` mimics this. Formulas are NOT extended. | test case `Model-col7x1` |
| Inserting a row directly below a `SUM(B5:B6)` block does not extend the SUM (Excel, LibreOffice and xl.py agree). Insert inside the block, or keep a blank spacer row inside the range. | test case `Model-row7x2` |
| Excel What-If data table (`<f t="dataTable" ...>`): LibreOffice imports it as `MULTIPLE.OPERATIONS` (formula visible as `TABLE(...)`), but returned the base-case value in every cell for a cross-sheet model and blanks for a same-sheet model. LibreOffice cannot verify a data table. Use `xl.py sensitivity` (brute force over UNO) to get verified numbers. | lab, `dt.xlsx` and `dt2b.xlsx` |
| Iterative calculation: with `calcPr iterate="1"`, LibreOffice solved interest on average debt to 89.47366 against an exact 89.47368, a gap inside `iterateDelta` 0.001. Without iteration the circular cells return `#VALUE!` (Err:522). | lab, `Circ` sheet |
| LibreOffice has no boolean type: `=A1>B1` is 1, and `ISLOGICAL()` of it is FALSE. A check written as `IF(ISLOGICAL(x),...)` passes in Excel and fails in LibreOffice. | jordan_valuation_xlsx.py master check, first run |
| `pandas.read_excel` on an openpyxl-written file returns NaN for every formula; after `--refresh-cache` it returns the numbers. | `tests/test_xl.py` |

## Real-world stress test: an Excel-saved valuation model

Damodaran's `fcffsimpleginzu.xlsx` (https://pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx, downloaded Oct 13, 2026) has 17 sheets, 553 shared-formula cells, x14 validations, threaded comments, an image, a table, `iterate="1"` and a deliberate circularity. `python3 tests/oracle_compare.py <file> "Input sheet" row 20` and `... "Valuation output" col G` gave:

| Test | Formula-level cells | Differences from LibreOffice's insert | Numeric values after recalc | Differences |
|---|---|---|---|---|
| Insert row 20 on Input sheet | 1,265 | 0 | 9,225 | 0 |
| Insert column G on Valuation output | 1,265 | 0 | 9,225 | 0 |

The x14 validations show the gap between the two save paths. `xl.py` shifted them in place (B37 to B38 and so on) and kept them as x14. LibreOffice converted them to the standard form, so its copy is no longer Excel's original structure. LibreOffice also rewrites `FALSE` as `FALSE()` and turns cached `#DIV/0!` results into literal `=#DIV/0!` formulas; the comparison normalises both. `xl.py audit` on the same file found the circular loop (synthetic rating > cost of capital > operating lease converter > synthetic rating) and 51 numbers typed into formulas (for example `=474.8+256.6`).

## Sources for facts not measured here

| Fact | Source |
|---|---|
| Sheets limits: "Up to 20 million cells or 100MB for spreadsheets that are created in or converted to Google Sheets." | https://support.google.com/drive/answer/37603 (opened Oct 13, 2026) |
| On Excel to Sheets conversion, "any cell with more than 50,000 characters will be removed in Sheets." | same page |
| Not supported in Sheets: "Macros (you can implement your macro in Apps Script)", "Linked spreadsheets in Excel files", and "When you transfer protected workbooks and worksheets from Excel to Google Sheets, your locked and hidden cells become viewable and editable in Google Sheets." | https://support.google.com/docs/answer/6055139 (opened Oct 13, 2026) |
| `calcPr` schema defaults: iterate false, iterateCount 100, iterateDelta 0.001. LibreOffice's importer defaults a missing `iterateDelta` to 0.0001, so always write it explicitly (`xlcore.force_full_calc` does). | https://schemas.liquid-technologies.com/officeopenxml/2006/calcpr.html ; LibreOffice `sc/source/filter/oox/workbooksettings.cxx` (secondary, via research agent; the 0.0001 matches what LibreOffice wrote in our lab file) |
| LibreOffice exports data tables without the `dt2D`, `r1` and `r2` attributes (marked `OOXTODO`), so a data table does not survive a LibreOffice save. | LibreOffice `sc/source/filter/excel/xetable.cxx` (secondary, via research agent) |
| LibreOffice 24.8 added XLOOKUP, XMATCH, FILTER, SORTBY, UNIQUE and LET; 25.8 added TAKE, DROP, HSTACK and CHOOSECOLS. This environment runs 24.2, which has none of them. | https://wiki.documentfoundation.org/ReleaseNotes/24.8 and /25.8 (secondary, via research agent) |

## Not yet verified (test before relying on them)

What Google's xlsx-to-Sheets conversion does to these: data tables, the iterative calculation flag, sparklines, dynamic arrays, `_xlfn.` functions, named ranges, structured references and custom number formats. No official Google page covers them. See `google_sheets.md` for the upload-and-export test that settles each one.
