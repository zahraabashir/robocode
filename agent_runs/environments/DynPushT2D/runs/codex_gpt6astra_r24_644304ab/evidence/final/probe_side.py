import numpy as np
from env_client import make_env
np.set_printoptions(precision=7,suppress=True)
def R(t):return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
for yy in [-.065,-.5]:
 e=make_env();s,_=e.reset(seed=1);p=s[:2].copy();a=s[2];rot=R(a);count=0
 targets=[[-.8,yy],[-.67 if yy>-.1 else -.19, yy]]
 for target in targets:
  t=p+rot@np.array(target)
  for k in range(70):
   d=t-s[16:18]
   if np.linalg.norm(d)<.001:break
   s,*_=e.step(np.clip(d,-.049,.049));count+=1
 print('START',yy,count,'block',s[:3],'localrobot',rot.T@(s[16:18]-s[:2]),flush=True)
 for k in range(8):
  old=s.copy();s,*_=e.step(R(old[2])@np.array([.01,0.]));count+=1
  dp=R(old[2]).T@(s[:2]-old[:2]);da=s[2]-old[2];q=R(old[2]).T@(old[16:18]-old[:2]);
  print('PUSH',yy,k,'q',q,'dp',dp,'da',da,flush=True)
 print('COUNT',count,flush=True);e.close()
