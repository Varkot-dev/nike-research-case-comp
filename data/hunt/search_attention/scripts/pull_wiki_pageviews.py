"""Pull daily Wikipedia pageviews (user agent only) for Nike and rival brand / product articles.

Source: Wikimedia REST API, https://wikimedia.org/api/rest_v1/metrics/pageviews/
Titles are first resolved through the MediaWiki API (redirects followed) so we query canonical titles.
Respects 429 Retry-After. Re-run: python3 -I pull_wiki_pageviews.py <outdir>
"""
import json, os, sys, time, urllib.parse, urllib.request

UA = "NikeCaseCompResearch/1.0 (academic case competition research; contact via repo)"
OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/wiki"
os.makedirs(OUT, exist_ok=True)
START, END = "20190101", "20261013"

# (project, label, candidate title)
ARTICLES = [
    ("en.wikipedia", "nike_inc", "Nike, Inc."),
    ("en.wikipedia", "air_jordan", "Air Jordan"),
    ("en.wikipedia", "nike_dunk", "Nike Dunk"),
    ("en.wikipedia", "air_force_1", "Air Force 1 (shoe)"),
    ("en.wikipedia", "air_max", "Nike Air Max"),
    ("en.wikipedia", "nike_pegasus", "Nike Pegasus"),
    ("en.wikipedia", "nike_vomero", "Nike Vomero"),
    ("en.wikipedia", "nike_vaporfly", "Nike Vaporfly"),
    ("en.wikipedia", "converse", "Converse (shoe company)"),
    ("en.wikipedia", "hoka", "Hoka One One"),
    ("en.wikipedia", "on_running", "On (company)"),
    ("en.wikipedia", "asics", "ASICS"),
    ("en.wikipedia", "new_balance", "New Balance"),
    ("en.wikipedia", "adidas", "Adidas"),
    ("en.wikipedia", "adidas_samba", "Adidas Samba"),
    ("en.wikipedia", "adidas_gazelle", "Adidas Gazelle"),
    ("en.wikipedia", "puma", "Puma (brand)"),
    ("en.wikipedia", "skechers", "Skechers"),
    ("en.wikipedia", "brooks", "Brooks Sports"),
    ("en.wikipedia", "saucony", "Saucony"),
    ("en.wikipedia", "salomon", "Salomon Group"),
    ("en.wikipedia", "lululemon", "Lululemon"),
    ("en.wikipedia", "under_armour", "Under Armour"),
    ("en.wikipedia", "deckers", "Deckers Brands"),
    ("en.wikipedia", "crocs", "Crocs"),
    ("en.wikipedia", "anta", "Anta Sports"),
    ("en.wikipedia", "li_ning", "Li-Ning"),
    ("en.wikipedia", "elliott_hill", "Elliott Hill"),
    ("en.wikipedia", "john_donahoe", "John Donahoe"),
    # Other language editions: attention outside the US
    ("zh.wikipedia", "zh_nike", "耐克"),
    ("zh.wikipedia", "zh_adidas", "愛迪達"),
    ("zh.wikipedia", "zh_anta", "安踏体育"),
    ("zh.wikipedia", "zh_li_ning", "李宁有限公司"),
    ("de.wikipedia", "de_nike", "Nike (Unternehmen)"),
    ("de.wikipedia", "de_adidas", "Adidas"),
    ("de.wikipedia", "de_on", "On (Unternehmen)"),
    ("de.wikipedia", "de_hoka", "Hoka"),
    ("ja.wikipedia", "ja_nike", "ナイキ"),
    ("ja.wikipedia", "ja_adidas", "アディダス"),
    ("ja.wikipedia", "ja_asics", "アシックス"),
]


def get(url, tries=8):
    for i in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Api-User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = int(e.headers.get("retry-after", "30")) + 5
                print(f"429, waiting {wait}s", flush=True)
                time.sleep(wait)
                continue
            if e.code == 404:
                return {"_404": True}
            print("HTTP", e.code, url, flush=True)
            time.sleep(10)
        except Exception as e:  # network blips
            print("ERR", e, flush=True)
            time.sleep(10)
    return None


def resolve(project, title):
    url = (f"https://{project}.org/w/api.php?action=query&format=json&redirects=1&titles="
           + urllib.parse.quote(title))
    d = get(url)
    if not d or "query" not in d:
        return title
    pages = d["query"].get("pages", {})
    for p in pages.values():
        if "missing" in p:
            return None
        return p["title"]
    return title


for project, label, title in ARTICLES:
    fn = os.path.join(OUT, f"{label}.json")
    if os.path.exists(fn):
        continue
    canon = resolve(project, title)
    time.sleep(1.5)
    if canon is None:
        print("MISSING", project, title, flush=True)
        json.dump({"label": label, "project": project, "title": title, "missing": True}, open(fn, "w"))
        continue
    t = urllib.parse.quote(canon.replace(" ", "_"), safe="")
    url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/all-access/user/"
           f"{t}/daily/{START}00/{END}00")
    d = get(url)
    time.sleep(1.5)
    if d is None:
        print("FAILED", label, flush=True)
        continue
    d["label"], d["project"], d["title_requested"], d["title_canonical"], d["url"] = label, project, title, canon, url
    json.dump(d, open(fn, "w"))
    print("OK", label, canon, len(d.get("items", [])), flush=True)
print("DONE", flush=True)
