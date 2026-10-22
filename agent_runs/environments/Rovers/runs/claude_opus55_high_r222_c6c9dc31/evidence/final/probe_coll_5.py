from probe_coll_util import *
import math
ox,oy=0.654,-0.199
for k in [0,1,2,3,4]:
    th=0.2*k
    obs,_=env.reset(seed=0)
    nrot=k
    for _ in range(nrot): obs,*_=step((0,0,0.2))
    obs=push(0,(1,0),obs,tol=2e-5); xw=rov(obs)[0][0]
    obs=goto(0,1.3,oy,obs); assert abs(rov(obs)[0][1]-oy)<1e-5
    obs=push(0,(-1,0),obs,tol=2e-5); xp=rov(obs)[0][0]
    obs=goto(0,1.3,0.5,obs);obs=goto(0,ox,0.5,obs); assert abs(rov(obs)[0][0]-ox)<1e-5 and abs(rov(obs)[0][1]-0.5)<1e-5
    obs=push(0,(0,-1),obs,tol=2e-5); yp=rov(obs)[0][1]
    print('rot',round(th,2),'theta',round(rov(obs)[0][2],3),'wall+x stop',round(xw,5),'pillar from+x gap',round(xp-(ox+.05),5),'pillar from+y gap',round((oy-.05)-yp,5))
