import sys, math, collections, json
import numpy as np
from env_client import make_env
from approach import GeneratedApproach, Block
from concurrent.futures import ThreadPoolExecutor
def run(seed):
    env = make_env(); obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    out=[]
    for t in range(1000):
        a = ap.get_action(obs)
        mode=ap.mode; pr=ap.push
        obs2, r, term, trunc, info = env.step(a)
        if mode=='push' and pr[3]=='r':
            dth=(obs2[2]-obs[2]+math.pi)%(2*math.pi)-math.pi
            if abs(dth)>0.004:
                B=Block(obs); v=B.Rm.T@(obs2[0:2]-obs[0:2])
                # use midpoint rotation for accuracy
                Rm=Block(obs).Rm; 
                u=v/dth
                c=(-u[1],u[0])
                out.append((pr[0],c[0],c[1],obs[12],obs[13],obs[14]))
        obs=obs2
        if term: break
    return out
allr=[]
with ThreadPoolExecutor(8) as ex:
    for o in ex.map(run, range(2000,2060)): allr+=o
d=collections.defaultdict(list)
for r in allr: d[r[0]].append(r[1:])
for k,v in d.items():
    v=np.array(v); print(k, len(v), 'median c', np.round(np.median(v[:,:2],0),3), 'iqr', np.round(np.percentile(v[:,:2],75,0)-np.percentile(v[:,:2],25,0),3))
json.dump(allr, open('cor_data.json','w'))
