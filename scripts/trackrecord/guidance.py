import csv,sys
out=sys.argv[1]
# call, call_date, era_ceo, cfo, page, target, metric, guidance text (verbatim fragment), low, high, better ('up' or 'down'), actual, actual_source, horizon
D='Donahoe'; H='Hill'
R=[
# Q4 FY22 call
('Q4 FY22','2022-06-27',D,'Friend',17,'Q1 FY23','Revenue growth reported %','first quarter ... real-dollar Revenue growth to be flat to slightly up',0,2,'up',3.6,'Q1 FY23 release (revenues 12,687 vs 12,248)','next-quarter'),
('Q4 FY22','2022-06-27',D,'Friend',18,'Q1 FY23','Gross margin change bps','gross margin pressure to exceed 100 basis points in the first quarter',-9999,-100,'up',-220,'Q1 FY23 release','next-quarter'),
('Q4 FY22','2022-06-27',D,'Friend',17,'FY23','Revenue growth currency-neutral %','Revenue for the full year to grow low double-digits on a currency-neutral basis',10,13,'up',16,'FY23 10-K (c-n growth)','full-year'),
('Q4 FY22','2022-06-27',D,'Friend',18,'FY23','Gross margin change bps','flat to declining by 50 basis points',-50,0,'up',-250,'FY23 10-K','full-year'),
('Q4 FY22','2022-06-27',D,'Friend',18,'FY23','SG&A growth %','SG&A to increase high single-digits to low double-digits',7,13,'down',10.6,'FY23 10-K (16,377 vs 14,804)','full-year'),
('Q4 FY22','2022-06-27',D,'Friend',18,'FY23','Effective tax rate %','effective tax rate to be in the mid-teens range',14,16,'down',18.2,'FY23 10-K','full-year'),
# Q1 FY23
('Q1 FY23','2022-09-29',D,'Friend',15,'FY23','Revenue growth currency-neutral %','continue to expect currency-neutral revenue growth of low double-digits',10,13,'up',16,'FY23 10-K','full-year'),
('Q1 FY23','2022-09-29',D,'Friend',15,'FY23','Revenue growth reported %','reported revenue growth of low-to-mid single-digits',1,6,'up',9.6,'FY23 10-K (51,217 vs 46,710)','full-year'),
('Q1 FY23','2022-09-29',D,'Friend',16,'FY23','Gross margin change bps','gross margin to decline between 200 to 250 basis points',-250,-200,'up',-250,'FY23 10-K','full-year'),
('Q1 FY23','2022-09-29',D,'Friend',16,'FY23','SG&A growth %','SG&A to increase high single-digits',7,9,'down',10.6,'FY23 10-K','full-year'),
('Q1 FY23','2022-09-29',D,'Friend',16,'FY23','Effective tax rate %','mid-to-high-teens range',15,19,'down',18.2,'FY23 10-K','full-year'),
('Q1 FY23','2022-09-29',D,'Friend',16,'Q2 FY23','Revenue growth reported %','reported revenue to grow low double-digits',10,13,'up',17.2,'Q2 FY23 release (13,315 vs 11,357)','next-quarter'),
('Q1 FY23','2022-09-29',D,'Friend',16,'Q2 FY23','Gross margin change bps','decline approximately 350 to 400 basis points',-400,-350,'up',-300,'Q2 FY23 release','next-quarter'),
# Q2 FY23
('Q2 FY23','2022-12-20',D,'Friend',12,'FY23','Revenue growth currency-neutral %','full year revenue to grow low teens on a currency-neutral basis',11,13,'up',16,'FY23 10-K','full-year'),
('Q2 FY23','2022-12-20',D,'Friend',13,'FY23','Revenue growth reported %','full year reported revenue growth of mid-single digits',4,6,'up',9.6,'FY23 10-K','full-year'),
('Q2 FY23','2022-12-20',D,'Friend',13,'FY23','Gross margin change bps','continue to expect gross margin to decline between 200 to 250 basis points',-250,-200,'up',-250,'FY23 10-K','full-year'),
('Q2 FY23','2022-12-20',D,'Friend',13,'FY23','SG&A growth %','continue to expect SG&A to increase high single digits',7,9,'down',10.6,'FY23 10-K','full-year'),
('Q2 FY23','2022-12-20',D,'Friend',13,'FY23','Effective tax rate %','effective tax rate to be in the high teens range',17,19,'down',18.2,'FY23 10-K','full-year'),
('Q2 FY23','2022-12-20',D,'Friend',13,'Q3 FY23','Gross margin change bps','third quarter gross margin will decline at a similar rate as the second quarter (Q2 = -300)',-325,-275,'up',-330,'Q3 FY23 release','next-quarter'),
('Q2 FY23','2022-12-20',D,'Friend',13,'Q3 FY23','SG&A dollars $M','third quarter SG&A dollars to be in line with the second quarter (Q2 = 4,124)',4083,4165,'down',3959,'Q3 FY23 release','next-quarter'),
# Q3 FY23
('Q3 FY23','2023-03-21',D,'Friend',14,'FY23','Revenue growth reported %','Fiscal 23 reported revenue to grow high single-digits',7,9,'up',9.6,'FY23 10-K','full-year'),
('Q3 FY23','2023-03-21',D,'Friend',14,'Q4 FY23','Revenue growth reported %','fourth quarter ... flat to low single-digit revenue growth',0,3,'up',4.8,'Q4 FY23 release (12,825 vs 12,234)','next-quarter'),
('Q3 FY23','2023-03-21',D,'Friend',14,'FY23','Gross margin change bps','gross margin to decline approximately 250 basis points',-275,-225,'up',-250,'FY23 10-K','full-year'),
('Q3 FY23','2023-03-21',D,'Friend',15,'FY23','SG&A growth %','SG&A to grow approximately 10%',9,11,'down',10.6,'FY23 10-K','full-year'),
('Q3 FY23','2023-03-21',D,'Friend',15,'FY23','Effective tax rate %','tax rate to be in the high teens range',17,19,'down',18.2,'FY23 10-K','full-year'),
# Q4 FY23
('Q4 FY23','2023-06-29',D,'Friend',14,'FY24','Revenue growth reported %','Fiscal 24 reported revenue to grow mid-single digits',4,6,'up',0.3,'FY24 10-K (51,362 vs 51,217)','full-year'),
('Q4 FY23','2023-06-29',D,'Friend',15,'FY24','Gross margin change bps','gross margins to expand 140 to 160 basis points',140,160,'up',110,'FY24 10-K','full-year'),
('Q4 FY23','2023-06-29',D,'Friend',15,'FY24','SG&A growth vs revenue growth, pts','SG&A to grow slightly above revenue (SG&A growth minus revenue growth)',0,2,'down',0.9,'FY24 10-K (SG&A +1.2% vs revenue +0.3%)','full-year'),
('Q4 FY23','2023-06-29',D,'Friend',15,'FY24','Effective tax rate %','effective tax rate to be similar to Fiscal 23 (18.2%)',17.2,19.2,'down',14.9,'FY24 10-K','full-year'),
('Q4 FY23','2023-06-29',D,'Friend',15,'Q1 FY24','Revenue growth reported %','first-quarter revenue growth to be flat to up low single-digits',0,3,'up',2.0,'Q1 FY24 release (12,939 vs 12,687)','next-quarter'),
('Q4 FY23','2023-06-29',D,'Friend',15,'Q1 FY24','Gross margin change bps','down 50-75 basis points on a reported basis',-75,-50,'up',-10,'Q1 FY24 release','next-quarter'),
('Q4 FY23','2023-06-29',D,'Friend',15,'Q1 FY24','SG&A growth %','SG&A to grow low double-digits on a reported basis',10,13,'down',5.0,'Q1 FY24 release','next-quarter'),
# Q1 FY24
('Q1 FY24','2023-09-28',D,'Friend',11,'FY24','Revenue growth reported %','continue to expect reported revenue to grow mid-single digits',4,6,'up',0.3,'FY24 10-K','full-year'),
('Q1 FY24','2023-09-28',D,'Friend',11,'FY24','Gross margin change bps','continue to expect gross margins to expand 140 to 160 basis points',140,160,'up',110,'FY24 10-K','full-year'),
('Q1 FY24','2023-09-28',D,'Friend',12,'FY24','SG&A growth %','SG&A ... at the high end of mid-single digits',5,6,'down',1.2,'FY24 10-K','full-year'),
('Q1 FY24','2023-09-28',D,'Friend',12,'FY24','Effective tax rate %','effective tax rate to be in the high-teens range',17,19,'down',14.9,'FY24 10-K','full-year'),
('Q1 FY24','2023-09-28',D,'Friend',12,'Q2 FY24','Revenue growth reported %','second quarter reported revenue growth to be up slightly',0,2,'up',0.5,'Q2 FY24 release (13,388 vs 13,315)','next-quarter'),
('Q1 FY24','2023-09-28',D,'Friend',12,'Q2 FY24','Gross margin change bps','expand approximately 100 basis points',75,125,'up',170,'Q2 FY24 release','next-quarter'),
('Q1 FY24','2023-09-28',D,'Friend',12,'Q2 FY24','SG&A growth %','second-quarter SG&A to grow mid to high single digits',4,9,'down',0.5,'Q2 FY24 release','next-quarter'),
('Q1 FY24','2023-09-28',D,'Friend',12,'Q2 FY24','Effective tax rate %','second-quarter effective tax rate to be in the high-teens range',17,19,'down',17.9,'Q2 FY24 release','next-quarter'),
# Q2 FY24
('Q2 FY24','2023-12-21',D,'Friend',13,'FY24','Revenue growth reported %','full year reported revenue now growing approximately 1% (cut from mid-single digits)',0,2,'up',0.3,'FY24 10-K','full-year'),
('Q2 FY24','2023-12-21',D,'Friend',13,'FY24','Gross margin change bps','continue to expect full year gross margins to expand 140 to 160 basis points',140,160,'up',110,'FY24 10-K','full-year'),
('Q2 FY24','2023-12-21',D,'Friend',13,'FY24','SG&A growth ex restructuring %','full year SG&A growth to improve to low single digits, excluding restructuring charges',1,3,'down',-1.1,'my arithmetic: (16,576-379)/16,377-1, FY24 10-K p. 91','full-year'),
('Q2 FY24','2023-12-21',D,'Friend',13,'FY24','Restructuring charge $M','restructuring charge of $400 million to $450 million',400,450,'down',443,'FY24 10-K p. 91','full-year'),
('Q2 FY24','2023-12-21',D,'Friend',14,'FY24','Effective tax rate %','continue to expect our full year effective tax rate to be in the high teens range',17,19,'down',14.9,'FY24 10-K','full-year'),
('Q2 FY24','2023-12-21',D,'Friend',13,'Q3 FY24','Revenue growth reported %','Q3 reported revenue to be slightly negative',-2,0,'up',0.3,'Q3 FY24 release (12,429 vs 12,390)','next-quarter'),
('Q2 FY24','2023-12-21',D,'Friend',13,'Q3 FY24','Gross margin change bps','Q3 margins expanding 160 to 180 basis points',160,180,'up',150,'Q3 FY24 release (includes ~50 bps restructuring)','next-quarter'),
('Q2 FY24','2023-12-21',D,'Friend',13,'Q4 FY24','Revenue growth reported %','Q4 reported revenue to be up low single digits',1,3,'up',-1.7,'Q4 FY24 release (12,606 vs 12,825)','two-quarters-out'),
('Q2 FY24','2023-12-21',D,'Friend',13,'Q4 FY24','Gross margin change bps','Q4 margins expanding 225 to 250 basis points',225,250,'up',110,'Q4 FY24 release','two-quarters-out'),
# Q3 FY24
('Q3 FY24','2024-03-21',D,'Friend',14,'FY24','Revenue growth reported %','continue to expect revenues to grow approximately 1%',0,2,'up',0.3,'FY24 10-K','full-year'),
('Q3 FY24','2024-03-21',D,'Friend',14,'Q4 FY24','Revenue growth reported %','Q4 revenue to be up slightly',0,2,'up',-1.7,'Q4 FY24 release','next-quarter'),
('Q3 FY24','2024-03-21',D,'Friend',14,'Q4 FY24','Gross margin change bps','Q4 gross margins to expand approximately 160-180 basis points',160,180,'up',110,'Q4 FY24 release','next-quarter'),
('Q3 FY24','2024-03-21',D,'Friend',14,'FY24','Gross margin change bps','gross margins expanding approximately 120 basis points',95,145,'up',110,'FY24 10-K','full-year'),
('Q3 FY24','2024-03-21',D,'Friend',14,'Q4 FY24','SG&A growth %','Q4 SG&A to be down slightly versus the prior year',-2,0,'down',-6.5,'Q4 FY24 release','next-quarter'),
('Q3 FY24','2024-03-21',D,'Friend',15,'FY24','SG&A growth ex restructuring %','Excluding the impact of restructuring charges ... full-year SG&A to be roughly flat',-1,1,'down',-1.1,'my arithmetic (as above)','full-year'),
('Q3 FY24','2024-03-21',D,'Friend',15,'FY25','Revenue growth reported %','early thoughts: We expect revenue and earnings to grow versus the prior year',0.01,99,'up',-9.8,'FY25 10-K (46,309 vs 51,362)','next-year preview'),
('Q3 FY24','2024-03-21',D,'Friend',15,'H1 FY25','Revenue growth reported %','revenue in the first half of the fiscal year to be down low single-digits',-3,-1,'up',-9.1,'my arithmetic: (11,589+12,354)/(12,939+13,388)-1','next-year preview'),
# Q4 FY24
('Q4 FY24','2024-06-27',D,'Friend',14,'FY25','Revenue growth reported %','Fiscal 25 reported revenue to be down mid-single-digits',-6,-4,'up',-9.8,'FY25 10-K','full-year'),
('Q4 FY24','2024-06-27',D,'Friend',14,'H1 FY25','Revenue growth reported %','with the first half down high single-digits',-9,-7,'up',-9.1,'my arithmetic (as above)','full-year'),
('Q4 FY24','2024-06-27',D,'Friend',14,'FY25','Gross margin change bps','full-year expansion of approximately 10 to 30 basis points',10,30,'up',-190,'FY25 10-K','full-year'),
('Q4 FY24','2024-06-27',D,'Friend',14,'FY25','SG&A growth %','full-year SG&A growth to be up slightly',0,2,'down',-2.9,'FY25 10-K (16,088 vs 16,576)','full-year'),
('Q4 FY24','2024-06-27',D,'Friend',14,'FY25','Effective tax rate %','full-year effective tax rate to be in the high-teens range',17,19,'down',17.1,'FY25 10-K','full-year'),
('Q4 FY24','2024-06-27',D,'Friend',15,'Q1 FY25','Revenue growth reported %','first-quarter revenue to be down approximately 10%',-11,-9,'up',-10.4,'Q1 FY25 release (11,589 vs 12,939)','next-quarter'),
('Q4 FY24','2024-06-27',D,'Friend',15,'Q1 FY25','Gross margin change bps','first-quarter gross margins to be in line with the full year guidance (+10 to +30)',10,30,'up',120,'Q1 FY25 release','next-quarter'),
('Q4 FY24','2024-06-27',D,'Friend',15,'Q1 FY25','SG&A growth %','first-quarter SG&A to be up mid-single-digits',4,6,'down',-1.7,'Q1 FY25 release','next-quarter'),
# Q1 FY25 (guidance withdrawn)
('Q1 FY25','2024-10-01',D,'Friend',9,'Q2 FY25','Revenue growth reported %','Q2 revenues to be down in the 8% to 10% range',-10,-8,'up',-7.7,'Q2 FY25 release (12,354 vs 13,388)','next-quarter'),
('Q1 FY25','2024-10-01',D,'Friend',9,'Q2 FY25','Gross margin change bps','Q2 gross margins to be down approximately 150 basis points',-175,-125,'up',-100,'Q2 FY25 release','next-quarter'),
('Q1 FY25','2024-10-01',D,'Friend',9,'Q2 FY25','SG&A growth %','SG&A to be roughly flat versus the prior year',-1,1,'down',-3.4,'Q2 FY25 release','next-quarter'),
('Q1 FY25','2024-10-01',D,'Friend',9,'Q2 FY25','Effective tax rate %','effective tax rate to be in the high teens range',17,19,'down',17.9,'Q2 FY25 release','next-quarter'),
('Q1 FY25','2024-10-01',D,'Friend',9,'FY25','Gross margin change bps','gross margins to decline versus the prior year (direction only)',-9999,-1,'up',-190,'FY25 10-K','full-year'),
# Q2 FY25 (Hill era)
('Q2 FY25','2024-12-19',H,'Friend',13,'Q3 FY25','Revenue growth reported %','Q3 revenues to be down low double digits',-13,-10,'up',-9.3,'Q3 FY25 release (11,269 vs 12,429)','next-quarter'),
('Q2 FY25','2024-12-19',H,'Friend',14,'Q3 FY25','Gross margin change bps','down approximately 300 to 350 basis points',-350,-300,'up',-330,'Q3 FY25 release','next-quarter'),
('Q2 FY25','2024-12-19',H,'Friend',14,'Q3 FY25','SG&A growth %','Q3 SG&A dollars to be slightly down year-over-year',-2,0,'down',-8.0,'Q3 FY25 release','next-quarter'),
# Q3 FY25
('Q3 FY25','2025-03-20',H,'Friend',16,'Q4 FY25','Revenue growth reported %','Q4 revenues to be down in the mid-teens range, albeit at the low end',-15,-13,'up',-12.0,'Q4 FY25 release (11,097 vs 12,606)','next-quarter'),
('Q3 FY25','2025-03-20',H,'Friend',16,'Q4 FY25','Gross margin change bps','down approximately 400-500 basis points',-500,-400,'up',-440,'Q4 FY25 release','next-quarter'),
('Q3 FY25','2025-03-20',H,'Friend',16,'Q4 FY25','SG&A growth %','Q4 SG&A dollars to be up low to mid-single-digits',1,6,'down',1.5,'Q4 FY25 release','next-quarter'),
('Q3 FY25','2025-03-20',H,'Friend',16,'FY25','Effective tax rate %','tax rate for the full year to be in the mid-teens range',14,16,'down',17.1,'FY25 10-K','full-year'),
# Q4 FY25
('Q4 FY25','2025-06-26',H,'Friend',13,'Q1 FY26','Revenue growth reported %','Q1 revenues to be down mid-single digits',-6,-4,'up',1.1,'Q1 FY26 release (11,720 vs 11,589)','next-quarter'),
('Q4 FY25','2025-06-26',H,'Friend',13,'Q1 FY26','Gross margin change bps','down approximately 350 to 425 basis points',-425,-350,'up',-320,'Q1 FY26 release','next-quarter'),
('Q4 FY25','2025-06-26',H,'Friend',13,'Q1 FY26','SG&A growth %','Q1 SG&A dollars to be up low single digits',1,3,'down',-0.8,'Q1 FY26 release','next-quarter'),
('Q4 FY25','2025-06-26',H,'Friend',13,'FY26','Effective tax rate %','tax rate for the full year to be 19% to 20%',19,20,'down',20.3,'FY26 10-K','full-year'),
# Q1 FY26
('Q1 FY26','2025-09-30',H,'Friend',11,'Q2 FY26','Revenue growth reported %','Q2 revenues to be down low single digits',-3,-1,'up',0.6,'Q2 FY26 release (12,427 vs 12,354)','next-quarter'),
('Q1 FY26','2025-09-30',H,'Friend',11,'Q2 FY26','Gross margin change bps','down approximately 300 to 375 basis points',-375,-300,'up',-300,'Q2 FY26 release','next-quarter'),
('Q1 FY26','2025-09-30',H,'Friend',11,'Q2 FY26','SG&A growth %','Q2 SG&A dollars to be up high single digits',7,9,'down',0.8,'Q2 FY26 release','next-quarter'),
('Q1 FY26','2025-09-30',H,'Friend',11,'Q2 FY26','Effective tax rate %','tax rate for the second quarter and the full year to be in the low 20% range',20,23,'down',20.7,'Q2 FY26 release','next-quarter'),
('Q1 FY26','2025-09-30',H,'Friend',12,'FY26','SG&A growth %','continue to expect SG&A to grow low single digits in fiscal 26',1,3,'down',0.2,'FY26 10-K (16,114 vs 16,088)','full-year'),
('Q1 FY26','2025-09-30',H,'Friend',12,'FY26','Effective tax rate %','full year ... low 20% range',20,23,'down',20.3,'FY26 10-K','full-year'),
# Q2 FY26
('Q2 FY26','2025-12-18',H,'Friend',11,'Q3 FY26','Revenue growth reported %','Q3 revenues to be down low single digits',-3,-1,'up',0.1,'Q3 FY26 release (11,279 vs 11,269)','next-quarter'),
('Q2 FY26','2025-12-18',H,'Friend',11,'Q3 FY26','Gross margin change bps','down approximately 175 to 225 basis points',-225,-175,'up',-130,'Q3 FY26 release','next-quarter'),
('Q2 FY26','2025-12-18',H,'Friend',12,'Q3 FY26','SG&A growth %','Q3 SG&A dollars to be up low single digits',1,3,'down',2.3,'Q3 FY26 release','next-quarter'),
# Q3 FY26
('Q3 FY26','2026-03-31',H,'Friend',13,'Q4 FY26','Revenue growth reported %','revenues in Q4 to be down 2% to 4%',-4,-2,'up',-1.1,'Q4 FY26 release (10,972 vs 11,097)','next-quarter'),
('Q3 FY26','2026-03-31',H,'Friend',13,'Q4 FY26','Gross margin change bps','Q4 down approximately 25 to 75 basis points (actual shown ex the 900 bps one-time IEEPA benefit; reported +890)',-75,-25,'up',-10,'Q4 FY26 call p. 8 (40.2% ex IEEPA)','next-quarter'),
('Q3 FY26','2026-03-31',H,'Friend',13,'Q4 FY26','SG&A growth %','Q4 SG&A dollars to be flat to down slightly',-2,0,'down',-1.6,'Q4 FY26 release','next-quarter'),
('Q3 FY26','2026-03-31',H,'Friend',13,'FY26','Effective tax rate %','full year tax rate to be in the low 20% range',20,23,'down',20.3,'FY26 10-K','full-year'),
# Q4 FY26
('Q4 FY26','2026-06-30',H,'Friend',12,'Q1 FY27','Revenue growth reported %','reported revenues to be down low to mid-single digits',-6,-1,'up',-4.3,'Q1 FY27 release (11,213 vs 11,720)','next-quarter'),
('Q4 FY26','2026-06-30',H,'Friend',12,'Q1 FY27','Gross margin change bps','gross margin in Q1 to be slightly positive',0,50,'up',60,'Q1 FY27 release','next-quarter'),
('Q4 FY26','2026-06-30',H,'Friend',12,'Q1 FY27','SG&A growth %','Q1 SG&A dollars to be flat',-1,1,'down',-2.6,'Q1 FY27 release','next-quarter'),
]
def verdict(lo,hi,better,a):
    if a is None: return 'pending'
    if lo<=a<=hi: return 'in line'
    above=a>hi
    good = above if better=='up' else not above
    return 'beat' if good else 'miss'
rows=[]
for (call,date,ceo,cfo,pg,tgt,met,txt,lo,hi,better,act,asrc,hor) in R:
    v=verdict(lo,hi,better,act)
    note=''
    if met.startswith('SG&A') and v=='beat': note='below guide (lower cost)'
    if lo==-9999: note='open-ended guide'
    rows.append(dict(call=call,call_date=date,ceo_era=ceo,cfo=cfo,target_period=tgt,horizon=hor,metric=met,guidance_quote=txt,
        guide_low=('' if lo==-9999 else lo),guide_high=('' if hi==99 else hi),actual=act,verdict=v,note=note,
        guidance_source=f'{call} official call transcript (investors.nike.com) p. {pg}',actual_source=asrc+' ; values from data/nike_filing_facts.csv unless marked my arithmetic'))
# pending rows
P=[('Q3 FY26','2026-03-31',H,'Friend',12,'Q4 FY26 to Q2 FY27','Revenue growth','revenues to be down low single digits versus the prior year (cumulative, 3 quarters)'),
   ('Q3 FY26','2026-03-31',H,'Friend',12,'Q4 FY26 to Q2 FY27','EPS','We expect earnings to be flattish'),
   ('Q4 FY26','2026-06-30',H,'Friend',11,'Q4 FY26 to Q2 FY27','Revenue growth','now expect revenue to be down low to mid-single digits (revised from low single digits)'),
   ('Q4 FY26','2026-06-30',H,'Friend',12,'FY27','Effective tax rate %','full year tax rate to be in the low 20% range (raised to mid-20 percent range on Oct 1 2026)'),
   ('Q1 FY27','2026-10-01','Hill','Denton',11,'FY27','Revenue growth reported %','revenues to decline in the high single-digit range'),
   ('Q1 FY27','2026-10-01','Hill','Denton',11,'FY27','EBIT','EBIT to decline by a greater percentage than revenue'),
   ('Q1 FY27','2026-10-01','Hill','Denton',11,'FY27','SG&A','SG&A to remain down year-over-year'),
   ('Q1 FY27','2026-10-01','Hill','Denton',12,'FY27','Adjusted diluted EPS','adjusted earnings per share to be in the range of $1.15 to $1.35 (excludes ~$0.15 Pace)'),
   ('Q1 FY27','2026-10-01','Hill','Denton',11,'Q2 FY27','Revenue headwind','two items will represent a headwind of approximately 400 basis points to revenues in the second quarter'),]
for (call,date,ceo,cfo,pg,tgt,met,txt) in P:
    rows.append(dict(call=call,call_date=date,ceo_era=ceo,cfo=cfo,target_period=tgt,horizon='pending',metric=met,guidance_quote=txt,guide_low='',guide_high='',actual='',verdict='pending',note='',guidance_source=f'{call} official call transcript (investors.nike.com) p. {pg}',actual_source=''))
M=[('Q4 FY25','2025-06-26',H,'Friend',8,'H1 FY26','Milestone: marketplace clean','remain on track to exit the first half of fiscal 26 in a healthy and clean position','miss','Partly met: Q2 FY26 call p. 7 says NA and EMEA inventory healthy and clean; Greater China and Converse were not, and the goal was re-dated to end of calendar 2026 (Q3 FY26 call p. 12)'),
   ('Q1 FY26','2025-09-30',H,'Friend',12,'FY26','Wholesale revenue growth','expect wholesale revenue to return to modest growth for fiscal 26','beat','FY26 wholesale 27,453 vs 25,883 = +6.1% (FY26 10-K p. 32)'),
   ('Q1 FY26','2025-09-30',H,'Friend',12,'FY26','NIKE Direct revenue growth','do not expect NIKE Direct to return to growth for fiscal 26','in line','FY26 NIKE Direct 17,720 vs 18,783 = -5.7% (FY26 10-K p. 32)'),
   ('Q3 FY26','2026-03-31',H,'Friend',12,'Dec 2026','Milestone: Win Now complete','expect to complete our Win Now actions by the end of the calendar year','miss','Q1 FY27 10-Q p. 20: Sportswear and Jordan actions to extend beyond fiscal 2027; Greater China beyond fiscal 2027 (judged at Oct 2 2026, before the deadline, because the company itself withdrew the date)'),
   ('Q3 FY26','2026-03-31',H,'Friend',13,'Fall 2026','Milestone: guidance practice','we will return to providing full year and long-term guidance at our Investor Day in the fall','beat','Full-year FY27 guidance restored early, on Oct 1 2026 (Q1 FY27 call p. 11); long-term targets still pending for Nov 16 to 17 2026'),]
for (call,date,ceo,cfo,pg,tgt,met,txt,v,note) in M:
    rows.append(dict(call=call,call_date=date,ceo_era=ceo,cfo=cfo,target_period=tgt,horizon='milestone',metric=met,guidance_quote=txt,guide_low='',guide_high='',actual='',verdict=v,note=note,guidance_source=f'{call} official call transcript (investors.nike.com) p. {pg}',actual_source=note))
w=csv.DictWriter(open(out,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# hit rates
import collections
def summ(filt,label):
    c=collections.Counter(r['verdict'] for r in rows if filt(r) and r['verdict']!='pending')
    n=sum(c.values())
    if n==0: print(label,': n=0'); return
    print(f"{label}: n={n} beat={c['beat']} in line={c['in line']} miss={c['miss']} | hit (beat+in line)={100*(c['beat']+c['in line'])/n:.0f}% miss={100*c['miss']/n:.0f}%")
for era in ('Donahoe','Hill'):
    summ(lambda r:r['ceo_era']==era,f'{era} all')
    summ(lambda r:r['ceo_era']==era and r['horizon']=='next-quarter',f'{era} next-quarter')
    summ(lambda r:r['ceo_era']==era and r['horizon'] in('full-year','two-quarters-out','next-year preview'),f'{era} full-year/longer')
    summ(lambda r:r['ceo_era']==era and r['horizon']=='milestone',f'{era} milestones')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('Revenue'),f'{era} revenue only')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('Revenue') and r['horizon']=='next-quarter',f'{era} revenue next-quarter')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('Revenue') and r['horizon']!='next-quarter',f'{era} revenue full-year/longer')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('Gross'),f'{era} gross margin')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('SG&A'),f'{era} SG&A')
    summ(lambda r:r['ceo_era']==era and r['metric'].startswith('Effective'),f'{era} tax')
# FY23 vs FY24-25 for Donahoe
summ(lambda r:r['ceo_era']=='Donahoe' and r['target_period'] in('FY23','Q1 FY23','Q2 FY23','Q3 FY23','Q4 FY23'),'Donahoe FY23 targets')
summ(lambda r:r['ceo_era']=='Donahoe' and r['target_period'] not in('FY23','Q1 FY23','Q2 FY23','Q3 FY23','Q4 FY23'),'Donahoe FY24-FY25 targets')
