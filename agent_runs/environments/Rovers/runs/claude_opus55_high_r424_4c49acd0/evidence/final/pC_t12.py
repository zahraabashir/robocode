from pC_lib import *; import time; reset(11); t=time.time()
while S.n<1100:
    t1=time.time(); r=step(); dt=time.time()-t1
    if S.n%50==0 or dt>3: print(S.n,r,round(dt,2),round(time.time()-t,1),flush=True)
    if r[1] or r[2]: print('end',S.n,r,flush=True); break
