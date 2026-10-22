import json, sys, time
from concurrent.futures import ProcessPoolExecutor
class T:
    def __init__(s,n): s.name=n
class O:
    def __init__(s,n,t): s.name=n; s.type=T(t)
class FakeState:
    def __init__(s,objs): s.objs=objs; s.o={n:O(n,v['type']) for n,v in objs.items()}
    def get_object_names(s): return set(s.objs)
    def get_object_from_name(s,n): return s.o[n]
    def get(s,o,f): return s.objs[o.name]['f'][f]
def run(args):
    seed, st = args
    import approach
    ap=approach.GeneratedApproach(None,None,{})
    import os, math
    if os.environ.get("HC"): ap.head_cands=tuple(float(v) for v in os.environ["HC"].split(","))
    t=time.time()
    ap.reset(FakeState(st['objs']), st['info'])
    tp=time.time()-t
    from approach import parse
    d=parse(FakeState(st['objs']))
    steps=ap._simulate(d)
    return seed, st['info'].get('object_count'), steps, ap.plan_cost, round(tp,2)
if __name__=='__main__':
    S=json.load(open(sys.argv[1]))
    lo,hi=int(sys.argv[2]),int(sys.argv[3])
    items=[(int(k),v) for k,v in S.items() if lo<=int(k)<hi]
    with ProcessPoolExecutor(16) as ex:
        res=list(ex.map(run, items))
    res.sort()
    if len(sys.argv)>4:
        for r in res: print(*r)
    print('TOTAL', sum(r[2] for r in res), 'N', len(res), 'maxt', max(r[4] for r in res))
