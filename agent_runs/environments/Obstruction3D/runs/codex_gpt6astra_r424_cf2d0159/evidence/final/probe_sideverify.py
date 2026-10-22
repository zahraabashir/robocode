from env_client import make_env
from probe_fk import fk
import numpy as np
q=np.array([0,.44754084944725037,-np.pi,-2.120941162109375,0,.009999980218708515,.6907963752746582]);base=np.array([-.4509332478046417,-.3362736999988556])
e=make_env();s,_=e.reset(seed=2,options={'object_count':0});ro=s.get_object_from_name('robot')
for k in range(70):
 a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.1,.1);a[3:10]=np.clip(q-[s.get(ro,'joint_'+str(j)) for j in range(1,8)],-.08,.08);a[-1]=1;s,*_=e.step(a)
a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
for t in e.observation_space.types:
 for o in s.get_objects(t):print(o.name,{f:s.get(o,f) for f in e.observation_space.type_features[t]},flush=True)
for k in range(5):
 a=np.zeros(11);a[0]=-.05;s,*_=e.step(a)
 print('LIFT',k,[(o.name,[s.get(o,'pose_'+v) for v in 'xyz'],s.get(o,'grasp_active')) for o in s.get_objects(e.observation_space.get_type('Kinematic3DCuboid'))],flush=True)
e.close()
