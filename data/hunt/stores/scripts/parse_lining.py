"""Parse Li Ning (2331.HK) quarterly POS counts (LI-NING core brand excl. LI-NING YOUNG, China).
Usage: python3 -I parse_lining.py <hkex_lining_dir> <out_csv>"""
import re, os, sys, glob, csv
rows = {}
for t in sorted(glob.glob(os.path.join(sys.argv[1], "*.txt"))):
    s = re.sub(r"\s+", " ", open(t, errors="ignore").read())
    for m in re.finditer(r"(?:As at|As of) (\d+ \w+ \d{4}), (?:the )?total number of LI-NING POS \(exclud(?:e|ing) LI-NING YOUNG\) in China amounted to (\d,\d{3})", s):
        rows.setdefault(m.group(1), [m.group(1), int(m.group(2).replace(",", "")), os.path.basename(t)[:-4]])
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f); w.writerow(["as_at", "lining_core_pos_china", "hkex_doc"]); w.writerows(rows.values())
print(len(rows))
