import re
EXCL=re.compile(r'\bgolf\b|mercurial|tiempo|\bvapor (12|edge)|cryoshot|phantom|hypervenom|tiger woods|\bcleat|\bmcs\b|slide|\bmule\b|\bfoam runner|\bcrocs|\bclog\b(?!posite)',re.I)
KIDS=re.compile(r'\b(gs|ps|td|toddler|kids?|grade school|preschool|infant)\b|\(gs\)|\(ps\)|\(td\)',re.I)
WMNS=re.compile(r'\bwmns\b|\(w\)|\bwomen',re.I)
def brand_of(n):
    s=n.lower().replace('’',"'")
    parts=re.split(r'\s+x\s+',s)
    tail=parts[-1]
    for b,pat in [('Jordan',r'\bjordan\b|^ajko|\baj\d'),('Nike',r'\bnike\b'),('adidas',r'adidas|yeezy'),('New Balance',r'new balance'),('ASICS',r'asics'),('Hoka',r'hoka'),('On',r'(^|\s)on (cloud|running)|^on\b|cloudtilt|cloudmonster'),('Puma',r'puma'),('Reebok',r'reebok'),('Converse',r'converse'),('Saucony',r'saucony'),('Vans',r'\bvans\b'),('Under Armour',r'under armour'),('Crocs',r'crocs'),('Salomon',r'salomon')]:
        if re.search(pat,tail): return b
    for b,pat in [('Jordan',r'\bjordan\b'),('Nike',r'\bnike\b'),('adidas',r'adidas|yeezy'),('New Balance',r'new balance'),('ASICS',r'asics'),('Hoka',r'hoka'),('Puma',r'puma'),('Reebok',r'reebok'),('Converse',r'converse'),('Saucony',r'saucony'),('Vans',r'\bvans\b')]:
        if re.search(pat,s): return b
    return 'Other'
COLLAB=re.compile(r'\sx\s|\s×\s',re.I)
def _num(pat,s):
    m=re.search(pat,s); return int(m.group(1)) if m else None
NIKE_NEW=r"air max dn|dn8|air max muse|air max pulse|\bmind 00|clogposite|lunar roam|caitlin 1|nocta glide|zoom hyperflight|first sight|v2k run|v5 rnr|rejuven8|air max craze|hot step|\bluka 1\b|air jordan future|jordan future|air jordan 40\d\d|\bsabrina 1\b|\bja 1\b|\bbook 1\b|\bair superfly|air max foamdome|vomero (plus|premium)|pegasus (premium|plus)|air max portal|\bwemb|gt hustle 1|\bgt cut 1|\bcosmic|\bair max 2k|\bair max sndr|\bshox\b.*\b(r4|ride)\b.*nothing"
def nike_class(n):
    s=n.lower().replace('’',"'")
    if COLLAB.search(n): return 'D_collab'
    if re.search(r'vomero 5|air pegasus 2k5|zoom flight|air zoom flight',s): return 'C_retro_classic'
    if re.search(NIKE_NEW+r'|tatum 1\b|gt future|zoom freak 1|\bluka 1\b',s): return 'A_new_model'
    if re.search(r"\ba.one\b|\ba.two\b",s): return 'A_new_model' if re.search(r"a.one",s) else 'B_perf_version'
    m=_num(r'lebron (\d+)',s)
    if m is not None: return 'B_perf_version' if m>=20 else 'C_retro_classic'
    m=_num(r'\bkd (\d+)',s)
    if m is not None: return 'B_perf_version' if m>=16 else 'C_retro_classic'
    if re.search(r'\bja \d|\bbook \d|\bsabrina \d|\bgt (cut|jump|hustle)|\bgiannis|\bfreak \d|\bimmortality|\bluka \d|\btatum \d|\bzion \d|air jordan (3[6-9]|4[0-9])\b|jordan (3[6-9]|4[0-2])\b|\bpegasus \d|\bvomero \d+|\balphafly|\bvaporfly|\bstreakfly|\binvincible|\bstructure|\binfinity|\bzoom fly|\bwinflo|\bmetcon|\bkiger|\bzegama|\bjourney run|\bquest|\bpromina|\bultrafly|\bgt future|\bmountain fly|\bair zoom (maxfly|victory)|\bmaxfly|\bpegasus trail|\bsabrina',s):
        # version ge2 or unnumbered perf
        return 'B_perf_version'
    if re.search(r"\bacg\b",s): return 'A_new_model'
    RET=r"\bdunk|air force 1|\baf1|air jordan \d{1,2}\b|air jordan (xx3|1 )|\bjordan (air ship|spizike|1)|air max|air dt max|air max2|\bblazer|\bcortez|\bterminator|foamposite|posite|\bshox|\bpenny|griffey|protro|\bkobe|air tech challenge|air flight|diamond turf|air trainer|\bwaffle|daybreak|huarache|spiridon|air pegasus|pegasus wave|moon shoe|alpha force|\braid|zoom generation|air 180|footscape|astrograbber|baltoro|field general|mac attack|ecstasy|air adjust|air streak|vomero 5|air rift|swoopes|zoom flight|presto|humara|safari|total 90|air liquid|air more uptempo|uptempo|p-rod|janoski|\bsb\b|air dt proto|air max tl|\bair jordan 4\d{3}|\bjordan (melo|super freak|trunner|jumpman)|\bair zoom|air maxim|\bair mowabb|\bcanyon|\bgato|ispa|\bair deschutz|magmascape|zegamadome|\bkukini|goadome|\bair raid"
    if re.search(RET,s): return 'C_retro_classic'
    return 'U_unmatched'
ADI_RETRO=r"samba|gazelle|campus|superstar|stan smith|forum|handball|sl ?72|taekwondo|yeezy|humanrace|climacool|adistar|crazy (8|98|1\b)|nmd|ozweego|spezial|rivalry|centennial|country|astir|orketro|ultraboost|zx|falcon|response cl|japan|tokyo|jabbar|top ten|niteball|hamburg|munchen|bermuda|gazelle|adimatic|mexicana|\bsl\b|aruku"
ADI_PERF=r"harden|anthony edwards|\bae ?\d|trae young|\bdame|d\.o\.n|\bdon issue|adizero|hyperboost|adios|evo sl|takumi|boston|supernova|adistar|ultraboost light|crazy iiinfinity|mad iiinfinity|badbo|tyshawn|blondey|pro model"
NB_RETRO=r"\b(204l|327|530|550|574|610|650|740|990|991|992|993|996|997|998|1000|1300|1906|2000|2002|2010|9060|1906l|1906r|1906a|t500|abzorb|allerdale|warped|wrpd|numeric)"
NB_PERF=r"kawhi|two wxy|fresh foam|hesi|coco|fuelcell|rebel|sc elite|supercomp|vongo|1080|more v|880|860|rc elite|fuel cell|propel"
ASICS_RETRO=r"gel-?(1130|kahana|nyc|kayano 14|1090|lyte|sonoma|quantum|k1011|1130)|gt-2160|skyhand|kayano 14|\bgel-"
def peer_class(n,b):
    s=n.lower().replace('’',"'")
    if COLLAB.search(n): return 'D_collab'
    ret,perf={'adidas':(ADI_RETRO,ADI_PERF),'New Balance':(NB_RETRO,NB_PERF),'ASICS':(ASICS_RETRO,r'novablast|superblast|metaspeed|magic speed|nimbus|kayano 3|gt-?2000|gt-?1000|cumulus|noosa|gel-?pulse|sky elite')}.get(b,('x','x'))
    if re.search(perf,s): return 'B_perf_version'
    if re.search(ret,s): return 'C_retro_classic'
    return 'U_unmatched'
def model_key(n):
    s=n.lower().replace('’',"'")
    s=re.split(r'[“"‘]',s)[0]
    s=re.sub(r'\([^)]*\)',' ',s)
    s=re.sub(r'air jordan 40\d\d','air jordan 40xx',s)
    s=re.sub(r'\b(flyknit|amp|pe|gore tex|gore-tex|elite|prime|96|proto|turbo|nrg|ny|animal|pack|ep|noir|shadow)\b',' ',s)
    s=re.sub(r'\b(nike|adidas|new balance|asics|retro|og|protro|se|premium|prm|sp|qs|wmns|gs|ps|td|\(w\)|\(gs\)|low|high|mid|made in usa|made in uk|flyease|x)\b','',s)
    s=re.sub(r'[^a-z0-9 .]+',' ',s); return re.sub(r'\s+',' ',s).strip()
