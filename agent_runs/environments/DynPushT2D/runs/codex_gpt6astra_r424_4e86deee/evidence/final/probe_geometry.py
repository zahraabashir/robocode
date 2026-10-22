from env_client import make_env
import numpy as np
np.set_printoptions(precision=5,suppress=True)
e=make_env()
for seed in range(12):
 s,_=e.reset(seed=seed)
 print('SEED',seed,'block',s[:6],'dims',s[12:16],'robot',s[16:22],'r',s[28],'goal',s[29:32],flush=True)
s,_=e.reset(seed=0)
for a in [[.049,0],[0,.049],[0,0],[-.049,-.049]]:
 old=s.copy();s,r,t,tr,info=e.step(np.array(a,dtype=float))
 print('KIN',a,'dr',s[16:22]-old[16:22],'state',s[16:22],flush=True)
for k in range(30):s,*_=e.step(np.array([-.049,-.049]))
print('CORNER',s[16:22],flush=True)
e.close()
