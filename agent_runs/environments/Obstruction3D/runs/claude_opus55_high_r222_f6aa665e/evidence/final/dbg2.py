import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach, fk
seed=int(sys.argv[1]); N=int(sys.argv[2]); t0=int(sys.argv[3])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(N):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    q = ap._q(obs); T,_,_ = fk(q)
    if t>=t0: print(t, np.round(T[:3,3],3), np.round(q,2), np.round(a[3:10],3))
