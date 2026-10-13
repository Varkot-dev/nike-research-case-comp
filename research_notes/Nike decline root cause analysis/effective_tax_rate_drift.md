# Effective tax rate drift: a separate, non-operating driver of the EPS and stock decline?

Research date: 2026-10-13. Hypothesis under test: *A rising effective tax rate (OECD Pillar Two minimum tax from FY2025, one-time benefits rolling off, foreign audit settlements) is a separate, non-operating driver of the EPS and share-price decline.*

Conventions: USD millions unless noted. FY ends May 31. "pp" = percentage points of effective tax rate (ETR). All Nike numbers come from `data/nike_filing_facts.csv` and `research_notes/04_financial_data_pack.md` (already verified there) unless a filing is cited directly; the filings cited directly below were downloaded from sec.gov on 2026-10-13 and their text was searched (OPENED). "My arithmetic" marks numbers I computed.

## 1. Bottom line

1. **The tax rate did rise, and it does cost EPS, but the effect is small.** ETR went from 14.9% (FY2024) to 17.1% (FY2025), 20.3% (FY2026), 22.7% (Q1 FY2027) and a guided "mid-20 percent range" for FY2027. At the FY2024 rate, FY2026 EPS would have been about $2.24 instead of $2.10, so tax explains about $0.14 (about 9%) of the $1.63 fall from $3.73 (my arithmetic). On the FY2027 guide ($1.25 midpoint at about 25%), tax explains about $0.17 (about 7%) of the $2.48 fall.
2. **The Pillar Two part of the hypothesis fails.** Nike's own FY2025 10-K says the 15% minimum tax "became effective for the Company beginning June 1, 2024" and "did not have a material impact on the Company's financial statements for fiscal 2025." The new ASU 2023-09 FY2026 rate reconciliation has no minimum-tax line. Low-tax US peers (Skechers, Lululemon) show no step-up when Pillar Two started either.
3. **Most of the increase is a symptom of the earnings collapse, not an independent cause.** Three mechanisms tie the higher rate to falling operating profit:
   - **Fixed-dollar tax items on a smaller base.** China withholding taxes ($83M), Mexico ($59M), stock-comp shortfalls ($44M) and unrecognized-tax-benefit changes ($52M), plus other China ($13M), total about $251M in FY2026, or 6.4 pp of ETR on $3,900M of pretax. The same dollars on FY2024's $6,700M of pretax would be 3.7 pp. The gap, about 2.7 pp, is purely the denominator shrinking (my arithmetic).
   - **The FDII benefit shrinks with US profit.** US pretax income fell from $5,588M (FY2024) to $2,680M (FY2026). The FDII benefit went from -4.8% of pretax (about $322M) to -2.9% ($113M), a loss of about 1.9 pp.
   - **Stock-comp tax shortfalls follow the share price.** The stock-comp line was -0.5% in FY2024, +1.5% in FY2025 and +1.1% in FY2026. Awards vesting below their grant value create tax deficiencies, so this is a reflexive loop from the stock decline back into EPS.
4. **The genuinely non-operating part is one-offs rolling off,** and it explains year-to-year noise rather than the trend:
   - FY2024's "non-recurring one-time benefits" (foreign tax credit regulation delay; Q1 FY2024 ETR was only 12.0%).
   - FY2025's $133M Section 987 deferred tax benefit (-3.4 pp), whose roll-off is Nike's stated main reason for the FY2026 increase.
   - Q1 FY2027 foreign audit settlements (+1.6 pp in one quarter, about $15M; my arithmetic).
   Before the decline Nike's ETR already swung between 9.1% and 18.2% (FY2019 to FY2024), and it was 18.2% in FY2023 near peak earnings. A rate around 20% is not new territory.
5. **Effect on the stock is small.** Trailing ETR was 13.7% for the four quarters to Aug 2021 and 20.7% for the four quarters to Aug 2026 (my arithmetic from quarterly filings). Applied to the valuation_vs_business decomposition (ln move -1.614 from $177.51 to $35.35), that is ln(0.793/0.863) = -0.085, or about 5% of the log decline. If the market fully capitalizes a permanent mid-20s rate, the ceiling is about 9%. Since much of the rise reverses as pretax recovers, about 5% is the better estimate.

**Verdict: minor, and largely a symptom.** About 5% of the log share-price decline and 7% to 9% of the EPS decline. Roughly half of the FY2024 to FY2026 rise is mechanical, from lower pretax profit and the share price itself. Most of the rest is one-time benefits rolling off. Pillar Two contributes nothing measurable. valuation_vs_business can footnote it: the tax rate subtracts about $0.14 to $0.17 of EPS and about 5% of the log decline, but it is not a brand or demand cause. It will largely reverse if EBIT recovers.

## 2. Falsifiable predictions and results

| # | If the hypothesis is true, then... | What the data show | Held? |
|---|---|---|---|
| P1 | **Pillar Two shows up in the filings:** a step-up from FY2025 (Pillar Two effective June 1, 2024), with a minimum-tax or top-up line in the rate reconciliation. | FY2025 10-K Note (Income Taxes): legislation "became effective for the Company beginning June 1, 2024. Based on the Company's analysis of Pillar Two provisions, these tax law changes did not have a material impact on the Company's financial statements for fiscal 2025." FY2026 ASU 2023-09 reconciliation (FY2026 10-K p. 71 to 72): no minimum-tax or top-up line. The Q1 FY2027 10-Q tax note does not mention Pillar Two. | **No** |
| P2 | **Peers:** other US-listed sportswear companies should show a similar step when Pillar Two started (CY2024 or FY2025). | SEC XBRL `EffectiveIncomeTaxRateContinuingOperations` (data.sec.gov, OPENED 2026-10-13): Skechers 17.8% (2022), 18.8% (2023), 16.9% (2024), lower after Pillar Two. Lululemon 28.8%, 29.6%, 29.5% (FY2023 to FY2025), flat. Deckers has a single point, 22.8% (FY Mar 2026). Under Armour and Crocs are dominated by losses and valuation-allowance items, so they are uninformative. | **No** |
| P3 | **Independence from operations:** the rate should rise even where pretax income is stable. | FY2025 to FY2026 pretax was flat ($3,885M to $3,900M) while ETR rose 3.2 pp. Nike gives the reason as the FY2025 one-time Section 987 benefit ($133M, 3.4 pp) rolling off (FY2026 10-K p. 35). So only the one-off component is independent of operations. | **Partly** (one-offs only) |
| P4 | **Timing:** the ETR rise should precede, or run independently of, the earnings decline. | The rate rose as earnings fell. Q1 FY2025 ETR was 19.6% vs 12.0% in Q1 FY2024, but Q1 FY2024 had a one-time benefit for FY2023 positions (FY2025 10-K tax note). EBIT fell from $6,539M to $3,778M in the same year. Quarterly ETR settled at 20% to 21% from Q1 FY2026, the quarters with the lowest pretax. | **No** |
| P5 | **Magnitude:** tax should explain a material share of the EPS fall. | Holding FY2024's 14.9% ETR: FY2025 EPS would be $2.22 vs $2.16 actual (-$0.06, 4% of the $1.57 fall). FY2026: $2.24 vs $2.10 (-$0.14, 9% of $1.63). FY2027 guide midpoint: $1.42 vs $1.25 (-$0.17, 7% of $2.48). (My arithmetic, using diluted shares from the data pack.) | **Minor** |
| P6 | **Symptom test (falsifies independence):** if the rate rise is mechanical, fixed-dollar items should take a larger share of a shrinking pretax base. | China withholding $83M (2.1%), other China $13M, Mexico $59M (1.5%), stock comp $44M (1.1%), change in unrecognized tax benefits $52M (1.3%): 6.4 pp on $3,900M of pretax vs 3.7 pp on $6,700M. FDII benefit -4.8% to -2.9% as US pretax fell from $5,588M to $2,680M (FY2026 10-K p. 71 to 72; FY2025 10-K reconciliation). | **Yes** (symptom) |
| P7 | **Reflexivity:** stock-comp tax shortfalls should appear after the share price fell. | Stock-based compensation line in the rate reconciliation: -1.1% (FY2023), -0.5% (FY2024), +1.5% (FY2025), +1.1% (FY2026). FY2025 10-K cites "decreased benefits from stock-based compensation." | **Yes** (symptom of the price fall) |
| P8 | **One-time benefits rolling off:** the year-over-year steps should match named one-offs. | FY2024: "non-recurring one-time benefits ... including the impact of the delay of the effective date of certain U.S. foreign tax credit regulations" (FY2025 10-K MD&A). FY2025: Section 987 benefit -3.4 pp, recognized in Q3 FY2025, when the ETR was 5.9%. FY2026: the roll-off is the stated main driver. FY2022 had a -4.7 pp Subpart F deferred benefit (FY2022 10-K p. 73), which made the 2021 to 2022 base unusually low. | **Yes** (explains noise, not trend) |
| P9 | **Audit settlements as a new drag:** settlements should raise the ETR and draw down reserves. | Q1 FY2027 ETR was 22.7% vs 21.1%, "primarily due to foreign tax audit settlements" (Q1 FY2027 10-Q Note 4). Gross unrecognized tax benefits fell from $1,026M (May 2025) to $953M (May 2026) and $931M (Aug 2026). Size: about 1.6 pp on $921M of pretax, or about $15M (my arithmetic). Open exposure includes the EU State Aid probe of Dutch rulings (FY2026 10-K tax note). | **Yes, small** |

Score: of the predictions that would show an independent, non-operating cause (P1, P2, P4, P5), none held fully. Predictions P6 and P7 hold, and they mark the rise as a symptom. P3, P8 and P9 hold only for one-offs, which explain year-to-year noise.

## 3. Data

### 3.1 Annual ETR, pretax and EPS

| FY | Pretax | Tax | ETR | US pretax | Foreign pretax | Diluted EPS | Source |
|---|---|---|---|---|---|---|---|
| 2019 | 4,801 | 772 | 16.1% | | | 2.49 | FY2019 10-K p. 26 |
| 2020 | 2,887 | 348 | 12.1% | 2,954 | -67 | 1.60 | FY2020 10-K p. 30, 75 |
| 2021 | 6,661 | 934 | 14.0% | | | 3.56 | FY2021 10-K p. 57 |
| 2022 | 6,651 | 605 | 9.1% | | | 3.75 | FY2022 10-K p. 56 |
| 2023 | 6,201 | 1,131 | 18.2% | | | 3.23 | FY2023 10-K p. 31 |
| 2024 | 6,700 | 1,000 | 14.9% | 5,588 | 1,112 | 3.73 | FY2024 10-K p. 57; FY2026 10-K p. 71 |
| 2025 | 3,885 | 666 | 17.1% | 3,220 | 665 | 2.16 | FY2025 10-K p. 32; FY2026 10-K p. 71 |
| 2026 | 3,900 | 792 | 20.3% | 2,680 | 1,220 | 2.10 | FY2026 10-K p. 55, 71 |
| 2027 guide | n/a | n/a | "mid-20 percent range" | | | adj. $1.15 to $1.35 | Q1 FY2027 release p. 1 |

FY2026 pretax includes the $986M expected IEEPA tariff recovery in cost of sales (FY2026 10-K p. 30). Without it, pretax would be about $2,914M and the fixed-dollar items would weigh even more.

### 3.2 Quarterly ETR (from the facts CSV; Q4 values derived as FY less 9M)

| | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| FY2022 | 11.0 | 10.9 | 16.4 | -4.7 |
| FY2023 | 19.7 | 19.3 | 16.0 | 17.3 |
| FY2024 | 12.0 | 17.9 | 16.5 | 13.1 |
| FY2025 | 19.6 | 17.9 | 5.9 (Sec. 987) | 33.6 (pretax only $318M) |
| FY2026 | 21.1 | 20.7 | 20.0 | 19.6 |
| FY2027 | 22.7 | | | |

The Q4 FY2025 33.6% rate on only $318M of pretax shows the denominator effect at its clearest.

### 3.3 Rate reconciliations

FY2025 and FY2024, old format (FY2025 10-K and FY2026 10-K tax note): federal 21.0 / 21.0; state 2.0 / 1.4; foreign earnings 1.1 / -2.5; US regs, foreign currency losses (Sec. 987) -3.4 / 0.0; FDII -5.3 / -4.8; stock comp 1.5 / -0.5; audits and contingency reserves 2.7 / 1.8; R&D credit -2.1 / -2.1; other -0.4 / 0.6; total 17.1 / 14.9. FY2023: FDII -6.1, stock comp -1.1, audits 1.0, total 18.2.

FY2026, ASU 2023-09 format (FY2026 10-K p. 71 to 72): federal $819M (21.0%); state $94M (2.4%); China withholding $83M (2.1%); China other $13M (0.3%); Mexico $59M (1.5%); other foreign $107M (2.7%); FDII -$113M (-2.9%); current Subpart F $179M (4.6%); deferred Subpart F incl. FTC -$120M (-3.1%); foreign tax credits -$353M (-9.1%); other cross-border $11M (0.3%); R&D credit -$65M (-1.7%); stock comp $44M (1.1%); other nondeductible -$28M (-0.7%); change in unrecognized tax benefits $52M (1.3%); other $11M (0.3%); total $792M (20.3%). The two formats are not line-for-line comparable.

### 3.4 Other tax facts

- Tax holiday benefit (foreign operations, expires 2031): $338M (FY2024), $271M (FY2025), $254M (FY2026); EPS $0.22, $0.18, $0.17 (FY2026 10-K p. 74). The benefit shrinks with foreign sourcing profit, so it too is linked to operations. Expiry in 2031 is a future risk, not a cause of the decline.
- Cash taxes paid: $1,226M (FY2025), $1,270M (FY2026) (FY2026 10-K p. 75). Cash taxes ran well above book tax expense ($666M, $792M) because of large deferred benefits. Book ETR therefore understates the cash burden, but that gap predates the decline.
- OBBBA (enacted July 4, 2025): "did not have a material impact" on FY2026 (FY2026 10-K tax note). Unverified in filings and from my background knowledge only: OBBBA changes to FDII and GILTI for tax years beginning after Dec 31, 2025 would first apply to Nike in FY2027 (beginning June 1, 2026). That could explain part of the jump to the mid-20s guide, but Nike has not said so. Treat this as an open question.
- OECD "side-by-side" framework, January 2026: "largely exempting U.S. headquartered companies from the application of certain Pillar Two provisions," pending national adoption (FY2026 10-K risk factors). Since Pillar Two was immaterial anyway, this upside is small.

## 4. Quantification

**EPS (holding FY2024's 14.9% ETR; my arithmetic):**
- FY2026: NI = 3,900 x 0.851 = 3,319, divided by 1,481.0M diluted shares = $2.24 vs actual $2.10. Tax is -$0.14 of the -$1.63 fall (9%).
- FY2027 guide: $1.25 x (0.851 / 0.75) = $1.42. Tax is -$0.17 of the -$2.48 fall (7%), assuming a 25% rate.
- Within FY2026's +5.4 pp, by mechanism (approximate; the reconciliation formats differ):

| Component | Approx. pp | Character |
|---|---|---|
| Denominator effect on fixed-dollar items | about 2.7 | Symptom of lower pretax |
| FDII shrinking with US profit | about 1.9 | Symptom of lower US profit |
| Stock-comp swing (-0.5 to +1.1) | about 1.6 | Symptom of the stock fall |
| FY2024 one-off benefits gone, offset by other reconciling items | the balance | Non-operating noise |
| Pillar Two | 0 measurable | n/a |

The components overlap, so they do not sum exactly.

**Stock (TTM ETR, my arithmetic):**
- Q2 FY2021 to Q1 FY2022: tax $969M / pretax $7,052M = 13.7%.
- Q2 FY2026 to Q1 FY2027: $806M / $3,899M = 20.7%.
- ln(0.793 / 0.863) = -0.085, which is 5.2% of the -1.614 log decline in valuation_vs_business and about 10% of its EPS leg (-0.882).
- Using the FY2027 guided 25% instead: -0.140, or 8.7%, as an upper bound.
- Measured against a normalized pre-decline rate of about 16% (FY2019 16.1%, FY2023 18.2%) rather than the unusually low 2021 to 2022 base (FY2022 had the -4.7 pp Subpart F one-off), the effect is about -0.05, or about 3%.

## 5. Can management fix it?

**Partly, and mostly indirectly.**
- The mechanical parts reverse as pretax recovers: the denominator effect, FDII and stock comp. If EBIT returns to FY2024 levels, the ETR should drift back toward the high teens without any tax planning.
- Audit settlements and the EU State Aid case are not in management's control.
- The side-by-side framework and OBBBA are policy outcomes.
- The 2031 tax-holiday expiry (worth $0.17 of EPS in FY2026) is a future headwind to watch, not part of the past decline.

## 6. Sources

| Source | Date | Status | Used for |
|---|---|---|---|
| Nike FY2026 Form 10-K, sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm | filed 2026-07-15 | OPENED (downloaded, text searched 2026-10-13) | Rate reconciliation p. 71 to 72, MD&A ETR p. 35, Pillar Two and side-by-side risk factor, OBBBA, tax holiday p. 74, US/foreign pretax p. 71 |
| Nike FY2025 Form 10-K, .../000032018725000047/nke-20250531.htm | filed 2025-07-17 | OPENED | Pillar Two "did not have a material impact" for FY2025; FY2023 to FY2025 reconciliation; MD&A reasons |
| Nike Q1 FY2027 Form 10-Q, .../000032018726000193/nke-20260831.htm | filed 2026-10-02 | OPENED | Note 4: 22.7% vs 21.1%, foreign audit settlements, UTB $931M |
| Q1 FY2027 earnings release (8-K Ex. 99.1) | 2026-10-01 | via repo data pack (previously verified) | FY2027 mid-20% ETR guide, adj. EPS $1.15 to $1.35 |
| `data/nike_filing_facts.csv` (repo) | built 2026-10 | verified repo data | Quarterly and annual pretax, tax, ETR, Sec. 987 $133M, Subpart F FY2022, UTB balances, cash taxes |
| `research_notes/Nike decline root cause analysis/valuation_vs_business.md` (repo) | 2026-10-13 | repo note | Log decomposition (-1.614 total; EPS leg) |
| SEC XBRL companyconcept API, EffectiveIncomeTaxRateContinuingOperations for NKE, SKX, LULU, DECK, UA, CROX | accessed 2026-10-13 | OPENED (JSON) | Peer ETR test (P2) |
| Nike newsroom, "NIKE, Inc. Reports Fiscal 2027 First Quarter Results," about.nike.com | 2026-10-01 | SNIPPET | Guide wording "subject to changes in earnings mix and discrete tax items" |
| Just-Style, "Nike trims outlook on bleak Q" | Oct 2026 | SNIPPET | Repeats mid-20% guide |
| 247wallst NKE earnings trends page | accessed 2026-10-13 | SNIPPET | Labels Q1 ETR as 19.6% vs 33.6%. These are actually the Q4 FY2026 and Q4 FY2025 figures, so the page is mislabeled; not used |
