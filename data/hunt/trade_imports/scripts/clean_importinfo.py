"""Parse raw ImportInfo pages into tidy CSVs:
 importinfo_monthly_bols.csv  (slug, month, bols)
 importinfo_company_summary.csv (slug, name, total, first, last, last30, last90, past_year)
 importinfo_recent_bols.csv (25 most recent BOLs per page: arrival, port, cartons, kg, shipper, consignee, commodity)"""
import os, re, json, html, csv, glob, datetime

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
raw = os.path.join(base, 'raw', 'importinfo')


def text(h):
    h = re.sub(r'<script.*?</script>', '', h, flags=re.S)
    return h


monthly, summ, recent = [], [], []
for fn in sorted(glob.glob(os.path.join(raw, '*_monthly.json'))):
    slug = os.path.basename(fn)[:-len('_monthly.json')]
    try:
        d = json.load(open(fn))
    except Exception:
        continue
    for r in d:
        # timestamps are mid-month local time; take UTC date + 3 days to be safe
        t = datetime.datetime.fromtimestamp(r['date'] / 1000, datetime.timezone.utc) + datetime.timedelta(days=3)
        monthly.append((slug, t.strftime('%Y-%m'), r['value']))

for fn in sorted(glob.glob(os.path.join(raw, '*.html'))):
    slug = os.path.basename(fn)[:-5]
    h = open(fn, encoding='utf-8', errors='replace').read()
    t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text(h))))
    m = re.search(r'There are a total of ([\d,]+) bills of lading on file for (.*?) between (.*?) and (.*?)\. Of those', t)
    def grab(label):
        mm = re.search(label + r' ([\d,]+)', t)
        return int(mm.group(1).replace(',', '')) if mm else None
    if m:
        summ.append(dict(slug=slug, name=m.group(2), total=int(m.group(1).replace(',', '')), first=m.group(3), last=m.group(4),
                         shipper_records=grab('Shipper Records'), consignee_records=grab('Consignee Records'),
                         last30=grab('Records in Last 30 Days'), last90=grab('Records in Last 90 Days'),
                         past_year=grab('Records in the Past Year')))
    # recent BOL table: rows of <td>
    tb = re.search(r'25 Most Recent Bills of Lading.*?<tbody>(.*?)</tbody>', h, flags=re.S)
    if tb:
        heads = None
        thead = re.search(r'25 Most Recent Bills of Lading.*?<thead>(.*?)</thead>', h, flags=re.S)
        if thead:
            heads = [html.unescape(re.sub(r'<[^>]+>', '', x)).strip() for x in re.findall(r'<th[^>]*>(.*?)</th>', thead.group(1), flags=re.S)]
        for row in re.findall(r'<tr[^>]*>(.*?)</tr>', tb.group(1), flags=re.S):
            cells = [html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', c))).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>', row, flags=re.S)]
            if heads and len(cells) == len(heads):
                rec = dict(zip(heads, cells)); rec['page_slug'] = slug
                recent.append(rec)

with open(os.path.join(base, 'importinfo_monthly_bols.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['slug', 'month', 'bols']); w.writerows(monthly)
with open(os.path.join(base, 'importinfo_company_summary.csv'), 'w', newline='') as f:
    if summ:
        w = csv.DictWriter(f, fieldnames=list(summ[0].keys())); w.writeheader(); w.writerows(summ)
if recent:
    keys = sorted({k for r in recent for k in r})
    with open(os.path.join(base, 'importinfo_recent_bols.csv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(recent)
print(len(monthly), len(summ), len(recent))
