from env_client import make_env
from kin import *
E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
fs=['joint_'+str(i) for i in range(1,8)]
def vec(s):return np.array([s.get(r,f) for f in fs])
x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
n=0
for angle in [np.pi/2,0]:
 for dx in [0,-.03,.03,-.06,.06]:
  for zt in np.arange(.25,.09,-.01):
   for dy in [0,-.02,.02,-.04,.04]:
    q=ik(x+.12+dx,zt);q[-1]=angle
    for j in range(20):
     a=np.zeros(11);a[3:10]=np.clip(q-vec(s),-.1,.1);a[1]=np.clip(y+dy-.001-s.get(r,'pos_base_y'),-.1,.1);a[10]=-1
     old=s;s,*_=E.step(a);n+=1
     if s.get(r,'grasp_active'):
      print('GRASP',dx,dy,zt,angle,'q',vec(s),'base',s.get(r,'pos_base_y'),'tf',[s.get(r,'grasp_tf_'+f) for f in ['x','y','z','qx','qy','qz','qw']],flush=True);E.close();raise SystemExit
     if np.max(np.abs(a[:10]))<1e-6 or np.linalg.norm(vec(s)-vec(old))<1e-7:break
   if n>900:
    s,_=E.reset(seed=0);n=0
  print('completed',angle,dx,flush=True)
E.close()
