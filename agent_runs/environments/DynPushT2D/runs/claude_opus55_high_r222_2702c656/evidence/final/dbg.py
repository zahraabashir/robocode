import sys, math
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 400
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
last=None
for t in range(N):
    a = ap.get_action(obs)
    key=(ap.mode, ap.push[0] if ap.push else None)
    if key!=last:
        print(t, key, 'blk', np.round(obs[0:3],3), 'err', np.round([obs[29]-obs[0], obs[30]-obs[1], math.degrees((obs[31]-obs[2]+math.pi)%(2*math.pi)-math.pi)],3), 'rob', np.round(obs[16:18],3))
        last=key
    obs, r, term, trunc, info = env.step(a)
    if term: print('done', t+1); break
