# Formula cookbook and portability

## Portability: write formulas that compute the same in Excel, LibreOffice (our verifier) and Google Sheets

| Need | Use | Avoid, and why |
|---|---|---|
| Lookup | `INDEX(range, MATCH(key, keys, 0))` | `XLOOKUP` and `XMATCH`: LibreOffice 24.2 here gives `#NAME?`, so the result cannot be verified. Written without the `_xlfn.` prefix it is also `#NAME?` in Excel. |
| Two-way lookup | `INDEX(grid, MATCH(r, rows, 0), MATCH(c, cols, 0))` | `OFFSET` (volatile, not traceable) |
| Pick a scenario | `CHOOSE(idx, a, b, c)` or `INDEX(a:c, idx)` | nested `IF` |
| Conditional sum | `SUMIFS`, `SUMPRODUCT((cond)*(vals))` | `SUM(IF(...))` array formulas (CSE) |
| Count errors | `SUMPRODUCT(--ISERROR(range))` | |
| Boolean check | `IF(a>b,1,0)` | relying on TRUE or FALSE as a type (LibreOffice has none) |
| Safe divide | `IF(d=0,0,n/d)` | blanket `IFERROR` |
| Year fraction or dates | `EOMONTH`, `EDATE`, `YEARFRAC(start,end,1)` | date arithmetic on text years |
| Dated cash flows | `XNPV(rate, values, dates)` and `XIRR(values, dates)` in Excel and LibreOffice. **Sheets uses the same order for XIRR but XNPV is `XNPV(rate, cashflow_amounts, cashflow_dates)`; check it after upload.** | `NPV` (FAST 4.01-02: it assumes end-of-period timing and is easily off by one period; discount explicitly with a discount-factor row) |
| Join text | `A1&" "&B1` | `TEXTJOIN` or `CONCAT` without the `_xlfn.` prefix |
| Newer functions you really need | write the stored name: `_xlfn.IFS`, `_xlfn.SWITCH`, `_xlfn.MAXIFS`, `_xlfn.MINIFS`, `_xlfn.TEXTJOIN`, `_xlfn.CONCAT`; dynamic arrays as `_xlfn._xlws.SORT`, `_xlfn._xlws.FILTER`, `_xlfn.UNIQUE` | expecting LibreOffice 24.2 to evaluate the dynamic-array group; it cannot |

Date systems: Excel serial 1 is 1900-01-01 and Excel wrongly treats 1900 as a leap year; Sheets counts from 1899-12-30. Serial numbers agree from 1900-03-01 onward. Some Mac files use the 1904 system (`<workbookPr date1904="1"/>`); check before writing date serials into an existing file.

## Patterns (template syntax is model_builder's; the A1 equivalent follows)

**Growth path**
`={rev[-1]}*(1+{growth})`, with the first period `={Inputs.base}*(1+{growth})`. A1: `=C14*(1+D13)`

**Margin ramp to target, linear over N periods**
`={Inputs.m0}+({Inputs.target}-{Inputs.m0})*({t}-1)/(MAX({t@all})-1)`

**Corkscrew (debt, PP&E, NOLs)**
```
Opening    = {close[-1]}            first: ={Inputs.opening}
Additions  = ...
Reductions = -MIN({open}+{additions}, {available_cash})
Closing    = {open}+{additions}+{reductions}
```

**Revolver draw or repay in a cash sweep (two rows, never one clever formula)**
`Draw = MAX(0, {min_cash}-{cash_pre_revolver})`
`Repay = -MIN({rev_open}, MAX(0, {cash_pre_revolver}-{min_cash}))`

**Interest without a circularity (opening balance) or with a breaker**
`={Inputs.rate}*IF({Inputs.circ}=1,AVERAGE({open},{close}),{open})`

**Mid-period discount factor with a stub period**
`w` (year weight) first = stub fraction, then 1; `t_end = {t_end[-1]}+{w}`; `t_mid = {t_end}-{w}/2`; `df = 1/(1+{Inputs.wacc})^{t_mid}`

**Terminal value, value-driver form (consistent reinvestment)**
`=NOPAT_next*(1-g/ROIC)/(WACC-g)`, discounted at `t_end` of the final year (end-of-year convention for TV even when flows are mid-year; state the choice).

**Implied exit multiple, as a cross-check beside the Gordon value**
`=TV/EBITDA_final`

**CAGR**
`=(end/start)^(1/years)-1`, with `years` a cell rather than a typed number.

**Share of total (guarded)**
`=IF(SUM({seg@all})=0,0,{seg}/SUM({seg@all}))`

**Units bridge (revenue = units x ASP), as the repo's CLAUDE.md requires**
Rows: `Units`, `ASP`, `Revenue = {units}*{asp}`, plus a check that revenue ties to the reported figure (`={rev}-{Inputs.reported_rev}`, tolerance 0.5).

**Dollar bridge between two periods (volume, rate, opex)**
`Volume effect = ({rev}-{rev[-1]})*{margin[-1]}`; `Rate effect = {rev}*({margin}-{margin[-1]})`; check that `volume + rate = {ebit}-{ebit[-1]}`.
