from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name('robot')
feats = ['pos_base_x','pos_base_y','pos_base_rot']+[f'joint_{i}' for i in range(1,8)]+['finger_state','grasp_active']
def rs(o): return np.array([o.get(R,f) for f in feats])
prev = rs(obs)
tests = [np.eye(11)[i]*0.1 for i in range(10)] + [np.eye(11)[i]*-0.1 for i in range(10)]
a = np.zeros(11); a[10]=-1; tests.append(a)
a = np.zeros(11); a[10]=1; tests.append(a)
a = np.zeros(11); a[3]=0.5; tests.append(a)
for a in tests:
    obs, r, term, trunc, info = env.step(a.astype(np.float32))
    cur = rs(obs)
    print(np.round(a,2).tolist(), 'd=', np.round(cur-prev,3).tolist(), r, term, trunc)
    prev = cur
env.close()
