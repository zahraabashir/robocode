from env_client import make_env
import numpy as np
for feature,index,d in [('x',0,-.05),('x',0,.05),('y',1,.05)]:
 e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot')
 for delta in [d,d/10,d/100,d/1000]:
  for j in range(40):
   a=np.zeros(5,dtype=np.float32);a[index]=delta;s,*_=e.step(a)
 print('base bound',feature,d,s.get(r,feature));e.close()
for dy in [-.05,-.01]:
 e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
 x=s.get(b,'x')+s.get(b,'width')/2
 for j in range(10):s,*_=e.step(np.array([np.clip(x-s.get(r,'x'),-.05,.05),0,0,.1,0],dtype=np.float32))
 for j in range(100):s,*_=e.step(np.array([0,dy,0,0,1],dtype=np.float32))
 by=s.get(b,'y');ry=s.get(r,'y');s,*_=e.step(np.array([0,.05,0,0,1],dtype=np.float32))
 print('descend',dy,'stopped',ry,'target_top',by+s.get(b,'height'),'grasp_dy',s.get(b,'y')-by);e.close()
