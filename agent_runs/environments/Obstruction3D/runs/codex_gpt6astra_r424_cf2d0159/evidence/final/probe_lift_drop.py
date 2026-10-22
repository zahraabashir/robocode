from env_client import make_env
from probe_fk import fk
import numpy as np
q=np.array([0,.44754084944725037,-np.pi,-2.120941162109375,0,.009999980218708515,.6907963752746582]);base=np.array([-.4509332478046417,-.3362736999988556])
e=make_env();s,_=e.reset(seed=2,options={'object_count':0});ro=s.get_object_from_name('robot')
for k in range(70):
 a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.1,.1);a[3:10]=np.clip(q-[s.get(ro,'joint_'+str(j)) for j in range(1,8)],-.08,.08);a[-1]=1;s,*_=e.step(a)
a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
ob=s.get_object_from_name('target_block');reg=s.get_object_from_name('target_region')
for k in range(10):
 a=np.zeros(11);a[4]=-.02;a[8]=.02;s,*_=e.step(a)
 print('LIFT',k,[s.get(ob,'pose_'+v) for v in 'xyz'],flush=True)
for k in range(10):
 a=np.zeros(11);a[:2]=np.clip([s.get(reg,'pose_'+v)-s.get(ob,'pose_'+v) for v in 'xy'],-.1,.1);s,*_=e.step(a)
 print('MOVE',k,[s.get(ob,'pose_'+v) for v in 'xyz'],flush=True)
a=np.zeros(11);a[-1]=1;s,r,t,tr,i=e.step(a);print('RELEASE',r,t,tr,i,[s.get(ob,'pose_'+v) for v in 'xyz'],flush=True)
for k in range(3):
 s,r,t,tr,i=e.step(np.zeros(11));print('POST',r,t,tr,i,[s.get(ob,'pose_'+v) for v in 'xyz'],flush=True)
e.close()
