"""usage: python3 -I pf_fetch.py <rawdir> <styleColor|styleCode> ...  (or '-' for stdin). Fetches api.nike.com product_feed threads/v3 (public, used by nike.com) per code."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import get
raw=sys.argv[1]; codes=sys.argv[2:]
if codes==["-"]: codes=[l.strip() for l in sys.stdin if l.strip()]
for c in codes:
    f="styleColor" if "-" in c else "styleCode"
    url=f"https://api.nike.com/product_feed/threads/v3/?anchor=0&count=50&filter=marketplace(US)&filter=language(en)&filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.{f}({c})"
    p,s=get(url,raw); print(c,s,p,flush=True)
