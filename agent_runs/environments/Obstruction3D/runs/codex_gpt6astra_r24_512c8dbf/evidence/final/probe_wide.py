from env_client import make_env
from kin import *
from itertools import product
fields=['joint_'+str(i) for i in range(1,8)]
found=False
for dx,dy in product([0,-.06,.06,-.12,.12],[0,-.06,.06,-.12,.12]):
 E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
 x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
 def vec(s):return np.array([s.get(r,f) for f in fields])
 q=ik(x+.12+dx,.30); by=y+dy-fk(q)[0][1]
 for k in range(12):
  a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.15,.15);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.15,.15);s,*_=E.step(a)
 for zt in np.arange(.3,.09,-.005):
  q=ik(x+.12+dx,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.18,.18);a[10]=-1
  old=s;s,*_=E.step(a)
  if s.get(r,'grasp_active'):
   print('GRASP',dx,dy,zt,vec(s),{f:s.get(r,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']},flush=True);found=True;break
  if np.linalg.norm(vec(s)-vec(old))<1e-7 and zt<.29:break
 print('END',dx,dy,round(zt,4),'fk',fk(vec(s))[0].round(4).tolist(),'basey',s.get(r,'pos_base_y'),flush=True)
 E.close()
 if found:break
