import sys, asyncio, json, datetime
from playwright.async_api import async_playwright
ids=json.load(open(sys.argv[1])); out=sys.argv[2]; extra_q=sys.argv[3].split('|') if len(sys.argv)>3 else []
async def main():
    res={}
    try: res=json.load(open(out))
    except Exception: pass
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium', headless=True,
            proxy={"server":"http://127.0.0.1:34089"}, args=["--disable-blink-features=AutomationControlled"])
        ctx = await b.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36")
        pg = await ctx.new_page()
        await pg.goto("https://www.goat.com/search?query=air%20jordan", timeout=45000, wait_until="domcontentloaded")
        await pg.wait_for_timeout(5000)
        for q in extra_q:
            url="/web-api/consumer-search/get-product-search-results?salesChannelId=1&queryString="+q.replace(' ','+')+"&pageNumber=1&pageLimit=12"
            t=await pg.evaluate("async (u)=>{const r=await fetch(u);return await r.text()}", url)
            try:
                pl=json.loads(t)['data']['productsList']
                res.setdefault('_search',{})[q]=pl
                print('search',q,[x['slug'] for x in pl[:3]],flush=True)
            except Exception as e: print('search fail',q,t[:100])
            await pg.wait_for_timeout(6000)
        for i in ids:
            if str(i) in res: continue
            url=f"/web-api/v1/product_variants/buy_bar_data?productTemplateId={i}&countryCode=US"
            t=await pg.evaluate("async (u)=>{const r=await fetch(u);return r.status+'|'+await r.text()}", url)
            st,body=t.split('|',1)
            try: res[str(i)]={'url':'https://www.goat.com'+url,'observed_utc':datetime.datetime.utcnow().isoformat(timespec='seconds'),'data':json.loads(body)}
            except Exception: print('fail',i,st,body[:80],flush=True)
            print(st,i,flush=True)
            json.dump(res,open(out,'w'))
            await pg.wait_for_timeout(6000)
        await b.close()
    json.dump(res,open(out,'w'))
asyncio.run(main())
