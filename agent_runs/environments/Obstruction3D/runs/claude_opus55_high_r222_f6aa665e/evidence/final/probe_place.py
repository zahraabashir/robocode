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
base=(0,0,0); yaw=1.5708
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
bx, by = obs.get(B,'pose_x'), obs.get(B,'pose_y')
q=q_of(obs)
for z in [0.4,0.33,0.255]:
    qt,e = ik(q, np.array([bx,by,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
tx,ty=0.3,-0.1
for p in [(bx,by,0.35),(tx,ty,0.35),(tx,ty,0.30),(tx,ty,0.27),(tx,ty,0.26)]:
    qt,e = ik(q, np.array(p), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs); print(p, ok, np.round(obs.data[B][:3],4))
for z in np.arange(0.26,0.24,-0.001):
    qt,e = ik(q, np.array([tx,ty,z]), down_R(yaw), base); obs,ok=goto(obs,qt); q=q_of(obs)
    if not ok: print("stop", z, np.round(obs.data[B][:3],4)); break
a=np.zeros(11,np.float32); a[10]=1; obs,r,te,*_=env.step(a); print("open", np.round(obs.data[R][10:12],3), np.round(obs.data[B][:3],4), r, te)
qt,e = ik(q, np.array([tx,ty,0.35]), down_R(yaw), base); obs,ok=goto(obs,qt); print("up", ok, np.round(obs.data[B][:3],4))
# regrasp and release in the air
qt,e = ik(q_of(obs), np.array([tx,ty,ee_pose(q,base)[2,3]]), down_R(yaw), base); obs,ok=goto(obs,qt)
a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a); print("regrasp", obs.data[R][11])
q=q_of(obs); qt,e = ik(q, np.array([tx,ty,0.33]), down_R(yaw), base); obs,ok=goto(obs,qt)
a=np.zeros(11,np.float32); a[10]=1; obs,*_=env.step(a); print("release air", np.round(obs.data[B][:3],4))
obs,*_=env.step(np.zeros(11,np.float32)); print("next", np.round(obs.data[B][:3],4))
env.close()
