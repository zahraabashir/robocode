import sys, numpy as np, kin, importlib as _il
from env_client import make_env
from common import *
GA = _il.import_module("approach_v2").GeneratedApproach
env = make_env()
obs, info = env.reset(seed=4, options={'object_count': 7})
ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(45):
    obs, *_ = env.step(ap.get_action(obs))
q0=getq(obs); b=getbase(obs); T=kin.fk(b, q0); print('tool', T[:3,3], 'grasp', obs.get(robot(obs),'grasp_active'))
tgt=ap._lookahead(q0); print('lookahead target tool', kin.fk(b,tgt)[:3,3], 'dq', np.round(tgt-q0,3))
for dz in [0.01,0.02,0.03,0.04]:
    q=q0
    for k in range(10): q,ok=kin.ik(b, q, T[:3,3]+np.array([0,0,dz*(k+1)/10]), T[:3,:3], iters=100, tol=1e-7)
    o2,bl=move_to(env, obs, q, grip=0.0, maxd=0.2)
    print(dz,'blocked',bl, 'dqmax', np.abs(q-q0).max())
    if not bl: obs,_=move_to(env,o2,q0)
