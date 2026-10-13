"""Hand-assembled minimal workbook (about 3 KB) for the Google Sheets conversion test.
Small on purpose: the Drive connector takes the file as base64 text inside the call, and
long payloads get corrupted in transit. Every probe row has an expected value in column C.
Run: python3 tests/gsheets_lite.py out.xlsx"""
import sys, zipfile
CT = '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>'
RELS = '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>'
WB = '<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Probe" sheetId="1" r:id="rId1"/><sheet name="Data" sheetId="2" r:id="rId2"/></sheets><definedNames><definedName name="Growth">Probe!$B$1</definedName></definedNames><calcPr iterate="1" iterateCount="100" iterateDelta="0.001"/></workbook>'
WBR = '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'
# xf 1 percent, 2 multiple, 3 money with parentheses and dash, 4 date, 5 blue font input
STY = ('<?xml version="1.0" encoding="UTF-8"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
       '<numFmts count="3"><numFmt numFmtId="164" formatCode="0.0%_);(0.0%);&quot;-&quot;_)"/><numFmt numFmtId="165" formatCode="0.0&quot;x&quot;"/><numFmt numFmtId="166" formatCode="$#,##0.00_);($#,##0.00);&quot;-&quot;_)"/></numFmts>'
       '<fonts count="2"><font><sz val="10"/><name val="Arial"/></font><font><sz val="10"/><color rgb="FF0000FF"/><name val="Arial"/></font></fonts>'
       '<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>'
       '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
       '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
       '<cellXfs count="6"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
       '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
       '<xf numFmtId="165" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
       '<xf numFmtId="166" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
       '<xf numFmtId="14" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
       '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/></cellXfs></styleSheet>')

def c(ref, v=None, f=None, s=None, t=None, arr=None):
    a = f' s="{s}"' if s else ""
    if t == "str":
        return f'<c r="{ref}"{a} t="inlineStr"><is><t>{v}</t></is></c>'
    if f is not None:
        fa = f' t="array" ref="{arr}"' if arr else ""
        f = f.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f'<c r="{ref}"{a}><f{fa}>{f}</f></c>'
    return f'<c r="{ref}"{a}><v>{v}</v></c>'

def build(path):
    rows = {}
    def put(r, *cells): rows.setdefault(r, []).extend(cells)
    put(1, c("A1", "Growth", t="str"), c("B1", 0.05, s=5))
    put(2, c("A2", "Base", t="str"), c("B2", 1000, s=5))
    P = [  # row, label, formula, expected, style, arr
        (4, "named range", "B2*(1+Growth)", 1050, None, None),
        (5, "cross-sheet SUMIFS", 'SUMIFS(Data!B2:B5,Data!C2:C5,"x")', 40, None, None),
        (6, "INDEX/MATCH", 'INDEX(Data!B2:B5,MATCH("c",Data!A2:A5,0))', 30, None, None),
        (7, "SUMPRODUCT", 'SUMPRODUCT(Data!B2:B5,--(Data!C2:C5="y"))', 60, None, None),
        (8, "XLOOKUP _xlfn", '_xlfn.XLOOKUP("b",Data!A2:A5,Data!B2:B5)', 20, None, None),
        (9, "IFS _xlfn", '_xlfn.IFS(B2>2000,"big",B2>500,"mid",TRUE,"small")', "mid", None, None),
        (10, "TEXTJOIN _xlfn", '_xlfn.TEXTJOIN(",",TRUE,Data!A2:A5)', "a,b,c,d", None, None),
        (11, "MAXIFS _xlfn", '_xlfn.MAXIFS(Data!B2:B5,Data!C2:C5,"x")', 30, None, None),
        (12, "EOMONTH", "EOMONTH(DATE(2026,1,15),0)", 46053, 4, None),
        (13, "XNPV (rate, flows, dates)", "XNPV(0.1,Data!D2:D4,Data!E2:E4)", None, None, None),
        (14, "CSE array", "SUM(Data!B2:B5*2)", 200, None, "B14"),
        (15, "percent format", "B1", 0.05, 1, None),
        (16, "multiple format", "12.5", 12.5, 2, None),
        (17, "negative money format", "-1234.5", -1234.5, 3, None),
        (18, "dynamic SORT (spill H18:H21)", "_xlfn._xlws.SORT(Data!B2:B5,1,-1)", 40, None, "H18:H21"),
        (20, "interest on avg debt (circular)", "B22*AVERAGE(B21,B24)", 89.47368, None, None),
        (22, "repayment", "B23-B20", None, None, None),
    ]
    for r, lab, f, exp, s, arr in P:
        if r == 22:
            continue
        cells = [c(f"A{r}", lab, t="str"), c(f"B{r}", f=f, s=s, arr=arr)]
        if exp is not None:
            cells.append(c(f"C{r}", exp, t="str" if isinstance(exp, str) else None))
        put(r, *cells)
    # circular block rows 21-24: B21 opening, B22 rate, B23 CFO, B24 closing = B21-(B23-B20)
    put(21, c("A21", "Opening", t="str"), c("B21", 1000, s=5))
    put(22, c("A22", "Rate", t="str"), c("B22", 0.1, s=5))
    put(23, c("A23", "CFO pre-interest", t="str"), c("B23", 300, s=5))
    put(24, c("A24", "Closing", t="str"), c("B24", f="B21-(B23-B20)"))
    put(26, c("A26", "year as text", t="str"), c("B26", "FY2027E", t="str"))
    # what-if data table 2D: row input B1 (growth), column input B2 (base) over B4-style output in B27
    put(27, c("A27", "data table", t="str"), c("B27", f="B2*(1+B1)"), c("C27", 0.02), c("D27", 0.05), c("E27", 0.08))
    put(28, c("B28", 900), '<c r="C28"><f t="dataTable" ref="C28:E30" dt2D="1" dtr="1" r1="B1" r2="B2"/><v>0</v></c><c r="D28"><v>0</v></c><c r="E28"><v>0</v></c>')
    put(29, c("B29", 1000), '<c r="C29"><v>0</v></c><c r="D29"><v>0</v></c><c r="E29"><v>0</v></c>')
    put(30, c("B30", 1100), '<c r="C30"><v>0</v></c><c r="D30"><v>0</v></c><c r="E30"><v>0</v></c>')
    def key(r):
        return r
    body = "".join(f'<row r="{r}">{"".join(rows[r])}</row>' for r in sorted(rows))
    ns = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"'
    dv = '<dataValidations count="1"><dataValidation type="decimal" operator="between" allowBlank="1" showErrorMessage="1" sqref="B1"><formula1>-0.5</formula1><formula2>0.5</formula2></dataValidation></dataValidations>'
    cf = '<conditionalFormatting sqref="B1:B2"><cfRule type="cellIs" dxfId="0" priority="1" operator="greaterThan"><formula>0.1</formula></cfRule></conditionalFormatting>'
    sheet1 = f'<?xml version="1.0" encoding="UTF-8"?><worksheet {ns}><sheetViews><sheetView workbookViewId="0"><pane ySplit="3" state="frozen" topLeftCell="A4"/></sheetView></sheetViews><sheetData>{body}</sheetData>{cf}{dv}</worksheet>'
    d = ["a|10|x|-100|46023", "b|20|y|60|46388", "c|30|x|60|46753", "d|40|y||"]
    drows = '<row r="1">' + c("A1", "Key", t="str") + c("B1", "Val", t="str") + c("C1", "Grp", t="str") + c("D1", "Flow", t="str") + c("E1", "Date", t="str") + "</row>"
    for i, line in enumerate(d, start=2):
        k, v, g, fl, dt = line.split("|")
        cells = c(f"A{i}", k, t="str") + c(f"B{i}", v) + c(f"C{i}", g, t="str")
        if fl: cells += c(f"D{i}", fl) + c(f"E{i}", dt)
        drows += f'<row r="{i}">{cells}</row>'
    sheet2 = f'<?xml version="1.0" encoding="UTF-8"?><worksheet {ns}><sheetData>{drows}</sheetData></worksheet>'
    # dxf for the conditional format needs a dxfs element in styles
    sty = STY.replace("</styleSheet>", '<dxfs count="1"><dxf><font><color rgb="FFFF0000"/></font></dxf></dxfs></styleSheet>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n, x in [("[Content_Types].xml", CT), ("_rels/.rels", RELS), ("xl/workbook.xml", WB), ("xl/_rels/workbook.xml.rels", WBR),
                     ("xl/styles.xml", sty), ("xl/worksheets/sheet1.xml", sheet1), ("xl/worksheets/sheet2.xml", sheet2)]:
            z.writestr(n, x)

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "lite.xlsx")
