#!/bin/bash
# Re-pull all macro/category raw files. Run from anywhere. Sleeps between requests.
set -u
D="$(cd "$(dirname "$0")/.." && pwd)"; R=$D/raw; mkdir -p $R/eurostat $R/nbs $R/nbs_cn
UA="Mozilla/5.0 (research script)"
# 1. FRED (fredgraph.csv needs no key)
for id in MRTSSM4482USS MRTSSM4482USN MRTSSM45111USN MRTSSM451USN MRTSSM448USN MRTSSM4481USS MRTSSM44812USN MRTSSM454USS MRTSSM4541USS RSCCAS RSCCASN RSSGHBMS RSXFS RSAFS RSNSR CUSR0000SEAE CUUR0000SEAE CUUR0000SERE01 CPIAUCSL PCU316210316210 WPU0431 WPU0432 IR10000 CES4244800001 CES4245100001 ECOMSA PCU44824482 PCU448210448210 PCU45114511 PCU451110451110 PCU4511104511101 PCU44814481 PCU3162131621 PCU316210316210P; do
  curl -sS --http1.1 "https://fred.stlouisfed.org/graph/fredgraph.csv?id=$id" -o $R/fred_$id.csv; sleep 0.5; done
# 2. BEA NIPA monthly flat file (no key); keep only the needed series
T=$(mktemp -d); curl -sS --http1.1 "https://apps.bea.gov/national/Release/TXT/NipaDataM.txt" -o $T/m.txt
grep -E '^"?(DSHUR[ACGX]|DSPGR[ACGX]|DCLOR[ACGX]|DGARR[ACGX]|DPCERC|DGDSRC|DNDGRC|DPCERG)"?,' $T/m.txt > $R/bea_nipa_monthly_subset.txt; rm -r $T
curl -sS --http1.1 "https://apps.bea.gov/national/Release/TXT/SeriesRegister.txt" -o $R/bea_SeriesRegister.txt
# 3. Eurostat retail trade (sts_trtu_m) and HICP footwear
for n in G47_NF_CLTH G476 G4791 G47; do for ind in VOL_SLS NETTUR; do
  curl -sS --http1.1 "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_trtu_m?format=JSON&nace_r2=$n&indic_bt=$ind&s_adj=SCA&unit=I21&sinceTimePeriod=2018-01&lang=EN" -o $R/eurostat/sts_trtu_m_${n}_${ind}_SCA.json; sleep 1; done; done
curl -sS --http1.1 "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_midx?format=JSON&coicop=CP0321&unit=I15&sinceTimePeriod=2018-01&lang=EN" -o $R/eurostat/hicp_CP0321_I15.json
# 4. Statistics Canada table 20-10-0056 (monthly retail by NAICS), Canada-level subset
T=$(mktemp -d); curl -sS --http1.1 -A "$UA" "https://www150.statcan.gc.ca/n1/tbl/csv/20100056-eng.zip" -o $T/t.zip && (cd $T && unzip -q t.zip)
python3 -I - "$T/20100056.csv" "$R/statcan_20100056_canada_subset.csv" <<'P'
import csv,sys
r=csv.DictReader(open(sys.argv[1],encoding='utf-8-sig')); w=csv.writer(open(sys.argv[2],'w'))
w.writerow(['ref_date','naics','sales_type','adjustment','value_cad_thousands','vector'])
for row in r:
  n=row['North American Industry Classification System (NAICS)']
  if row['GEO']=='Canada' and any(k in n for k in ['[4582]','[4581]','[459A]','[44-45]','[458]']):
    w.writerow([row['REF_DATE'],n,row['Sales'],row['Adjustments'],row['VALUE'],row['VECTOR']])
P
rm -r $T
# 5. UK ONS retail sales index (generator CSV), textiles/clothing/footwear stores volume YoY and non-food
for c in idog idoc eapv; do curl -sS --http1.1 -A "$UA" "https://www.ons.gov.uk/generator?format=csv&uri=/businessindustryandtrade/retailindustry/timeseries/$c/drsi" -o $R/ons_$c.csv; sleep 2; done
# 6. China NBS: listing pages then releases (see pull_nbs_cn.sh for the Chinese releases)
echo done
