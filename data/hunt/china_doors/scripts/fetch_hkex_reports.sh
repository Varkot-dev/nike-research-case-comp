#!/bin/bash
# Download full annual/interim reports from HKEXnews (public), convert to text. PDFs kept outside repo (size); text saved in raw/hkex_reports/
mkdir -p raw/hkex_reports $PDFDIR
while read co tag path; do
  f=$PDFDIR/${co}_${tag}.pdf
  [ -s $f ] || curl -s -m 180 -A 'research-bot/1.0' -o $f "https://www1.hkexnews.hk$path"
  pdftotext -layout $f raw/hkex_reports/${co}_${tag}.txt 2>/dev/null
  echo $co $tag $(stat -c %s $f) $(wc -c < raw/hkex_reports/${co}_${tag}.txt)
  sleep 1
done <<'LIST'
ps AR2021 /listedco/listconews/sehk/2022/0414/2022041400445.pdf
ps AR2022 /listedco/listconews/sehk/2023/0420/2023042001349.pdf
ps IR2022 /listedco/listconews/sehk/2022/0908/2022090800363.pdf
ps IR2023 /listedco/listconews/sehk/2023/0907/2023090700396.pdf
ps AR2023 /listedco/listconews/sehk/2024/0422/2024042200990.pdf
ps IR2024 /listedco/listconews/sehk/2024/0909/2024090900388.pdf
ps AR2024 /listedco/listconews/sehk/2025/0422/2025042201129.pdf
ps IR2025 /listedco/listconews/sehk/2025/0908/2025090800378.pdf
ps AR2025 /listedco/listconews/sehk/2026/0421/2026042100610.pdf
ps IR2026 /listedco/listconews/sehk/2026/0907/2026090700493.pdf
ts AR2122 /listedco/listconews/sehk/2022/0629/2022062900949.pdf
ts IR2223 /listedco/listconews/sehk/2022/1114/2022111400636.pdf
ts AR2223 /listedco/listconews/sehk/2023/0620/2023062000699.pdf
ts IR2324 /listedco/listconews/sehk/2023/1121/2023112100644.pdf
ts AR2324 /listedco/listconews/sehk/2024/0618/2024061800300.pdf
ts IR2425 /listedco/listconews/sehk/2024/1121/2024112100793.pdf
ts AR2425 /listedco/listconews/sehk/2025/0617/2025061700335.pdf
ts IR2526 /listedco/listconews/sehk/2025/1120/2025112000912.pdf
ts AR2526 /listedco/listconews/sehk/2026/0624/2026062400677.pdf
LIST
