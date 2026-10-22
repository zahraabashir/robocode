import sys, numpy as np, kin, os, importlib as _il
from env_client import make_env
from common import *
GA = _il.import_module("approach_v2").GeneratedApproach
env = make_env()
obs, info = env.reset(seed=4, options={'object_count': 7})
ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(44):
    obs, *_ = env.step(ap.get_action(obs))
print('grasp', obs.get(robot(obs),'grasp_active'))
for n in sorted(obs.get_object_names()):
    try: d=objd(obs,n); print(n, round(d['pose_x'],3), round(d['pose_y'],3), round(d['pose_z'],3), round(d['half_extent_x'],3), round(d['half_extent_y'],3), round(d['half_extent_z'],3))
    except Exception: pass
q0=getq(obs); T=kin.fk(getbase(obs), q0); print('tool', T[:3,3])
import pickle
for dv in [(0,0,0.003),(0,0,0.01),(0.003,0,0),(-0.003,0,0),(0,0.003,0),(0,-0.003,0),(0.008,0,0.002)]:
    q,ok=kin.ik(getbase(obs), q0, T[:3,3]+np.array(dv), T[:3,:3], iters=100, tol=1e-6)
    o2,bl=move_to(env, obs, q, grip=0.0)
    print(dv, 'blocked', bl, 'dq', np.round(q-q0,3))
    if not bl: obs,_=move_to(env,o2,q0)
print('--- incremental lift')
q=q0
for k in range(1,10):
    q,ok=kin.ik(getbase(obs), q, T[:3,3]+np.array([0,0,0.005*k]), T[:3,:3], iters=100, tol=1e-6)
    obs,bl=move_to(env, obs, q, grip=0.0)
    print(k, 'blocked', bl, np.round(kin.fk(getbase(obs), getq(obs))[:3,3],3), 'objz', round(objd(obs,'obstruction1')['pose_z'],3))
    if bl: break
