import sys, json
from env_client import make_env
import numpy as np, kin
from common import *
dx=float(sys.argv[1]); dzt=float(sys.argv[2]); YAW=float(sys.argv[3])
env = make_env()
obs, info = env.reset(seed=0)
base = getbase(obs)
def goto(p, yaw=None):
    yaw = YAW if yaw is None else yaw
    global obs
    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
    obs, bl = move_to(env, obs, qt); return bl
o=objd(obs,'target_block')
top=o['pose_z']+o['half_extent_z']
res=[]
for dy in np.arange(-0.10,0.1001,0.01):
    goto([o['pose_x']+dx,o['pose_y']+dy,0.26]); bl=goto([o['pose_x']+dx,o['pose_y']+dy,top+dzt])
    res.append('X' if bl else '.')
print(f"{dx:+.2f}", ''.join(res))
