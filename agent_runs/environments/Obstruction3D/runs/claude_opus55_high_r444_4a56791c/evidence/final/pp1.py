import sys
from env_client import make_env
import numpy as np, kin
from common import *
seed=int(sys.argv[1])
env = make_env()
obs, info = env.reset(seed=seed)
base = getbase(obs)
def goto(p, yaw=0, grip=0):
    global obs
    qt, ok = kin.ik(base, getq(obs), np.array(p), kin.topdown_R(yaw))
    obs, bl = move_to(env, obs, qt, grip); return bl, ok
def pr(tag):
    b=objd(obs,'target_block'); R=robot(obs)
    print(tag, 'block', np.round([b['pose_x'],b['pose_y'],b['pose_z']],4), 'q', np.round([b['pose_qx'],b['pose_qy'],b['pose_qz'],b['pose_qw']],3), 'grasp', obs.get(R,'grasp_active'), 'fs', round(obs.get(R,'finger_state'),3))
for n in obs.get_object_names():
    if n!='robot': d=objd(obs,n); print(n, np.round([d['pose_x'],d['pose_y'],d['pose_z'],d['half_extent_x'],d['half_extent_y'],d['half_extent_z']],3), np.round([d['pose_qz'],d['pose_qw']],3))
b=objd(obs,'target_block'); r=objd(obs,'target_region')
print(goto([b['pose_x'],b['pose_y'],0.25]))
print(goto([b['pose_x'],b['pose_y'],b['pose_z']]))
pr('at')
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); pr('closed')
print(goto([b['pose_x'],b['pose_y'],0.25]))
pr('lifted')
a=np.zeros(11,dtype=np.float32); a[10]=1; obs,rew,term,*_=env.step(a); pr('released in air')
for i in range(3):
    obs,rew,term,*_=env.step(np.zeros(11,dtype=np.float32)); pr('after')
