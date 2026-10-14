"""Stocktwits public stream (no login): retail investor message volume and self-tagged Bullish/Bearish sentiment.

Source: https://api.stocktwits.com/api/2/streams/symbol/<SYM>.json?max=<id>  (30 messages per page, newest first)
Pulls up to MAX_PAGES pages per symbol going back in time, plus watchlist_count (followers) snapshot.
Re-run: python3 -I pull_stocktwits.py <rawdir>
"""
import json, os, sys, time, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/stocktwits"
os.makedirs(OUT, exist_ok=True)
UA = "Mozilla/5.0 (research)"
SYMS = {"NKE": 160, "ONON": 40, "DECK": 40, "LULU": 40, "ADDYY": 20, "UAA": 20, "SKX": 10, "BIRK": 10}

for sym, pages in SYMS.items():
    fn = os.path.join(OUT, f"{sym}.json")
    if os.path.exists(fn):
        continue
    msgs, meta, mx = [], None, None
    for p in range(pages):
        url = f"https://api.stocktwits.com/api/2/streams/symbol/{sym}.json" + (f"?max={mx}" if mx else "")
        d = None
        for i in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                    d = json.load(r)
                break
            except Exception as e:
                print("ERR", sym, e, flush=True)
                time.sleep(30)
        if not d:
            break
        meta = meta or d.get("symbol")
        page = d.get("messages", [])
        if not page:
            break
        for m in page:
            msgs.append({"id": m["id"], "created_at": m["created_at"],
                         "sentiment": ((m.get("entities") or {}).get("sentiment") or {}).get("basic"),
                         "user_followers": (m.get("user") or {}).get("followers")})
        mx = page[-1]["id"] - 1
        time.sleep(2)
    json.dump({"symbol": sym, "meta": meta, "messages": msgs, "pulled": time.strftime("%Y-%m-%d")}, open(fn, "w"))
    print("OK", sym, len(msgs), msgs[-1]["created_at"] if msgs else None, flush=True)
print("DONE", flush=True)
