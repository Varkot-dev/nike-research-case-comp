"""Parse NBS monthly retail sales releases (Chinese and English) into a tidy CSV.
Run: python3 -I scripts/parse_nbs.py  (from data/hunt/macro_category)"""
import re, html, glob, csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
num = r'(?<![\w.])(-?\d[\d,]*(?:\.\d+)?|-(?=\s))'
rows = []
def clean(f):
    t = open(f, encoding='utf-8', errors='ignore').read()
    m = re.search(r'<title>(.*?)</title>', t, re.S)
    title = html.unescape(m.group(1)).strip() if m else ''
    txt = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)))
    return title, txt
CN = {'sports_recreation': '体育、娱乐用品类', 'apparel_footwear': '服装、鞋帽、针纺织品类',
      'total_retail': '社会消费品零售总额', 'above_size_goods': '其中：限额以上单位商品零售额', 'cosmetics': '化妆品类', 'gold_jewelry': '金银珠宝类'}
EN = {'sports_recreation': 'Sports & recreational articles', 'apparel_footwear': 'Clothes, shoes, hats and textiles',
      'total_retail': 'Total retail sales of consumer goods', 'above_size_goods': 'Of which: Retail sales of goods by enterprises (units) above the designated size',
      'cosmetics': 'Cosmetics', 'gold_jewelry': 'Gold, silver and jewelry'}
def period_cn(title):
    m = re.search(r'(\d{4})年(\d{1,2})月份?', title)
    if '上半年' in title:
        return re.search(r'(\d{4})年', title).group(1), 6
    if re.search(r'1\u2014(\d+)月', title):
        y = re.search(r'(\d{4})年', title).group(1); mo = re.search(r'1\u2014(\d+)月', title).group(1); return y, int(mo)
    if m: return m.group(1), int(m.group(2))
    return None, None
MONTHS = {m: i+1 for i, m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
def period_en(title):
    y = re.search(r'(20\d\d)', title)
    if not y: return None, None
    if 'First Half' in title: return y.group(1), 6
    ms = [MONTHS[w] for w in re.findall(r'(January|February|March|April|May|June|July|August|September|October|November|December)', title)]
    return y.group(1), (ms[-1] if ms else None)
for lang, files, labels, pfun in [('cn', glob.glob('raw/nbs_cn/rel_*'), CN, period_cn), ('en', glob.glob('raw/nbs/rel_*'), EN, period_en)]:
    for f in sorted(files):
        title, txt = clean(f)
        y, mo = pfun(title)
        if not y or not mo: continue
        # restrict to the table: start at the table header
        start = txt.find('绝对量') if lang == 'cn' else txt.find('Absolute Value')
        if start < 0: continue
        tab = txt[start:start + 4000]
        for key, lab in labels.items():
            i = tab.find(lab)
            if i < 0: continue
            nums = re.findall(num, tab[i + len(lab): i + len(lab) + 80])[:4]
            nums = [None if n == '-' else float(n.replace(',', '')) for n in nums]
            jan_feb = (mo == 2)
            rec = dict(lang=lang, file=f, title=title, year=int(y), month=mo, series=key)
            if jan_feb or len(nums) < 4:
                rec.update(month_value=None, month_yoy=None, ytd_value=nums[0] if nums else None, ytd_yoy=nums[1] if len(nums) > 1 else None)
            else:
                rec.update(month_value=nums[0], month_yoy=nums[1], ytd_value=nums[2], ytd_yoy=nums[3])
            rows.append(rec)
# de-duplicate: prefer cn, then en
seen = {}
for r in rows:
    k = (r['year'], r['month'], r['series'])
    if k not in seen or (seen[k]['lang'] == 'en' and r['lang'] == 'cn' and r['ytd_yoy'] is not None): seen[k] = r
for r in seen.values(): r['title'] = r['title'].replace('\u2014', '-')
out = sorted(seen.values(), key=lambda r: (r['series'], r['year'], r['month']))
with open('china_nbs_retail_categories_monthly.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=['series','year','month','month_value','month_yoy','ytd_value','ytd_yoy','lang','title','file'])
    w.writeheader(); [w.writerow(r) for r in out]
print(len(out))
