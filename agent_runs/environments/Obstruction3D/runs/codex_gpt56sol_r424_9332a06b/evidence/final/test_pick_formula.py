import concurrent.futures
import numpy as np
from env_client import make_env

def v(s,n,f): return s.get(s.get_object_from_name(n),f)
def trial(seed):
 e=make_env();s,_=e.reset(seed=seed); x=v(s,'target_block','pose_x'); y=v(s,'target_block','pose_y')
 # Empirical planar reach interpolation.
 q2=.35+2.0*(x-.336); q4=-2.2+1.5*(x-.336); q6=-.6+.8*(x-.336)
 tar=np.array([0,q2,-np.pi,q4,0,q6,np.pi/2])
 ok=False
 for t in range(12):
  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)])
  a=np.zeros(11,np.float32);a[1]=np.clip(y-.00135-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2)
  if t>=7:a[10]=-1
  s,*_=e.step(a)
  if v(s,'robot','grasp_active')>.5:ok=True;break
 e.close();return seed,round(x,3),np.round(tar[[1,3,5]],3).tolist(),ok

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
 for z in ex.map(trial,range(20)):print(z,flush=True)
