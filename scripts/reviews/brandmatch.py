"""Brand rules shared by Part 2 parsers (title-prefix match, as listing titles start with the brand)."""
import re
FOCUS = ["Nike", "Jordan", "Converse", "adidas", "HOKA", "On", "New Balance", "Brooks", "ASICS", "Skechers", "Under Armour", "PUMA"]
_P = [("Jordan", r"(nike )?(air )?jordan"), ("Nike", r"nike"), ("Converse", r"converse"), ("HOKA", r"hoka( one one)?"),
      ("On", r"on( running| cloud\w*)?(?=[\s'’]|$)|on-running|on ag"), ("Brooks", r"brooks"), ("ASICS", r"asics"),
      ("New Balance", r"new balance"), ("adidas", r"adidas"), ("Skechers", r"skechers"), ("Under Armour", r"under armour"),
      ("PUMA", r"puma"), ("Saucony", r"saucony"), ("Reebok", r"reebok"), ("Mizuno", r"mizuno"), ("Vans", r"vans")]
def brand_of(title):
    t = (title or "").strip().lower().replace("’", "'")
    for name, pat in _P:
        if re.match(r"(%s)\b" % pat, t):
            if name == "Nike" and re.search(r"\bjordan\b", t): return "Jordan"
            return name
    return "Other"
def group_of(b):
    return "Nike Inc" if b in ("Nike", "Jordan", "Converse") else b
