from env_client import make_env
import numpy as np
Q=np.array([0,.44754085,-np.pi,-2.12094116,0,.00999998,.690796375])
e=make_env();s,_=e.reset(seed=2,options={'object_count':0});r=s.get_object_from_name('robot');t=s.get_object_from_name('target_block')
def move(q=None,b=None):
 global s
 for _ in range(80):
  a=np.zeros(11)
  if q is not None:a[3:10]=q-np.array([s.get(r,'joint_'+str(i)) for i in range(1,8)])
  if b is not None:a[:2]=b-np.array([s.get(r,'pos_base_'+a) for a in 'xy'])
  m=max(abs(a[:10]))
  if m<1e-5:break
  a[:10]*=min(1,.05/m);ss,*_=e.step(a)
  if all(ss.get(r,f)==s.get(r,f) for f in ['pos_base_x','pos_base_y']+['joint_'+str(i) for i in range(1,8)]):break
  s=ss
p=np.array([s.get(t,'pose_'+a) for a in 'xyz']);move(b=p[:2]-[.64,.001]);move(q=Q)
a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
print('grasp',s.get(r,'grasp_active'),'joints',[s.get(r,'joint_'+str(i)) for i in range(1,8)],'block',[s.get(t,'pose_'+a) for a in 'xyz'],flush=True)
for i in range(4):
 q=Q.copy();q[1]-=.05*(i+1);q[5]+=.05*(i+1);move(q=q);print('lift',i,[s.get(t,'pose_'+a) for a in 'xyz'],flush=True)
e.close()
