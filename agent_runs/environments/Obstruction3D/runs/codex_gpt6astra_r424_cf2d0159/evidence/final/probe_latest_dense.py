from env_client import make_env
from approach import GeneratedApproach
from kinematics_fit import fk
import numpy as np,time
E=make_env();s,inf=E.reset(seed=2,options={'object_count':5});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,inf);start=time.time();last=None
for t in range(400):
 a=p.get_action(s);s,r,term,tr,_=E.step(a);ro=s.get_object_from_name('robot');key=(p.goal,p.phase)
 if key!=last or t%30==0:
  print(t,key,'height',p.height,'held',s.get(ro,'grasp_active'),'ee',fk(np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]))[0],flush=True);last=key
 if term or tr:break
print('RESULT',t,term,tr,time.time()-start,flush=True);E.close()
