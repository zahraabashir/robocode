from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=1)
def rb(o):
    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"]]
def st(a):
    global obs
    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); return t
for d,a in [("right",[0.01,0,0,0,0]),("up",[0,0.01,0,0,0])]:
    for i in range(200):
        y0=rb(obs); st(a)
        if rb(obs)==y0: print(d,"stopped",rb(obs)); break
env.close()
