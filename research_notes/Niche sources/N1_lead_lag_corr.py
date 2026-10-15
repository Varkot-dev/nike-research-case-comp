import numpy as np
rev={2015:30601,2016:32376,2017:34350,2018:36397,2019:39117,2020:37403,2021:44538,2022:46710,2023:51217,2024:51362,2025:46309,2026:46398}
g={y:(rev[y]/rev[y-1]-1)*100 for y in rev if y-1 in rev}
na_fw={2021:11644,2023:14897,2024:14537,2025:12684,2026:13317}
series={
 'Piper all-teens Nike footwear share, Spring (pct)':{2019:41,2020:47,2021:56,2022:60,2023:61,2024:59,2025:49},
 'Interbrand Nike brand value (USD B)':{2020:34.4,2021:42.5,2022:50.3,2023:53.8,2024:45.4,2025:33.7},
 'Interbrand Nike rank (negated)':{2013:-24,2014:-22,2015:-17,2016:-18,2017:-18,2018:-17,2019:-16,2020:-15,2021:-11,2022:-10,2023:-9,2024:-14,2025:-23},
 'Kantar BrandZ Nike value (USD B)':{2021:83.7,2022:109.6,2023:74.9,2024:71.6,2025:49.4,2026:41.2},
 'Kantar BrandZ Nike rank (negated)':{2013:-56,2014:-34,2015:-28,2016:-24,2017:-26,2018:-29,2019:-21,2020:-21,2021:-17,2022:-13,2023:-21,2024:-27,2025:-51,2026:-69},
 'Brand Finance Global500 Nike rank (negated)':{2013:-60,2014:-35,2015:-31,2016:-29,2017:-28,2018:-40,2019:-41,2020:-40,2021:-47,2022:-49,2023:-54,2024:-62,2025:-66},
 'ACSI Nike score':{2018:77,2019:81,2020:78,2021:78,2022:81,2024:85,2025:83},
}
out=[]
def corr(s,k,use_change=False):
    xs=[];ys=[]
    d=dict(s)
    if use_change:
        d={y:d[y]-d[y-1] for y in d if y-1 in d}
    for y,v in d.items():
        fy=y+k
        if fy in g: xs.append(v); ys.append(g[fy])
    n=len(xs)
    if n<4: return (n,None)
    r=np.corrcoef(xs,ys)[0,1]
    return (n,round(float(r),2))
print('Nike revenue growth by FY',{y:round(v,1) for y,v in g.items()})
for name,s in series.items():
    for ch in (False,True):
        row=[name,'change' if ch else 'level']
        for k in (-1,0,1,2):
            row.append(corr(s,k,ch))
        print(row)
