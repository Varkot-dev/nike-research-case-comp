import sys,json,urllib.request,os,time
out=sys.argv[1]
ciks={'NKE':320187,'LULU':1397187,'RL':1037038,'EL':1001250,'SBUX':829224,'TPR':1116132,'UAA':1336917,'VFC':103379,'PVH':78239,'COLM':1050797,'DECK':910521,'CROX':1334036,'WWW':110471,'HBI':1359841,'LEVI':94845,'SKX':1065837,'CPRI':1530721,'FOSL':883569,'CRI':1060822,'GPS':39911,'HAS':46080,'MAT':63276,'HOG':793952,'COTY':1024305,'TIF':98246,'ANF':1018840,'AEO':919012,'URBN':912615,'LB':701985,'JWN':72333,'FL':850209,'GIII':821002,'OXM':75288,'PLCE':1041859,'CHS':897429,'SHOO':913241,'MCD':63908,'YUM':1041061,'CMG':1058090,'NWL':814453,'WHR':106640,'PII':931015,'KSS':885639,'M':794367,'BBY':764478,'EL2':1001250,'CL':21665,'KMB':55785,'CLX':21076,'HSY':47111,'KO':21344,'PEP':77476,'MDLZ':1103982,'GIS':40704,'K':55067,'CPB':16732,'TAP':24545,'STZ':16918,'MNST':865752,'PM':1413329,'MO':764180,'ELF':1600033,'PTON':1639825,'GOLF':1593538,'BC':14930,'LEA':842162,'NCLH':1513761,'MAR':1048286,'HLT':1585689,'DRI':940944,'DPZ':1286681,'YETI':1670592,'HELE':48465,'SONO':1314727,'GPRO':1500435,'TPX':1206264,'LZB':57131,'LCUT':1269678}
os.makedirs(out,exist_ok=True)
for t,c in ciks.items():
    fn=f'{out}/{t}.json'
    if os.path.exists(fn): continue
    req=urllib.request.Request(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json',headers={'User-Agent':'Mozilla/5.0'})
    try:
        d=urllib.request.urlopen(req,timeout=60).read(); open(fn,'wb').write(d); print(t,len(d))
    except Exception as e: print(t,'ERR',e)
    time.sleep(0.3)
