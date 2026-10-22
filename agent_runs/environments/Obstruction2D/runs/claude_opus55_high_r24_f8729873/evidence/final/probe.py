from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=1)
R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
def bs(o): return tuple(round(float(o.get(B,f)),3) for f in ['x','y','theta'])
bx = obs.get(B,'x')+obs.get(B,'width')/2
# move to x above block center
for i in range(40):
    dx = np.clip(bx-obs.get(R,'x'),-0.05,0.05)
    obs,r,t,tr,_ = env.step(np.array([dx,0,0,0,0],dtype=np.float32))
print(rs(obs), bs(obs))
# go down
for i in range(30):
    prev = rs(obs)
    obs,r,t,tr,_ = env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
    print('down', rs(obs))
    if rs(obs)==prev: break
for i in range(5):
    obs,r,t,tr,_ = env.step(np.array([0,0,0,0.1,0],dtype=np.float32))
    print('ext', rs(obs))
for i in range(3):
    obs,r,t,tr,_ = env.step(np.array([0,0,0,0.0,1],dtype=np.float32))
    print('vac', rs(obs), bs(obs))
for i in range(4):
    obs,r,t,tr,_ = env.step(np.array([0,0.05,0,0.0,1],dtype=np.float32))
    print('up', rs(obs), bs(obs))
