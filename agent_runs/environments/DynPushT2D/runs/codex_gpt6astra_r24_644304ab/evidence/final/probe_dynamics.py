from env_client import make_env
import numpy as np
np.set_printoptions(precision=5,suppress=True)
e=make_env()
for seed in range(3):
 s,i=e.reset(seed=seed)
 print('RESET',seed,'max',e.max_steps,'state',s.tolist(),flush=True)
 for k,a in enumerate(([.049,0],[0,.049],[0,0],[-.049,0],[0,-.049])):
  old=s.copy();s,r,t,tr,i=e.step(np.array(a,dtype=np.float64))
  print('FREE',seed,k,'robot',s[16:22],'block',s[:6],'robot_delta',s[16:18]-old[16:18],flush=True)
e.close()
e=make_env();s,_=e.reset(seed=2)
for k in range(55):
 old=s.copy();a=np.array([0., .049]) if k<38 else np.zeros(2)
 s,r,t,tr,i=e.step(a)
 if np.linalg.norm(s[:3]-old[:3])>1e-8 or k in (0,20,54):
  print('COLLIDE',k,'robot',s[16:22],'block',s[:6],'delta',s[:3]-old[:3],flush=True)
e.close()
