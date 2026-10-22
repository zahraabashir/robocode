import numpy as np
from env_client import make_env
env = make_env()
obs, info = env.reset(seed=0)
def st(o):
    r=o.get_object_from_name('robot')
    return [round(float(o.get(r,k)),4) for k in ['pos_base_x','pos_base_y','pos_base_rot']], [round(float(o.get(r,f'joint_{i}')),3) for i in range(1,8)]
print(st(obs))
print(obs.get_object_names())
for n in obs.get_object_names():
    o=obs.get_object_from_name(n)
    try: print(n,[round(float(obs.get(o,k)),3) for k in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
    except Exception as e: pass
def A(**kw):
    a=np.zeros(11,dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])]=v
    return a
o,*_=env.step(A(a0=-0.2)); print('dx-0.2',st(o))
o,*_=env.step(A(a0=0.3)); print('dx+0.3',st(o))
o,*_=env.step(A(a2=0.2)); print('rot',st(o))
for i in range(7): o,*_=env.step(A(a2=0.2))
print('rot total',st(o))
o,*_=env.step(A(a0=-0.1)); print('dx-0.1 after rot',st(o))
o,*_=env.step(A(a1=-0.1)); print('dy-0.1 after rot',st(o))
# combined
p=st(o)
o,*_=env.step(A(a1=0.1,a3=0.1)); print('combined',p,'->',st(o))
env.close()
