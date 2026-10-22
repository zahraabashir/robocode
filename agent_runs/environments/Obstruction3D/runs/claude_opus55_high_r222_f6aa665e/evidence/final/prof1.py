import sys, time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); OC=int(sys.argv[2]) if len(sys.argv)>2 else None
env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
t=time.time(); ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info); print("reset", round(time.time()-t,3))
for k in range(1000):
    t=time.time(); a = ap.get_action(obs); dt=time.time()-t
    if dt>0.2: print(k, round(dt,3), ap.cur[0] if ap.cur else None, ap.cur[3] if ap.cur and ap.cur[0]=="move" else "")
    obs, r, term, trunc, info = env.step(a)
    if term: print("done", k); break
