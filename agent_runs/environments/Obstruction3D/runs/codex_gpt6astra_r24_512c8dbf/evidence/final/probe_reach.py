from env_client import make_env
from kin import *
E=make_env()
for reach in [.4,.45,.5,.55]:
 s,_=E.reset(seed=1);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block');x,y,z=[s.get(b,'pose_'+f) for f in 'xyz'];fs=['joint_'+str(i) for i in range(1,8)]
 for zt in [.28]*15+list(np.arange(.28,.14,-.005)):
  q=ik(reach,zt);a=np.zeros(11);a[3:10]=np.clip(q-[s.get(r,f) for f in fs],-.1,.1);a[0]=np.clip(x-.12-reach-s.get(r,'pos_base_x'),-.1,.1);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.1,.1);a[10]=-1;s,*_=E.step(a)
  if s.get(r,'grasp_active'):print('GRASP',reach,zt,flush=True);break
 else:print('FAIL',reach,'q',[s.get(r,f) for f in fs],flush=True)
E.close()
