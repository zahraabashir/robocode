from env_client import make_env
import numpy as np

e=make_env()
for j in [0,1,2,3,4,5,6,7,8,9,10]:
 for direction in [-1,1]:
  s,_=e.reset(seed=0); rob=s.get_object_from_name('robot');a=np.zeros(11,dtype=np.float32);a[j]=direction*(.2 if j<10 else 1)
  for k in range(8):
   t,r,d,tr,i=e.step(a)
   fields=['pos_base_x','pos_base_y','pos_base_rot']+['joint_'+str(n) for n in range(1,8)]+['finger_state','grasp_active']
   changes={f:round(float(t.get(rob,f)),5) for f in fields if abs(s.get(rob,f)-t.get(rob,f))>1e-7}
   print(j,direction,k,changes,flush=True);s=t
   if not changes: break
e.close()
