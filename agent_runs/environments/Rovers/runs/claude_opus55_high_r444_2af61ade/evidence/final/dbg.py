import sys
from test_approach import *
import approach
for seed in map(int, sys.argv[1:]):
    env = make_env(); obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    print("seed",seed,"pred",ap.pred, [len(a) for a in ap.actions])
    steps=0
    while steps<300:
        obs,r,term,tr,info=env.step(ap.get_action(obs)); steps+=1
        if term: break
    print(" steps",steps,term, "pred", ap.pred, ap.log[:6])
    env.close()
