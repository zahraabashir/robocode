import sys, math, collections
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor
def run(seed):
    env = make_env(); obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    c=collections.Counter(); npush=0; last=None
    for t in range(1000):
        a = ap.get_action(obs)
        c[(ap.mode, ap.push[3] if ap.push else None)]+=1
        if ap.mode=='push' and last!='push': npush+=1
        last=ap.mode
        obs, r, term, trunc, info = env.step(a)
        if term: break
    return c, npush
tot=collections.Counter(); np_=0
with ThreadPoolExecutor(8) as ex:
    for c,n in ex.map(run, range(1000,1080)): tot+=c; np_+=n
print({k:v/80 for k,v in tot.items()}, 'pushes', np_/80)
