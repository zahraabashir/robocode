import sys, os, importlib
from env_client import make_env
import numpy as np, kin
M = importlib.import_module(os.environ.get("APPROACH","approach"))
seed=int(sys.argv[1]); N=int(sys.argv[2]); S=int(sys.argv[3])
env = make_env()
obs, info = env.reset(seed=seed)
ap = M.GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
for t in range(N):
    q0=ap._q(obs)
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    if t>=S: print(t, ap.current, len(ap.plan), ap.plan[0][0] if ap.plan else None, np.round(a[3:],3), np.round(kin.fk(ap.base, ap._q(obs))[:3,3],3))
    if term: print('SOLVED'); break
