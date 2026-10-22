import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
cnt=int(sys.argv[1])
def run(seed):
    env = make_env()
    try:
        obs, info = env.reset(seed=seed, options={"object_count": cnt})
    except Exception as e:
        return seed, 'err', str(e)[:100]
    n=len([o for o in obs if o.type.name=='objective'])
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
    steps=0
    while steps < 300:
        obs, r, term, trunc, info = env.step(ap.get_action(obs)); steps+=1
        if term: break
    env.close()
    return seed, n, term, steps, ap.replans, round(tp,2), round(time.time()-t0,1)
from concurrent.futures import ThreadPoolExecutor
NT=int(sys.argv[4]) if len(sys.argv)>4 else 8
with ThreadPoolExecutor(NT) as ex: res=list(ex.map(run, range(int(sys.argv[2]), int(sys.argv[3]))))
for r in res:
    if len(r)<5 or not r[2] or r[4]: print(r)
ok=[r for r in res if r[2] is True]
print(sorted(ok,key=lambda r:-r[5])[:4])
print('solved',len(ok),len(res),'mean',np.mean([r[3] for r in ok]),'maxplan',max(r[5] for r in ok))
