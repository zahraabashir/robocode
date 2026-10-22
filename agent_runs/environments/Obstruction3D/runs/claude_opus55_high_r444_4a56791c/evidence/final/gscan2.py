import sys
from env_client import make_env
import numpy as np, kin
from common import *
yaw=float(sys.argv[1]); name=sys.argv[2]; seed=int(sys.argv[3])
env = make_env()
obs, info = env.reset(seed=seed)
base = getbase(obs)
def goto(p):
    global obs
    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
    obs, bl = move_to(env, obs, qt); return bl
o=objd(obs,name); R=robot(obs)
d=np.array([-np.sin(yaw),np.cos(yaw)]); a=np.array([np.cos(yaw),np.sin(yaw)])
bottom=o['pose_z']-o['half_extent_z']
out=[]
for sa in np.arange(-0.024,0.025,0.004):
    x,y=np.array([o['pose_x'],o['pose_y']])+sa*a
    goto([x,y,0.24]); bl=goto([x,y,bottom+0.046])
    act=np.zeros(11,dtype=np.float32); act[10]=-1; obs,*_=env.step(act)
    g=obs.get(R,'grasp_active'); out.append((round(sa,3), round(y,3), 'B' if bl else ('G' if g else '.')))
    act[10]=1; obs,*_=env.step(act)
print(out)
