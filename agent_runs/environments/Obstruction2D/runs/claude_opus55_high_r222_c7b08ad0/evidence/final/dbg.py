import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); opts = {'object_count': int(sys.argv[2])} if len(sys.argv)>2 else None
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed, options=opts)
print(info)
ap.reset(obs, info)
r,rects = ap._parse(obs)
for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
print('robot', r)
tt=0
for t in range(300):
    t0=time.time(); a = ap.get_action(obs); tt+=time.time()-t0
    obs, rew, term, trunc, _ = env.step(a)
    rr,_ = ap._parse(obs)
    if t<300 and (t%5==0 or ap.phase!='to_grasp'): print(t, ap.phase, ap.task['obj'], np.round(a,3), round(rr['x'],3), round(rr['y'],3), ap.stuck)
    if term: print('done', t); break
print('compute', tt)
_,rects = ap._parse(obs)
for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
