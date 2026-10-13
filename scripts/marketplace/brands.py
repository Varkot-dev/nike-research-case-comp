import re
BRANDS=[("Nike",r"nike"),("Jordan",r"jordan|air jordan"),("Converse",r"converse"),("HOKA",r"hoka( one one)?"),("On",r"on( running| cloud)?(?=[\s'’]|$)|on-running"),
("Brooks",r"brooks"),("ASICS",r"asics"),("New Balance",r"new balance"),("adidas",r"adidas"),("Skechers",r"skechers"),("Saucony",r"saucony"),
("Under Armour",r"under armour"),("PUMA",r"puma"),("Reebok",r"reebok"),("Mizuno",r"mizuno"),("Altra",r"altra"),("Vans",r"vans"),("Merrell",r"merrell"),
("Salomon",r"salomon"),("Allbirds",r"allbirds"),("Crocs",r"crocs"),("Fila",r"fila"),("Hey Dude",r"hey dude"),("Steve Madden",r"steve madden"),("Kizik",r"kizik"),("Ryka",r"ryka"),("UGG",r"ugg"),("Timberland",r"timberland"),("Champion",r"champion")]
def brand_of(title):
    t=(title or "").strip().lower().replace("’","'")
    for name,pat in BRANDS:
        if re.match(r"(%s)\b"%pat,t): return name
    return "Other:"+(t.split()[0] if t else "")
FOCUS=["Nike","Jordan","HOKA","On","Brooks","ASICS","New Balance","adidas","Skechers","Saucony","Under Armour","PUMA"]
MODEL_FALLBACK=[("New Balance",r"fresh foam|\b(880|1080|860|990|9060|550|530)v?\d*\b"),("ASICS",r"\bgel-"),("Brooks",r"\b(ghost \d|adrenaline gts|glycerin)"),
("HOKA",r"\b(clifton|bondi)\b"),("Nike",r"\b(pegasus|vomero|air max|air force 1|dunk low|revolution \d)\b"),("adidas",r"\b(ultraboost|samba|gazelle|campus 00s)\b"),("On",r"\bcloud(monster|surfer|nova|tilt| 5| 6)\b")]
_brand_of=brand_of
def brand_of(title):
    b=_brand_of(title)
    if b.startswith("Other:"):
        t=(title or "").lower()
        for name,pat in MODEL_FALLBACK:
            if re.search(pat,t): return name
    return b
