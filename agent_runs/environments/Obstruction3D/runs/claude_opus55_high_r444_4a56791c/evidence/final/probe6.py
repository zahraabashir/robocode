import sys, numpy as np, kin, importlib as _il
from env_client import make_env
from common import *
GA = _il.import_module("approach_v2").GeneratedApproach
env = make_env()
obs, info = env.reset(seed=101, options={'object_count': 9})
ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
N=int(sys.argv[1])
for t in range(N):
    a=ap.get_action(obs); q0=getq(obs)
    obs, *_ = env.step(a)
    print(t, 'act', np.round(a[3:10],3), 'moved', np.abs(getq(obs)-q0).max()>1e-7, 'tool', np.round(kin.fk(getbase(obs),getq(obs))[:3,3],3))
q0=getq(obs); b=getbase(obs); T=kin.fk(b, q0); print('tool', T[:3,3])
q=q0
for k in range(1,20):
    q,ok=kin.ik(b, q, T[:3,3]-np.array([0,0,(0.024 if k>1 else 0)+0.001*k]), T[:3,:3], iters=100, tol=1e-7)
    obs,bl=move_to(env, obs, q, grip=0.0, maxd=0.2)
    print(k, 'blocked', bl, np.round(kin.fk(b, getq(obs))[:3,3],3))
    if bl: break
