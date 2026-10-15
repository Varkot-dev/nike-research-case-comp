"""Pull 'Kit manufacturer' columns from Wikipedia league season pages (REST HTML), 2014-15 to 2026-27."""
import sys, os, time, urllib.request, urllib.parse, io, re
import pandas as pd
UA = {"User-Agent": "nike-research-casecomp/1.0 (student research)"}
RAW = sys.argv[1]; OUT = sys.argv[2]
euro = ["Premier League","La Liga","Serie A","Bundesliga","Ligue 1","Eredivisie","Primeira Liga","EFL Championship","Süper Lig","Belgian Pro League","Scottish Premiership","Saudi Pro League"]
cal = ["Campeonato Brasileiro Série A","J1 League"]
pages=[]
for y in range(2014, 2027):
    s = f"{y}–{str(y+1)[2:]}"
    for L in euro: pages.append((L, s, f"{s} {L}"))
for y in range(2015, 2027):
    for L in cal: pages.append((L, str(y), f"{y} {L}"))
rows=[]
for L, season, title in pages:
    fn = os.path.join(RAW, re.sub(r'[^A-Za-z0-9]+','_',title)+".html")
    if not os.path.exists(fn):
        url = "https://en.wikipedia.org/api/rest_v1/page/html/" + urllib.parse.quote(title.replace(" ","_"))
        html=None
        for k in range(5):
            try:
                html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read(); break
            except Exception as e:
                if "404" in str(e): break
                time.sleep(15*(k+1))
        if html is None: print("MISS", title); continue
        open(fn,"wb").write(html)
        time.sleep(3)
    try: tabs = pd.read_html(fn)
    except Exception as e: print("NOTAB", title); continue
    got=False
    for t in tabs:
        if isinstance(t.columns, pd.MultiIndex): t.columns=[" ".join(map(str,c)) for c in t.columns]
        cols=[str(c) for c in t.columns]
        kc=[c for c in cols if re.search(r'kit (manufacturer|supplier|maker)|kit\s*$|manufacturer', c, re.I)]
        tc=[c for c in cols if re.search(r'^(team|club)', c, re.I)]
        if kc and tc and len(t)>=6:
            for _,r in t.iterrows():
                rows.append(dict(league=L, season=season, page=title, team=str(r[tc[0]]), kit_raw=str(r[kc[0]])))
            got=True; break
    if not got: print("NOKIT", title)
df=pd.DataFrame(rows); df.to_csv(OUT, index=False); print(len(df))
