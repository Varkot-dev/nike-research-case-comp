import subprocess,re,json,sys,time,os
RAW='/tmp/claude-0/-home-user-nike-research-case-comp/2bf9f309-3096-5c65-b9c3-02b984182743/scratchpad/raw/h2'
os.makedirs(RAW,exist_ok=True)
slugs=sys.argv[1].split(',')
mk=sys.argv[2] if len(sys.argv)>2 else 'BMN'
ranges=[('2023-01-01','2023-12-31'),('2024-01-01','2024-12-31'),('2025-01-01','2025-12-31'),('2026-01-01','2026-10-15')]
for s in slugs:
    inst=s.replace('-anleihe','')
    for a,b in ranges:
        fn=f'{RAW}/{s}_{mk}_{a[:4]}.html'
        if os.path.exists(fn) and os.path.getsize(fn)>600: continue
        url=f'https://www.finanzen.net/Ajax/BondController_HistoricPriceList/{inst}/{mk}/{a}_{b}'
        subprocess.run(['curl','-sS','-m','40','-X','POST','-d','','-A','Mozilla/5.0 (X11; Linux x86_64) Chrome/120','-H','X-Requested-With: XMLHttpRequest','-H','Origin: https://www.finanzen.net','-H',f'Referer: https://www.finanzen.net/anleihen/historisch/{s}',url,'-o',fn])
        time.sleep(0.4)
    print(s,[os.path.getsize(f'{RAW}/{s}_{mk}_{y}.html') if os.path.exists(f'{RAW}/{s}_{mk}_{y}.html') else 0 for y in (2023,2024,2025,2026)])
