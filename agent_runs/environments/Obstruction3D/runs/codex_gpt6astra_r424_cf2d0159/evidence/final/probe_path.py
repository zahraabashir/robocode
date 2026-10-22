from env_client import make_env
from approach import GeneratedApproach,fk
import numpy as np
E=make_env();s,info=E.reset(seed=0);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info)
for k in range(20):
 a=p.get_action(s);r=s.get_object_from_name('robot');q=np.array([s.get(r,'joint_'+str(i)) for i in range(1,8)]);pos,rot=fk(q)
 print(k,p.phase,'model',np.round(pos+[s.get(r,'pos_base_x'),s.get(r,'pos_base_y'),0],3),'a',np.round(a,3),flush=True)
 s,_,_,_,_=E.step(a)
E.close()
