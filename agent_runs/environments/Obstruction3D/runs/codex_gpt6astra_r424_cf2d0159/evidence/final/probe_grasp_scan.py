from env_client import make_env
from probe_fk import fk
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def solve(x,z):
 def fun(v):
  q=q0.copy();q[[1,3,5]]=v;p,r=fk(q)
  return np.r_[5*(p[[0,2]]-[x,z]),r[:,2]-[0,0,-1]]
 v=least_squares(fun,q0[[1,3,5]],max_nfev=100).x;q=q0.copy();q[[1,3,5]]=v;return q
q=solve(.48,.15)
e=make_env()
for dy in np.arange(-.09,.091,.03):
 for dx in np.arange(-.06,.061,.02):
  s,_=e.reset(seed=0);o=s.get_object_from_name('target_block');bx=s.get(o,'pose_x')-.48+dx;by=s.get(o,'pose_y')-.001+dy;ro=s.get_object_from_name('robot')
  for t in range(65):
   cur=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);a=np.zeros(11);a[:2]=np.clip([bx-s.get(ro,'pos_base_x'),by-s.get(ro,'pos_base_y')],-.1,.1)
   if t>5:a[3:10]=np.clip(q-cur,-.035,.035)
   a[-1]=-1;s,r,term,tr,i=e.step(a)
   if s.get(ro,'grasp_active'):
    print('SUCCESS',dx,dy,t,{f:s.get(ro,f) for f in s.type_features[ro.type]},'OBJECT',[(n,s.get(s.get_object_from_name(n),'grasp_active')) for n in s.get_object_names()],flush=True);e.close();quit()
  print('FAIL',dx,dy,'q2',s.get(ro,'joint_2'),flush=True)
e.close()
