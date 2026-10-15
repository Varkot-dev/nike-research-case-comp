#!/bin/bash
# list CC captures for adidas international product pages (retry on resets)
cd "$(dirname "$0")/../raw/cc"
for c in CC-MAIN-2026-34 CC-MAIN-2025-33; do for d in www.adidas.co.uk www.adidas.de www.adidas.co.jp; do
 f=idx_${d}_${c}.jsonl; ok=0
 for t in 1 2 3 4 5 6 7 8; do
  curl -sS -m 150 "https://index.commoncrawl.org/${c}-index?url=${d}/*&output=json&filter=status:200&limit=4000" > $f 2>/dev/null
  if head -c1 $f | grep -q '{'; then ok=1; break; fi; sleep $((10*t))
 done; echo "$d $c ok=$ok lines=$(wc -l < $f)"
done; done
