import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); t0=int(sys.argv[2]); t1=int(sys.argv[3]); OC=int(sys.argv[4]) if len(sys.argv)>4 else None
env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(t1):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    if t>=t0:
        q=ap._q(obs); b=ap._base(obs); T=ap._ee_world(q,b)
        print(t, ap.cur[0], ap.cur[3] if ap.cur[0]=="move" else "", "jp", None if ap.jplan is None else (ap.jplan is not False), "a", np.round(a,3), "base", np.round(b,3), "ee", np.round(T[:3,3],3))
    if term: break
