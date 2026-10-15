import json, datetime, sys, csv
RAW = sys.argv[1]; OUT = sys.argv[2]
D = datetime.date.fromisoformat
TAGS = {
 'eps': ['EarningsPerShareDiluted'],
 'rev': ['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueGoodsNet'],
 'opinc': ['OperatingIncomeLoss'],
 'pretax': ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'],
 'netint': ['InterestIncomeExpenseNonoperatingNet','InterestIncomeExpenseNet','InterestExpense'],
 'ni': ['NetIncomeLoss','ProfitLoss'],
 'shs': ['WeightedAverageNumberOfDilutedSharesOutstanding'],
 'cfo': ['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'capex': ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'cash': ['CashAndCashEquivalentsAtCarryingValue'],
 'sti': ['ShortTermInvestments','MarketableSecuritiesCurrent','AvailableForSaleSecuritiesDebtSecuritiesCurrent'],
 'ltd': ['LongTermDebtNoncurrent','LongTermNotesPayable','LongTermDebt'],
 'ltdc': ['LongTermDebtCurrent','DebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent'],
 'stb': ['NotesPayable','ShortTermBorrowings','CommercialPaper'],
 'eq': ['StockholdersEquity'],
 'gp': ['GrossProfit'],
}
INST = {'cash','sti','ltd','ltdc','stb','eq'}
def pick(facts, tags, inst):
    out = {}
    for tag in tags:
        if tag not in facts: continue
        for unit, arr in facts[tag]['units'].items():
            for x in arr:
                if x['form'] not in ('10-K','10-K405','10-KT'): continue
                if inst:
                    if 'start' in x: continue
                else:
                    if 'start' not in x: continue
                    n = (D(x['end'])-D(x['start'])).days
                    if not 350 < n < 380: continue
                k = x['end']
                if k not in out or x['filed'] < out[k][1]: out[k] = (x['val'], x['filed'], tag)
        # keep first tag that has data, but allow later tags to fill missing years
    return out
def pick_multi(facts, tags, inst):
    res = {}
    for tag in tags:
        o = pick(facts, [tag], inst)
        for k,v in o.items():
            if k not in res: res[k] = v
    return res
rows = []
for t in sys.argv[3:]:
    f = json.load(open(f'{RAW}/cf_{t}.json'))['facts']
    f = f.get('us-gaap', {})
    data = {}
    for key, tags in TAGS.items():
        data[key] = pick_multi(f, tags, key in INST)
    ends = sorted(data['eps'].keys())
    for e in ends:
        r = {'ticker': t, 'fye': e, 'filed': data['eps'][e][1]}
        for key in TAGS:
            v = data[key].get(e)
            if v is None and key in INST:
                # instant dates match period end
                pass
            r[key] = v[0] if v else ''
        rows.append(r)
cols = ['ticker','fye','filed']+list(TAGS)
with open(OUT,'w',newline='') as fh:
    w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(rows)
import collections
c = collections.Counter(); 
for r in rows:
    for k in TAGS:
        if r[k]=='' : c[(r['ticker'],k)]+=1
print(len(rows)); 
for t in sys.argv[3:]:
    n=[r for r in rows if r['ticker']==t]
    print(t,len(n),n[0]['fye'],n[-1]['fye'],{k:c[(t,k)] for k in TAGS if c[(t,k)]})
