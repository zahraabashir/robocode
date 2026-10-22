from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name('robot')
F = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
def rs(o): return np.array([o.get(R,f) for f in F])
prev = rs(obs)
for k,a in enumerate([np.eye(11)[i]*0.1 for i in range(10)] + [np.eye(11)[i]*0.3 for i in range(10)]):
    a[10]=0
    obs,r,t,tr,info = env.step(a.astype(np.float32))
    cur = rs(obs); print(k, r, t, np.round(cur-prev,4)); prev=cur
a=np.zeros(11,dtype=np.float32); a[10]=-1
obs,r,t,tr,info = env.step(a); print('close', np.round(rs(obs),3))
a[10]=1
obs,r,t,tr,info = env.step(a); print('open', np.round(rs(obs),3))
