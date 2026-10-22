from env_client import make_env
from approach import GeneratedApproach
from kin import fk,ik
import numpy as np,time
E=make_env();s,info=E.reset(seed=0,options={'object_count':50});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);r=p.robot;fs=['joint_'+str(i) for i in range(1,8)]
def signature(s):return np.array([s.get(r,f) for f in ['pos_base_x','pos_base_y']+fs])
for t in range(1000):
 a=p.get_action(s)
 if p.phase=='above' and p.stall>=3:break
 s,rw,done,tr,info=E.step(a)
 if done:print('EARLYSUCCESS');raise SystemExit
v=signature(s);m,rot=fk(v[2:]);m+=np.r_[v[:2]+[.12,0],0]
print('STALLED',t,'obj',p.obj.name,'model',m.tolist(),'signature',v.tolist(),flush=True)
for o in p.objects:
 if np.linalg.norm(p.pos(s,o)[:2]-m[:2])<.12:print('NEAR',o.name,p.pos(s,o).tolist(),p.size(s,o).tolist(),flush=True)
a=np.zeros(11,dtype=np.float32);a[10]=-1;s,*_=E.step(a)
print('RECLOSE',s.get(r,'grasp_active'),[o.name for o in p.objects if s.get(o,'grasp_active')],flush=True)
if s.get(r,'grasp_active'):
 p.failed_places.append(m[:2].copy())
for ztarget in [.18,.24,.3]:
 q=ik(.5,ztarget);q[6]=v[-1]
 for _ in range(4):
  a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-signature(s)[2:],-.2,.2);s,*_=E.step(a)
 print('LIFT',ztarget,'model',fk(signature(s)[2:])[0].tolist(),flush=True)
for k in range(1000-t):
 s,rw,done,tr,info=E.step(p.get_action(s))
 if done or tr:break
 if p.stall>10:break
print('RESULT',done,'steps',t+k+1,'phase',p.phase,'obj',p.obj.name,'stall',p.stall,flush=True)
E.close()
