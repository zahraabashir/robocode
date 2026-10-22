from env_client import make_env
from approach import ik, fk, down_R
import numpy as np, sys
seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
env = make_env()
def q_of(o,R): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, R, qt, maxn=40):
    for _ in range(maxn):
        q = q_of(obs,R); d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
        obs2, *_ = env.step(a)
        if np.allclose(q_of(obs2,R), q): return obs2, False
        obs = obs2
    return obs, True
for dtip in [float(v) for v in sys.argv[4].split(",")]:
  for dx in [0.0]:
    obs, info = env.reset(seed=seed)
    R = obs.get_object_from_name("robot"); B = obs.get_object_from_name(name)
    bx, by, bz = obs.get(B,'pose_x'), obs.get(B,'pose_y'), obs.get(B,'pose_z')
    q=q_of(obs,R)
    for z in [0.36, bz+0.155+dtip]:
        qt,e = ik(q, np.array([bx+dx,by,z]), down_R(yaw)); obs,ok=goto(obs,R,qt); q=q_of(obs,R)
    a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
    print(dtip, dx, "reached", ok, "grasp", obs.get(R,'grasp_active'), "finger", round(obs.get(R,'finger_state'),3), np.round(obs.data[R][12:15],4))
env.close()
