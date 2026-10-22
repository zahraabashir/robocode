from env_client import make_env
import numpy as np
import time
E=make_env();s,_=E.reset(seed=0)
robot=s.get_object_from_name('robot')
print('robot', {f:float(s.get(robot,f)) for f in ['pos_base_x','pos_base_y','grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True)
start=time.time()
for x in np.arange(-.4,.61,.1):
 for y in np.arange(-.4,.61,.1):
  s,_=E.reset(seed=0)
  for k in range(10):
   a=np.zeros(11,dtype=np.float32)
   a[:2]=np.clip([x-s.get(robot,'pos_base_x'),y-s.get(robot,'pos_base_y')],-.2,.2)
   if np.linalg.norm(a[:2])<1e-5:break
   s,*_=E.step(a)
  a=np.zeros(11,dtype=np.float32);a[-1]=-1;s,r,d,tr,i=E.step(a)
  if s.get(robot,'grasp_active'):
   print('GRASP',x,y,{f:float(s.get(robot,f)) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True)
 print('row',x,'elapsed',time.time()-start,flush=True)
E.close()
