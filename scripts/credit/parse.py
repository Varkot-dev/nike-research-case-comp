import re,glob,os,csv,sys
RAW='/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/raw/h2'
def num(x): return float(x.replace('.','').replace(',','.'))
def load(slug,mk='BMN'):
    rows={}
    for f in sorted(glob.glob(f'{RAW}/{slug}_{mk}_*.html')):
        h=open(f,errors='ignore').read()
        toks=[x.strip() for x in re.sub(r'<[^>]+>','|',h).split('|')]
        t='|'+'|'.join(x for x in toks if x)+'|'
        for m in re.finditer(r'\|(\d\d)\.(\d\d)\.(\d{4})\|([\d.,]+)\|([\d.,]+)\|([\d.,]+)\|([\d.,]+)\|',t):
            d=f'{m[3]}-{m[2]}-{m[1]}'
            rows[d]=dict(open=num(m[4]),close=num(m[5]),high=num(m[6]),low=num(m[7]))
    return rows
if __name__=='__main__':
    for s in sys.argv[1:]:
        r=load(s); ds=sorted(r)
        print(s,len(r),ds[:1],ds[-1:], r[ds[-1]] if ds else None)
