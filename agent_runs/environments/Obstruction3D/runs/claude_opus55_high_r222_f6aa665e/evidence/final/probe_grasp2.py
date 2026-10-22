from env_client import make_env
from kin import *
import numpy as np, sys
env = make_env()
R=None
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, qt, grip=0.0, maxn=40):
    for _ in range(maxn):
        q = q_of(obs); d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
        obs2, r, te, tr, info = env.step(a)
        if np.allclose(q_of(obs2), q): return obs2, False
        obs = obs2
    return obs, True
base=(-0.12,0,0)
yaw=float(sys.argv[1])
for zc in [0.235,0.245,0.255,0.265,0.28]:
    obs, info = env.reset(seed=0)
    R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
    bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
    q=q_of(obs)
    for z in [0.4,0.33,zc]:
        qt,e = ik(q, np.array([bx,by,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
    res=[]
    for g in [-1,-1,-1]:
        a=np.zeros(11,np.float32); a[10]=g
        obs,r,te,tr,info=env.step(a); res.append(tuple(np.round(obs.data[R][10:12],3)))
    print(zc, ok, res, info)
env.close()
