from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r = obs.get_object_from_name('robot')
F = ['pos_base_x','pos_base_y','pos_base_rot','joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7','finger_state','grasp_active']
def show(o): return [round(o.get(r,f),4) for f in F]
print(show(obs))
for a in [[0.1,0,0,0,0,0,0,0,0,0,0],[0,0.1,0,0,0,0,0,0,0,0,0],[0,0,0.1,0,0,0,0,0,0,0,0],[0,0,0,0.3,0.05,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,-1],[0,0,0,0,0,0,0,0,0,0,1]]:
    obs, rew, term, trunc, info = env.step(np.array(a,dtype=np.float32))
    print(a, rew, term, trunc, info, show(obs))
env.close()
