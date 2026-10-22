from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r = obs.get_object_from_name('robot'); b=obs.get_object_from_name('target_block')
def g(o,f,s=None): return float((s or obs).get(o,f))
def step(a):
    global obs
    a=np.clip(np.array(a,dtype=np.float32),env.action_space.low,env.action_space.high)
    obs,rew,te,tr,_=env.step(a); return te
# go to x=0.489
while abs(g(r,'x')-0.489)>1e-4:
    step([np.clip(0.489-g(r,'x'),-.05,.05),0,0,0,0])
step([0,0,0,0.1,0])
prev=None
for i in range(200):
    step([0,-0.01,0,0,0])
    y=g(r,'y')
    if prev is not None and abs(prev-y)<1e-6: break
    prev=y
print("stopped robot y", g(r,'y'), "arm", g(r,'arm_joint'), "block top", g(b,'y')+g(b,'height'))
# vacuum on, lift
step([0,0,0,0,1]); 
for i in range(5): step([0,0.05,0,0,1])
print("block after lift", g(b,'x'), g(b,'y'), "robot", g(r,'x'),g(r,'y'),g(r,'vacuum'))
env.close()
