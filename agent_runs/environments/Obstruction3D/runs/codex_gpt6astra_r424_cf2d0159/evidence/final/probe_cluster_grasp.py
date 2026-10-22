from env_client import make_env
from approach import ik
from kinematics_fit import fk
import numpy as np
E=make_env()
for yaw in [0,np.pi/4,3*np.pi/4,np.pi/2]:
 for dx,dy in [(0,0),(.015,0),(-.015,0),(0,.015),(0,-.015)]:
  s,_=E.reset(seed=2);ro=s.get_object_from_name('robot');objs=list(s.get_objects(E.observation_space.get_type('Kinematic3DCuboid')));ob=max([o for o in objs if 'obstruction' in o.name],key=lambda o:s.get(o,'pose_z'));p=np.array([s.get(ob,'pose_'+v) for v in 'xyz']);guess=np.array([0,.4,-np.pi,-1.8,0,-1.,yaw])
  def move(q=None,base=None):
   global s
   for k in range(45):
    a=np.zeros(11);a[-1]=1
    if q is not None:a[3:10]=q-[s.get(ro,'joint_'+str(j)) for j in range(1,8)]
    if base is not None:a[:2]=base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')]
    m=np.max(abs(a[:10]));a[:10]*=min(1,.12/max(m,1e-9));old=s;s,*_=E.step(a)
    if m<1e-5:return True
    if k>2 and all(abs(s.get(ro,'joint_'+str(j))-old.get(ro,'joint_'+str(j)))<1e-7 for j in range(1,8)) and base is None:return False
   return False
  q=ik(.55,.35,guess);move(q=q);ee,_=fk(np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]));base=p[:2]-ee[:2]+[dx,dy];move(base=base)
  success=False
  for z in np.arange(.33,p[2]+.004,-.005):
   q=ik(.55,z,guess);move(q=q)
   a=np.zeros(11);a[-1]=-1;s,*_=E.step(a)
   held=[o.name for o in objs if s.get(o,'grasp_active')>.5]
   if held:
    print('SUCCESS',yaw,dx,dy,'z',z,'held',held,'goal',ob.name,'goalpos',p,flush=True);success=True;break
  if not success:print('FAIL',yaw,dx,dy,'ee',fk(np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]))[0],'goalpos',p,flush=True)
E.close()
