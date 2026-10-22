# descend EE over free table spot, find where motion gets blocked
from env_client import make_env
import numpy as np
from kin import fk, ik, down_R
env = make_env()
obs, info = env.reset(seed=1)
R = obs.get_object_from_name('robot')
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
base=(o:=obs, o.get(R,'pos_base_x'), o.get(R,'pos_base_y'), o.get(R,'pos_base_rot'))[1:]
q=q_of(obs)
print('start ee', fk(q,base)[:3,3])
x,y=0.25,-0.3
def goto(qt):
    global obs
    for _ in range(40):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-4: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q): return False
    return False
for z in np.arange(0.35,-0.1,-0.01):
    qt,ok=ik(q_of(obs),np.array([x,y,z]),down_R(0),base)
    moved=goto(qt)
    ee=fk(q_of(obs),base)[:3,3]
    print(round(z,3),ok,moved,np.round(ee,3))
    if not moved: break
env.close()
