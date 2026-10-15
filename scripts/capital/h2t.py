import re,sys,html
def txt(p):
    t=open(p,errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); return re.sub(r'\s+',' ',t)
if __name__=='__main__':
    for p in sys.argv[1:]:
        t=txt(p)
        m=re.search(r'(NIKE, Inc\.[^.]{0,120}?(Declares|Raises|Reports|Announces|Board)[^.]{0,120})',t)
        d=re.search(r'([A-Z][a-z]{2,8} \d{1,2}, 20\d\d)',t[t.find('Press Release'):] if 'Press Release' in t else t)
        print(p.split('/')[-1], '|', d.group(1) if d else '', '|', (m.group(1)[:140] if m else t[300:420]))
