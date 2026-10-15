"""USPTO Patent Public Search (ppubs.uspto.gov) client. Anonymous session, no key, no email."""
import requests, json, time
B = "https://ppubs.uspto.gov/api/"
class PP:
    def __init__(self):
        self.s = requests.Session(); self.tok = None; self.case = None; self.n = 0
        self.login()
    def login(self):
        r = self.s.post(B + "users/me/session", data="-1", headers={"content-type": "application/json"}, timeout=60)
        self.tok = r.headers["x-access-token"]; self.case = r.json()["userCase"]["caseId"]
    def post(self, path, body, tries=4):
        for i in range(tries):
            try:
                r = self.s.post(B + path, json=body, headers={"x-access-token": self.tok, "content-type": "application/json"}, timeout=120)
                if r.status_code == 200: return r.json()
                if r.status_code in (401, 403): self.login()
                last = (r.status_code, r.text[:200])
            except Exception as e:
                last = str(e)
            time.sleep(3 * (i + 1))
        raise RuntimeError(f"ppubs failed {path} {last}")
    def search(self, q, dbs=("USPAT", "US-PGPUB"), page=100, cursor="*", fields=None):
        body = {"cursorMarker": cursor, "databaseFilters": [{"databaseName": d, "countryCodes": []} for d in dbs],
                "fields": fields or ["documentId", "patentNumber", "applicationNumber", "applicationFilingDate", "datePublished", "inventionTitle", "type", "assigneeName", "kindCode", "cpcAdditional", "cpcInventive", "uspcFullClassificationFlattened", "applicationFilingDate", "primaryExaminer"],
                "op": "OR", "pageSize": page, "q": q, "searchType": 1, "sort": "date_publ desc", "highlights": "0", "qt": "brs", "spellCheck": False, "viewName": "tile", "plurals": False, "britishEquivalents": False, "caseId": self.case, "ignorePersist": True, "userEnteredQuery": q}
        self.n += 1
        return self.post("searches/searchWithBeFamily", body)

def full(p, q, dbs=("USPAT","US-PGPUB"), start=0, page=100, sort="date_publ desc"):
    d=[{"databaseName":x,"countryCodes":[]} for x in dbs]
    query={"caseId":p.case,"hl_snippets":"2","op":"OR","q":q,"queryName":q,"highlights":"0","qt":"brs","spellCheck":False,"viewName":"tile","plurals":False,"britishEquivalents":False,"databaseFilters":d,"searchType":1,"ignorePersist":True,"userEnteredQuery":q}
    body={"start":start,"pageCount":page,"sort":sort,"docFamilyFiltering":"noFiltering","searchType":1,"familyIdEnglishOnly":None,"familyIdFirstPreferred":None,"familyIdSecondPreferred":None,"familyIdThirdPreferred":None,"showDocPerFamilyPref":None,"queryId":0,"tagDocSearch":False,"query":query}
    return p.post("searches/searchWithBeFamily", body)

def count(p, q, dbs=("USPAT","US-PGPUB")):
    d=[{"databaseName":x,"countryCodes":[]} for x in dbs]
    b={"cursorMarker":"*","databaseFilters":d,"fields":["documentId"],"op":"OR","pageSize":1,"q":q,"searchType":0,"sort":"date_publ desc"}
    return p.post("searches/generic", b)["numFound"]
