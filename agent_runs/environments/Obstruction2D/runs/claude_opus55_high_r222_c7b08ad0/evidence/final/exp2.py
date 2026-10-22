from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
def bs(o): return tuple(round(float(o.get(B,f)),3) for f in ['x','y','theta'])
def st(a):
    global obs
    obs,r,t,tr,_ = env.step(np.array(a,dtype=np.float32)); return r,t
# extend arm
for i in range(3): st([0,0,0,0.1,0]); print('arm',rs(obs))
for i in range(60): st([-0.05,0,0,0,0])
print('left', rs(obs))
for i in range(60): st([0.05,0,0,0,0])
print('right', rs(obs))
for i in range(10): st([0,0.05,0,0,0])
print('up', rs(obs))
# go grasp block with arm extended
tx=0.489
for i in range(40): st([np.clip(tx-obs.get(R,'x'),-.05,.05),0,0,0,0])
for i in range(80):
    st([0,-0.01,0,0,0])
print('down',rs(obs))
st([0,0,0,0,1]); 
for i in range(4): st([0,0.05,0,0,1])
print('lift',rs(obs),bs(obs))
st([0,0,0,0,0]); print('release', bs(obs))
st([0,0,0,0,0]); print('release', bs(obs))
env.close()
