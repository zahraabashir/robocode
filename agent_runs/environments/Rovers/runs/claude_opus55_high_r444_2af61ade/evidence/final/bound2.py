import sys, json
import numpy as np
from env_client import make_env
import approach
from concurrent.futures import ThreadPoolExecutor
def f(seed):
    env=make_env(); obs,info=env.reset(seed=seed); env.close()
    approach.IMG_TH=None
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    a=max(len(x) for x in ap.actions)
    approach.IMG_TH=-np.pi/2
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    return seed, a, max(len(x) for x in ap.actions)
with ThreadPoolExecutor(1) as ex: out=list(ex.map(f, range(int(sys.argv[1]))))
print("mean plan", np.mean([a for s,a,b in out]), "mean rot", np.mean([b for s,a,b in out]))
print("gaps", [(s,a,b) for s,a,b in out if a!=b])
