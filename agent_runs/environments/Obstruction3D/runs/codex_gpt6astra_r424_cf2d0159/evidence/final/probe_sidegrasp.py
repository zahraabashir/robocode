from env_client import make_env
from probe_fk import fk
from scipy.optimize import least_squares
import numpy as np
q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def solve(z,theta,yaw,q):
 axis=np.array([np.sin(theta),0,-np.cos(theta)])
 def fun(v):
  qq=np.array([0,v[0],-np.pi,v[1],0,v[2],yaw]);p,r=fk(qq)
  return np.r_[5*(p[[0,2]]-[.52,z]),r[:,2]-axis]
 sol=least_squares(fun,q[[1,3,5]],max_nfev=90)
 return np.array([0,sol.x[0],-np.pi,sol.x[1],0,sol.x[2],yaw])
def curq(s,ro):return np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)])
e=make_env()
for theta in [np.pi/2,np.pi/3,np.pi/4]:
 for yaw in [np.pi/2,0,np.pi]:
  for offset in [.12,.06,0,.18]:
   s,_=e.reset(seed=2,options={'object_count':0});o=s.get_object_from_name('target_block');ro=s.get_object_from_name('robot');target=np.array([s.get(o,'pose_'+v) for v in 'xyz']);q=q0.copy()
   base=target[:2]-[.52+offset*np.sin(theta),.001]
   for zi,z in enumerate(np.arange(.40,target[2]-.021,-.01)):
    q=solve(z,theta,yaw,q)
    for j in range(60 if zi==0 else 8):
     a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.10,.10);a[3:10]=np.clip(q-curq(s,ro),-.08,.08);a[-1]=1
     s,*_=e.step(a)
     if np.max(np.abs(q-curq(s,ro)))<1e-4:break
    a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
    if s.get(ro,'grasp_active'):
     print('SUCCESS',theta,yaw,offset,z,'target',target,'FK',fk(curq(s,ro)),'robot',{f:s.get(ro,f) for f in s.type_features[ro.type]},flush=True);e.close();quit()
   print('FAIL',theta,yaw,offset,'target',target,'FK',fk(curq(s,ro))[0],flush=True)
e.close()
