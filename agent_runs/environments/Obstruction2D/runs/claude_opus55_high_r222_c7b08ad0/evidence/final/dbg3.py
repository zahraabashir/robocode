import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); oc=int(sys.argv[2]); T=int(sys.argv[3])
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed, options={'object_count':oc}); ap.reset(obs, info)
for t in range(T):
    a = ap.get_action(obs); obs, *_ = env.step(a)
r,rects = ap._parse(obs); ap.r=r
print(ap.phase, ap.task, ap.held)
print('robot', {k: round(v,3) for k,v in r.items()})
for k,v in sorted(rects.items()): print(k, {q: round(v[q],3) for q in ['x0','x1','y0','y1']})
print('need here', ap._clear_y_at(r['x'], rects, ap.held))
for n,o in rects.items(): print(n, ap._clear_y_at(r['x'], {n:o}, ap.held))
