from env_client import make_env
from kin import *
import numpy as np, sys, time, json
env = make_env()
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); cx=float(sys.argv[3]); cy=float(sys.argv[4]); step=float(sys.argv[5]); n=int(sys.argv[6])
obs, info = env.reset(seed=seed)
R = obs.get_object_from_name("robot")
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, qt, maxn=40):
    for _ in range(maxn):
        q = q_of(obs); d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
        obs2, r, te, tr, _ = env.step(a)
        if np.allclose(q_of(obs2), q): return obs2, False
        obs = obs2
    return obs, True
base=(-0.12,0,0)
q=q_of(obs)
qhome,_=ik(q,np.array([cx,cy,0.36]),down_R(yaw),base)
obs,ok=goto(obs,qhome); q=q_of(obs)
out={}
for i in range(-n,n+1):
  for j in range(-n,n+1):
    x,y=cx+i*step, cy+j*step
    qa,_=ik(qhome,np.array([x,y,0.34]),down_R(yaw),base); obs,ok=goto(obs,qa); q=q_of(obs)
    stop=None
    for z in np.arange(0.33,0.22,-0.005):
        qt,_=ik(q,np.array([x,y,z]),down_R(yaw),base); obs,ok=goto(obs,qt); q=q_of(obs)
        if not ok: stop=round(z+0.005,3); break
    out[(i,j)]=stop
    for zz in np.arange(ee_pose(q,base)[2,3],0.345,0.02):
        qt,_=ik(q,np.array([x,y,zz]),down_R(yaw),base); obs,ok=goto(obs,qt); q=q_of(obs)
    obs,ok=goto(obs,qhome); q=q_of(obs)
# print map: rows = x (i), cols = y (j)
print("yaw",yaw,"center",cx,cy,"step",step)
for i in range(n,-n-1,-1):
    print("%+.3f "%(cx+i*step)+" ".join("  -  " if out[(i,j)] is None else "%.3f"%out[(i,j)] for j in range(-n,n+1)))
env.close()
