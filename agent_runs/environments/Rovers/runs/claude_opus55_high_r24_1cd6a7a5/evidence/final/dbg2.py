import sys
import numpy as np
from env_client import make_env
import os, importlib; GeneratedApproach = importlib.import_module(os.environ.get("APP", "approach")).GeneratedApproach
seed = int(sys.argv[1]); N = int(sys.argv[2])
env = make_env()
obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
print("req", getattr(ap, "my_req", None))
for i in range(2): print(i, [(tuple(np.round(ap.bfs[i].pos(c),2)), op) for c, op, L in ap.plans[i]["steps"]])
names = {v:k for k,v in {"sample": -5/6, "calibrate": -0.5, "image": -1/6, "noop": 1/6, "send": 0.5, "drop": 5/6}.items()}
for step in range(N):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    g = obs.get
    rs = [(round(g(rv,'x'),2), round(g(rv,'y'),2), round(g(rv,'theta'),2), int(g(rv,'at_home')), int(g(rv,'store_full')), int(g(rv,'calibrated'))) for rv in ap.sc.rovers]
    ops = [min(names, key=lambda b: abs(b-a[3])), min(names, key=lambda b: abs(b-a[7]))]
    objs = ''.join('%d%d%d ' % (g(o,'have_image_rover0'), g(o,'have_image_rover1'), g(o,'received_image')) for o in ap.sc.objectives)
    sm = ''.join('%d%d%d ' % (g(s,'analyzed_rover0'), g(s,'analyzed_rover1'), g(s,'received_analysis')) for s in ap.sc.samples)
    print(step, [names[o] for o in ops], rs, objs, '|', sm, term)
    if term: break
