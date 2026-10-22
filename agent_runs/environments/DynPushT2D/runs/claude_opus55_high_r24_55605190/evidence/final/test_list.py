import sys, numpy as np
from test_approach import run
from concurrent.futures import ThreadPoolExecutor
seeds=[int(x) for x in sys.argv[1:]]
with ThreadPoolExecutor(8) as ex:
    res=list(ex.map(run, seeds))
for s,ok,n,dt,e in res: print(s,ok,n,f'{dt:.1f}s',np.round(e,3))
print('success', sum(r[1] for r in res), '/', len(res), 'mean steps', np.mean([r[2] for r in res]))
