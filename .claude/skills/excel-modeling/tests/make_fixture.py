"""Build tests/fixture.xlsx: a small model with the features that break naive tools
(shared formulas, sparkline, chart, data validation, conditional format, comment,
defined name, cross-sheet links, a SUM block, a checks row)."""
import re, sys, zipfile, shutil
import xlsxwriter

def build(path):
    wb = xlsxwriter.Workbook(path)
    blue = wb.add_format({"font_color": "#0000FF", "num_format": "#,##0;(#,##0);-"})
    bluep = wb.add_format({"font_color": "#0000FF", "num_format": "0.0%"})
    num = wb.add_format({"num_format": "#,##0;(#,##0);-"})
    green = wb.add_format({"font_color": "#008000", "num_format": "#,##0;(#,##0);-"})
    pct = wb.add_format({"num_format": "0.0%"})
    inp = wb.add_worksheet("Inputs")
    m = wb.add_worksheet("Model")
    ck = wb.add_worksheet("Checks")
    inp.write_row("A1", ["Assumption", "Value"])
    rows = [("Base revenue ($m)", 1000, blue), ("Revenue growth", 0.05, bluep), ("COGS % revenue", 0.55, bluep),
            ("SG&A % revenue", 0.30, bluep), ("Tax rate", 0.21, bluep)]
    for i, (k, v, f) in enumerate(rows, start=2):
        inp.write(f"A{i}", k); inp.write(f"B{i}", v, f)
    wb.define_name("Growth", "=Inputs!$B$3")
    inp.data_validation("B3", {"validate": "decimal", "criteria": "between", "minimum": -0.5, "maximum": 0.5})
    inp.write_comment("B2", "Source: illustrative fixture")
    years = ["FY2025", "FY2026", "FY2027", "FY2028", "FY2029"]
    m.write_row("A1", ["$m"] + years)
    lab = ["Revenue", "COGS", "Gross profit", "SG&A", "Other opex", "EBIT", "Tax", "Net income", "", "Opex total"]
    for i, l in enumerate(lab, start=2):
        m.write(f"A{i}", l)
    cols = "BCDEF"
    for j, c in enumerate(cols):
        p = cols[j - 1] if j else None
        m.write_formula(f"{c}2", "=Inputs!$B$2" if j == 0 else f"={p}2*(1+Growth)", green if j == 0 else num)
        m.write_formula(f"{c}3", f"=-{c}2*Inputs!$B$4", num)
        m.write_formula(f"{c}4", f"={c}2+{c}3", num)
        m.write_formula(f"{c}5", f"=-{c}2*Inputs!$B$5", num)
        m.write(f"{c}6", -10, blue)
        m.write_formula(f"{c}7", f"={c}4+SUM({c}5:{c}6)", num)
        m.write_formula(f"{c}8", f"=-{c}7*Inputs!$B$6", num)
        m.write_formula(f"{c}9", f"={c}7+{c}8", num)
        m.write_formula(f"{c}11", f"=SUM({c}5:{c}6)", num)
    m.conditional_format("B9:F9", {"type": "cell", "criteria": "<", "value": 0, "format": wb.add_format({"font_color": "red"})})
    m.add_sparkline("G2", {"range": "Model!B2:F2"})
    ch = wb.add_chart({"type": "column"})
    ch.add_series({"name": "EBIT", "categories": "=Model!$B$1:$F$1", "values": "=Model!$B$7:$F$7"})
    m.insert_chart("A14", ch)
    ck.write("A1", "Gross profit ties (should be 0)")
    ck.write_formula("B1", "=ROUND(SUM(Model!B4:F4)-SUM(Model!B2:F2)-SUM(Model!B3:F3),6)")
    ck.write("A2", "Opex total ties EBIT bridge")
    ck.write_formula("B2", "=ROUND(Model!F7-Model!F4-Model!F11,6)")
    wb.close()
    # Convert Model row 4 (C4:F4) into an Excel-style shared formula group, as Excel itself saves it
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            d = zin.read(it.filename)
            if it.filename == "xl/worksheets/sheet2.xml":
                s = d.decode()
                s = re.sub(r'<c r="C4"([^>]*)><f>C2\+C3</f>', r'<c r="C4"\1><f t="shared" ref="C4:F4" si="0">C2+C3</f>', s)
                for c in "DEF":
                    s = re.sub(rf'<c r="{c}4"([^>]*)><f>{c}2\+{c}3</f>', rf'<c r="{c}4"\1><f t="shared" si="0"/>', s)
                assert s.count('si="0"') == 4, "shared formula rewrite failed"
                d = s.encode()
            zout.writestr(it, d)
    shutil.move(tmp, path)

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "fixture.xlsx")
