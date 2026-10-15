import sys, json, urllib.parse, urllib.request, csv, time
UA = "nike-research-casecomp/1.0 (student research; contact via repo)"
def q(sparql):
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(sparql)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/sparql-results+json"})
    return json.load(urllib.request.urlopen(req, timeout=120))
# P5995 kit supplier, qualifiers P580 start, P582 end
sparql = """
SELECT ?team ?teamLabel ?supplier ?supplierLabel ?start ?end ?instLabel ?countryLabel WHERE {
  ?team p:P5995 ?st . ?st ps:P5995 ?supplier .
  OPTIONAL { ?st pq:P580 ?start } OPTIONAL { ?st pq:P582 ?end }
  OPTIONAL { ?team wdt:P31 ?inst } OPTIONAL { ?team wdt:P17 ?country }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}"""
r = q(sparql)
out = sys.argv[1]
json.dump(r, open(out, "w"))
print(len(r["results"]["bindings"]))
