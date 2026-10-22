import numpy as np
from env_client import make_env
from approach import ik,fk
E=make_env()
def vals(s,r):return np.array([s.get(r,'joint_'+str(i)) for i in range(1,8)])
for seed in [2,0,5]:
 for yaw in [0,np.pi,-np.pi/2,np.pi/2]:
  s,_=E.reset(seed=seed,options={'object_count':0});r=s.get_object_from_name('robot');o=s.get_object_from_name('target_block');p=np.array([s.get(o,'pose_'+a) for a in 'xyz'])
  def move(q,b=None):
   global s
   for _ in range(70):
    a=np.zeros(11);a[3:10]=q-vals(s,r)
    if b is not None:a[:2]=b-np.array([s.get(r,'pos_base_'+v) for v in ['x','y']])
    m=max(abs(a[:10]));
    if m<1e-5:break
    a[:10]*=min(1,.1/m);ss,*_=E.step(a)
    if np.max(abs(vals(ss,r)-vals(s,r)))<1e-6 and b is None: s=ss;break
    s=ss
  q=ik(.5,.3);q[6]=yaw;move(q);move(q,p[:2]-[.5,.001])
  for z in np.arange(.3,.069,-.005):
   q=ik(.5,z);q[6]=yaw;move(q)
   a=np.zeros(11);a[10]=-1;s,*_=E.step(a)
   if s.get(r,'grasp_active'):
    print('SUCCESS',seed,yaw,z,'p',p,'q',vals(s,r),'base',[s.get(r,'pos_base_'+v) for v in ['x','y']],'tf',[s.get(r,'grasp_tf_'+v) for v in ['x','y','z','qx','qy','qz','qw']],flush=True);E.close();quit()
  print('FAIL',seed,yaw,'tip',fk(vals(s,r))[0],flush=True)
E.close()
