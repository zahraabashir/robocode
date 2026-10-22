from env_client import make_env
from approach import GeneratedApproach,ik
from kinematics_fit import fk
import numpy as np
class Probe(GeneratedApproach):
 def config(self,z):
  z=round(float(z),6)
  if z not in self.cache:
   guess=np.array([0,.4,-np.pi,-1.8,0,-1.,self.yaw]);self.cache[z]=ik(self.x,z,guess)
  return self.cache[z]
E=make_env()
for yaw in [np.pi/2,0,np.pi/4,3*np.pi/4]:
 s,inf=E.reset(seed=2,options={'object_count':5});pol=Probe(E.action_space,E.observation_space,{});pol.yaw=yaw;pol.reset(s,inf);ro=s.get_object_from_name('robot');last=None;stuck=0;done=False
 print('START',yaw,pol.goal,pol.tasks,flush=True)
 for t in range(250):
  a=pol.get_action(s);s,r,term,tr,_=E.step(a);q=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);vec=np.r_[q,[s.get(ro,'pos_base_'+v) for v in 'xy']];stuck=stuck+1 if last is not None and np.max(abs(vec-last))<1e-7 else 0;last=vec
  if s.get(ro,'grasp_active'):
   print('GRASP',yaw,t,pol.goal,'ee',fk(q)[0],flush=True);done=True;break
  if stuck>=6:
   print('STUCK',yaw,t,pol.phase,pol.goal,'ee',fk(q)[0],'desired',pol.height,flush=True)
   a=np.zeros(11);a[-1]=-1;s,*_=E.step(a)
   print('STUCK_CLOSE',s.get(ro,'grasp_active'),flush=True)
   if s.get(ro,'grasp_active'):done=True;break
   break
 if not done:print('FAIL',yaw,flush=True)
E.close()
