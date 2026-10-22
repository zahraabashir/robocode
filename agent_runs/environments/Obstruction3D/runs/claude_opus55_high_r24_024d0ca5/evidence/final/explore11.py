from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=1
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
def goto(qt):
    global obs
    for _ in range(60):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-5: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
yaw=float(sys.argv[1]); y=float(sys.argv[2])
for x in np.arange(0.36,0.62,0.02):
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
    base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
    qt,ok=ik(q_of(obs),np.array([x,y,0.32]),down_R(yaw),base); goto(qt)
    z=0.32
    while z>0.0:
        qt,ok=ik(q_of(obs),np.array([x,y,z-0.004]),down_R(yaw),base)
        if not ok: print('ikfail'); break
        if not goto(qt): break
        z-=0.004
    print(round(x,3),'lowest',round(z,3))
env.close()
