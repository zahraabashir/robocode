from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
def rb(o):
    r=o.get_object_from_name('robot'); return [round(float(o.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"]]
def blk(o,n='target_block'):
    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),4) for f in ["x","y","theta"]]
def st(a):
    global obs
    obs,r,t,tr,_=env.step(np.array(a,dtype=np.float32)); return t
# go to x=0.489
while abs(rb(obs)[0]-0.489)>1e-4:
    d=np.clip(0.489-rb(obs)[0],-0.05,0.05); st([d,0,0,0,0])
print(rb(obs))
for i in range(80):
    y0=rb(obs)[1]; st([0,-0.01,0,0,0])
    if abs(rb(obs)[1]-y0)<1e-6: print("stopped at",rb(obs)); break
print(rb(obs), blk(obs))
st([0,0,0,0,1]); print("vac", rb(obs), blk(obs))
for i in range(5): st([0,0.05,0,0,1])
print("lift", rb(obs), blk(obs))
st([0.05,0,0.1,0.1,1]); print("move", rb(obs), blk(obs))
st([0,0,0,0,0]); print("release", rb(obs), blk(obs))
for i in range(3): st([0,0,0,0,0])
print("after", rb(obs), blk(obs))
env.close()
