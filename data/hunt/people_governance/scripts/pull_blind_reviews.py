"""Scrape public Blind (teamblind.com) company review list pages (no login): rating, title, status, role, date.
Only the first lines visible without login are kept. Usage: python3 -I pull_blind_reviews.py OUTDIR Slug1 Slug2 ..."""
import sys, os, re, csv, time, html, urllib.request
OUT = sys.argv[1]; SLUGS = sys.argv[2:]
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
PAT = re.compile(r'(\d) \.(\d) " (.*?) " (Current|Former) Employee • \S+ • (.*?) • (\w+ \d{1,2} \d{4}) Pros (.*?) Cons (.*?) Helpful')
rows = []
for slug in SLUGS:
    pg = 1; maxpg = 1
    while pg <= maxpg:
        p = os.path.join(OUT, f'raw/blind/{slug}_p{pg}.html')
        if not os.path.exists(p):
            try:
                open(p, 'wb').write(urllib.request.urlopen(urllib.request.Request(f'https://www.teamblind.com/company/{slug}/reviews?page={pg}', headers={'User-Agent': UA}), timeout=60).read())
            except Exception as e:
                print('err', slug, pg, e); break
            time.sleep(2.5)
        h = open(p, encoding='utf-8', errors='replace').read()
        if pg == 1:
            ps = [int(x) for x in re.findall(r'/company/' + re.escape(slug) + r'/reviews\?page=(\d+)', h)]
            maxpg = max(ps + [1]); hd = re.search(r'(\d\.\d) \( ([\d,]+) Reviews\)', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)))
            print(slug, 'pages', maxpg, hd.groups() if hd else None, flush=True)
        t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h))).replace('"', '"')
        for m in PAT.finditer(t):
            rows.append(dict(company=slug, rating=int(m.group(1)), title=m.group(3)[:120], status=m.group(4), role=m.group(5)[:80],
                             date=time.strftime('%Y-%m-%d', time.strptime(m.group(6), '%B %d %Y')), cons=m.group(8)[:300]))
        pg += 1
w = csv.DictWriter(open(os.path.join(OUT, 'blind_reviews_peers.csv'), 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows))
