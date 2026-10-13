# Modeling standards: how a banker-grade model is laid out

The rules below combine the FAST Standard 02c (https://fast-standard.org/wp-content/uploads/2019/10/FAST-Standard-02c-July-2019.pdf, Appendix C) and the ICAEW Financial Modelling Code (https://www.icaew.com/-/media/corporate/files/technical/technology/excel-community/financial-modelling-code.ashx) with sell-side practice. Rule numbers in brackets are FAST's. A rule the user or an existing workbook contradicts loses: match the file you were given.

## 1. Architecture
- **Separate inputs, calculations and outputs** [1.01-01, 1.02-02]. Default sheet order: `Cover` (title, master check, colour key, sheet map) > `Inputs` > timeline calculation sheets > `Valuation` or `Outputs` > `Checks`. Logic flows left to right across sheets and top to bottom within a sheet [1.02-01, 2.01-04].
- **One timeline, same columns on every timeline sheet** [1.01-02, 1.01-03, 2.01-02]. Column A holds the label and column B the unit; periods start in the same column everywhere, so `D` means the same year on every sheet. No subtotal columns in the middle of a timeline (ICAEW: no "variegated" timelines).
- **Each input lives in exactly one cell** (ICAEW). Everything else links to it. Never type the same assumption twice.
- **Calculate once** [1.01-07]. If two outputs need EBIT, both link to the EBIT row.
- **No links to links** [3.06-02]. A cross-sheet reference points at the source row, not at a row that merely repeats it. Exception: a local "import" row at the top of a calculation block, coloured green, is acceptable and often clearer (ICAEW).

## 2. Rows and formulas
- **One formula per row, consistent across every period** [3.02-01]. The only allowed break is the first period (opening balance, or a link to actuals). `xl.py audit` flags mid-row breaks; `model_builder` makes them impossible.
- **No numbers inside formulas** [3.04-01] except universal constants (0, 1, 12, 100 and so on). `=B5*1.05` is wrong; `=B5*(1+Growth)` with the growth rate in its own cell is right.
- **Short formulas** [3.03-01]. If it does not fit on a thumb, split it into helper rows. No nested IFs [3.03-07]; choose with `INDEX` or `CHOOSE` [3.03-06].
- **Avoid OFFSET and INDIRECT** [4.01-03]. They are volatile (recalculate on every change) and invisible to precedent tracing. Avoid whole-column references (`A:A`) in calculation rows. Avoid partial-range references [3.02-03].
- **IFERROR only around a specific, expected error**, never around a whole calculation, because it hides broken links. Guard a denominator explicitly instead: `=IF(B2=0,0,B7/B2)`.
- **Flags instead of IFs on dates** [2.02-06]. Add rows such as `Forecast flag (1/0)`, `Period number` and `Years from valuation date`, then multiply by them. The DCF in `scripts/jordan_valuation_xlsx.py` uses `t`, `w`, `t_end` and `t_mid` rows for this.
- **Corkscrews for balances** [2.02-05]: opening (= prior closing), plus additions, minus reductions, equals closing, one row each. Never compute a closing balance in one formula.
- **Sign convention** [1.01-08]: pick one and state it on the Cover. Sell-side default: costs negative on the income statement build, so totals are plain SUMs. Use an explicit `-1*` or a leading minus for every sign flip [3.04-04].
- **Units on every row** [3.05-04] in column B (`$m`, `%`, `x`, `#`, `yrs`). Percentages are stored as fractions (0.05, displayed as 5.0%).

## 3. Formatting (sell-side convention unless the file says otherwise)
| Element | Format |
|---|---|
| Hard-coded input | blue font `0000FF` (ICAEW also wants a fill or border, so inputs stay visible to colour-blind readers and in greyscale prints; use a light fill on the input block) |
| Formula | black |
| Link from another sheet | green `008000` |
| Link to another file | red; avoid external links altogether [1.03-02] |
| Scenario switch or key lever | yellow fill |
| Money | `#,##0_);(#,##0);"-"_)`: negatives in parentheses, zero as a dash, trailing space so the numbers align with the parentheses |
| Percent | `0.0%_);(0.0%);"-"_)` |
| Multiple | `0.0"x"` |
| Year header | text (`"FY2027E"`), never the number 2,027 |
| Actual versus estimate | suffix `A` or `E` on the header, or a flag row |

Also: Arial or Calibri at one size; no merged cells (use "Center Across Selection") [4.02-02]; gridlines off on presentation sheets; freeze panes at the first period column; nothing hidden (group rows instead) [2.01-08]; put the master check where it shows from every sheet [2.03-05].

## 4. Checks
- Every model ships with a `Checks` sheet. Each check is either a difference that must be about zero (with a tolerance cell, since float and iteration noise are real; see fidelity.md) or a comparison that must be TRUE, never one formula trying to handle both (LibreOffice has no booleans).
- Standard checks: balance sheet balances; cash flow ending cash equals balance sheet cash; segments sum to the consolidated total; growth rows recompute the revenue path; WACC above terminal growth; margin path hits its target; no `#` errors (`=SUMPRODUCT(--ISERROR(range))=0`).
- One master check (1 = all pass), named `MasterCheck`, shown on the Cover.

## 5. Scenarios and sensitivities
- **Scenario switch:** one cell with a validation list (`Bear, Base, Bull`), an index `=MATCH(switch,{"Bear","Base","Bull"},0)`, and a live column per scenario input `=CHOOSE(idx, bear, base, bull)`. All cases stay visible side by side, in blue. Never overwrite inputs with a macro.
- **Sensitivity tables:**
  1. An Excel Data Table (What-If) stays live in Excel. Its input cells must be on the same sheet as the table, it recalculates single-threaded and slowly, it does not survive a LibreOffice save, and it cannot be verified here (fidelity.md).
  2. Preferred here: `xl.py sensitivity` brute-forces the grid through the full model, then `--write` lays it out as a labelled static block that names the command that produced it.
  3. A formula grid that re-derives the output algebraically is acceptable only for simple closed-form outputs (for example, a TV grid by WACC and g); it silently diverges once the model has non-linearities such as MAX floors or tax shields.
- Grid conventions (anthropics/financial-services dcf-model, verified on the source): an odd number of rows and columns (5x5, sometimes 7x7), so there is a true centre; the centre cell equals the model's live output; highlight it. `xl.py sensitivity` asserts these, plus every cell distinct and monotonic along each axis. The axis steps must bracket the scenarios.
- Standard DCF grids: WACC x terminal growth, revenue growth x EBIT margin. Add a tornado (`xl.py tornado`) to rank which inputs matter before choosing grid axes.

## 6. Circularity
- FAST [1.01-11] and ICAEW say no deliberate circularity. Sell-side LBOs often compute interest on average balances anyway.
- If a model has one: add a **circuit breaker** input (1 = average balance, 0 = opening balance) inside each interest formula, `=Rate*IF(Circ=1,AVERAGE(Open,Close),Open)`. Switch iterative calculation on explicitly with `{"op": "iterate", "on": true}`, which writes `iterate`, `iterateCount=100` and `iterateDelta=0.001`. Set check tolerances above `iterateDelta`.
- Better, solve it algebraically. For interest on average debt with a full cash sweep, I = r(2D0 - C)/(2 - r), where D0 is opening debt and C is cash before interest. Verified in the lab: 89.47368 exact versus 89.47366 iterated.
- If a circular model shows `#VALUE!` or `#NUM!`, the loop has diverged and will not recover by itself: set the breaker to 0, recalculate, then set it back to 1.

## 7. Valuation mechanics checklist
- Mid-period discounting: t_mid = period end minus half the period length. A stub first year needs its own weight row, so cash flow is pro-rated and timing is shifted.
- Terminal value: compute both the Gordon growth value and the exit multiple, and show the implied multiple of one next to the other. The value-driver form NOPAT(1+g)(1 - g/ROIC)/(WACC - g) keeps reinvestment consistent with growth.
- Show the terminal value share of total value. Above about 75% the thesis is a terminal-value bet, so say so.
- Bridge to equity value: EV minus net debt minus leases (if EBIT is pre-lease) minus minorities plus investments, divided by diluted shares at the money (treasury stock method).
- Show per-share value against the current price as a percentage up or down, and keep the price date as a labelled market-data input.

## 8. Review pass before anyone sees it (what a VP checks first)
1. Does the master check say OK in every scenario? (`xl.py sensitivity` over the switch, or the `LOSession` loop in `scripts/jordan_valuation_xlsx.py`.)
2. `xl.py audit`: zero inconsistent rows, zero literals in formulas, zero ref-to-blank, zero bare new-function names.
3. Trace the headline number (`xl.py trace Output!C10 --depth 3`): does every leaf end in a blue, sourced input?
4. Flex each key input by +/-10% and check the output moves in the right direction by a plausible amount.
5. Units: no percent stored as 5 instead of 0.05, no $k mixed with $m, and years as text.
6. Every input has a source in the note column (repo rule: filing and page, or a label such as ASSUMPTION or market data).
