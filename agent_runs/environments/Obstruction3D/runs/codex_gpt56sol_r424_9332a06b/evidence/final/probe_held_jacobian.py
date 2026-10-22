from env_client import make_env
from approach import GeneratedApproach
import numpy as np
def xyz(s):
 o=s.get_object_from_name('target_block');return np.array([s.get(o,'pose_'+c) for c in 'xyz'])
e=make_env();s,i=e.reset(seed=11);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
for t in range(100):
 s,*_=e.step(p.get_action(s))
 if p.mode=='release':break
print('at',t,xyz(s))
for idx in [4,6,8]:
 for d in [.04,-.04]:
  old=xyz(s);a=np.zeros(11,np.float32);a[idx]=d;a[10]=-1;s,*_=e.step(a)
  print(idx,d,xyz(s)-old)
e.close()
