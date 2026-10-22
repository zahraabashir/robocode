from probe_coll_util import *
import math
res=[]
for k in range(0,17):
    phi=0.1*k
    obs,_=env.reset(seed=0)
    n=int(round(phi/0.1))
    for _ in range(n): obs,*_=step((0,0,0.1))
    th=rov(obs)[0][2]
    obs=goto(0,2.0,-1.75,obs); obs=goto(0,2.0,1.0,obs); assert abs(rov(obs)[0][1]-1.0)<1e-5
    obs=push(0,(0,1),obs,tol=1e-5); gy=1.75-rov(obs)[0][1]
    obs=goto(0,2.0,1.0,obs);obs=goto(0,1.2,1.0,obs);obs=goto(0,1.2,1.9,obs); assert abs(rov(obs)[0][0]-1.2)<1e-5,rov(obs)
    obs=push(0,(1,0),obs,tol=1e-5); gx=1.75-rov(obs)[0][0]
    print('phi',round(phi,2),'theta',round(th,3),'gap below mound(+y dir)',round(gy,5),'gap left of mound(+x dir)',round(gx,5))
