from env_client import make_env
import numpy as np, kin
from common import *
env = make_env()
obs, info = env.reset(seed=0)
b = objd(obs,'target_block')
base = getbase(obs)
hits=[]
for dx in np.arange(-0.08,0.081,0.02):
  for dy in np.arange(-0.08,0.081,0.02):
    for z in [0.33, 0.25]:
        qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,z]), kin.topdown_R(0))
        obs, blocked = move_to(env, obs, qt)
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,r,t,tr,info = env.step(a)
    R=robot(obs)
    if obs.get(R,'grasp_active') or obs.get(R,'finger_state'):
        hits.append((dx,dy)); print('HIT',round(dx,2),round(dy,2),blocked,[round(obs.get(R,f),4) for f in ['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']], objd(obs,'target_block')['pose_z'])
    a[10]=1; obs,*_=env.step(a)
    qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,0.33]), kin.topdown_R(0)); obs,_=move_to(env,obs,qt)
print(hits, tr)
