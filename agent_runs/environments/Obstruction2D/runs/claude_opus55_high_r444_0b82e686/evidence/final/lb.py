import sys, math
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor
def run(seed):
    env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed); ap.reset(obs, info)
    r,objs,s=ap._parse(obs); b=objs['target_block']
    gy=b['top']+0.21; py=0.1+0.21+b['h']
    lb=math.ceil(max(abs(b['cx']-r['x']),abs(gy-r['y']))/0.05)+math.ceil(max(abs(s['x']+s['w']/2-b['cx']),abs(py-gy))/0.05)
    for t in range(300):
        obs,rew,term,tr,_=env.step(ap.get_action(obs))
        if term: break
    env.close()
    return seed, info['object_count'], t+1, lb
with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[1]), int(sys.argv[2]))))
for r in res: print(r, r[2]-r[3])
