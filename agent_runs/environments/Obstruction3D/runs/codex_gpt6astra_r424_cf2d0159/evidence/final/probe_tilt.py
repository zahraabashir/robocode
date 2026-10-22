from env_client import make_env
from probe_fk import fk
from scipy.spatial.transform import Rotation as R
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2]); qdown=np.array([0,.5,-np.pi,-1.8,0,-np.pi+.5+1.8,np.pi/2]);_,rd=fk(qdown)
def solve(p,rt,q):
 def fun(v):
  pp,rr=fk(v);return np.r_[5*(pp-p),R.from_matrix(rr.T@rt).as_rotvec()]
 return least_squares(fun,q,max_nfev=120).x
e=make_env()
for angle in [-30,30,-60,60,90,-90,120,-120,180]:
 rt=R.from_euler('y',angle,degrees=True).as_matrix()@rd
 s,_=e.reset(seed=0,options={'object_count':0});o=s.get_object_from_name('target_block');ro=s.get_object_from_name('robot');target=np.array([s.get(o,'pose_'+v) for v in 'xyz']);base=target[:2]-[.55,.001];q=q0.copy()
 print('ANGLE',angle,flush=True)
 for j,L in enumerate(np.arange(.30,.029,-.005)):
  p=np.r_[target[:2]-base,target[2]]-L*rt[:,2];q=solve(p,rt,q)
  for t in range(100 if j==0 else 3):
   cur=np.array([s.get(ro,'joint_'+str(k)) for k in range(1,8)]);a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.1,.1);dq=q-cur;a[3:10]=dq*min(1,.035/max(1e-9,np.max(abs(dq))));a[-1]=-1
   s,r,term,tr,i=e.step(a)
   if s.get(ro,'grasp_active'):
    print('SUCCESS',angle,L,{f:s.get(ro,f) for f in s.type_features[ro.type]},flush=True);e.close();quit()
 print('FAIL',angle,flush=True)
e.close()
