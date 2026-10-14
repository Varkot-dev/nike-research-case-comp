"""Sample 400 China partner/owned store ids from the Nike locator, hit Nike's public per-store endpoint
(no login), record closingDate, hours present, and any updated-time fields. Generic UA, 0.4s sleep."""
import csv, json, random, requests, time
UA={'User-Agent':'research-bot/1.0'}
loc=[r for r in csv.DictReader(open('../stores/nike_locator_2026-10-14.csv')) if r['iso2Country']=='CN']
random.seed(7)
by={}
for r in loc: by.setdefault(r['facilityType'],[]).append(r)
sample=[]
for k,n in [('MONO_BRAND_NON_FRANCHISEE_PARTNER_STORE',170),('FRANCHISEE_PARTNER_STORE',140),('NIKE_OWNED_STORE',90)]:
    sample+=random.sample(by[k],n)
out=[]; keys=None
for r in sample:
    try:
        x=requests.get('https://api.nike.com/store/store_locations/v1/'+r['id'],headers=UA,timeout=30)
        j=x.json() if x.status_code==200 else {}
    except Exception as e: j={}
    od=j.get('operationalDetails',{})
    hrs=od.get('hoursOfOperation',{}).get('regularHours',{})
    anyh=any(hrs.get(d) for d in hrs)
    extra={k:v for k,v in j.items() if k.lower() in ('lastupdated','updatedat','modified','lastmodified','status','createdat')}
    out.append(dict(id=r['id'],facilityType=r['facilityType'],company=r['company'],city=r['city'],opening_listed=r['openingDate'],http=x.status_code if 'x' in dir() else 0,openingDate_api=od.get('openingDate',''),closingDate_api=od.get('closingDate',''),has_regular_hours=int(anyh),storeStatus=j.get('storeStatus',''),published=j.get('published',''),creationDate=j.get('creationDate',''),modificationDate=j.get('modificationDate',''),extra=json.dumps(extra),top_keys='|'.join(sorted(j.keys()))[:300]))
    time.sleep(0.4)
w=csv.DictWriter(open('nike_api_cn_sample.csv','w'),fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
