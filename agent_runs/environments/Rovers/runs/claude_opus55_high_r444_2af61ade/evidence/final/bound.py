import sys, json
import numpy as np
from env_client import make_env
import approach
from concurrent.futures import ThreadPoolExecutor
res=json.load(open('res_seq.json'))
actual={r[0]:r[3] for r in res}
orig=approach.seg_hits_box
def f(seed):
    env=make_env(); obs,info=env.reset(seed=seed); env.close()
    approach.seg_hits_box=orig
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    a=max(len(x) for x in ap.actions)
    approach.seg_hits_box=lambda px,*a: np.zeros(np.shape(px),dtype=bool)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    return seed, a, max(len(x) for x in ap.actions)
with ThreadPoolExecutor(1) as ex: out=list(ex.map(f, range(120)))
print("mean plan", np.mean([a for s,a,b in out]), "mean bound", np.mean([b for s,a,b in out]))
print("actual-plan", [(s,actual[s],a) for s,a,b in out if actual[s]!=a])
print("gaps", [(s,a,b) for s,a,b in out if a!=b])
