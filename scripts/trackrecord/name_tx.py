import re,sys,pathlib
src=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
for f in sorted(src.glob('938*.txt')):
    t=f.read_text(errors='ignore')
    h=t[:400]
    m=re.search(r'FY\s*(\d{2,4})\s*Q(\d)',h) or None
    if m:
        fy=m.group(1)[-2:]; q=m.group(2)
    else:
        m=re.search(r'Q(\d)FY(\d\d)',h); q=m.group(1); fy=m.group(2)
    pages=t.split('\f')
    body=''.join(f'\n[[page {i+1}]]\n'+p for i,p in enumerate(pages) if p.strip())
    (out/f'tx_Q{q}FY{fy}.txt').write_text(body)
    print(f.name,'->',f'tx_Q{q}FY{fy}.txt')
