import sys,csv,statistics,math,bisect,datetime
sys.path.insert(0,'.')
from es import *; from events import EV
# classification: id -> (dated, quantitative, vs_prior_company_target, bundled_near_term_guide, vs_consensus, group, target_summary, evidence, tag)
C={
'E01':('Y','Y','raised','none','above (SNIPPET: ATH after)','UP','$50B FY2020 revenue (about 10% CAGR from $30.6B FY15); HSD-LDD growth, 30-50 bps GM/yr, mid-teens EPS','Prior target was $36B by FY2017 (2013 meeting) so $50B is a raise; CNBC Oct 19 2015 "headed to $200"','SNIPPET'),
'E02':('Y','Y','reaffirmed (headline $50B pushed ~2 yrs)','none','better than low expectations (SNIPPET)','NEUTRAL','5-yr: HSD revenue growth, mid-teens EPS growth, digital 15% to 30% of sales; $50B pushed to ~2022 on CNBC','Analysts expected a weak event (Goldman: range-bound); Reuters: stock +3%, top Dow gainer','SNIPPET'),
'E03':('Y','Y','raised','none','above (prior-target proxy)','UP','Through FY25: revenue HSD to LDD, high-teens EBIT margin, mid-to-high-teens EPS growth (prior LT: HSD revenue, mid-teens EPS)','Raised vs Nike own prior LT targets; stock +15.5% (search snippet states +$20.75 / +15.5%, matches price file)','SNIPPET'),
'E04':('N','N','withdrawn','guide withdrawn; Investor Day postponed','below (no guide)','DOWN','FY25 guidance withdrawn, quarterly guidance only, Nov 19 2024 Investor Day postponed','Bernstein: withdrawing guidance was "a different matter"; shares -5% to -7% reported','SNIPPET'),
'E05':('Y','Y','new/higher (not sourced)','none','NA','NEUTRAL','2021-2025: sales +8% to 10% CAGR cc, op margin 12% to 14% by 2025, gross margin 53% to 55%, DTC 50% of sales','Targets from adidas annual report (search snippet); no free consensus comparison found','SNIPPET'),
'E06':('Y','Y','new (2028)','2026 EBIT guide EUR2.3B below Street','below near-term, above long-term unknown','DOWN','2028: op margin above 10%, op profit mid-teens CAGR 2026-28; 2026 op profit about EUR2.3B incl EUR400M tariff/FX hit','RBC: guide implies 8.5% to 8.8% margin vs 10% target; shares -7% intraday (Invezz)','SNIPPET'),
'E07':('Y','Y','raised','none','NA','UP','2018 revenue $7.5B (25% CAGR), op income $800M; LT growth target raised from 22% to 25%','Company press release Sep 16 2015 (search snippet); stock ATH after','SNIPPET'),
'E08':('Y','Y','new (2023)','2019 guide below consensus (rev +3-4% vs 5%; EPS 31-33c vs 33c)','below near-term','DOWN','2023: low-double-digit revenue growth/op margin, EPS CAGR about 40%; 2019 revenue +3% to 4%, NA flat','Benzinga/CNBC/Bloomberg: 2019 outlook below Street; Cowen: margin goals "pressure on everything going right"','SNIPPET'),
'E09':('N','N','n/a (leadership)','none','n/a','EXCLUDE','CEO Stephanie Linnartz replaced by Kevin Plank from Apr 1 2024','Leadership change, not a target event; shown for completeness only','SNIPPET'),
'E10':('N','N','none (FY25 outlook referenced)','none','vague/qualitative','DOWN','Invitation-only; qualitative product/brand/commercial update; FY25 outlook reaffirmed, no new multi-year numerics','Company announcement of format (search snippet); Investing.com: stock -5.5%','SNIPPET'),
'E11':('Y','Y','new (2022)','none','in line (SNIPPET: realistic, ATH)','NEUTRAL','2018-2022: about 10% cc sales CAGR, EBIT margin about 10% by 2022 (from nearly 6%), gross margin 49% to 50%','Puma release Mar 20 2018; Independent Research: priced in; another analyst: targets realistic','SNIPPET'),
'E12':('Y','Y','lowered/delayed (8.5% by 2027 vs earlier 2025 aim)','Q4 EBIT 109M vs 131M consensus','below','DOWN','nextlevel cost plan: EBIT margin 8.5% by 2027 (7.1% in 2024), 10% long term','Morgan Stanley called it a downgrade of earlier 2025 target; Q4 EBIT below consensus (optionfinance); prelims released Jan 22 after close, shares -16% to -20% Jan 23','SNIPPET'),
'E13':('Y','Y','reaffirmed (same Power of Three goals)','none','in line','NEUTRAL','Double revenue to $12.5B by 2026; double men and e-commerce, quadruple international','Coresight: same targets as 2019 plan; two of three already met early','SNIPPET'),
'E14':('Y','Y','new (FY27)','FY23 EPS guide cut to $2.60-2.70 from $3.05-3.15; revenue +5-6% from at least +7%','below near-term','DOWN','FY27: revenue mid-to-high single-digit CAGR, op margin about 15%, EPS HSD-LDD CAGR; $7B cash to shareholders','OPENED SEC 8-K Ex 99.1 Sep 28 2022 (guidance cut tabulated)','OPENED'),
'E15':('N','partial','reaffirmed (10%+ margin FY28 in no-growth case)','none','vague','DOWN','Brand-by-brand strategy; 10%+ op margin by FY28 even at flat sales; 11.5% to 12% at $11B sales; few other numbers','SGB Mar 7 2025 (opened): few numbers or timelines, analysts disappointed; shares -12% then -7%','OPENED'),
'E16':('Y','Y','new','none','NA','NEUTRAL','Three-year roadmap "Catalyzing Growth"; numeric targets not retrieved','Kontoor later said 2022 results were ahead of Investor Day targets; event ran from 2:30pm ET so day 0 partly pre-event','SNIPPET'),
'E17':('Y','Y','new (2030, Helly Hansen only)','none','NA','NEUTRAL','Helly Hansen: revenue above $1.1B by 2030 (~10% CAGR), mid-teens op margin, >$500M cumulative cash','Business Wire / FashionUnited Sep 2 2026 (search snippets)','SNIPPET'),
'E18':('Y','Y','new (2025)','2022 outlook reaffirmed','NA','NEUTRAL','2025: net sales $4.5-4.7B (9-11% CAGR), op margin about 14%, EPS $7.35-7.95, TSR 13-17%','OPENED SEC 8-K Ex 99.1 Sep 22 2022','OPENED'),
'E19':('Y','Y','raised (organic growth 6-8% from 4-6%)','FY22 EPS reaffirmed','above prior target','UP','FY27: revenue $9-10B (6-8% organic), adjusted EBIT margin 15%, $750M buyback, TSR 10-12%','OPENED SEC 8-K Ex 99.1 Jun 1 2022','OPENED'),
'E20':('Y','Y','new (2025)','none','NA','NEUTRAL','PVH+ Plan 2025: HSD revenue CAGR to $12.5B, op margin 15%, FCF >$1B, +$1B buyback','sgbonline summary (search snippet), Apr 13 2022','SNIPPET'),
'E21':('Y','Y','new (FY25)','none','NA','NEUTRAL','FY25 revenue $8B (6-7% CAGR), EPS >$5, $3B cumulative capital return','Business Wire summary (search snippet)','SNIPPET'),
'E22':('Y','Y','new (FY27-28)','none','above (SNIPPET: analysts raised EPS and PTs)','UP','FY27-28: MSD revenue growth, strong margin expansion (op margin >22% by FY28), LDD EPS growth, $4B return, new $3B buyback','Business Wire; analyst summary: estimates and PTs raised after event','SNIPPET'),
'E23':('Y','Y','new (FY25)','none','NA','NEUTRAL','FY25: mid-to-high single-digit revenue CAGR','Coresight preview (paywalled); Sep 19 2022','SNIPPET'),
'E24':('Y','partial','reaffirmed','FY26 outlook reaffirmed','in line (briefing.com: failed to inspire)','NEUTRAL','3-yr outlook: MSD compounded revenue growth, >=$2B excess FCF returned through FY28','Briefing.com Sep 16 2025: shares off trend after reaffirming','SNIPPET'),
'E25':('Y','Y','new','none','mixed (FY27 +7% growth "well above consensus" per TipRanks note; FY26 revenue down)','NEUTRAL','FY25 $4.4B, FY26 $4.1B, FY27 $4.4B revenue; op margin 2.3% / 3.7% / HSD','OPENED SEC 8-K Ex 99.1 Feb 19 2025 (table); TipRanks note SNIPPET','OPENED'),
'E26':('Y','Y','raised/new','none','above (SNIPPET: "surprisingly strong")','UP','FY23-25: comps +7-9%, revenue +10-12%, non-GAAP EPS +15-20%; about 45k stores by FY25','Motley Fool / Benzinga: bullish outlook, PT raises; Sep 13 2022 was CPI crash day (S&P -4.3%)','SNIPPET'),
'E27':('Y','Y','new (FY28)','none','NA (investors want margin proof)','NEUTRAL','FY28: adjusted op margin 13.5% to 15% (vs 10.1% latest quarter), EPS $3.35-4.00, revenue >=5% p.a.','Stocktwits/TIKR (search snippets): stock fell for 4th straight session','SNIPPET'),
'E28':('N','N','n/a','Q3 guide: sales -12% to -10%, EPS $0.20-0.30 vs $0.63 est','below','DOWN','Beauty Reimagined vision, up to 7,000 job cuts, no numeric multi-year target','Benzinga Feb 4 2025: Q3 EPS guide far below consensus; stock -16%','SNIPPET'),
'E29':('Y','Y','new (2026)','none','above (SNIPPET: analysts largely bullish)','UP','2026: revenue about $5B (17% CAGR), op margin >26%, FCF >$1B','Price rise +8.5% matches price file','SNIPPET'),
}
def pre(t,day0,n=10):
    L=load(t); 
    if not L: return None
    ds,cl=L; d0=datetime.date.fromisoformat(day0); i=bisect.bisect_left(ds,d0)
    if i-n-1<0: return None
    return cl[i-1]/cl[i-1-n]-1
rows=[]
for e in EV:
    i,t,c,ev,ad,d0,bm,sk=e
    HS=(0,1,2,3,5,20)
    r=rets(t,d0,HS); b=rets(bm,d0,HS); sp=rets('^GSPC',d0,HS)
    sec=basket(d0,[t,'UA','UAA'] if t in('UA','UAA') else [t],HS) if sk=='apparel' else rets('XLY' if sk=='xly' else 'XLP',d0,HS)
    xly=rets('XLY',d0)
    L=load(t); ds,cl=L; ii=bisect.bisect_left(ds,datetime.date.fromisoformat(d0)); hi=max(cl[max(0,ii-253):ii]); dd=cl[ii-1]/hi-1; r12=cl[ii-1]/cl[max(0,ii-253)]-1
    pre_raw=pre(t,d0); pre_sp=pre('^GSPC',d0)
    k=C[i]
    row=dict(event_id=i,ticker=t,company=c,event=ev,announce_date=ad,day0=d0,dated=k[0],quantitative=k[1],vs_prior_company_target=k[2],bundled_near_term_guide=k[3],vs_consensus=k[4],stance_group=k[5],target_summary=k[6],evidence=k[7],source_tag=k[8],price_source='Yahoo chart API adjclose')
    for h in (0,1,2,3,5,20):
        row[f'ret_d{h}']=r[h]; 
        row[f'vs_sp_d{h}']=r[h]-sp[h] if sp.get(h) is not None and r[h] is not None else None
        row[f'vs_local_d{h}']=r[h]-b[h] if b and r[h] is not None and b.get(h) is not None else None
        row[f'vs_sector_d{h}']=r[h]-sec[h] if sec and sec.get(h) is not None and r[h] is not None else None
    row['drawdown_from_52w_high']=dd; row['prior_12m_ret']=r12
    row['pre10_raw']=pre_raw; row['pre10_vs_sp']=pre_raw-pre_sp if pre_raw is not None else None
    row['sector_benchmark']='equal-weight US apparel/footwear basket ex subject' if sk=='apparel' else ('XLY' if sk=='xly' else 'XLP')
    rows.append(row)
import json
json.dump(rows,open('rows.json','w'),default=str)
cols=list(rows[0].keys())
def fmt(v):
    if isinstance(v,float): return f'{v*100:.2f}' if True else v
    return '' if v is None else str(v)
pct=lambda k: k.startswith(('ret_d','vs_sp_d','vs_local_d','vs_sector_d','pre10','drawdown','prior_12m'))
with open('events.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow([c+('_pct' if pct(c) else '') for c in cols])
    for r in rows: w.writerow([(f'{r[c]*100:.2f}' if (pct(c) and r[c] is not None) else ('' if r[c] is None else r[c])) for c in cols])
print(len(rows))
