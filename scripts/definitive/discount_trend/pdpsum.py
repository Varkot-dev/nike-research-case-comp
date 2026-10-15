import csv,collections,statistics as st
r=list(csv.DictReader(open('pdp_panel.csv')))
g=collections.defaultdict(list); bad=collections.Counter()
for x in r:
    if x['status']!='ok' or not x['full'] or float(x['full'])<=0: bad[(x['coll'],x['brand'])]+=1; continue
    g[(x['coll'],x['brand'])].append(max(0,1-float(x['current'])/float(x['full'])))
for k in sorted(g):
    d=g[k]; dd=[v for v in d if v>0.005]
    n=len(d); p=len(dd)/n
    se=(p*(1-p)/n)**.5
    print(k[0],k[1],'n',n,'pool',[x['pool'] for x in r if (x['coll'],x['brand'])==k][0],'share_disc %.1f (+-%.1f)'%(100*p,196*se),'depth_disc %.1f'%(100*st.mean(dd)) if dd else '-','avg_all %.1f'%(100*st.mean(d)),'bad',bad[k])
