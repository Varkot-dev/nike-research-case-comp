"""Pull US trademark applications (filed 2005..2026 YTD) for Nike and peers from the USPTO trademark search backend.
Writes tm_raw_<co>.jsonl. Run: python3 -I g7_tm_pull.py   (no credentials, no email in any request)"""
import json, re, sys
sys.path.insert(0, ".")
from tmlib import fetch
CO = {
 "Nike":        ({"match": {"ownerName": "nike"}},     r"^(nike,? inc\b|nike usa|nike innovate|brs, inc)"),
 "adidas":      ({"match": {"ownerName": "adidas"}},   r"^adidas( |-)"),
 "On":          ({"bool": {"should": [{"match_phrase": {"ownerName": "on clouds gmbh"}}, {"match_phrase": {"ownerName": "on ag"}}, {"match_phrase": {"ownerName": "on holding ag"}}]}}, r"^(on clouds gmbh|on ag|on holding ag)"),
 "Deckers":     ({"match": {"ownerName": "deckers"}},  r"^(deckers outdoor corp|ugg holdings|hoka)"),
 "NewBalance":  ({"match_phrase": {"ownerName": "new balance"}}, r"^new balance (athletics|athletic shoe)"),
 "ASICS":       ({"match": {"ownerName": "asics"}},    r"^asics (corporation|tiger|america|digital)"),
 "Puma":         ({"match": {"ownerName": "puma"}},    r"^(puma se|puma ag rudolf|puma-sportschuhfabriken)"),
 "Lululemon":   ({"match": {"ownerName": "lululemon"}}, r"^lululemon athletica"),
}
for co, (qq, rx) in CO.items():
    rows = fetch(qq, 2005, 2026)
    keep = []
    for r in rows:
        on = r["ownerName"] if isinstance(r["ownerName"], list) else [r["ownerName"]]
        if any(re.match(rx, o.lower().strip()) for o in on):
            keep.append(r)
    with open(f"tm_raw_{co}.jsonl", "w") as f:
        for r in keep: f.write(json.dumps(r) + "\n")
    print(co, len(rows), "fetched", len(keep), "kept", flush=True)
