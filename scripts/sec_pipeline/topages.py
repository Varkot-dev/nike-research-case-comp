"""Convert an SEC HTML filing to text split into printed pages.
Output: <out>/<name>.txt with '=== PAGE <seq> | printed: <label> ===' headers."""
import re, sys, os
from bs4 import BeautifulSoup, NavigableString
MARK = "\u0000PAGEBREAK\u0000"
def cell_text(td):
    t = td.get_text(" ", strip=True)
    return re.sub(r"\s+", " ", t)
def convert(path, outdir):
    html = open(path, "rb").read().decode("utf-8", "ignore")
    soup = BeautifulSoup(html, "lxml")
    for s in soup(["script", "style"]): s.decompose()
    for hidden in soup.find_all(style=re.compile(r"display:\s*none")): hidden.decompose()
    for el in soup.find_all(style=re.compile(r"page-break-(after|before)\s*:\s*always")):
        if re.search(r"page-break-before", el.get("style", "")): el.insert_before(NavigableString(MARK))
        else: el.insert_after(NavigableString(MARK))
    for tbl in soup.find_all("table"):
        lines = []
        for tr in tbl.find_all("tr"):
            cells = [cell_text(td) for td in tr.find_all(["td", "th"])]
            cells = [c for c in cells if c not in ("", "$", "%", ")")]
            if cells: lines.append(" | ".join(cells))
        tbl.replace_with(NavigableString("\n[TABLE]\n" + "\n".join(lines) + "\n[/TABLE]\n"))
    for br in soup.find_all("br"): br.replace_with("\n")
    for blk in soup.find_all(["p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr"]):
        blk.insert_after("\n")
    text = soup.get_text()
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    pages = [p.strip() for p in text.split(MARK)]
    pages = [p for p in pages if p]
    out = []
    for i, p in enumerate(pages, 1):
        lines = [l.strip() for l in p.split("\n") if l.strip()]
        label = ""
        for cand in reversed(lines[-4:]):
            m = re.search(r"(?:^|\s)([A-Z]?-?\d{1,3})$", cand)
            if m and len(cand) < 60: label = m.group(1); break
        out.append(f"=== PAGE {i} | printed: {label or 'n/a'} ===\n" + "\n".join(lines))
    name = os.path.basename(path).rsplit(".", 1)[0] + ".txt"
    open(os.path.join(outdir, name), "w").write("\n".join(out) + "\n")
    return name, len(pages)
if __name__ == "__main__":
    outdir = sys.argv[1]; os.makedirs(outdir, exist_ok=True)
    for p in sys.argv[2:]:
        print(*convert(p, outdir))
