from env_client import make_env
from approach import GeneratedApproach
import time
E=make_env();s,inf=E.reset(seed=8,options={'object_count':10});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,inf);start=time.time();last=None
for k in range(1000):
 a=p.get_action(s);s,r,term,tr,_=E.step(a);ro=s.get_object_from_name('robot');held=s.get(ro,'grasp_active');key=(p.goal,p.yaw,held)
 if key!=last or k%50==0:
  print(k,p.goal,p.phase,'yaw',p.yaw,'height',p.height,'retries',p.retries,'held',held,flush=True);last=key
 if term or tr or time.time()-start>57:break
print('RESULT',k+1,term,tr,time.time()-start,p.goal,p.phase,p.yaw,p.height,flush=True);E.close()
