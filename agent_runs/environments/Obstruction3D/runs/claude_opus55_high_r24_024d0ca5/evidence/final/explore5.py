from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
obs, info = env.reset(seed=1)
R = obs.get_object_from_name('robot')
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
x,y=float(sys.argv[1]),float(sys.argv[2])
def goto(qt):
    global obs
    for _ in range(40):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-4: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q): 
            print('blocked; q',np.round(q,3),'d',np.round(d,3)); return False
    return False
for z in np.arange(0.35,0.0,-0.005):
    qt,ok=ik(q_of(obs),np.array([x,y,z]),down_R(0),base)
    if not goto(qt): print('blocked at',z); break
# try single joint moves
q0=q_of(obs)
for j in range(7):
    for s in [0.02,-0.02]:
        a=np.zeros(11,dtype=np.float32); a[3+j]=s
        o2,*_=env.step(a)
        moved=not np.allclose(q_of(o2),q_of(obs))
        print(j,s,moved, 'eez', round(fk(q_of(o2),base)[2,3],4))
        obs=o2
        if moved:
            a[3+j]=-s; obs,*_=env.step(a)
env.close()
