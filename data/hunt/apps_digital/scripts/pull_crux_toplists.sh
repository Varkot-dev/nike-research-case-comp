#!/bin/bash
# Pull CrUX top-list rank buckets (zakird/crux-top-lists, built from Google CrUX BigQuery) and keep only brand origins.
# Usage: pull_crux_toplists.sh  (writes raw/crux/global_filtered.csv and raw/crux/country_filtered.csv)
OUT=/home/user/nike-research-case-comp/data/hunt/apps_digital/raw/crux
mkdir -p $OUT
PAT='//(www\.|m\.)?(nike|adidas|hoka|on|on-running|newbalance|underarmour|puma|asics|skechers|stockx|goat|footlocker|dickssportinggoods|jdsports|lululemon|converse|brooksrunning|vans|reebok|snkrs|finishline|champssports|zappos|dsw|famousfootwear|academy|hibbett|lids|fanatics|nikeinc|jordan)\.com,'
BASE=https://raw.githubusercontent.com/zakird/crux-top-lists/main/data
if [ "$1" != "country" ]; then
echo "month,origin,rank" > $OUT/global_filtered.csv
for y in 2021 2022 2023 2024 2025 2026; do for m in 01 02 03 04 05 06 07 08 09 10 11 12; do
  ym=$y$m; [ $ym -lt 202102 ] && continue; [ $ym -gt 202609 ] && continue
  curl -sS -m 300 $BASE/global/$ym.csv.gz | zcat 2>/dev/null | grep -E "$PAT" | sed "s/^/$ym,/" >> $OUT/global_filtered.csv
  echo "global $ym $(grep -c ^$ym $OUT/global_filtered.csv)"; sleep 1
done; done
fi
echo "country,month,origin,rank" > $OUT/country_filtered.csv
for c in us gb de fr it es nl ca au jp kr cn mx br in tr pl se ch be at dk no ie nz sg ph za ae sa il; do
 for y in 2025 2026; do for m in 01 02 03 04 05 06 07 08 09 10 11 12; do
  ym=$y$m; [ $ym -gt 202609 ] && continue
  curl -sS -m 120 $BASE/country/$c/$ym.csv.gz | zcat 2>/dev/null | grep -E "$PAT" | sed "s/^/$c,$ym,/" >> $OUT/country_filtered.csv
  sleep 0.5
 done; done; echo "country $c done"
done
