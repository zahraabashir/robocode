from env_client import make_env
from probe_fk import fk
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def solve(x,z):
 def fun(v):
  q=q0.copy();q[[1,3,5]]=v;p,r=fk(q);return np.r_[5*(p[[0,2]]-[x,z]),r[:,2]-[0,0,-1]]
 v=least_squares(fun,q0[[1,3,5]],max_nfev=100).x;q=q0.copy();q[[1,3,5]]=v;return q
e=make_env()
for z in [.27,.3,.24,.33,.36]:
 s,_=e.reset(seed=0,options={'object_count':0});o=s.get_object_from_name('target_block');ro=s.get_object_from_name('robot');target=np.array([s.get(o,'pose_'+v) for v in 'xyz']);q=solve(.62,z)
 print('INIT',z,target,q,flush=True)
 for t in range(60):
  cur=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);a=np.zeros(11);a[:2]=np.clip([-.6-s.get(ro,'pos_base_x'),-.2-s.get(ro,'pos_base_y')],-.1,.1)
  if t>10:a[3:10]=np.clip(q-cur,-.04,.04)
  s,r,term,tr,i=e.step(a)
 for ix,dx in enumerate(np.arange(-.15,.151,.015)):
  ys=np.arange(-.15,.151,.015)
  if ix%2:ys=ys[::-1]
  for dy in ys:
   for t in range(4):
    a=np.zeros(11);a[:2]=np.clip([target[0]-.62+dx-s.get(ro,'pos_base_x'),target[1]-.001+dy-s.get(ro,'pos_base_y')],-.1,.1);s,r,term,tr,i=e.step(a)
   a=np.zeros(11);a[-1]=-1;s,r,term,tr,i=e.step(a)
   if s.get(ro,'grasp_active'):
    print('SUCCESS',z,dx,dy,{f:s.get(ro,f) for f in s.type_features[ro.type]},flush=True);e.close();quit()
 print('FAIL',z,flush=True)
e.close()
