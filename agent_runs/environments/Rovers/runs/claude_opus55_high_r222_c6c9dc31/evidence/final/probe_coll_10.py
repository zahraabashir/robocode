from probe_coll_util import *
import numpy as np
obs,_=env.reset(seed=3)
out=[]
for y in list(np.arange(-2.27,1.65,0.1))+[1.6,1.65,1.7,1.75,1.8]:
    obs=goto(1,-1.0,rov(obs)[1][1],obs); obs=goto(1,-1.0,y,obs)
    if abs(rov(obs)[1][1]-y)>1e-4: out.append(('cant reach',round(y,3),[round(v,3) for v in rov(obs)[1]])); break
    obs=push(1,(1,0),obs,tol=1e-5)
    out.append((round(y,3),round(rov(obs)[1][0],5)))
print(out)
