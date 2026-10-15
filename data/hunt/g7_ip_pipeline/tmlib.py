"""USPTO trademark search backend client (tmsearch.uspto.gov). No credentials, no email, no API key.
Endpoint is the public JSON backend used by the USPTO Trademark Search web app (successor to TESS)."""
import requests, json, time
URL = "https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch"
H = {"Content-Type": "application/json", "Accept": "application/json",
     "Origin": "https://tmsearch.uspto.gov", "Referer": "https://tmsearch.uspto.gov/search/search-information"}
def q(body, tries=4):
    for i in range(tries):
        try:
            r = requests.post(URL, headers=H, data=json.dumps(body), timeout=90)
            if r.status_code == 200:
                return r.json()
        except Exception as e:
            pass
        time.sleep(2 * (i + 1))
    raise RuntimeError("tmsearch failed")
FIELDS = ["id","wordmark","filedDate","abandonDate","cancelDate","alive","registrationDate","registrationId",
          "internationalClass","drawingCode","currentBasis","originalBasis","statusCode","statusDescription",
          "ownerName","firstUseAnyDate","firstUseCommerceDate","ownerType","markType","goodsAndServices","designCode","registrationType"]
def fetch(query, y0=2000, y1=2026, per=1000):
    """page by calendar year with from/size (sort cursors are not returned by the backend)"""
    out = []
    for y in range(y0, y1 + 1):
        rng = {"range": {"filedDate": {"gte": f"{y}-01-01", "lte": f"{y}-12-31"}}}
        frm = 0
        while True:
            b = {"query": {"bool": {"must": [query], "filter": [rng]}}, "size": per, "from": frm,
                 "_source": FIELDS, "sort": [{"filedDate": "asc"}], "track_total_hits": True}
            d = q(b)
            hs = d["hits"]["hits"]
            out += [dict(h["source"], _fy=y) for h in hs]
            tot = d["hits"]["totalValue"]
            frm += per
            if frm >= tot or not hs: break
            if frm + per > 10000: raise RuntimeError("year bucket too large")
    return out
