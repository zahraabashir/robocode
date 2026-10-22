from env_client import make_env
from approach import ik,fk
import numpy as np
E=make_env();s,info=E.reset(seed=2,options={'object_count':0});print(info)
r=s.get_object_from_name('robot')
for t in E.observation_space.types:
 for o in s.get_objects(t):print(o.name,{f:s.get(o,f) for f in E.observation_space.type_features[t]})
for v in [-1,1,-1,1]:
 a=np.zeros(11);a[10]=v;s,*_=E.step(a);print(v,[(f,s.get(r,f)) for f in ['finger_state','grasp_active']])
E.close()
