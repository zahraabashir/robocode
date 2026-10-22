from env_client import make_env
import numpy as np

e=make_env()
for j in [4,6,8]:
 for delta in [-.2,.2]:
  s,_=e.reset(seed=0);a=np.zeros(11,dtype=np.float32);a[0]=-.2
  for _ in range(5):s=e.step(a)[0]
  r=s.get_object_from_name('robot');f='joint_'+str(j-2)
  for k in range(35):
   old=s.get(r,f);a=np.zeros(11,dtype=np.float32);a[j]=delta;s=e.step(a)[0];new=s.get(r,f)
   if old==new:break
  print('LIMIT',j,delta,k,new,flush=True)
e.close()
