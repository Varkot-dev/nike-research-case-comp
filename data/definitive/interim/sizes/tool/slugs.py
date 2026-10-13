import json, subprocess, sys, time, csv
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
codes=sys.argv[2:]; out=sys.argv[1]
w=csv.writer(open(out,'w',newline='')); w.writerow(['style_code','listed','slug','commerce_start','status'])
for c in codes:
    u=("https://api.nike.com/product_feed/threads/v3/?filter=marketplace(US)&filter=language(en)"
       f"&filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.styleColor({c})")
    r=subprocess.run(["curl","-s","-A",UA,"-H","nike-api-caller-id: com.nike.commerce.nikedotcom.web",u],capture_output=True,text=True).stdout
    row=[c,False,'','','']
    try:
        for o in json.loads(r).get('objects',[]):
            for pi in o['productInfo']:
                if pi['merchProduct']['styleColor']==c:
                    row=[c,True,pi['productContent'].get('slug'),pi['merchProduct'].get('commerceStartDate','')[:10],pi['merchProduct'].get('status')]
    except Exception as e: row[4]='err'
    w.writerow(row); print(row,flush=True); time.sleep(4)
