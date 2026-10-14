"""Extract Nike manufacturing map factory list embedded in the site's JS bundle (JSON.parse('[...]')).
Usage: python parse_nike_map.py <bundle.js> <out.csv> [snapshot_label]"""
import sys, json, csv
src, out = sys.argv[1:3]; label = sys.argv[3] if len(sys.argv) > 3 else ''
s = open(src, encoding='utf-8', errors='replace').read()
i = s.find("JSON.parse('[{\"contractor_id\"")
j = s.find("}]')", i)
import re
txt = s[i + len("JSON.parse('"): j + 2]
# undo JS string-literal escapes (\xNN, \uNNNN, \', \\) while keeping JSON escapes valid
txt = re.sub(r'\\x([0-9a-fA-F]{2})', lambda m: chr(int(m.group(1), 16)), txt)
txt = txt.replace("\\'", "'")
recs = json.loads(txt)
keys = ['contractor_id', 'name', 'supplier_name', 'factory_tier', 'product_type', 'brand', 'country/region', 'region', 'city',
        'workers', 'workers_line', 'workers_female', 'workers_migrant', 'average_worker_age', 'special_events']
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['snapshot'] + keys)
    for r in recs:
        w.writerow([label] + [r.get(k, '') for k in keys])
print(len(recs))
