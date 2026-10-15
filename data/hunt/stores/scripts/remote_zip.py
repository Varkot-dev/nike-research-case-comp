"""Extract selected members from a remote ZIP (All The Places output.zip) via HTTP Range requests,
without downloading the multi-GB archive. Usage: python3 -I remote_zip.py <zip_url> <outdir> <member_regex>"""
import io, re, sys, os, zipfile, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (academic research script)"}
class HttpFile(io.RawIOBase):
    def __init__(self, url):
        self.url = url; self.pos = 0
        r = urllib.request.urlopen(urllib.request.Request(url, method="HEAD", headers=UA), timeout=60)
        self.size = int(r.headers["Content-Length"])
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off); return self.pos
    def read(self, n=-1):
        if n is None or n < 0: n = self.size - self.pos
        if n == 0 or self.pos >= self.size: return b""
        end = min(self.size, self.pos + n) - 1
        h = dict(UA); h["Range"] = f"bytes={self.pos}-{end}"
        data = urllib.request.urlopen(urllib.request.Request(self.url, headers=h), timeout=300).read()
        self.pos += len(data); return data
    def readinto(self, b):
        d = self.read(len(b)); b[:len(d)] = d; return len(d)
def extract(url, outdir, pat):
    os.makedirs(outdir, exist_ok=True)
    z = zipfile.ZipFile(io.BufferedReader(HttpFile(url), buffer_size=1 << 20))
    got = []
    for n in z.namelist():
        if re.search(pat, n):
            dest = os.path.join(outdir, os.path.basename(n))
            with z.open(n) as src, open(dest, "wb") as dst: dst.write(src.read())
            got.append(dest)
    return got
if __name__ == "__main__":
    print(extract(sys.argv[1], sys.argv[2], sys.argv[3]))
