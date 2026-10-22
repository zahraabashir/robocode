import sys
from test_approach import *
for seed in map(int, sys.argv[1:]):
    env = make_env(); obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    steps=0
    while True:
        if not ap.actions[0] and not ap.actions[1]:
            for o in obs:
                if o.type.name in ('rover','objective') or (o.type.name=='sample'): print(' ',o.name,[round(float(v),2) for v in obs.data[o]])
            break
        obs,r,term,tr,info=env.step(ap.get_action(obs)); steps+=1
        if term: break
    print(seed, steps, term)
    env.close()
