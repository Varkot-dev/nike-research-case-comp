#!/bin/bash
# Download Chinese-language NBS monthly retail sales releases listed in raw/nbs_cn/links.txt
cd "$(dirname "$0")/.."
while IFS= read -r l; do
  h=$(echo "$l" | sed -E 's/href="\.\/([^"]+)".*/\1/')
  f=raw/nbs_cn/rel_$(echo $h | tr '/' '_')
  [ -s "$f" ] || { curl -sS --http1.1 -A "Mozilla/5.0" "https://www.stats.gov.cn/sj/zxfb/$h" -o "$f"; sleep 1; }
done < raw/nbs_cn/links.txt
