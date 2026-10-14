"""Monthly counts of Reddit POST TITLES mentioning a brand / product term, by subreddit, 2019-01 to 2026-10.

Source: Arctic Shift public Reddit archive API (https://arctic-shift.photon-reddit.com, no login, no key).
Endpoint: /api/posts/search/aggregate?aggregate=created_utc&frequency=month&subreddit=S&title=Q&after=A&before=B
Also pulls the total post count per month per subreddit (no title filter) for normalisation.
Title search is full-text (word match), case-insensitive. Queried in half-year windows (full-year windows time out server side).
Re-run: python3 -I pull_reddit_arcticshift.py <rawdir>   (already-saved files are skipped)
"""
import json, os, sys, time, urllib.parse, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else "../raw/reddit"
os.makedirs(OUT, exist_ok=True)
UA = "NikeCaseCompResearch/1.0 (academic)"
BASE = "https://arctic-shift.photon-reddit.com/api/posts/search/aggregate"
WINDOWS = sorted([(f"{y}-01-01", f"{y}-07-01") for y in range(2019, 2027)]
                 + [(f"{y}-07-01", f"{y + 1}-01-01") for y in range(2019, 2027)])

SUBS = {
    "RunningShoeGeeks": ["", "nike", "hoka", "asics", "adidas", "saucony", "brooks", "puma", "new balance", "on",
                          "pegasus", "vomero", "vaporfly", "alphafly", "zoomfly", "invincible", "streakfly",
                          "clifton", "bondi", "mach", "novablast", "superblast", "adizero", "boston", "endorphin",
                          "cloudmonster", "cloudboom"],
    "Sneakers": ["", "nike", "jordan", "dunk", "af1", "air force", "air max", "adidas", "samba", "new balance",
                 "asics", "hoka", "puma", "onitsuka", "salomon", "vomero", "cortez", "yeezy"],
    "running": ["", "nike", "hoka", "asics", "saucony", "brooks", "adidas", "new balance", "on cloud", "pegasus",
                "vomero"],
    "malefashionadvice": ["", "nike", "adidas", "new balance", "samba", "asics", "dunk", "jordan", "salomon",
                          "onitsuka", "converse"],
    "Nike": [""],
    "adidas": [""],
    "Hoka": [""],
    "Brooksrunning": [""],
    "NewBalance": [""],
    "Jordans": [""],
    "Repsneakers": [""],
    "Sneakermarket": [""],
}


def get(url, tries=6):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=180) as r:
                d = json.load(r)
            if d.get("data") is not None:
                return d
            print("server said", d.get("error"), flush=True)
        except urllib.error.HTTPError as e:
            try:
                print("HTTP", e.code, e.read()[:100], flush=True)
            except Exception:
                print("HTTP", e.code, flush=True)
        except Exception as e:
            print("ERR", e, flush=True)
        time.sleep(15 * (i + 1))
    return None


for sub, terms in SUBS.items():
    for term in terms:
        label = term.replace(" ", "_") or "_ALL"
        fn = os.path.join(OUT, f"{sub}__{label}.json")
        if os.path.exists(fn):
            continue
        rows, ok = [], True
        for a, b in WINDOWS:
            q = {"aggregate": "created_utc", "frequency": "month", "subreddit": sub,
                 "after": a, "before": b}
            if term:
                q["title"] = term
            d = get(BASE + "?" + urllib.parse.urlencode(q))
            time.sleep(4)
            if d is None:
                ok = False
                print("FAILED", sub, term, a, flush=True)
                continue
            rows.extend(d["data"])
        json.dump({"subreddit": sub, "term": term, "complete": ok, "rows": rows}, open(fn, "w"))
        print("OK", sub, term, len(rows), "complete" if ok else "PARTIAL", flush=True)
print("DONE", flush=True)
