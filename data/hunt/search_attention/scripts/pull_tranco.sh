#!/bin/sh
# Tranco research ranking of domains (daily, aggregate of Chrome UX Report, Cloudflare Radar, Umbrella, Majestic, Farsight).
# API: https://tranco-list.eu/api/ranks/domain/<domain>  (no key). One request every 3 s.
OUT=${1:-../raw/tranco}
mkdir -p "$OUT"
for d in nike.com adidas.com newbalance.com hoka.com on.com on-running.com asics.com lululemon.com puma.com skechers.com brooksrunning.com saucony.com underarmour.com jordan.com converse.com footlocker.com dickssportinggoods.com finishline.com jdsports.com stockx.com goat.com zappos.com runningwarehouse.com solecollector.com hypebeast.com; do
  [ -s "$OUT/$d.json" ] || curl -sS -m 60 -A "NikeCaseCompResearch/1.0" "https://tranco-list.eu/api/ranks/domain/$d" -o "$OUT/$d.json"
  sleep 3
done
