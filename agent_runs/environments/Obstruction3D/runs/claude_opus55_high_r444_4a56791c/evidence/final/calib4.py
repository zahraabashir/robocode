import sys, json
from env_client import make_env
import numpy as np, kin
from common import *
GF=['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); bdy=float(sys.argv[3]); brot=float(sys.argv[4]); zs=float(sys.argv[5])
env = make_env()
obs, info = env.reset(seed=seed)
# move base
a=np.zeros(11,dtype=np.float32); a[1]=bdy; a[2]=brot; obs,*_=env.step(a)
b = objd(obs,'target_block')
base = getbase(obs)
data=[]
for dx in np.arange(-0.16,-0.019,0.02):
  for dy in np.arange(-0.06,0.061,0.02):
    for z in [0.35, zs]:
        qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,z]), kin.topdown_R(yaw))
        obs, blocked = move_to(env, obs, qt)
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,r,t,tr,info = env.step(a)
    R=robot(obs)
    if obs.get(R,'grasp_active'):
        bb=objd(obs,'target_block')
        data.append(dict(base=list(getbase(obs)), q=list(getq(obs)), g=[obs.get(R,f) for f in GF], obj=[bb[k] for k in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']], dxdy=[dx,dy]))
    a[10]=1; obs,*_=env.step(a)
    qt, ok = kin.ik(base, getq(obs), np.array([b['pose_x']+dx,b['pose_y']+dy,0.35]), kin.topdown_R(yaw)); obs,_=move_to(env,obs,qt)
print(len(data), [d['dxdy'] for d in data])
json.dump(data, open(f'calib_{seed}_{yaw}_{bdy}_{brot}_{zs}.json','w'))
