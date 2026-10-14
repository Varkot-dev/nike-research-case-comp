"""Locate the PDF page of a quoted sentence in a cleaned transcript (=== PAGE n === markers)."""
import re, pathlib, functools

TDIR = pathlib.Path(__file__).resolve().parent.parent / "transcripts"

def _norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())

@functools.lru_cache(maxsize=None)
def _pages(quarter):
    txt = (TDIR / f"{quarter}.txt").read_text()
    parts = re.split(r"^=== PAGE (\d+) ===$", txt, flags=re.M)
    pages = [(int(parts[i]), _norm(parts[i + 1])) for i in range(1, len(parts), 2)]
    full = "".join(p for _, p in pages)
    starts, pos = [], 0
    for n, p in pages:
        starts.append((pos, n)); pos += len(p)
    return full, starts

def find_page(quarter, sentence):
    full, starts = _pages(quarter)
    key = _norm(sentence)
    for k in (key[:80], key[:50], key[:30], key[-40:]):
        if len(k) < 15:
            continue
        i = full.find(k)
        if i >= 0:
            pg = starts[0][1]
            for s, n in starts:
                if s <= i: pg = n
                else: break
            return pg
    return None
