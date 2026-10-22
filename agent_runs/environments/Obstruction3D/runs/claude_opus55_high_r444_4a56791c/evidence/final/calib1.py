import sys; YAW=float(sys.argv[1])
from env_client import make_env
import numpy as np, kin
from common import *
env = make_env()
obs, info = env.reset(seed=0)
b = objd(obs,'target_block'); print(b)
base = getbase(obs); q = getq(obs)
p = np.array([b['pose_x'], b['pose_y'], 0.40])
for z in np.arange(0.40, 0.0, -0.005):
    p[2]=z
    qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(YAW))
    obs, blocked = move_to(env, obs, qt)
    if blocked: print('blocked at', z); break
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,*_ = env.step(a)
    R=robot(obs)
    g=obs.get(R,'grasp_active'); fs=obs.get(R,'finger_state')
    if g or fs: print(round(z,3), 'grasp', g, fs, [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
    a[10]=1; obs,*_=env.step(a)
