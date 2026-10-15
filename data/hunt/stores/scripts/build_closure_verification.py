"""Build closure_verification.csv for the 33 US in-line doors that left the Nike locator
between the ATP crawls of 2026-07-18 and 2026-07-25.

Inputs (all saved under raw/):
  atp_delisted_33_2026-07-18_props.json  full ATP properties of the 33 delisted ids (diff of the
                                         2026-07-18-13-32-19 and 2026-07-25-13-32-20 nike.geojson runs)
  nike_api_closures_2026-10-14/<id>.json Nike's own store record, fetched 2026-10-14 from
                                         https://api.nike.com/store/store_locations/v1/<id>
                                         (the API the nike.com/retail store pages call)
Independent corroboration was opened by hand on 2026-10-14 and is entered in CORROB below.
Usage: python3 -I build_closure_verification.py   (run from data/hunt/stores)
"""
import csv, json, os

RAW = "raw"
API = "https://api.nike.com/store/store_locations/v1/"

TS = ("https://www.louisvelazquez.com/sportswear-giant-continues-store-closures-nationwide/",
      "2026-07-24", "OPENED",
      "TheStreet piece (republished on author's site) lists this address under 'Nike (NKE) has closed multiple stores during July 2026'")
MQ = ("https://maquinadoesporte.com.br/?p=240865", "2026-08", "OPENED",
      "Maquina do Esporte, citing Fast Company's count of at least 24, lists this city among closed Nike Well Collective stores")

# ref prefix -> (url, date, OPENED/SNIPPET, note). "" url = no independent source found.
CORROB = {
    "1B61E6D3": MQ,
    "277d91ad": ("https://finance.yahoo.com/markets/stocks/articles/giant-athletic-shoe-company-retail-194700040.html",
                 "2026-07-18", "OPENED",
                 "TheStreet via Yahoo: 'Nike also closed its store in the upscale Santana Row shopping district of San Jose'"),
    "339EF669": ("", "", "", "No independent report found; MapQuest page still shows hours"),
    "35d89b69": ("", "", "", "No independent report found"),
    "37204af9": ("https://finance.yahoo.com/markets/stocks/articles/giant-athletic-shoe-company-retail-194700040.html",
                 "2026-07-18", "OPENED",
                 "Fenton center email to News & Observer: store 'closed earlier than planned as part of Nike's broader national retail strategy'"),
    "44362512": MQ,
    "4b7f28d1": ("https://whatnow.com/boston/retail/alo-bringing-luxury-activewear-and-wellness-to-dedhams-legacy-place/",
                 "2026-08-14", "OPENED",
                 "ALO 'will take over the former Nike space at 222 Legacy Place'"),
    "52ce2612": ("https://www.mapquest.com/us/ohio/nike-by-crocker-park-646097278", "2026-10-14", "OPENED",
                 "MapQuest/Foursquare listing tagged 'Permanently closed'; crockerpark.com/directory lists no Nike (Yelp title 'CLOSED' is snippet only)"),
    "54ea62fd": MQ,
    "5aa17133": ("https://www.thesummitbirmingham.com/directory", "2026-10-14", "OPENED",
                 "Mall directory no longer lists a Nike store (absence only)"),
    "5ae13e18": ("", "", "", "No independent report found"),
    "5bf2cc9b": TS,
    "673a6fa8": TS,
    "6806cab3": MQ,
    "69eefa69": MQ,
    "795ef43e": TS,
    "84dfd5d7": ("https://thestreetchestnuthill.com/tenants/nike-by-chestnut-hill/", "2026-10-14", "OPENED",
                 "Mall tenant page for Nike now returns 404; explore page lists no Nike (absence only)"),
    "87ce16a8": ("https://www.bridgeport-village.com/directory", "2026-10-14", "OPENED",
                 "Center directory no longer lists Nike (absence only)"),
    "96a96ea2": TS,
    "98e0b077": ("https://www.natickmall.com/en/directory/", "2026-10-14", "OPENED",
                 "208-tenant directory lists Nike only as a shop inside Macy's, no standalone Nike (absence only)"),
    "9f0417b2": MQ,
    "a3eb9e55": MQ,
    "a6759b2b": TS,
    "a79a1c7c": MQ,
    "b3c39d9c": ("https://maquinadoesporte.com.br/?p=240865", "2026-08", "OPENED",
                 "Listed (Long Beach) per Fast Company count; Yelp title 'NIKE WELL COLLECTIVE - CLOSED - Updated August 2026' is snippet only"),
    "b636bb42": ("https://communityimpact.com/the-woodlands/business/nike-and-pressed-juicery-closed-at-market-street-in-the-woodlands/",
                 "2026-07-17", "OPENED",
                 "Market Street officials confirmed July 16 that Nike (Ste. 885) is 'no longer operating'"),
    "c403059c": ("", "", "", "No independent report found"),
    "c688c589": ("", "", "", "No independent report found"),
    "ca3319c3": ("https://www.ridgedalecenter.com/en/directory/", "2026-10-14", "OPENED",
                 "111-tenant mall directory lists no Nike (absence only)"),
    "cdeca7ba": ("", "", "", "No independent report found"),
    "d52a1dc2": TS,
    "e33b73c8": TS,
    "ef4d5095": ("https://www.hobokengirl.com/nike-hoboken-closed-july-2026/", "2026-07-16", "OPENED",
                 "'According to Google, this location is permanently closed' (site visit July 15)"),
}

props = json.load(open(os.path.join(RAW, "atp_delisted_33_2026-07-18_props.json")))
rows = []
for p in props:
    ref = p["ref"]
    d = json.load(open(os.path.join(RAW, "nike_api_closures_2026-10-14", ref + ".json")))
    od = d.get("operationalDetails", {})
    hrs = od.get("hoursOfOperation", {}).get("regularHours", {})
    days_open = sum(1 for v in hrs.values() if v)
    url, date, kind, note = CORROB[ref[:8]]
    closed = bool(od.get("closingDate")) and days_open == 0
    if closed and url and "absence only" not in note:
        basis = "Nike record + independent report"
    elif closed and url:
        basis = "Nike record + directory absence"
    elif closed:
        basis = "Nike record only"
    else:
        basis = "Nike record shows no closing date"
    rows.append({
        "store_id": ref,
        "store_number": d.get("storeNumber"),
        "name": d.get("name"),
        "nike_store_concept": d.get("storeConcept"),
        "facility_type": d.get("facilityType"),
        "address": p.get("addr:street_address"),
        "city": p["addr:city"],
        "state": p["addr:state"],
        "opening_date": od.get("openingDate"),
        "status": "confirmed closed" if closed else "unknown",
        "nike_closing_date": od.get("closingDate"),
        "evidence_url": API + ref,
        "evidence_date": "2026-10-14",
        "evidence_type": "OPENED",
        "evidence_note": f"Nike store record: closingDate {od.get('closingDate')}, regular hours empty on all 7 days, concept still '{d.get('storeConcept')}' (not reclassified); id absent from all 11 crawls 2026-07-25 to 2026-10-03; no Nike door of any type within 3 km in 2026-10-14 feed",
        "corroboration_url": url,
        "corroboration_date": date,
        "corroboration_type": kind,
        "corroboration_note": note,
        "confirmation_basis": basis,
    })

with open("closure_verification.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), Counter(r["status"] for r in rows), Counter(r["confirmation_basis"] for r in rows))
