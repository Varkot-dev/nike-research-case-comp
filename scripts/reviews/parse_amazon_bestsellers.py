"""Parse Amazon Best Sellers pages (Wayback + live) for rank, title, brand, stars, rating count.
Inputs: fetch logs (jsonl with url,status,file) given as args. Output CSV to stdout path argv[1]."""
import sys, json, re, csv, os
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brandmatch import brand_of
NODES = {"679286011": "mens_running", "679360011": "womens_running", "679312011": "mens_fashion_sneakers",
         "679394011": "womens_fashion_sneakers", "6127770011": "mens_athletic", "6127771011": "womens_athletic"}
out = sys.argv[1]; pages = {}
for lg in sys.argv[2:]:
    for l in open(lg):
        d = json.loads(l)
        if d["status"] != 200 or "amazon.com" not in d["url"] or not os.path.exists(d["file"]): continue
        m = re.search(r"/(\d{9,11})(?:/|$|\?)", d["url"] + "/"); node = m.group(1) if m else None
        if node not in NODES: continue
        mm = re.search(r"/web/(\d{14})id_", d["url"])
        date, src = ((mm.group(1)[:4] + "-" + mm.group(1)[4:6] + "-" + mm.group(1)[6:8]), "wayback") if mm else (d["t"][:10], "live")
        pages[(NODES[node], date)] = (d["file"], d["url"], src)
rows = []
for (cat, date), (f, url, src) in sorted(pages.items()):
    soup = BeautifulSoup(open(f, encoding="utf-8", errors="ignore").read(), "html.parser")
    cards = soup.select("#gridItemRoot") or soup.select("li.zg-item-immersion")
    for c in cards:
        r = c.select_one(".zg-bdg-text, .zg-badge-text")
        rank = int(re.sub(r"\D", "", r.get_text())) if r and re.search(r"\d", r.get_text()) else None
        t = c.find(lambda tag: tag.name in ("div", "span") and tag.get("class") and any("line-clamp" in x or "p13n-sc-truncate" in x for x in tag["class"]))
        name = t.get_text(" ", strip=True) if t else (c.find("img").get("alt") if c.find("img") else None)
        a = c.find("a", href=re.compile(r"/dp/")); asin = re.search(r"/dp/([A-Z0-9]{10})", a["href"]).group(1) if a else None
        st = c.select_one(".a-icon-alt"); stars = None
        if st:
            m = re.search(r"([\d.]+) out of 5", st.get_text()); stars = float(m.group(1)) if m else None
        cnt = None
        ra = c.find("a", href=re.compile(r"product-reviews"))
        if ra:
            m = re.search(r"([\d,]+)\s*$", ra.get_text(" ", strip=True)); cnt = int(m.group(1).replace(",", "")) if m else None
        if cnt is None and st:
            sm = c.find("span", class_="a-size-small", string=re.compile(r"^[\d,]+$"))
            if sm: cnt = int(sm.get_text().replace(",", ""))
        if name:
            rows.append(dict(category=cat, snapshot_date=date, source=src, rank=rank, brand=brand_of(name), title=name[:150],
                             asin=asin, stars=stars, rating_count=cnt, url=url))
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), "rows,", len(pages), "pages")
