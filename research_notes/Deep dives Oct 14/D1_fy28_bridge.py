"""D1 labelled-arithmetic bridge: FY27 guide midpoint to FY28, vs consensus.
Run: python3 -I D1_fy28_bridge.py   (prints every table used in D1_fy28_bridge.md)
Inputs marked FILING come from Nike's Q1 FY27 10-Q / FY26 10-K / Oct 1 2026 8-K (investors.nike.com mirror).
Inputs marked ASSUMPTION are judgment anchored to the evidence named in the note.
"""
# ---------------- FILING inputs ($M) ----------------
FY26 = dict(NA=20511, EMEA=12572, GC=5847, APLA=6243, CONV=1174, GBD=49, CORP=2)
Q1_26 = dict(NA=5020, EMEA=3331, GC=1512, APLA=1490, CONV=366, GBD=9, CORP=-8)
Q1_27 = dict(NA=5127, EMEA=3176, GC=1180, APLA=1463, CONV=263, GBD=6, CORP=-2)
R26 = 46398
GUIDE_MID = -0.08          # "decline high-single digits" read as -7% to -9%
EPS27 = 1.25               # adjusted EPS guide midpoint (1.15 to 1.35)
TAX27 = 0.25               # "mid-20 percent range"
SH27 = 1485.0              # Q1 FY27 diluted 1,484.2
NETINT = 55.0              # net interest income (FY26 50; Q1 FY27 14)
OTHER_INC = 50.0           # other income in EBIT (FY26 53; Q1 FY27 19)
SGA26 = 16114.0
# consensus (Yahoo/MarketScreener, Oct 13-14, see expectations_gap.md)
C27 = dict(rev=43152, eps=1.288, ebit=2479)
C28 = dict(rev=43645, eps=1.646, ebit=3179, ni=2418)

R27 = R26 * (1 + GUIDE_MID)
q1 = sum(Q1_27.values())
rest = R27 - q1
base_rest = {k: FY26[k] - Q1_26[k] for k in FY26}
# ASSUMPTION: Q2-Q4 FY27 segment path consistent with guide midpoint
g_rest = dict(GC=-0.30, CONV=-0.30, APLA=-0.03)
fy27 = {}
rest_fixed = 0
for k, g in g_rest.items():
    rest_fixed += base_rest[k] * (1 + g)
rest_fixed += base_rest['GBD'] + base_rest['CORP'] * 0
na_em_target = rest - rest_fixed
na_g = -0.055
na_rest = base_rest['NA'] * (1 + na_g)
em_rest = na_em_target - na_rest
fy27['NA'] = Q1_27['NA'] + na_rest
fy27['EMEA'] = Q1_27['EMEA'] + em_rest
for k, g in g_rest.items():
    fy27[k] = Q1_27[k] + base_rest[k] * (1 + g)
fy27['GBD'] = Q1_27['GBD'] + base_rest['GBD']
fy27['CORP'] = Q1_27['CORP'] + 0
print("FY27 guide-midpoint segment path (ASSUMPTION for Q2-Q4)")
print(f"  total {R27:,.0f}  Q1 actual {q1:,.0f}  Q2-Q4 needed {rest:,.0f} vs LY {sum(base_rest.values()):,.0f} = {rest/sum(base_rest.values())-1:+.1%}")
print(f"  EMEA Q2-Q4 solved: {em_rest/base_rest['EMEA']-1:+.1%}")
for k in fy27:
    print(f"  {k:5s} FY27 {fy27[k]:8,.0f}  vs FY26 {fy27[k]/FY26[k]-1:+.1%}")
print(f"  check sum {sum(fy27.values()):,.0f}")

# ---------------- FY27 P&L at guide midpoint ----------------
NI27 = EPS27 * SH27
PT27 = NI27 / (1 - TAX27)
EBIT27 = PT27 - NETINT
DC27, OH27 = 4800.0, None
SGA27 = SGA26 * 0.97 - 0.15 * SH27 / (1 - TAX27)   # reported -3% (Q1 run rate) less Pace charge in SG&A
OH27 = SGA27 - DC27
GP27 = EBIT27 + SGA27 - OTHER_INC
GM27 = GP27 / R27
print(f"\nFY27 midpoint: NI {NI27:,.0f} pretax {PT27:,.0f} EBIT {EBIT27:,.0f} ({EBIT27/R27:.2%}) SGA adj {SGA27:,.0f} GP {GP27:,.0f} GM {GM27:.2%}")
print(f"  Pace charge excluded: ${0.15*SH27/(1-TAX27):,.0f}M pretax")
ccgp27 = C27['ebit'] + SGA27 - OTHER_INC
print(f"  consensus FY27 implied GM (same SG&A): {ccgp27/C27['rev']:.2%}")

# ---------------- FY28 scenarios ----------------
S = {
 'Low':  dict(NA=-.02, EMEA=-.03, GC=-.20, APLA=-.01, CONV=-.20,
              bps=dict(tariff=-10, logistics=0, product=10, asp=-40, fx=-20, other=-30, converse=-10),
              dc=.01, pace_gross=250, reinv=.50, wage=.025, tax=.26, sh=1490),
 'Base': dict(NA=0.0, EMEA=0.0, GC=-.12, APLA=.01, CONV=-.10,
              bps=dict(tariff=-10, logistics=20, product=40, asp=-20, fx=0, other=-20, converse=-5),
              dc=.0, pace_gross=375, reinv=.40, wage=.015, tax=.25, sh=1488),
 'High': dict(NA=.03, EMEA=.03, GC=-.04, APLA=.04, CONV=0.0,
              bps=dict(tariff=-10, logistics=50, product=80, asp=20, fx=30, other=0, converse=0),
              dc=.01, pace_gross=600, reinv=.30, wage=.005, tax=.24, sh=1480),
}
GM_GC = 0.475   # Q1 FY27 GC gross margin (10-Q p.26-28); company 42.8%
GM_CO = 0.428
WAGE = 0.025
res = {}
for name, s in S.items():
    seg28 = {k: fy27[k] * (1 + s.get(k, 0)) for k in fy27}
    seg28['CORP'] = fy27['CORP']
    R28 = sum(seg28.values())
    mix_bps = ((seg28['GC'] / R28) - (fy27['GC'] / R27)) * (GM_GC - GM_CO) * 1e4
    bps = dict(s['bps']); bps['china_mix'] = mix_bps
    gm_bps = sum(bps.values())
    GM28 = GM27 + gm_bps / 1e4
    DC28 = DC27 * (1 + s['dc'])
    pace_net = s['pace_gross'] * (1 - s['reinv'])
    OH28 = OH27 * (1 + s['wage']) - pace_net
    SGA28 = DC28 + OH28
    EBIT28 = R28 * GM28 - SGA28 + OTHER_INC
    PT28 = EBIT28 + NETINT
    NI28 = PT28 * (1 - s['tax'])
    EPS28 = NI28 / s['sh']
    # bridge ($/share), sequential
    k27 = (1 - TAX27) / SH27
    vol = (R28 - R27) * GM27 * k27
    rate = R28 * gm_bps / 1e4 * k27
    opex = -(SGA28 - SGA27) * k27
    tax = -(s['tax'] - TAX27) * PT28 / SH27 + 0   # tax-rate effect on FY28 pretax
    pre_tax_eps = PT28 * (1 - TAX27) / SH27
    shares = EPS28 - (PT28 * (1 - s['tax']) / SH27)
    check = EPS27 + vol + rate + opex + tax + shares
    lines = {k: R28 * v / 1e4 * k27 for k, v in bps.items()}
    res[name] = dict(R28=R28, seg28=seg28, gm_bps=gm_bps, GM28=GM28, SGA28=SGA28, EBIT28=EBIT28, EPS28=EPS28,
                     vol=vol, rate=rate, opex=opex, tax=tax, shares=shares, check=check, lines=lines, bps=bps,
                     dsga_bps=(SGA28 / R28 - SGA27 / R27) * 1e4, pace_net=pace_net, OH28=OH28, DC28=DC28)
    print(f"\n=== {name} ===  revenue {R28:,.0f} ({R28/R27-1:+.1%} vs FY27 mid)  EBIT {EBIT28:,.0f} ({EBIT28/R28:.2%})  EPS {EPS28:.3f}")
    for k in ['NA','EMEA','GC','APLA','CONV','GBD']:
        print(f"   {k:5s} {seg28[k]:8,.0f} ({s.get(k,0):+.0%}) delta {seg28[k]-fy27[k]:+,.0f}")
    print(f"   GM27 {GM27:.2%} -> GM28 {GM28:.2%} ({gm_bps:+.0f} bps): " + ", ".join(f"{k} {v:+.0f}" for k, v in bps.items()))
    print(f"   SG&A {SGA27:,.0f} -> {SGA28:,.0f} ({SGA28/SGA27-1:+.1%}); as % rev {SGA27/R27:.2%} -> {SGA28/R28:.2%} ({(SGA28/R28-SGA27/R27)*1e4:+.0f} bps); Pace net {pace_net:.0f}")
    print(f"   bridge $/sh: start {EPS27:.3f} | volume {vol:+.3f} | GM rate {rate:+.3f} | opex {opex:+.3f} | tax {tax:+.3f} | shares {shares:+.3f} | end {check:.3f}")
    print("   GM rate lines $/sh: " + ", ".join(f"{k} {v:+.3f}" for k, v in lines.items()))
    print(f"   gap vs consensus 1.646: {EPS28-C28['eps']:+.3f} ({EPS28/C28['eps']-1:+.1%}); after tariff offset +0.08/+0.12: {EPS28+0.08-C28['eps']:+.3f} / {EPS28+0.12-C28['eps']:+.3f}")
    print(f"   revenue vs consensus 43,645: {R28-C28['rev']:+,.0f} ({R28/C28['rev']-1:+.1%})")

# consensus-implied bridge
print("\nConsensus-implied (derived)")
dE = C28['ebit'] - C27['ebit']
vol_c = (C28['rev'] - C27['rev']) * (ccgp27 / C27['rev'])
print(f"  EBIT +{dE:,.0f}; volume at FY27 cons GM {vol_c:,.0f}; residual GM+opex {dE-vol_c:,.0f} = {(dE-vol_c)/C28['rev']*1e4:.0f} bps of FY28 rev")
print(f"  EBIT margin {C27['ebit']/C27['rev']:.2%} -> {C28['ebit']/C28['rev']:.2%} (+{(C28['ebit']/C28['rev']-C27['ebit']/C27['rev'])*1e4:.0f} bps)")
print(f"  NI/EPS implied shares {C28['ni']/C28['eps']:.0f}M; implied tax {1-C28['ni']/(C28['ebit']+NETINT):.1%}")
b = res['Base']
print(f"  Base EBIT margin {b['EBIT28']/b['R28']:.2%} vs FY27 mid {EBIT27/R27:.2%} (+{(b['EBIT28']/b['R28']-EBIT27/R27)*1e4:.0f} bps)")
# gap split: start level, then FY28 step
print(f"  start gap: guide mid 1.25 vs consensus FY27 {C27['eps']} = {EPS27-C27['eps']:+.3f}")
print(f"  FY28 EPS step: consensus +{C28['eps']-C27['eps']:.3f} ({C28['eps']/C27['eps']-1:+.1%}); base +{b['EPS28']-EPS27:.3f} ({b['EPS28']/EPS27-1:+.1%})")

# tariff offset arithmetic
tax_k = (1 - 0.25) / 1488
for eps in (0.08, 0.12):
    print(f"  tariff offset ${eps:.2f} = {eps/tax_k/b['R28']*1e4:.0f} bps GM on base FY28 revenue, ${eps/tax_k:,.0f}M pretax")

# grids
print("\nGrid A: EPS by FY28 revenue ($B) x EBIT margin (tax 25%, 1,488M sh, net interest +55)")
margins = [5.5, 6.0, 6.5, 7.0, 7.28, 7.5, 8.0, 9.0]
revs = [41000, 42000, 42686, 43645, 44500]
print("rev\\m  " + " ".join(f"{m:6.2f}" for m in margins))
for r in revs:
    print(f"{r/1000:5.2f}  " + " ".join(f"{(r*m/100+NETINT)*0.75/1488:6.3f}" for m in margins))
print("\nEBIT margin needed for EPS 1.646 at each revenue:")
for r in revs:
    need = (1.646 * 1488 / 0.75 - NETINT) / r
    print(f"  {r:,}: {need:.2%}")
print("\nGrid B: EPS by revenue x GM (SG&A = base FY28 $, other inc 50)")
gms = [41.0, 41.5, 42.0, 42.5, 43.0, 43.5]
sg = b['SGA28']
print(f"(SG&A {sg:,.0f})")
print("rev\\GM " + " ".join(f"{g:6.1f}" for g in gms))
for r in revs:
    print(f"{r/1000:5.2f}  " + " ".join(f"{((r*g/100-sg+OTHER_INC+NETINT)*0.75/1488):6.3f}" for g in gms))
print("\nGM needed for 1.646 at each revenue (base SG&A):")
for r in revs:
    pt = 1.646 * 1488 / 0.75
    print(f"  {r:,}: {(pt-NETINT-OTHER_INC+sg)/r:.2%}")

# sensitivities
print("\nPer-unit sensitivities (FY28 base)")
k = 0.75 / 1488
print(f"  100 bps GM = ${b['R28']*0.01:,.0f}M = ${b['R28']*0.01*k:.3f}/sh")
print(f"  $100M SG&A = ${100*k:.3f}/sh")
print(f"  1 pt revenue = ${b['R28']*0.01:,.0f}M; at FY27 GM {GM27:.1%} = ${b['R28']*0.01*GM27*k:.3f}/sh; at 35% decremental = ${b['R28']*0.01*0.35*k:.3f}/sh")
print(f"  1 pt tax = ${b['EBIT28']*0.01/1488+NETINT*0.01/1488:.3f}/sh")
print(f"  10M shares = ${b['EPS28']*10/1488:.3f}/sh")
print(f"  guide low/high start (1.15/1.35) shifts every end-point by -0.10/+0.10")
print(f"  FX translation 1% on non-US revenue (56% of rev): ${0.56*b['R28']*0.01:,.0f}M revenue")

# GC carryover arithmetic
print(f"\nGC partner-online carryover: 743 total, 310 in FY27, 433 in FY28 = {433/fy27['GC']:.1%} of FY27 GC revenue")

# required growth to hit consensus
print("\nRequired growth to reach consensus revenue 43,645 from FY27 midpoint 42,686 (+2.2%)")
for gc, cv in [(-.12, -.10), (-.22, -.20), (-.04, 0)]:
    other = fy27['NA'] + fy27['EMEA'] + fy27['APLA'] + fy27['GBD']
    need = (C28['rev'] - fy27['GC'] * (1 + gc) - fy27['CONV'] * (1 + cv) - fy27['CORP']) / other - 1
    print(f"  GC {gc:+.0%}, Converse {cv:+.0%}: NA+EMEA+APLA must grow {need:+.1%}")
# if FY27 is at consensus 43,152 instead
for gc, cv in [(-.12, -.10)]:
    scale = C27['rev'] / R27
    other = (fy27['NA'] + fy27['EMEA'] + fy27['APLA']) * scale
    need = (C28['rev'] - fy27['GC'] * (1 + gc) - fy27['CONV'] * (1 + cv) - 44) / other - 1
    print(f"  with FY27 at consensus 43,152 (extra 466 spread over NA/EMEA/APLA): needed growth {need:+.1%}")

# gap decomposition vs consensus (Base)
print("\nGap decomposition Base vs consensus (EBIT then per share)")
mc = C28['ebit']/C28['rev']
dR = b['R28'] - C28['rev']
rev_eff = dR * mc
mar_eff = b['R28'] * (b['EBIT28']/b['R28'] - mc)
k = 0.75/1488
print(f"  EBIT: cons {C28['ebit']:,} base {b['EBIT28']:,.0f} diff {b['EBIT28']-C28['ebit']:,.0f} = revenue shortfall at cons margin {rev_eff:,.0f} + margin step {mar_eff:,.0f}")
fy27part = (R27 - C27['rev']) * mc
print(f"  of the revenue effect, FY27 starting-level part ({R27-C27['rev']:,.0f}) = {fy27part:,.0f}; FY28 growth part {rev_eff-fy27part:,.0f}")
cons_eps_at_our_sh = (C28['ebit']+NETINT)*0.75/1488
print(f"  consensus EBIT converted at 25% tax / 1,488M shares = {cons_eps_at_our_sh:.3f} vs published 1.646 (share/tax inconsistency {cons_eps_at_our_sh-1.646:+.3f})")
print(f"  $/sh: revenue {rev_eff*k:+.3f}, margin {mar_eff*k:+.3f}, consensus share/tax inconsistency {cons_eps_at_our_sh-1.646:+.3f}, tax/share base-vs-25%/1488 {b['EPS28']-(b['EBIT28']+NETINT)*k:+.3f}; total {b['EPS28']-1.646:+.3f}")
# revenue-only case: base revenue, consensus margin step (GM+opex residual 114 bps of rev on top of FY27 mid margin)
m_alt = EBIT27/R27 + (C28['ebit']/C28['rev'] - C27['ebit']/C27['rev'])
e_alt = (b['R28']*m_alt + NETINT)*k
print(f"  revenue-only case (base revenue, consensus margin step +{(C28['ebit']/C28['rev'] - C27['ebit']/C27['rev'])*1e4:.0f} bps on FY27 mid margin): margin {m_alt:.2%}, EPS {e_alt:.3f}, gap {e_alt-1.646:+.3f}")
# margin-only: consensus revenue, base margin
e2 = (C28['rev']*(b['EBIT28']/b['R28'])+NETINT)*k
print(f"  margin-only case (consensus revenue, base margin {b['EBIT28']/b['R28']:.2%}): EPS {e2:.3f}")
# 35% decremental variant of earlier note
for rv in (43152, 42686):
    e3 = (C28['ebit'] - (C28['rev']-rv)*0.35 + NETINT)*k
    print(f"  earlier-note style: consensus margin step kept, revenue {rv:,} with 35% decremental: EPS {e3:.3f}")

# segment attribution of the volume line (segment gross margin, Q1 FY27 10-Q pp.26-31)
SEGGM = dict(NA=.434, EMEA=.444, GC=.475, APLA=.423, CONV=.452, GBD=0.0)
SEGEBIT = dict(NA=1170/5127, EMEA=728/3176, GC=248/1180, APLA=324/1463, CONV=25/263)
print("\nSegment volume attribution, FY28 vs FY27 midpoint ($M revenue change, $/sh at segment GM, $/sh at Q1 FY27 segment EBIT margin)")
kk = 0.75/1485
for name in ('Low', 'Base', 'High'):
    r = res[name]
    tot_gm = tot_eb = 0
    out = []
    for sgm in ('NA', 'EMEA', 'GC', 'APLA', 'CONV'):
        d = r['seg28'][sgm] - fy27[sgm]
        a = d * SEGGM[sgm] * kk; e = d * SEGEBIT[sgm] * kk
        tot_gm += a; tot_eb += e
        out.append(f"{sgm} {d:+,.0f} / {a:+.3f} / {e:+.3f}")
    print(f"  {name}: " + " | ".join(out) + f" | sum {tot_gm:+.3f} / {tot_eb:+.3f}")
