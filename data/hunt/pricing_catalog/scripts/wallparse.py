# Parse a nike.com wall page (live or archived): reported item count and first-page product prices.
import re, json
def parse_wall(t):
    n=None
    m=re.search(r'"totalResources":([0-9]+)',t) or re.search(r'wall-header__item_count[^>]*>\(([0-9,]+)\)',t)
    if m: n=int(m.group(1).replace(',',''))
    prices=[]
    # flat JSON objects holding a current and a full/initial price (works for 2019-2026 wall formats)
    for o in re.finditer(r'\{[^{}]*"currentPrice":([0-9.]+)[^{}]*\}',t):
        s=o.group(0)
        f=re.search(r'"(?:initialPrice|fullPrice)":([0-9.]+)',s)
        if f: prices.append((float(f.group(1)),float(o.group(1))))
    # dedupe repeated serialisations (page JSON often appears twice)
    return n,prices

def parse_wall_any(t):
    """JSON prices if present, else rendered product-card price wrappers (2024-2026 server-rendered walls)."""
    n,p=parse_wall(t)
    method="json"
    if not p:
        method="html"
        for w in t.split('product-price__wrapper')[1:]:
            w=w[:1500]
            red=re.search(r'data-testid="product-price-reduced"[^>]*>\$([0-9.,]+)',w)
            full=re.search(r'data-testid="product-price"[^>]*>\$([0-9.,]+)',w)
            if full:
                f=float(full.group(1).replace(',',''))
                c=float(red.group(1).replace(',','')) if red else f
                p.append((f,c))
    return n,p,method
