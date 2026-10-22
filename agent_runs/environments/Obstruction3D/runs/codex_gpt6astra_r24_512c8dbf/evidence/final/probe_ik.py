from env_client import make_env
from kin import *
E=make_env();s,_=E.reset(seed=0)
r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
def vals(s,obj,fs):return np.array([s.get(obj,f) for f in fs])
fs=['joint_'+str(i) for i in range(1,8)]
x,y,z=vals(s,b,['pose_x','pose_y','pose_z'])
def move(q,by):
 global s
 for i in range(30):
  delta=q-vals(s,r,fs);a=np.zeros(11);a[3:10]=np.clip(delta,-.15,.15);a[1]=np.clip(by-s.get(r,'pos_base_y'),-.15,.15)
  if np.max(np.abs(a))<1e-5:return True
  old=s;s,*_=E.step(a)
  if np.max(np.abs(vals(s,r,fs)-vals(old,r,fs)))<1e-7 and abs(s.get(r,'pos_base_y')-old.get(r,'pos_base_y'))<1e-7:
   print('blocked',np.round(vals(s,r,fs),3));return False
 return False
for d in [.18,.12,.06,.24]:
 s,_=E.reset(seed=0)
 q=ik(x+.12,.25,d);print('high',d,np.round(q,3),move(q,y-.001),flush=True)
 for zt in np.arange(.22,.039,-.015):
  q=ik(x+.12,zt,d);ok=move(q,y-.001)
  a=np.zeros(11);a[10]=-1;s,*_=E.step(a)
  if s.get(r,'grasp_active'):
   print('GRASP',d,zt,vals(s,r,fs),{f:s.get(r,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']},flush=True);E.close();raise SystemExit
  print('try',round(zt,3),ok,flush=True)
E.close()
