from env_client import make_env
from approach import GeneratedApproach
from kinematics_fit import fk
import numpy as np

e=make_env();s,info=e.reset(seed=10,options={'object_count':5});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
for k in range(800):
 a=p.get_action(s);s,r,t,tr,info=e.step(a)
 if t:print('SUCCESS',k,flush=True);break
 if p.stalled>5 and p.phase=='lift':
  ro=s.get_object_from_name('robot');q=np.array([s.get(ro,'joint_'+str(i)) for i in range(1,8)]);print('STUCK',k,p.goal,'q',q,'ee',fk(q)[0],'height',p.height,flush=True)
  for obj in s.get_objects(p.cube_type):print(obj.name,[s.get(obj,'pose_'+v) for v in 'xyz'],[s.get(obj,'half_extent_'+v) for v in 'xyz'],s.get(obj,'grasp_active'),flush=True)
  candidates=[]
  for factor in [.5,.2,.05,2,4]:
   aa=np.zeros(11);aa[3:10]=(p.config(min(.35,p.height))-q)*factor;candidates.append(('same_dir_'+str(factor),np.clip(aa,e.action_space.low,e.action_space.high)))
  aa=np.zeros(11);aa[3:10]=p.config(.35)-q;aa[3:10]*=min(1,.2/max(abs(aa[3:10])));candidates.append(('jump_high',aa))
  for d in [.05,-.05,.1,-.1]:
   aa=np.zeros(11);aa[4]=-d;aa[8]=d;candidates.append(('q2lift'+str(d),aa))
  for ax in [0,1]:
   for d in [-.05,.05,-.15,.15]:
    aa=np.zeros(11);aa[ax]=d;candidates.append(('base'+str(ax)+'_'+str(d),aa))
  for label,aa in candidates:
   before=np.array([s.get(ro,'joint_'+str(i)) for i in range(1,8)]+[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')]);s,*_=e.step(aa);after=np.array([s.get(ro,'joint_'+str(i)) for i in range(1,8)]+[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')]);accepted=np.max(abs(after-before))>1e-6
   print('TRY',label,accepted,flush=True)
   if accepted:
    q=after[:7];ee,_=fk(q);p.height=max(ee[2]+.025,p.height);break
  else:break
else:print('TIMEOUT',p.phase,p.goal,flush=True)
e.close()
