from env_client import make_env
from kin import *
import numpy as np, sys, time
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
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
bx,by=obs.get(B,'pose_x'),obs.get(B,'pose_y')
q=q_of(obs); t=time.time()
axis=sys.argv[1]; bx+=float(sys.argv[2]); by+=float(sys.argv[3])
for d in np.arange(-0.12,0.121,0.02):
    x,y = (bx+d,by) if axis=='x' else (bx,by+d)
    cur=ee_pose(q,base)[:3,3]
    for zz in np.arange(cur[2],0.34,0.02):
        qt,_=ik(q,np.array([cur[0],cur[1],zz]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
    qt,_=ik(q,np.array([x,y,0.34]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
    if not ok: print('move fail')
    stop=None
    for z in np.arange(0.32,0.22,-0.005):
        qt,_=ik(q,np.array([x,y,z]),down_R(0),base); obs,ok=goto(obs,qt); q=q_of(obs)
        if not ok: stop=z; break
    print(axis, round(d,3), stop)
print(time.time()-t)
env.close()
