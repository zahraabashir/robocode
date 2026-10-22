import sys, math
import numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach, Block
seed=int(sys.argv[1]); N=int(sys.argv[2])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(N):
    if t==N-1:
        B=Block(obs); rp=obs[16:18].copy()
        for i in range(6):
            r=ap._act(obs,B,rp); print(ap.mode, ap.push[0], 'goal',ap.push_goal, 'act', r, 'banned', ap.banned, ap.push_steps)
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
