from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=1
obs, info = env.reset(seed=seed)
R = obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
bx,by,bz=[obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]
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
configs=[]
for z in [0.235,0.26,0.29]:
  for yaw in [0,np.pi/4,np.pi/2]:
    for off in [(0,0),(0.03,0),(0,0.035),(0.05,0),(0,0.05)]:
        configs.append((z,yaw,off))
for z,yaw,off in configs:
    obs,_=env.reset(seed=seed)
    qt,_=ik(q_of(obs),np.array([bx+off[0],by+off[1],0.32]),down_R(yaw),base); r1=goto(qt)
    qt,ok=ik(q_of(obs),np.array([bx+off[0],by+off[1],z]),down_R(yaw),base); r2=goto(qt)
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,*_=env.step(a)
    g=obs.get(R,'grasp_active')
    print(z,round(yaw,2),off,r1,r2,'grasp',g,obs.get(R,'finger_state'))
env.close()
