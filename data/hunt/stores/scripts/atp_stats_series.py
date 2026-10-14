"""Pull All The Places per-run spider stats (feature counts) for footwear/sporting retail spiders.
Usage: python3 -I atp_stats_series.py <outdir>
Writes atp_spider_counts_long.csv (run_id, date, spider, features, errors)."""
import json, re, sys, time, urllib.request, os, csv
UA={"User-Agent":"Mozilla/5.0 (academic research script)"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120)
out = sys.argv[1]
H = json.load(get("https://data.alltheplaces.xyz/runs/history.json"))
PAT = re.compile(r'^(nike|converse|jordan|foot_locker.*|champs.*|kids_foot_locker|dicks_sporting_goods|dicks_house_of_sport|golf_galaxy.*|academy_us|hibbett.*|city_gear|jd_sports.*|finish_line.*|shoe_palace|dtlr|snipes.*|sports_direct.*|intersport.*|adidas.*|puma.*|new_balance.*|skechers.*|asics.*|hoka.*|on_.*|lululemon.*|under_armour.*|vans.*|anta.*|li_ning.*|dsw.*|macys.*|kohls.*|journeys.*|shoe_carnival.*|famous_footwear.*|rack_room.*|nordstrom.*|jcpenney.*|scheels.*|big_5.*|sportsmans.*|decathlon.*|topsports.*|pou_?sheng.*|yy_sports.*|footasylum.*|size_.*|the_athletes_foot.*|rebel_.*|sport_chek.*|xxl.*|zalando.*|courir.*|footshop.*|asos.*|athletes_foot.*)$')
rows = []
runs = [r for r in H if r.get('stats_url')]
for r in runs:
    rid = r['run_id']
    try:
        d = json.load(get(r['stats_url']))
    except Exception as e:
        print("fail", rid, e); continue
    res = d['results'] if isinstance(d, dict) else d
    for x in res:
        s = x.get('spider', '')
        if PAT.match(s):
            rows.append([rid, rid[:10], s, x.get('features'), x.get('errors')])
    print(rid, len(rows), flush=True)
    time.sleep(1.0)
with open(os.path.join(out, 'atp_spider_counts_long.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['run_id', 'run_date', 'spider', 'features', 'errors']); w.writerows(rows)
