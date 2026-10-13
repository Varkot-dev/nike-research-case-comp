"""Reference implementation for insert_rows/insert_cols: perform the same insertion
inside LibreOffice (which rewrites references like Excel) and save. Used by the tests
to prove xl.py's XML-level insertion produces identical formulas."""
import os, subprocess, sys, tempfile, time, uno
from com.sun.star.beans import PropertyValue

def prop(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p

def run(src, dst, sheet, axis, at, n):
    prof = tempfile.mkdtemp(prefix="lo_oracle_")
    port = 2002 + os.getpid() % 1000
    proc = subprocess.Popen(["soffice", f"-env:UserInstallation=file://{prof}", "--headless", "--norestore",
                             f"--accept=socket,host=localhost,port={port};urp;"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        for _ in range(60):
            try:
                ctx = resolver.resolve(f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext"); break
            except Exception:
                time.sleep(0.5)
        desk = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        doc = desk.loadComponentFromURL(uno.systemPathToFileUrl(os.path.abspath(src)), "_blank", 0, (prop("Hidden", True),))
        sh = doc.Sheets.getByName(sheet)
        if axis == "row":
            sh.Rows.insertByIndex(at - 1, n)
        else:
            sh.Columns.insertByIndex(at - 1, n)
        doc.calculateAll()
        doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(dst)), (prop("FilterName", "Calc MS Excel 2007 XML"),))
        doc.close(True)
    finally:
        proc.terminate(); proc.wait()

if __name__ == "__main__":
    src, dst, sheet, axis, at, n = sys.argv[1:7]
    run(src, dst, sheet, axis, int(at), int(n))
