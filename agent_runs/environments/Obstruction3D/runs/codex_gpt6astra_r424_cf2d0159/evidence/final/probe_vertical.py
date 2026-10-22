from env_client import make_env
from probe_fk import fk
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def solve(x,z,guess):
 def fun(v):
  q=q0.copy();q[[1,3,5]]=v;p,r=fk(q);return np.r_[5*(p[[0,2]]-[x,z]),r[:,2]-[0,0,-1]]
 v=least_squares(fun,guess[[1,3,5]],max_nfev=100).x;q=q0.copy();q[[1,3,5]]=v;return q
qs=[];q=q0
for z in np.arange(.4,.089,-.005):q=solve(.48,z,q);qs.append(q)
e=make_env()
for dy in [0,-.02,.02,-.04,.04]:
 for dx in [0,-.02,.02,-.04,.04]:
  s,_=e.reset(seed=0);o=s.get_object_from_name('target_block');bx=s.get(o,'pose_x')-.48+dx;by=s.get(o,'pose_y')-.001+dy;ro=s.get_object_from_name('robot')
  for stage,q in enumerate(qs):
   for t in range(60 if stage==0 else 4):
    cur=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);a=np.zeros(11);a[:2]=np.clip([bx-s.get(ro,'pos_base_x'),by-s.get(ro,'pos_base_y')],-.1,.1);a[3:10]=np.clip(q-cur,-.02,.02);a[-1]=-1
    s,r,term,tr,i=e.step(a)
    if s.get(ro,'grasp_active'):
     print('SUCCESS',dx,dy,stage,{f:s.get(ro,f) for f in s.type_features[ro.type]},flush=True);e.close();quit()
  cur=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);print('FAIL',dx,dy,'FK',fk(cur)[0],flush=True)
e.close()
