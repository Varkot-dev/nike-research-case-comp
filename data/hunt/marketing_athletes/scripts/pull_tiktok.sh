#!/bin/bash
# Public TikTok profile pages (no login): follower/heart/video counts from embedded JSON. Usage: pull_tiktok.sh <rawdir>
for h in nike adidas puma newbalance on hoka jumpman23 underarmour lululemon asics asicsamerica adidasoriginals nikefootball adidasfootball nikebasketball nikerunning brooksrunning salomon skechers converse vans anta lining; do
  curl -sS -m 30 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36" "https://www.tiktok.com/@$h" -o "$1/$h.html"; sleep 4
done
