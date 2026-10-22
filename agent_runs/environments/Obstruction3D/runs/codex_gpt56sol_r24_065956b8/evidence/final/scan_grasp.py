from env_client import make_env
import numpy as np

def v(s,n,f): return float(s.get(s.get_object_from_name(n),f))
e=make_env();s,_=e.reset(seed=0)
tx=v(s,'target_block','pose_x');ty=v(s,'target_block','pose_y')
print('target',tx,ty,v(s,'target_block','pose_z'))
for bx in [-.12,-.22,-.32,-.42,-.52,-.62]:
 for yo in [0,-.04,.04]:
  # absolute positioning by observed robot state
  for grip in [1,-1]:
   r=s.get_object_from_name('robot');cx=float(s.get(r,'pos_base_x'));cy=float(s.get(r,'pos_base_y'))
   a=np.zeros(11,np.float32);a[0]=np.clip(bx-cx,-.2,.2);a[1]=np.clip(ty+yo-cy,-.2,.2);a[10]=grip
   s,re,te,tr,info=e.step(a)
  print(bx,yo,'robot',v(s,'robot','pos_base_x'),v(s,'robot','pos_base_y'),'grasp',v(s,'robot','grasp_active'),v(s,'target_block','grasp_active'),[v(s,'robot',f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
  if v(s,'robot','grasp_active')>0: raise SystemExit
e.close()
