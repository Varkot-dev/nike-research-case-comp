"""Free web-traffic estimates for nike.com and peers.
1) Semrush public overview page https://www.semrush.com/website/{d}/overview/ : 6 months of visits (desktop/mobile),
   search traffic (organic/paid), backlinks, traffic by country. Data embedded in the page's astro-island props.
2) HypeStat https://hypestat.com/info/{d} : monthly visits, MoM change, daily uniques, pages/visit, bounce.
Raw HTML saved gzipped to raw/web_traffic/{date}/. Tidy output: web_semrush_history.csv, web_semrush_country.csv, web_hypestat_snapshot.csv
"""
import re, html, json, os, gzip, time, csv, datetime, urllib.request
D = datetime.date.today().isoformat()
BASE = "/home/user/nike-research-case-comp/data/hunt/apps_digital"
RAW = f"{BASE}/raw/web_traffic/{D}"; os.makedirs(RAW, exist_ok=True)
DOMAINS = ["nike.com", "adidas.com", "hoka.com", "on.com", "newbalance.com", "asics.com", "puma.com", "underarmour.com",
           "skechers.com", "lululemon.com", "brooksrunning.com", "converse.com", "vans.com", "stockx.com", "goat.com",
           "footlocker.com", "dickssportinggoods.com", "jdsports.com", "finishline.com", "zappos.com", "adidas.co.uk",
           "adidas.de", "nike.com.cn", "deckers.com", "saucony.com", "anta.com", "reebok.com", "alo yoga".replace(" yoga", "yoga.com"), "jdsports.co.uk", "amazon.com"]
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

def get(url, fn):
    if os.path.exists(fn):
        return gzip.open(fn, "rt", errors="ignore").read()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            s = r.read().decode("utf8", "ignore")
    except Exception as e:
        print("ERR", url, e, flush=True); return None
    with gzip.open(fn, "wt") as f: f.write(s)
    time.sleep(2.0)
    return s

def dec(v):
    if isinstance(v, list) and len(v) == 2 and isinstance(v[0], int):
        t, val = v
        if t == 1: return [dec(x) for x in val]
        if t == 0: return dec(val)
        return val
    if isinstance(v, dict): return {k: dec(x) for k, x in v.items()}
    if isinstance(v, list): return [dec(x) for x in v]
    return v

hist, ctry, hyp = [], [], []
for d in DOMAINS:
    s = get(f"https://www.semrush.com/website/{d}/overview/", f"{RAW}/semrush_{d}.html.gz")
    if s:
        for p in re.findall(r'props="([^"]*)"', s):
            try: obj = dec(json.loads(html.unescape(p)))
            except Exception: continue
            data = obj.get("page", {}).get("data", {}) if isinstance(obj, dict) else {}
            if not data: continue
            for r in (data.get("trafficByDevice") or {}).get("history") or []:
                hist.append([d, r["displayDate"], "visits", r.get("visits")]); hist.append([d, r["displayDate"], "desktop_visits", r.get("desktopVisits")]); hist.append([d, r["displayDate"], "mobile_visits", r.get("mobileVisits")])
            for r in (data.get("searchTraffic") or {}).get("history") or []:
                for k in ("organic", "paid", "total"): hist.append([d, r["displayDate"], "search_" + k, r.get(k)])
            for r in (data.get("backlinks") or {}).get("referringDomainsHistory") or []:
                hist.append([d, r["displayDate"], "referring_domains", r.get("referringDomains")])
            tc = data.get("trafficByCountry") or {}
            for r in tc.get("series") or []:
                ctry.append([d, tc.get("displayDate"), r.get("country"), json.dumps({k: v for k, v in r.items() if k not in ("country", "countryName")})])
    h = get(f"https://hypestat.com/info/{d}", f"{RAW}/hypestat_{d}.html.gz")
    if h:
        t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)))
        def grab(p):
            m = re.search(p, t); return m.group(1) if m else ""
        hyp.append([D, d, grab(r"Monthly Visits ([0-9,]+) "), grab(r"Monthly Visits [0-9.]+[KMB]? ([▼▲] ?[0-9.]+%)"),
                    grab(r"Daily Unique Visitors ([0-9,]+)"), grab(r"Pages per Visit ([0-9.]+)"), grab(r"Bounce Rate ([0-9.]+%)"),
                    grab(r"Monthly Visits \(SEMrush\) ([0-9,]+)"), grab(r"ranks ([0-9,]+) globally")])
    print(d, len(hist), len(ctry), flush=True)
w = lambda fn, hdr, rows: csv.writer(open(f"{BASE}/{fn}", "w", newline="")).writerows([hdr] + rows)
w("web_semrush_history.csv", ["domain", "month", "metric", "value"], hist)
w("web_semrush_country_raw.csv", ["domain", "display_date", "country", "fields_json"], ctry)
w("web_hypestat_snapshot.csv", ["pulled", "domain", "monthly_visits", "mom_change", "daily_uniques", "pages_per_visit", "bounce_rate", "semrush_monthly_visits", "hypestat_global_rank"], hyp)
