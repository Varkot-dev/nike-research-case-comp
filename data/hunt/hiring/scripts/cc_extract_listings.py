"""Fetch archived Nike job-search listing pages from Common Crawl WARCs and extract
(a) the total open-postings count shown for that search (with its filter), and
(b) every embedded job object (req id, posting start date, category, country, brand, company, family).
Old site jobs.nike.com (to ~2025): state JSON with "pagination":{...,"count":N} and "atsPayload" job objects.
New site careers.nike.com (2025+): window.__PRELOAD_STATE__ with jobSearch.totalJob and jobs[].
Usage: python3 cc_extract_listings.py <ccdir> <outdir> [max_pages_per_crawl]
Writes <outdir>/cc_listing_counts.csv and <outdir>/cc_job_objects.csv (appends per crawl; resumable)."""
import gzip, json, os, re, sys, time, csv, glob, urllib.request, urllib.parse
ccdir, outdir = sys.argv[1], sys.argv[2]; cap = int(sys.argv[3]) if len(sys.argv) > 3 else 25
dec = json.JSONDecoder()
cnt_f = os.path.join(outdir, "cc_listing_counts.csv"); job_f = os.path.join(outdir, "cc_job_objects.csv")
done = set()
if os.path.exists(cnt_f):
    for r in csv.DictReader(open(cnt_f)): done.add(r["crawl"])
CNT_COLS = ["crawl", "timestamp", "url", "site", "filter_json", "is_unfiltered", "total"]
JOB_COLS = ["crawl", "timestamp", "site", "req_id", "posting_start", "category", "is_retail", "country", "city", "brand", "company", "job_family", "job_category_cf", "title"]
cw = csv.DictWriter(open(cnt_f, "a", newline=""), fieldnames=CNT_COLS)
jw = csv.DictWriter(open(job_f, "a", newline=""), fieldnames=JOB_COLS)
if not done: cw.writeheader(); jw.writeheader()
def fetch(r):
    off, ln = int(r["offset"]), int(r["length"])
    for i in range(5):
        try:
            b = urllib.request.urlopen(urllib.request.Request("https://data.commoncrawl.org/" + r["filename"], headers={"Range": f"bytes={off}-{off+ln-1}", "User-Agent": "academic-research-cc-client"}), timeout=90).read()
            return gzip.decompress(b).decode("utf-8", "replace")
        except Exception: time.sleep(3 * (i + 1))
    return None
def listing_kind(u):
    p = urllib.parse.urlparse(u)
    if p.netloc == "jobs.nike.com":
        q = urllib.parse.parse_qs(p.query)
        if "jobSearch" in q or p.path.rstrip("/") in ("", "/en", "/jobs") or "internships" in p.path:
            filt = {k: v for k, v in q.items() if k in ("jsCat", "jsCat[0]", "jsLocation[0]", "jsKeywords[0]", "jsBrand[0]", "jsPositionType[0]") or k.startswith(("jsCat", "jsLocation", "jsKeywords", "jsBrand", "jsPosition"))}
            filt = {k: v for k, v in filt.items() if v and v != [""]}
            return "old", filt
    if p.netloc == "careers.nike.com" and re.search(r"^/([a-z]{2}(-[a-z]{2})?/)?jobs(/page/\d+)?/?$", p.path):
        q = urllib.parse.parse_qs(p.query)
        return "new", {k: v for k, v in q.items() if k.startswith(("filter", "keyword", "location"))}
    return None, None
for fn in sorted(glob.glob(os.path.join(ccdir, "cdx_*.jsonl.gz"))):
    crawl = os.path.basename(fn)[4:-9]
    if crawl in done: continue
    R = [json.loads(l) for l in gzip.open(fn, "rt")]
    cands = []
    for r in R:
        k, f = listing_kind(r["url"])
        if k: cands.append((0 if not f else (1 if any("Cat" in x or "category" in x for x in f) else 2), r, k, f))
    # unfiltered first, then category filters, then the rest; de-dup by digest
    cands.sort(key=lambda x: (x[0], x[1]["timestamp"]))
    seen, n = set(), 0
    for pri, r, k, f in cands:
        if n >= cap: break
        if r.get("digest") in seen: continue
        seen.add(r.get("digest"))
        t = fetch(r); n += 1; time.sleep(0.25)
        if not t: continue
        total, jobs, sel = None, [], f
        if k == "old":
            m = re.search(r'"pagination":\{"page":\d+,"pages":\d+,"count":(\d+)\}', t)
            total = int(m.group(1)) if m else None
            ms = re.search(r'"selection":(\{.*?\})', t)
            if ms:
                try:
                    s = json.loads(ms.group(1)); sel = {kk: vv for kk, vv in s.items() if kk in ("categories", "brands", "locations", "keywords", "position_type") and vv}
                except Exception: pass
            for mm in re.finditer(r'"atsPayload":', t):
                try: o, _ = dec.raw_decode(t, mm.end())
                except Exception: continue
                loc = ((o.get("location") or {}).get("administrational") or {})
                jobs.append({"req_id": o.get("positionId") or o.get("id"), "posting_start": (o.get("postingStartDate") or "")[:10], "category": o.get("category"),
                             "is_retail": o.get("isRetailJob"), "country": loc.get("country"), "city": loc.get("city"), "brand": o.get("brand"),
                             "title": ((o.get("content") or {}).get("title") or "")[:120]})
        else:
            i = t.find("window.__PRELOAD_STATE__ = ")
            if i >= 0:
                try:
                    st, _ = dec.raw_decode(t, i + len("window.__PRELOAD_STATE__ = "))
                    js = st.get("jobSearch", {}); total = js.get("totalJob"); sel = (js.get("params") or {}).get("filter") or {}
                    kw = (js.get("params") or {}).get("keyword")
                    if kw: sel = dict(sel, keyword=kw)
                    for o in js.get("jobs") or []:
                        cf = {x.get("cfKey"): x.get("value") for x in (o.get("customFields") or []) if isinstance(x, dict)}
                        loc = (o.get("locations") or [{}])[0]
                        jobs.append({"req_id": o.get("requisitionID"), "posting_start": (o.get("postedDate") or o.get("createDate") or "")[:10],
                                     "category": ";".join(sum([x.get("value") or [] for x in (o.get("jobCardExtraFields") or []) if x.get("attribute_name") == "job_categories"], [])),
                                     "is_retail": cf.get("cf_job_category") == "Retail", "country": loc.get("country"), "city": loc.get("city"),
                                     "brand": o.get("brandName"), "company": cf.get("cf_company"), "job_family": cf.get("cf_job_family"),
                                     "job_category_cf": cf.get("cf_job_category"), "title": (o.get("title") or "")[:120]})
                except Exception as e:
                    pass
        cw.writerow({"crawl": crawl, "timestamp": r["timestamp"], "url": r["url"][:400], "site": k, "filter_json": json.dumps(sel, sort_keys=True), "is_unfiltered": int(not sel), "total": total})
        for j in jobs:
            jw.writerow({"crawl": crawl, "timestamp": r["timestamp"], "site": k, **{c: j.get(c, "") for c in JOB_COLS[3:]}})
    print(crawl, "listing candidates", len(cands), "fetched", n, flush=True)
