from env_client import make_env
import numpy as np
env=make_env(); obs,_=env.reset(seed=1)
T=lambda n: env.observation_space.get_type(n)
r1=[o for o in obs.get_objects(T('rover')) if o.name=='rover1'][0]
# sample1 at (-1.485,-1.367); rover1 at (-1,-1.75)
tx,ty=-1.485,-1.367+0.35
def step(a):
    global obs
    obs,r,te,tr,info=env.step(np.array(a,dtype=np.float32)); return obs
for _ in range(10):
    x,y=obs.get(r1,'x'),obs.get(r1,'y')
    dx=np.clip(tx-x,-.2,.2); dy=np.clip(ty-y,-.2,.2)
    step([0,0,0,1/6,dx,dy,0,1/6])
print(obs.get(r1,'x'),obs.get(r1,'y'))
# now move down 0.2 (dist goes 0.35->0.15) with sample op
step([0,0,0,1/6,0,-0.2,0,-5/6])
print('post-move sample attempt: store', obs.get(r1,'store_full'), obs.get(r1,'y'))
