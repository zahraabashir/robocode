import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed = int(sys.argv[1])
env = make_env()
obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
print("tasks", ap.tasks, "mytasks", ap.my_tasks)
for i in range(2): print(i, "visits", ap.plans[i]['visits'], "path", [tuple(np.round(ap.planners[i].pos(c),2)) for c in ap.plans[i]['path']][:40])

for step in range(int(sys.argv[2]) if len(sys.argv)>2 else 60):
    pass
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    g = obs.get
    rs = [(round(g(rv,'x'),2), round(g(rv,'y'),2), int(g(rv,'store_full')), int(g(rv,'calibrated'))) for rv in ap.sc.rovers]
    objs = [(int(g(o,'have_image_rover0')), int(g(o,'have_image_rover1')), int(g(o,'received_image'))) for o in ap.sc.objectives]
    sm = [(int(g(s,'analyzed_rover0')), int(g(s,'analyzed_rover1')), int(g(s,'received_analysis'))) for s in ap.sc.samples]
    print(step, np.round(a,2).tolist(), rs, objs, sm, term)
    if term: break
