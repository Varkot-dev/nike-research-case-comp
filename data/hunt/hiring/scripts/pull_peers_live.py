"""Live peer job-board snapshots (public, no login).
- On (Eightfold PCSX API: jobs.on.com/api/pcsx/search)
- adidas (careers.adidas-group.com/jobs HTML counter, total and per team filter)
Usage: python3 pull_peers_live.py <rawdir>"""
import json, sys, time, urllib.request, urllib.parse, re, os
raw = sys.argv[1]
UA = {"User-Agent": "Mozilla/5.0 (academic research)", "Accept": "application/json"}
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read().decode("utf-8", "replace")
        except Exception as e: print("retry", u, e, file=sys.stderr); time.sleep(4 * (i + 1))
    return None
# On
pos, start, total = [], 0, None
while True:
    d = json.loads(get(f"https://jobs.on.com/api/pcsx/search?domain=on.com&query=&location=&start={start}&sort_by=relevance"))["data"]
    total = d.get("count", total); p = d.get("positions") or []
    pos += p; start += len(p)
    if not p or (total and start >= total): break
    time.sleep(0.8)
json.dump({"pulled_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "count": total, "positions": pos}, open(os.path.join(raw, "on_positions.json"), "w"))
print("On", total, len(pos))
# adidas
teams = ["Brand Management & Communications","Corporate Services","Data","Design","Digital","Finance","General Management & Business Development","Legal & Regulatory","Merchandising & Planning","People & Culture","Product Development & Operations","Production","Real Estate & Facilities","Retail","Retail (Store)","Sales","Supply Chain & Sourcing","Technology"]
res = {}
h = get("https://careers.adidas-group.com/jobs"); open(os.path.join(raw, "adidas_jobs.html"), "w").write(h)
res["ALL"] = int(re.search(r'data-count-to="(\d+)"', h).group(1))
for t in teams:
    h = get("https://careers.adidas-group.com/jobs?" + urllib.parse.urlencode({"team": t}))
    res[t] = int(re.search(r'data-count-to="(\d+)"', h).group(1)); time.sleep(1.2)
json.dump({"pulled_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "counts": res}, open(os.path.join(raw, "adidas_team_counts.json"), "w"), indent=1)
print("adidas", res)
