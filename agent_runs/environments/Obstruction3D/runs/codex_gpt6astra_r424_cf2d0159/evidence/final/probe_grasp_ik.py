from env_client import make_env
from probe_fk import fk
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def solve(x,z,L):
 def fun(v):
  q=q0.copy();q[[1,3,5]]=v;p,r=fk(q);p+=r@[0,0,L]
  return np.r_[5*(p[[0,2]]-[x,z]),r[:,2]-[0,0,-1]]
 sol=least_squares(fun,q0[[1,3,5]],max_nfev=200)
 q=q0.copy();q[[1,3,5]]=sol.x
 return q,fk(q),np.linalg.norm(sol.fun)
def robot(s):
 o=s.get_object_from_name('robot');return o,np.array([s.get(o,'joint_'+str(j)) for j in range(1,8)])
e=make_env()
for L in [.12,.15,.08]:
 for z in [.10,.13,.07,.16]:
  q,(p,rot),err=solve(.48,z,L);print('IK',L,z,q,p,rot[:,2],err,flush=True)
  for dx in [-.06,0,.06]:
   s,_=e.reset(seed=0);o=s.get_object_from_name('target_block');target=np.array([s.get(o,'pose_'+v) for v in 'xyz']);bx=target[0]-.48+dx;by=target[1]-p[1]
   # first move base with existing raised posture, then lower joint targets
   for t in range(45):
    ro,cur=robot(s);a=np.zeros(11);a[:2]=np.clip([bx-s.get(ro,'pos_base_x'),by-s.get(ro,'pos_base_y')],-.1,.1)
    if t>5:a[3:10]=np.clip(q-cur,-.05,.05)
    if t>38:a[-1]=-1
    s,r,term,tr,i=e.step(a)
    if s.get(ro,'grasp_active'):
     print('SUCCESS',L,z,dx,{f:s.get(ro,f) for f in s.type_features[ro.type]},flush=True);e.close();quit()
   ro,cur=robot(s);print('FAIL',L,z,dx,'base',s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y'),'q',cur,'gap',np.linalg.norm(q-cur),flush=True)
e.close()
