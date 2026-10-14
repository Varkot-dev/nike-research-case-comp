# Shared classifier: map a nike.com or adidas.com product URL slug to category buckets.
import re
FAN=re.compile(r'\b(nfl|mlb|nba|wnba|college|ncaa|club-fc|fc-|-fc\b|national-team|stadium|replica|jersey|fan|psg|barcelona|chelsea|liverpool|tottenham|inter-milan|atletico|al-nassr|england|france|usmnt|uswnt|brazil|portugal|netherlands|croatia|canada|mexico|korea|nigeria|australia|-team-|bills|cowboys|eagles|lakers|warriors|celtics|yankees|dodgers|cubs|steelers|chiefs|packers|49ers)\b')
CLASSIC=re.compile(r'(dunk|air-force-1|af1|air-max|blazer|cortez|p-6000|v2k|killshot|vomero-5|field-general|total-90|shox|tn|sb-)')
def slug(url):
    u=url.split("?")[0]
    if "/t/" in u: return u.split("/t/")[1].split("/")[0].lower()
    m=re.search(r'/us/([^/]+)/[A-Z0-9]{6}\.html',u); return m.group(1).lower() if m else u.lower()
def is_shoe(s):
    return bool(re.search(r'(shoes?|sneakers?|cleats?|slides?|sandals?|boots?|spikes?|flip-flops?|mules?|clogs?)(-[a-z0-9]{5,9})?$',s) or re.search(r'-shoes?-',s))
def category(url,brand="nike"):
    s=slug(url)
    shoe=is_shoe(s)
    fan=bool(FAN.search(s.replace("-"," ").replace(" ","-"))) or bool(re.search(r'(nfl|mlb|nba|college|jersey|stadium|replica)',s))
    if brand=="nike":
        if "jordan" in s: cat="jordan"
        elif "running" in s or re.search(r'(pegasus|vomero|invincible|structure|alphafly|vaporfly|zoom-fly|winflo|infinity-run|journey-run|downshifter|revolution)',s): cat="running"
        elif "basketball" in s or re.search(r'(lebron|kd-?\d|giannis|ja-\d|sabrina|book-\d|g-t-|gt-cut|gt-hustle|gt-jump)',s): cat="basketball"
        elif fan: cat="fan_gear"
        elif "soccer" in s or "football" in s: cat="soccer_football"
        elif CLASSIC.search(s): cat="lifestyle_classics"
        elif "sportswear" in s or "lifestyle" in s or "acg" in s or "tech-fleece" in s or "club-fleece" in s: cat="lifestyle_other"
        elif "training" in s or "yoga" in s or "pro-" in s or "dri-fit" in s: cat="training"
        else: cat="other"
    else:
        if re.search(r'(running|adizero|ultraboost|supernova|adistar|solar|duramo|terrex|trail|4dfwd|boston)',s): cat="running"
        elif re.search(r'(basketball|harden|dame|ae-1|anthony-edwards|trae|crazy|d\.?o\.?n)',s): cat="basketball"
        elif fan: cat="fan_gear"
        elif re.search(r'(soccer|predator|copa|x-crazyfast|f50|jersey)',s): cat="soccer_football"
        elif re.search(r'(samba|gazelle|campus|superstar|stan-smith|spezial|forum|sl-72|handball|taekwondo|country|japan|tokyo|sl72|stan)',s): cat="lifestyle_classics"
        elif re.search(r'(originals|adicolor|trefoil|firebird|beckenbauer|track)',s): cat="lifestyle_other"
        else: cat="other"
    return cat,("footwear" if shoe else "apparel_equip")
