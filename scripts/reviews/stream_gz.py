"""Stream a remote .gz over HTTPS to stdout (decompressed), resuming with HTTP Range on dropped connections.
Nothing is written to disk. Usage: python3 -I stream_gz.py <url> | consumer"""
import sys, zlib, time, requests
url = sys.argv[1]; off = 0; d = zlib.decompressobj(16 + zlib.MAX_WBITS); out = sys.stdout.buffer; fails = 0
total = int(requests.head(url, timeout=60).headers["content-length"])
while off < total:
    try:
        r = requests.get(url, headers={"Range": f"bytes={off}-"}, stream=True, timeout=120)
        if r.status_code not in (200, 206): raise IOError(f"status {r.status_code}")
        if off and r.status_code != 206: raise IOError("server ignored Range")
        for chunk in r.iter_content(1 << 20):
            if not chunk: continue
            off += len(chunk); out.write(d.decompress(chunk))
        fails = 0
    except BrokenPipeError:
        break
    except Exception as e:
        fails += 1
        print(f"[stream_gz] reconnect at {off}/{total} after {type(e).__name__}: {e}", file=sys.stderr, flush=True)
        if fails > 50: raise
        time.sleep(min(60, 5 * fails))
out.write(d.flush()); out.flush()
print(f"[stream_gz] done {off}/{total} bytes, eof={d.eof}", file=sys.stderr, flush=True)
