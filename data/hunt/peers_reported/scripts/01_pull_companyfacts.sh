#!/bin/bash
# Pull SEC XBRL companyfacts JSON for US/SEC-filing peers. Generic UA (no personal data). Sleeps 0.5s between requests.
OUT=/home/user/nike-research-case-comp/data/hunt/peers_reported/raw/sec_companyfacts
UA="NikeCaseCompResearch research-bot admin@example.org"
for c in 320187:nike 910521:deckers 1397187:lululemon 103379:vf 1336917:underarmour 1065837:skechers 1858985:on 1334036:crocs 1988894:amer 1977102:birkenstock 1050797:columbia 1089063:dicks; do
  cik=${c%%:*}; n=${c##*:}; p=$(printf "%010d" $cik)
  curl -s -A "$UA" "https://data.sec.gov/api/xbrl/companyfacts/CIK$p.json" -o $OUT/$n.json
  curl -s -A "$UA" "https://data.sec.gov/submissions/CIK$p.json" -o $OUT/${n}_submissions.json
  ls -la $OUT/$n.json | awk '{print $5}'; sleep 0.5
done
