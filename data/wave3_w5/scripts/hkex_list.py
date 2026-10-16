import json,urllib.request,urllib.parse,sys,time
UA='Mozilla/5.0 (research script)'
def lst(sid,frm,to,title=''):
    p=dict(sortDir=0,sortByOptions='DateTime',category=0,market='SEHK',stockId=sid,documentType=-1,fromDate=frm,toDate=to,title=title,searchType=0,t1code=-2,t2Gcode=-2,t2code=-2,rowRange=300,lang='E')
    r=urllib.request.urlopen(urllib.request.Request('https://www1.hkexnews.hk/search/titleSearchServlet.do?'+urllib.parse.urlencode(p),headers={'User-Agent':UA}),timeout=60).read()
    return json.loads(json.loads(r)['result'])
if __name__=='__main__':
    sid=int(sys.argv[1]);frm=sys.argv[2];to=sys.argv[3];t=sys.argv[4] if len(sys.argv)>4 else ''
    for r in lst(sid,frm,to,t): print(r['DATE_TIME'],'|',r['TITLE'][:100],'|',r['FILE_LINK'])
