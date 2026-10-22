from env_client import make_env
from kin import *
import numpy as np, sys
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, qt, grip=0.0, maxn=40):
    for _ in range(maxn):
        q = q_of(obs)
        d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        d = np.clip(d, -0.2, 0.2)
        a = np.zeros(11, np.float32); a[3:10] = d; a[10] = grip
        obs2, r, te, tr, _ = env.step(a)
        if np.allclose(q_of(obs2), q): return obs2, False
        obs = obs2
    return obs, True
yaw = float(sys.argv[1]) if len(sys.argv)>1 else 0.0
bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
base = (-0.12,0,0)
q = q_of(obs)
for z in [0.45,0.40,0.36,0.34,0.32,0.30,0.29,0.28,0.27,0.26,0.25,0.24,0.235,0.23,0.225,0.22,0.215,0.21,0.205,0.20]:
    qt, e = ik(q, np.array([bx,by,z]), down_R(yaw), base)
    obs, ok = goto(obs, qt)
    q = q_of(obs)
    print(z, ok, round(e,5), np.round(obs.data[B][:3],4))
    if not ok: break
# close
a = np.zeros(11, np.float32); a[10] = -1
for k in range(3):
    obs,_,_,_,_ = env.step(a); print('close', k, np.round(obs.data[R][10:12],3))
print("after close robot", np.round(obs.data[R][10:],4), "block", np.round(obs.data[B],4))
T = ee_pose(q_of(obs), base)
print("EE", np.round(T,4))
# lift
qt,e = ik(q_of(obs), T[:3,3]+[0,0,0.1], T[:3,:3], base)
obs, ok = goto(obs, qt)
print("lift", ok, np.round(obs.data[B][:7],4), np.round(obs.data[R][10:],4))
T = ee_pose(q_of(obs), base); print("EE", np.round(T[:3,3],4))
env.close()
