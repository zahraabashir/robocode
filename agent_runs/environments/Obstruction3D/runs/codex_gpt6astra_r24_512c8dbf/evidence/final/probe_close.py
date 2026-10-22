from env_client import make_env
from kin import *
E=make_env();s,_=E.reset(seed=1);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
print('block',[s.get(b,'pose_'+f) for f in 'xyz'])
for i in range(20):
 a=np.zeros(11);a[10]=1 if i%2==0 else -1;s,rew,te,tr,inf=E.step(a)
 print(i,inf, s.get(r,'finger_state'),s.get(r,'grasp_active'))
E.close()
