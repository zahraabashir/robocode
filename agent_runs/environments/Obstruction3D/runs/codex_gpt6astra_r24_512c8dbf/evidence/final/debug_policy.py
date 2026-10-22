from env_client import make_env
from approach import GeneratedApproach
from kin import fk
import sys,numpy as np
seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
E=make_env();s,i=E.reset(seed=seed,options={'object_count':int(sys.argv[2])}) if len(sys.argv)>2 else E.reset(seed=seed);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i)
for t in range(180):
 a=p.get_action(s);s,rew,te,tr,inf=E.step(a)
 if t%10==0 or te:
  r=p.robot;q=np.array([s.get(r,'joint_'+str(k)) for k in range(1,8)]);m,_=fk(q);m+=np.array([s.get(r,'pos_base_x')+.12,s.get(r,'pos_base_y'),0])
  print(t,p.phase,p.obj,'pos',p.pos(s,p.obj).round(4),'model',m.round(4),'a',a.round(4),'stall',p.stall,flush=True)
 if te:print('SUCCESS');break
E.close()
