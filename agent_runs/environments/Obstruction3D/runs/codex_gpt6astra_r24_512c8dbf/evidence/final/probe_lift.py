from env_client import make_env
from approach import GeneratedApproach
from kin import ik,fk
import numpy as np
E=make_env();s,i=E.reset(seed=2,options={'object_count':50});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,i);r=p.robot
qs=lambda s:np.array([s.get(r,'joint_'+str(j)) for j in range(1,8)])
for t in range(200):
 s,_,te,_,_=E.step(p.get_action(s))
 if p.stall>=3 and p.phase=='lift':break
q=qs(s);m,_=fk(q);base=np.array([s.get(r,'pos_base_x'),s.get(r,'pos_base_y')]);print('STUCK',t,p.obj,p.pos(s,p.obj),'q',q,'model',m,'base',base,'wrist',p.wrist,flush=True)
for dz,dx,dy in [(v,0,0) for v in [.005,.01,.08,.12,.2]]+[(.1,dx,dy) for dx,dy in [(-.02,0),(.02,0),(0,-.02),(0,.02),(-.05,0),(0,-.05),(0,.05)]]:
 q=qs(s);m,_=fk(q);goal=ik(.5,m[2]+dz);goal[6]=q[6];d=goal-q;scale=max(1,np.max(abs(d))/.2);a=np.zeros(11);a[3:10]=d/scale;a[0]=dx;a[1]=dy
 s,_,te,_,_=E.step(a);change=np.max(abs(qs(s)-q));print('TRY',dz,dx,dy,'CHANGE',change,flush=True)
 if change>1e-6:
  for k in range(500):
   s,_,te,_,_=E.step(p.get_action(s))
   if te:break
  print('END',te,k,p.phase,p.obj,p.stall,flush=True);break
E.close()
