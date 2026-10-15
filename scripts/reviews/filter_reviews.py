"""Stream decompressed review jsonl on stdin, keep rows whose parent_asin is in matched_products.csv.
Writes gzip CSV: parent_asin, asin, rating, title, text, timestamp, verified_purchase, helpful_vote, user_id."""
import sys, json, csv, gzip
keep = set(r["parent_asin"] for r in csv.DictReader(gzip.open(sys.argv[1], "rt") if sys.argv[1].endswith(".gz") else open(sys.argv[1])))
out = gzip.open(sys.argv[2], "wt", newline=""); w = csv.writer(out)
w.writerow(["parent_asin", "asin", "rating", "title", "text", "timestamp", "verified_purchase", "helpful_vote", "user_id"])
n = k = 0; KEY = '"parent_asin": "'
for line in sys.stdin:
    n += 1
    i = line.find(KEY)
    if i < 0 or line[i + 16:i + 26] not in keep: continue
    try: d = json.loads(line)
    except Exception: continue
    if d.get("parent_asin") not in keep: continue
    k += 1
    w.writerow([d["parent_asin"], d.get("asin"), d.get("rating"), d.get("title"), (d.get("text") or "")[:2000], d.get("timestamp"),
                d.get("verified_purchase"), d.get("helpful_vote"), d.get("user_id")])
    if n % 5000000 == 0: print("lines", n, "kept", k, file=sys.stderr, flush=True)
out.close(); print("lines", n, "kept", k, file=sys.stderr)
