"""Extract Nike official earnings call transcripts (investors.nike.com PDFs) to clean text.

Usage: python3 -I 01_extract_transcripts.py <pdf_dir> <out_dir>
pdf_dir holds t_<dbid>.pdf as downloaded from the URLs in transcripts/README.md.
Each output file keeps the PDF page breaks as lines '=== PAGE n ===' so quotes can be cited by page.
Em and en dashes are replaced with hyphens (repo house rule).
"""
import subprocess, sys, pathlib, re

DBIDS = [9384, 9385, 9386, 9387, 9388, 9389, 9390, 9391, 9392, 9393, 9394, 9395,
         9396, 9397, 9398, 9399, 9400, 9401, 9402, 9403, 9404, 9405, 9406, 9540, 9591]

def quarter_name(i):
    return f"Q{i % 4 + 1}FY{21 + i // 4}"

def main(pdf_dir, out_dir):
    pdf_dir, out_dir = pathlib.Path(pdf_dir), pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, dbid in enumerate(DBIDS):
        q = quarter_name(i)
        raw = subprocess.run(["pdftotext", str(pdf_dir / f"t_{dbid}.pdf"), "-"],
                             capture_output=True, text=True).stdout
        raw = raw.replace("\u2014", " - ").replace("\u2013", "-").replace(" ", " ")
        pages = raw.split("\f")
        if pages and not pages[-1].strip():
            pages = pages[:-1]
        out = [f"# NIKE, Inc. {q} earnings call, official transcript (investors.nike.com db id {dbid})\n"]
        for n, p in enumerate(pages, 1):
            out.append(f"\n=== PAGE {n} ===\n")
            out.append(re.sub(r"\n{3,}", "\n\n", p.strip("\n")) + "\n")
        (out_dir / f"{q}.txt").write_text("".join(out))
        print(q, dbid, len(pages), "pages")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
