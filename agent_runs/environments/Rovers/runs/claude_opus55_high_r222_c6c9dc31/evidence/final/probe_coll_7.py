from probe_coll_util import *
import math
ox,oy=0.654,-0.199
for k in range(0,16):
    obs,_=env.reset(seed=0)
    for _ in range(k): obs,*_=step((0,0,0.4))
    th=rov(obs)[0][2]
    obs=goto(0,1.3,oy,obs); assert abs(rov(obs)[0][1]-oy)<1e-5
    obs=push(0,(-1,0),obs,tol=1e-5); xp=rov(obs)[0][0]
    print('theta',round(th,3),'pillar gap(from +x)',round(xp-(ox+.05),5))
