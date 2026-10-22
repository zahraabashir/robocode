from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name('robot')
F = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
def rs(o): return np.round(np.array([o.get(R,f) for f in F]),3)
for g in [-1,-1,-1,0,1,1,1]:
    a=np.zeros(11,dtype=np.float32); a[10]=g
    obs,*_ = env.step(a); print(g, rs(obs)[-2:])
for dx in [-0.1,-0.1,0.05,0.05,0.05,0.05]:
    a=np.zeros(11,dtype=np.float32); a[0]=dx
    obs,*_ = env.step(a); print(dx, rs(obs)[:3])
