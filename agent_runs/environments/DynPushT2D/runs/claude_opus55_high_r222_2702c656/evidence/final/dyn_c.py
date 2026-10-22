import numpy as np
from env_client import make_env
np.set_printoptions(precision=4,suppress=True)
env=make_env()
obs,_=env.reset(seed=1)
maxv=0;rews=set()
# push left (-x) from right side off-center (offset +0.3 in y) then continue to wall
b=obs[0:3].copy()
def goto(obs,tx,ty):
    global maxv
    while np.linalg.norm(obs[16:18]-[tx,ty])>1e-4:
        obs,r,te,tr,info=env.step(np.clip(np.array([tx,ty])-obs[16:18],-0.0499,0.0499)); rews.add(r)
        maxv=max(maxv,np.abs(obs[3:6]).max())
    return obs
obs=goto(obs,1.5,0.4); obs=goto(obs,4.8,0.4); obs=goto(obs,4.8,b[1]+0.3)
print("start",obs[0:3],obs[16:18])
t=0
for t in range(120):
    obs,r,te,tr,info=env.step(np.array([-0.0499,0])); rews.add(r)
    maxv=max(maxv,np.abs(obs[3:6]).max())
    if t%8==0: print(t,obs[0:3],"robot",obs[16:18])
print("maxv",maxv,"rews",rews)
n=env_steps=0
steps=0
obs,_=env.reset(seed=3)
for i in range(1100):
    obs,r,te,tr,info=env.step(np.array([0.01*np.sin(i/20),0.0]))
    if te or tr: print("done at",i+1,te,tr,r,info); break
else: print("no termination in 1100")
