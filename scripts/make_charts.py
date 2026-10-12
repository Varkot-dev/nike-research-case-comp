"""Builds all report charts. Data quality flags: V = checked against search summaries
citing SEC/Nike releases; A = approximate (model memory, NOT verified); S = secondary source."""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "charts")
os.makedirs(OUT, exist_ok=True)

BLUE, ORANGE, GRAY, RED, GREEN = "#2a6fb0", "#e07b00", "#8a8f98", "#c0392b", "#2e8b57"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "figure.dpi": 130, "savefig.bbox": "tight"})
SRC = "Sources: Nike SEC filings via search summaries; hatched = approximate/unverified"

def save(name):
    plt.savefig(os.path.join(OUT, name)); plt.close()

# ---------- 1. Annual revenue + gross margin ----------
yrs = ["FY19","FY20","FY21","FY22","FY23","FY24","FY25","FY26"]
rev = [39.117,37.403,44.538,46.710,51.217,51.362,46.309,46.398]
gm  = [44.7,43.4,44.8,46.0,43.5,44.6,42.7,42.9]
eps = [2.49,1.62,3.56,3.75,3.23,3.73,2.16,2.10]
ver = [False,False,False,False,False,False,True,True]
fig, ax = plt.subplots(figsize=(8,4.6))
bars = ax.bar(yrs, rev, color=[BLUE if v else "#9db9d6" for v in ver],
              hatch=None)
for b,v in zip(bars,ver):
    if not v: b.set_hatch("//"); b.set_edgecolor("white")
ax.set_ylabel("Revenue ($ billions)"); ax.set_ylim(0,60)
for x,r in zip(yrs,rev): ax.text(x, r+0.8, f"{r:.1f}", ha="center", fontsize=9)
ax2 = ax.twinx(); ax2.spines["right"].set_visible(True)
ax2.plot(yrs, gm, color=ORANGE, marker="o", lw=2); ax2.set_ylim(38,48); ax2.set_ylabel("Gross margin (%)", color=ORANGE)
ax.set_title("Revenue has stalled since FY23 and gross margin has slipped")
ax.legend(handles=[Patch(color=BLUE,label="Revenue (checked)"),Patch(facecolor="#9db9d6",hatch="//",edgecolor="white",label="Revenue (approximate)"),
                   plt.Line2D([],[],color=ORANGE,marker="o",label="Gross margin")], loc="lower left", fontsize=8, frameon=False)
fig.text(0.01,-0.02,SRC,fontsize=7,color=GRAY)
save("01_annual_revenue_margin.png")

# ---------- 2. Annual EPS + FY27 guidance ----------
fig, ax = plt.subplots(figsize=(8,4.4))
labs = yrs+["FY27E"]
vals = eps+[1.25]
cols = [BLUE if v else "#9db9d6" for v in ver]+[ORANGE]
bs = ax.bar(labs, vals, color=cols)
for b,v in zip(bs[:-1],ver):
    if not v: b.set_hatch("//"); b.set_edgecolor("white")
ax.errorbar(["FY27E"],[1.25],yerr=[[0.10],[0.10]],color="black",capsize=6,lw=1.5)
for x,v in zip(labs,vals): ax.text(x, v+0.18, f"${v:.2f}", ha="center", fontsize=9)
ax.set_ylabel("Diluted EPS ($)"); ax.set_ylim(0,4.4)
ax.set_title("Earnings per share fell by about 44% from FY24; guidance implies another drop")
fig.text(0.01,-0.04,"FY27E = midpoint of adjusted EPS guidance $1.15 to $1.35 (excludes about $0.15 Pace cost). FY26 includes a one-time tariff recovery of $0.52/share.\n"+SRC,fontsize=7,color=GRAY)
save("02_eps_and_guidance.png")

# ---------- 3. Quarterly revenue + GM ----------
q = ["Q1 24","Q2 24","Q3 24","Q4 24","Q1 25","Q2 25","Q3 25","Q4 25","Q1 26","Q2 26","Q3 26","Q4 26","Q1 27"]
qrev = [12.939,13.388,12.429,12.606,11.589,12.354,11.269,11.097,11.700,12.400,11.300,10.970,11.210]
qgm  = [44.2,44.6,44.8,44.7,44.7,43.6,41.5,40.3,42.2,40.6,40.2,49.2,42.8]
qver = [False]*6+[True]*7
fig, ax = plt.subplots(figsize=(10,4.8))
bs = ax.bar(q,qrev,color=[BLUE if v else "#9db9d6" for v in qver])
for b,v in zip(bs,qver):
    if not v: b.set_hatch("//"); b.set_edgecolor("white")
ax.set_ylim(0,16); ax.set_ylabel("Quarterly revenue ($ billions)")
ax2 = ax.twinx(); ax2.spines["right"].set_visible(True)
ax2.plot(q,qgm,color=ORANGE,marker="o",lw=2); ax2.set_ylim(36,52); ax2.set_ylabel("Gross margin (%)",color=ORANGE)
ax2.annotate("49.2% includes a one-time\n$986M tariff recovery\n(about 40.2% without it)",xy=(11,49.2),xytext=(6.2,50.4),
             arrowprops=dict(arrowstyle="->",color=RED),color=RED,fontsize=8,va="top")
ax.set_title("Quarterly revenue and gross margin (fiscal quarters)")
fig.text(0.01,-0.03,"Q4 FY26 ex-tariff margin is my own subtraction of the reported 900 bps. "+SRC,fontsize=7,color=GRAY)
save("03_quarterly.png")

# ---------- 4. Geography ----------
geo_years = ["FY23","FY24","FY25","FY26 (est)"]
geo = {"North America":[21.608,21.369,19.572,20.5],"EMEA":[13.418,13.695,12.257,12.6],
       "Greater China":[7.248,7.547,6.586,5.85],"APLA":[6.431,6.543,6.251,6.2],"Converse":[2.427,2.082,1.692,1.2]}
cols = [BLUE,ORANGE,RED,GREEN,GRAY]
fig, ax = plt.subplots(figsize=(8.5,4.6))
w=0.16
import numpy as np
x=np.arange(len(geo_years))
for i,(k,v) in enumerate(geo.items()):
    ax.bar(x+(i-2)*w,v,w,label=k,color=cols[i])
ax.set_xticks(x); ax.set_xticklabels(geo_years); ax.set_ylabel("Revenue ($ billions)")
ax.legend(frameon=False,fontsize=8,ncol=3)
ax.set_title("Greater China and Converse are shrinking fastest")
fig.text(0.01,-0.03,"FY23-FY24 from memory; FY25 from SEC XBRL via search; FY26 are aggregator estimates (~). Treat as directional.",fontsize=7,color=GRAY)
save("04_geography.png")

# ---------- 5. Stock price ----------
pt = ["Dec 2019","Dec 2020","Dec 2021","Dec 2022","Dec 2023","Dec 2024","Dec 2025","Oct 9 2026"]
px = [101.31,141.47,166.66,117.01,108.57,75.67,63.6,34.71]
fig, ax = plt.subplots(figsize=(9,4.6))
ax.plot(pt,px,color=BLUE,marker="o",lw=2.2)
for xx,p in zip(pt,px): ax.text(xx,p+6,f"${p:.0f}",ha="center",fontsize=9)
ax.axhline(179.10,color=GRAY,ls="--",lw=1); ax.text(0,182,"All-time high ~$179 (Nov 5, 2021, intraday)",fontsize=8,color=GRAY)
ax.set_ylim(0,200); ax.set_ylabel("Share price ($)")
ax.set_title("NKE has fallen about 80% from its peak and sits near a 13-year low")
fig.text(0.01,-0.03,"Year-end closes are approximate (memory); Dec 2025 is derived from a reported -46% YTD figure; Oct 2026 close from Macrotrends (secondary).",fontsize=7,color=GRAY)
save("05_stock_price.png")

# ---------- 6. Executive exits timeline (one row per person) ----------
people = [("2020-02","Eric Sprunk","COO (retired)"),("2020-02","Elliott Hill","Pres., Consumer (retired; returned as CEO 2024)"),
 ("2021-03","Ann Hebert","VP/GM North America (resigned)"),("2024-04","Andy Campion","CFO then COO (left)"),
 ("2024-09","John Donahoe","CEO (retirement announced)"),("2024-10","John Slusher","Global Sports Marketing (retired)"),
 ("2025-01","Monique Matheson","CHRO (retired)"),("2025-03","Daniel Heaf","Chief Strategy Officer (role eliminated)"),
 ("2025-03","KeJuan Wilkins","Chief Comms Officer (left)"),("2025-05","Heidi O'Neill","President, Consumer/Product/Brand (role eliminated)"),
 ("2025-07","Jared Carver","CEO, Converse (left)"),("2025-10","John Hoke","Chief Innovation Officer (retired)"),
 ("2025-12","Muge Dogan","CTO (role eliminated)"),("2025-12","Craig Williams","Chief Commercial Officer (role eliminated)"),
 ("2026-01","Carl Grebert","EMEA head (retiring)"),("2026-03","Angela Dong","Greater China head (stepped down)"),
 ("2026-04","Tony Bignell","Innovation chief (left)"),("2026-09","Matt Friend","CFO (left)"),("2026-09","Johanna Nielsen","Chief Accounting Officer (resigned)")]
def tx(s): y,m=s.split("-"); return int(y)+(int(m)-1)/12
fig, ax = plt.subplots(figsize=(11,7))
n=len(people)
for i,(d,name,role) in enumerate(people):
    y=n-1-i; xx=tx(d); c = RED if xx>=tx("2024-10") else BLUE
    ax.hlines(y,2019.7,xx,color="#dddddd",lw=1); ax.plot(xx,y,"o",color=c,ms=8)
    ax.text(xx+0.12,y,f"{name}: {role}",va="center",fontsize=8.5,color=c)
ax.axvline(tx("2024-10"),color=ORANGE,ls="--"); ax.text(tx("2024-10")-0.08,n-0.2,"Hill becomes CEO (Oct 14, 2024)",color=ORANGE,fontsize=8.5,ha="right")
ax.set_yticks([]); ax.set_xlim(2019.7,2029.2); ax.set_ylim(-1,n+0.5); ax.set_xticks(range(2020,2028))
ax.spines["left"].set_visible(False)
ax.set_title("Senior exits since 2020: 5 before Hill, 14 under Hill (Donahoe counted as pre-Hill)",fontsize=10.5)
ax.legend(handles=[Patch(color=BLUE,label="Before Hill"),Patch(color=RED,label="Hill era")],frameon=False,loc="lower left")
fig.text(0.01,0.0,"Dates are announcement or effective month as reported; sources differ. Several exits were official retirements, others were eliminated roles. Not a complete census.",fontsize=7,color=GRAY)
save("06_exec_exits_timeline.png")

# ---------- 7. Exits per year ----------
cnt = {}
for d,name,role in people: cnt[d[:4]] = cnt.get(d[:4],0)+1
yy = sorted(cnt)
fig, ax = plt.subplots(figsize=(7,4))
ax.bar(yy,[cnt[y] for y in yy],color=[BLUE if int(y)<2025 else RED for y in yy])
for y in yy: ax.text(y,cnt[y]+0.1,str(cnt[y]),ha="center")
ax.set_ylabel("Named senior exits"); ax.set_title("Named senior exits by calendar year")
fig.text(0.01,-0.04,"Counts only people named in this research (not a census). 2024 includes Donahoe. 2026 runs through October. Colors split at 2025 for readability.",fontsize=7,color=GRAY)
save("07_exits_per_year.png")

# ---------- 8. Layoffs ----------
lay = [("Feb 2024",1600),("Jan 2026",775),("Apr 2026",1400)]
fig, ax = plt.subplots(figsize=(6.5,3.8))
ax.bar([l[0] for l in lay],[l[1] for l in lay],color=[BLUE,RED,RED])
for l in lay: ax.text(l[0],l[1]+30,f"~{l[1]:,}",ha="center")
ax.set_ylabel("Jobs cut (approx.)"); ax.set_title("Announced layoff rounds with a stated size")
fig.text(0.01,-0.05,"Excludes Apr 2024 ('hundreds'), Aug 2024 (<1% corporate) and the Oct 2026 Pace program (no headcount given).",fontsize=7,color=GRAY)
save("08_layoffs.png")

# ---------- 9. Q1 FY27 segment moves ----------
seg = ["North America","EMEA","Greater China","APLA","Converse","Nike Direct","Wholesale"]
chg = [2,-5,-22,0,-28,-8,-1]
fig, ax = plt.subplots(figsize=(8,4.2))
ax.barh(seg[::-1],chg[::-1],color=[GREEN if c>0 else RED if c<0 else GRAY for c in chg[::-1]])
for i,c in enumerate(chg[::-1]): ax.text(c+(0.6 if c>=0 else -0.6),i,f"{c:+d}%",va="center",ha="left" if c>=0 else "right",fontsize=9)
ax.axvline(0,color="black",lw=0.8); ax.set_xlim(-35,8); ax.set_xlabel("Year-over-year change, Q1 FY27 (%)")
ax.set_title("Q1 FY27: only North America grew")
fig.text(0.01,-0.05,"Secondary source (Vanderbilt Report); APLA reported as flat or -2% by different sources; Greater China -22% reported, -26% currency-neutral.",fontsize=7,color=GRAY)
save("09_q1fy27_segments.png")

# ---------- 10. Scenario value ----------
sc = {"Bear":(0.95,22),"Base":(1.9,19),"Bull":(2.8,18)}  # illustrative FY28 EPS x P/E
fig, ax = plt.subplots(figsize=(7,4))
names=list(sc); prices=[sc[n][0]*sc[n][1] for n in names]
ax.bar(names,prices,color=[RED,GRAY,GREEN]); ax.axhline(34.71,color="black",ls="--"); ax.text(2.45,35.6,"Now $34.71",ha="right",fontsize=8)
for n,p in zip(names,prices): ax.text(n,p+1,f"${p:.0f}\n({sc[n][0]:.2f} EPS x {sc[n][1]} P/E)",ha="center",fontsize=8)
ax.set_ylim(0,75); ax.set_ylabel("Implied share price ($)")
ax.set_title("ILLUSTRATIVE scenario framework (assumptions are mine, not forecasts)")
fig.text(0.01,-0.05,"Inputs are placeholder assumptions to show the method; replace with sourced estimates before using in a recommendation.",fontsize=7,color=RED)
save("10_scenarios_illustrative.png")
print("done", os.listdir(OUT))
