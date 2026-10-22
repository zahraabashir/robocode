from env_client import make_env
from approach import GeneratedApproach
import time,sys
for seed in map(int,sys.argv[1:] or ['0','1','2']):
 E=make_env();s,info=E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();last=None
 for t in range(min(E.max_steps,350)):
  a=p.get_action(s);s,r,term,trunc,inf=E.step(a)
  if p.phase!=last:
   print(seed,t,p.phase,'block',p.pos(s,p.block).round(3),'held',s.get(p.robot,'grasp_active'),flush=True);last=p.phase
  if term or trunc:break
 print('RESULT',seed,info,t+1,term,round(time.monotonic()-start,2),'phase',p.phase,flush=True);E.close()
