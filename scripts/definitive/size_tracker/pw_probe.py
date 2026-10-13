import sys, json, os
from playwright.sync_api import sync_playwright
url=sys.argv[1]; out=sys.argv[2]
os.makedirs(out,exist_ok=True)
logs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", proxy={"server":os.environ["HTTPS_PROXY"]})
    ctx=b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36", ignore_https_errors=False)
    pg=ctx.new_page()
    def onresp(r):
        ct=r.headers.get("content-type","")
        if "json" in ct:
            try:
                body=r.body()
                fn=os.path.join(out,"resp_%03d.json"%len(logs)); open(fn,"wb").write(body)
                logs.append({"url":r.url,"status":r.status,"file":fn,"len":len(body)})
            except Exception as e: logs.append({"url":r.url,"err":str(e)})
    pg.on("response",onresp)
    try: pg.goto(url,wait_until="networkidle",timeout=60000)
    except Exception as e: print("goto",e)
    pg.wait_for_timeout(4000)
    open(os.path.join(out,"page.html"),"w").write(pg.content())
    print(pg.title())
    b.close()
for l in logs: print(l)
