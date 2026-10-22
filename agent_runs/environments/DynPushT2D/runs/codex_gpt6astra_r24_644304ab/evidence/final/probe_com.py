import numpy as np
from env_client import make_env

def R(t):return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
for xx in [-.3,.3]:
 e=make_env();s,_=e.reset(seed=1);p=s[:2].copy();a=s[2];rot=R(a);count=0
 # Approach upper face through upper free halfplane.
 target=p+rot@np.array([xx,.5])
 for k in range(70):
  d=target-s[16:18]
  if np.linalg.norm(d)<.001:break
  s,*_=e.step(np.clip(d,-.049,.049));count+=1
 print('START',xx,count,'block',s[:3], 'localrobot',rot.T@(s[16:18]-s[:2]),flush=True)
 for k in range(25):
  old=s.copy();a0=old[2];s,*_=e.step(R(a0)@np.array([0.,-.02]));count+=1
  dp=R(a0).T@(s[:2]-old[:2]);da=s[2]-old[2];q=R(a0).T@(old[16:18]-old[:2]);
  if abs(da)>1e-7:
   print('PUSH',xx,k,'q',q,'dp',dp,'da',da,'c_y',dp[0]/da,'I',q[0]*dp[1]/da,flush=True)
 print('COUNT',count,flush=True);e.close()
