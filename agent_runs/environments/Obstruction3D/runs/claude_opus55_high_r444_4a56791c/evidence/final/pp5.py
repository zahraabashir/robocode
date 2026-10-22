import sys
from env_client import make_env
import numpy as np, kin
from common import *
seed=int(sys.argv[1]); name=sys.argv[2]
env = make_env()
obs, info = env.reset(seed=seed)
base = getbase(obs)
def goto(p, yaw=0, grip=0):
    global obs
    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
    obs, bl = move_to(env, obs, qt, grip); return bl, ok
o=objd(obs,name); R=robot(obs); print(o)
for yaw in [0]:
  for dz in list(np.arange(0.024,0.034,0.002))+list(np.arange(0.044,0.056,0.002)):
    goto([o['pose_x'],o['pose_y'],0.26],yaw); bl,ok=goto([o['pose_x'],o['pose_y'],o['pose_z']+dz],yaw)
    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
    print(round(yaw,2), round(dz,3), bl, ok, obs.get(R,'grasp_active'), round(obs.get(R,'finger_state'),3))
    a[10]=1; obs,*_=env.step(a)
