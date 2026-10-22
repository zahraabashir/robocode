# check gravity: grasp block, lift, release midair
from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=1)
R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
bs=lambda: tuple(round(float(obs.get(B,f)),3) for f in ['x','y'])
bx = obs.get(B,'x')+obs.get(B,'width')/2
for i in range(40):
    obs,*_ = env.step(np.array([np.clip(bx-obs.get(R,'x'),-.05,.05),0,0,0,0],dtype=np.float32))
top=obs.get(B,'y')+obs.get(B,'height')
while obs.get(R,'y')-0.11-top>0.004:
    obs,*_ = env.step(np.array([0,-min(.05,obs.get(R,'y')-0.11-top-0.003),0,0,0],dtype=np.float32))
print(obs.get(R,'y')-0.11-top)
obs,*_ = env.step(np.array([0,0,0,0,1],dtype=np.float32))
for i in range(4): obs,*_ = env.step(np.array([0,0.05,0,0,1],dtype=np.float32))
print(bs())
for i in range(4): obs,*_ = env.step(np.array([0,0.05,0,0,0],dtype=np.float32)); print(bs())
