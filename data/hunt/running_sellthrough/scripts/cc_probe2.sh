#!/bin/bash
# Parallel Common Crawl index probe: counts of captured URLs per crawl and URL pattern. Output raw/cc_probe2.tsv
: > raw/cc_probe2.tsv
probe(){ r=$(curl -s -m 90 "https://index.commoncrawl.org/$1-index?url=$2&output=json&limit=300" | grep -c '"url"'); printf '%s\t%s\t%s\n' "$1" "$2" "$r" >> raw/cc_probe2.tsv; }
export -f probe
for c in CC-MAIN-2024-33 CC-MAIN-2025-38 CC-MAIN-2026-34; do
 for p in 'www.runningwarehouse.com/*Pegasus*' 'www.zappos.com/p/nike-pegasus*' 'www.fleetfeet.com/products/*pegasus*' 'www.roadrunnersports.com/*Pegasus*' 'www.amazon.com/*zgbs*' 'www.jackrabbit.com/*egasus*' 'www.dickssportinggoods.com/p/nike-*pegasus*' 'www.nike.com/t/*pegasus*'; do echo "$c $p"; done
done | xargs -P 8 -L 1 bash -c 'probe "$0" "$1"'
