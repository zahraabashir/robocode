import sys, json
from concurrent.futures import ProcessPoolExecutor
from test_approach import run
seeds=list(range(int(sys.argv[1]), int(sys.argv[2])))
with ProcessPoolExecutor(8) as ex:
    res=list(ex.map(run, seeds))
tot=0
for r in res:
    print(r['seed'], r['n'], r['steps'], r['term'], r['plan'], r['tplan'])
    tot+=r['steps']
print('TOTAL', tot, 'fails', sum(1 for r in res if not r['term']), 'maxplan', max(r['tplan'] for r in res))
