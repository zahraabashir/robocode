from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r0 = obs.get_object_from_name('rover0')
def p(o): return tuple(round(obs.get(o,f),4) for f in ['x','y','theta'])
# rover0 to the wall with fine steps
for i in range(200):
    obs,*_ = env.step(np.array([-0.01,0,0,0, 0,0,0,0],dtype=np.float32))
print('r0 min x at y=-1.75', p(r0))
# move up along wall, testing whether wall ends
xs=[]
for i in range(40):
    obs,*_ = env.step(np.array([0,0.1,0,0, 0,0,0,0],dtype=np.float32))
    # try to move left
    b=obs.get(r0,'x')
    obs,*_ = env.step(np.array([-0.05,0,0,0, 0,0,0,0],dtype=np.float32))
    xs.append((round(obs.get(r0,'y'),2), round(obs.get(r0,'x'),3)))
print(xs)
env.close()
