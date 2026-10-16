import re,glob,collections,csv
MONTHS='january february march april may june july august september october november december'.split()
rows=[]
for f in glob.glob('/tmp/claude-0/scr/srsm/n*.xml'):
    for u,l in re.findall(r'<loc>([^<]*)</loc><lastmod>([^<]*)',open(f).read()):
        if '/news/articles/' in u: rows.append((u.split('/news/articles/')[1],l[:10]))
out=[]
for s,l in rows:
    m=re.search(r'release-dates?-(.*)$',s)
    if not m: continue
    t=m.group(1)
    y=re.search(r'(20\d\d)',t); y=y.group(1) if y else ''
    mo=''
    for i,mn in enumerate(MONTHS):
        if re.search(r'(^|-)'+mn+r'(-|$)',t): mo=i+1;break
    season=''
    for sn in ['spring','summer','fall','holiday','winter','autumn']:
        if sn in t: season=sn;break
    out.append((s,l,y,mo,season,t))
csv.writer(open('/tmp/claude-0/scr/sr_news_release.csv','w')).writerows([('slug','pub','target_year','target_month','target_season','tail')]+out)
print(len(out), sum(1 for o in out if o[2] and o[3]), sum(1 for o in out if o[2] and not o[3] and o[4]))
