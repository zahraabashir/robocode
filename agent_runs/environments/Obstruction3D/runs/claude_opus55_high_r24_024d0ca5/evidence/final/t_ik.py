import numpy as np, time
from kin import tool_fk, tool_ik, down_R, HOME
base=(-0.12,0,0)
q=HOME.copy(); t=time.time(); n=0
for p in [(0.15,0.2,0.13),(0.45,-0.3,0.12),(0.3,0,0.3),(0.12,-0.35,0.12),(0.5,0.3,0.15)]:
    qt,ok=tool_ik(q,np.array(p),down_R(0.3),base); n+=1
    print(p,ok,np.round(qt,2), np.round(tool_fk(qt,base)[:3,3],4))
print('time per ik',(time.time()-t)/n)
