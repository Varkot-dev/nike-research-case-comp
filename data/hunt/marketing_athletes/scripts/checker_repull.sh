#!/bin/bash
# Checker re-pull sample (2026-10-14). Usage: bash scripts/checker_repull.sh raw/checker
D=$1; mkdir -p "$D"; UA="Mozilla/5.0 (X11; Linux x86_64) Chrome/120"
for s in "2025-10-01 2026-06-30 2526" "2019-10-01 2020-10-15 1920" "2023-10-01 2024-06-30 2324" "2019-10-01 2020-03-11 2020q1"; do set -- $s
  curl -sS -A "$UA" -o "$D/colendri_$3.html" "https://www.colendri.com/stats/?group_by=brand&metric=minutes&league_ids=3&date_from=$1&date_to=$2"; sleep 5; done
curl -sS -L -A "$UA" -o "$D/trc2026.html" https://therunningchannel.com/marathon-majors-results-2026/; sleep 3
curl -sS -L -A "$UA" -o "$D/trc2025.html" https://therunningchannel.com/marathon-majors-wrapped-2025/; sleep 3
curl -sS -L -A "$UA" -o "$D/runpack2025.html" https://www.runpack.fr/39054-classement-des-marques-aux-championnats-du-monde-dathletisme-2025; sleep 3
curl -sS -L -A "$UA" -o "$D/runpack2019.html" https://www.runpack.fr/3250-infographie-top-3-des-chaussures-sur-les-6-world-marathon-majors-en-2019; sleep 3
curl -sS -L -A "$UA" -o "$D/fh2026.html" https://www.footyheadlines.com/4277483658/2026-world-cup-boot-battle-nike-and-adidas-neck-and-neck.html; sleep 3
for r in 1216568016 1376216022 1063018789; do curl -sS -A "NikeCaseCompResearch/1.0" -o "$D/wiki_$r.txt" "https://en.wikipedia.org/w/index.php?oldid=$r&action=raw"; sleep 6; done
curl -sS -A "NikeCaseCompResearch/1.0" -o "$D/wk_bl.txt" "https://en.wikipedia.org/w/index.php?title=2025%E2%80%9326_Bundesliga&action=raw"
curl -sS -A "NikeCaseCompResearch/1.0" -o "$D/wd_Q483915.json" https://www.wikidata.org/wiki/Special:EntityData/Q483915.json
for h in nike adidas jordan nikefootball nikebasketball nikerunning nikesportswear nikewomen adidasfootball adidasoriginals puma newbalance; do
  curl -sS -A "$UA" -H "Accept-Language: en-US" -o "$D/yt_$h.html" "https://www.youtube.com/@$h"; sleep 4; done
for h in nike adidas puma; do curl -sS -m 30 -A "$UA Safari/537.36" -o "$D/tt_$h.html" "https://www.tiktok.com/@$h"; sleep 5; done
