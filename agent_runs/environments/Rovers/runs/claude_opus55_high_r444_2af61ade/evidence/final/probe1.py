from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r0 = obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
def p(o): return tuple(round(obs.get(o,f),3) for f in ['x','y','theta','store_full','calibrated','at_home'])
# move rover0 -x, rover1 nothing
for i in range(8):
    obs,r,te,tr,inf = env.step(np.array([-0.2,0,0,0, 0,0,0,0],dtype=np.float32))
    print(i,p(r0),p(r1),r,te,tr)
# try bigger than limits
obs,r,te,tr,inf = env.step(np.array([0,0.5,0,0, 0,0,0,0],dtype=np.float32)); print('big',p(r0))
obs,r,te,tr,inf = env.step(np.array([0,0,0.4,0, 0,0,0,0],dtype=np.float32)); print('rot',p(r0))
# move rover1 +y up the left side
for i in range(25):
    obs,r,te,tr,inf = env.step(np.array([0,0,0,0, 0,0.2,0,0],dtype=np.float32))
print('r1 after up',p(r1))
env.close()
