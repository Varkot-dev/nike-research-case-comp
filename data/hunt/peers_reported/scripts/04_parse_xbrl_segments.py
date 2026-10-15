"""Parse downloaded XBRL instances: all revenue/gross-profit/inventory facts with their dimensional context.
Output: raw/sec_xbrl_dimensional_facts.csv (long; deduplicated keeping latest filing per (company,tag,start,end,dims))."""
import re, glob, os, csv, sys, xml.etree.ElementTree as ET
S=sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/xbrl'
OUT='/home/user/nike-research-case-comp/data/hunt/peers_reported/raw/sec_xbrl_dimensional_facts.csv'
KEEP=re.compile(r'^(Revenues|RevenueFromContractWithCustomerExcludingAssessedTax|RevenueFromContractWithCustomerIncludingAssessedTax|SalesRevenueNet|Revenue|RevenueFromContractsWithCustomers|GrossProfit|CostOfRevenue|CostOfGoodsAndServicesSold|CostOfSales|InventoryNet|Inventories|InventoryFinishedGoods|InventoryFinishedGoodsNetOfReserves|OperatingIncomeLoss|SegmentReportingInformationRevenue.*|.*EarningsBeforeInterestAndTaxes.*)$')
best={}
files=sorted(glob.glob(S+'/*.xml'))
for fn in files:
    b=os.path.basename(fn); parts=b.split('_'); co=parts[0]; form=parts[2]; acc=parts[3].replace('.xml','')
    try: root=ET.parse(fn).getroot()
    except Exception as e: print('bad',b,e); continue
    ctx={}
    for c in root.iter():
        if not c.tag.endswith('}context'): continue
        cid=c.get('id'); st=en=inst=None; dims=[]
        for e in c.iter():
            t=e.tag.split('}')[-1]
            if t=='startDate': st=e.text.strip()
            elif t=='endDate': en=e.text.strip()
            elif t=='instant': inst=e.text.strip()
            elif t=='explicitMember': dims.append(e.get('dimension').split(':')[-1]+'='+e.text.strip().split(':')[-1])
            elif t=='typedMember': dims.append(e.get('dimension').split(':')[-1]+'=typed')
        ctx[cid]=(st,en or inst,';'.join(sorted(dims)))
    for e in root:
        tag=e.tag.split('}')[-1]
        if not KEEP.match(tag): continue
        c=ctx.get(e.get('contextRef'))
        if not c or e.text is None: continue
        try: v=float(e.text)
        except: continue
        unit=e.get('unitRef')
        k=(co,tag,c[0],c[1],c[2])
        rep=parts[1]
        if k not in best or rep>best[k]['report_date']:
            best[k]=dict(company=co,tag=tag,start=c[0],end=c[1],dims=c[2],value=v,unit=unit,form=form,report_date=rep,accn=acc)
with open(OUT,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['company','tag','start','end','dims','value','unit','form','report_date','accn']); w.writeheader()
    for k in sorted(best): w.writerow(best[k])
print(len(best),'facts', os.path.getsize(OUT))
