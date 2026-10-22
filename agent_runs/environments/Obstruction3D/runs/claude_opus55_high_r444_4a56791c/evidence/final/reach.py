import numpy as np, kin
from env_client import make_env
from common import *
env=make_env(); obs,_=env.reset(seed=312, options={'object_count':15}); b=getbase(obs); q0=getq(obs)
print('base', b)
JL=np.array([np.inf,2.41,np.inf,2.66,np.inf,2.23,np.inf])-0.02
mount=b[:2]+0.12*np.array([np.cos(b[2]),np.sin(b[2])]); print('mount', mount)
for ang in [0, 0.8, 1.57, -1.57, 2.5]:
  res=[]
  for r in np.arange(0.0,0.2,0.01):
    p=np.array([mount[0]+r*np.cos(ang), mount[1]+r*np.sin(ang), 0.15])
    ok=False
    for yaw in [0,np.pi/2,np.pi/4,-np.pi/4]:
      for t in range(4):
        qs=q0+np.random.uniform(-1,1,7)*(t>0)
        q,o=kin.ik(b,qs,p,kin.topdown_R(yaw),iters=200,tol=1e-5,lim=JL)
        if o: ok=True;break
      if ok: break
    res.append(ok)
  print(ang, ''.join('1' if x else '0' for x in res))
print('per yaw, angle 0 and 0.8, z .14')
for ang in [0,0.8,-0.8]:
 for yaw in np.arange(0,np.pi,np.pi/8):
  res=[]
  for r in np.arange(0.10,0.17,0.005):
    p=np.array([r*np.cos(ang), r*np.sin(ang), 0.14]); ok=False
    for t in range(4):
        qs=q0+np.random.uniform(-1,1,7)*(t>0)
        q,o=kin.ik(b,qs,p,kin.topdown_R(yaw),iters=200,tol=1e-5,lim=JL)
        if o: ok=True;break
    res.append(ok)
  print(ang, round(yaw,2), ''.join('1' if x else '0' for x in res))
