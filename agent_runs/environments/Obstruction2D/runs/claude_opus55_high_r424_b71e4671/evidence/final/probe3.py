from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=21)
r = obs.get_object_from_name('robot')
for d in [0.001,-0.001]:
    prev=None
    for i in range(2000):
        obs,*_=env.step(np.array([d*50 if i<1 else d,0,0,0,0],dtype=np.float32)) if False else env.step(np.array([d,0,0,0,0],dtype=np.float32))
        x=float(obs.get(r,'x'))
        if prev is not None and x==prev: break
        prev=x
    print("limit",d,x)
prev=None
for i in range(2000):
    obs,*_=env.step(np.array([0,0.002,0,0,0],dtype=np.float32)); y=float(obs.get(r,'y'))
    if prev is not None and y==prev: break
    prev=y
print("ymax",y)
env.close()
