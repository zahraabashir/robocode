from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
def rb(o):
    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),3) for f in ["x","y","theta","arm_joint","vacuum"]]
def blk(o,n='target_block'):
    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),3) for f in ["x","y","theta"]]
print(rb(obs))
for a in [[0.05,0,0,0,0],[0,-0.05,0,0,0],[0,0,0.196,0,0],[0,0,-0.196,0,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0,-0.1,0]]:
    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); print(a, rb(obs), r,t,tr)
# move down until stop
for i in range(20):
    obs,r,t,tr,_=env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
print("after down", rb(obs))
for i in range(20):
    obs,r,t,tr,_=env.step(np.array([-0.05,0,0,0,0],dtype=np.float32))
print("after left", rb(obs))
env.close()
