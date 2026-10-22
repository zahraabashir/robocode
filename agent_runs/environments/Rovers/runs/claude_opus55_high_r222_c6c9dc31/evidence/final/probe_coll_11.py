from probe_coll_util import *
import math
# seed with clear lander area
for s in range(40):
    obs,_=env.reset(seed=s)
    P=[v for v in obst(obs).values() if v[2]<0.1]
    if all(math.hypot(p[0]+1.9,p[1]+2.0)>1.3 for p in P): break
print('seed',s)
L=(-1.9,-2.0)
for name,start,d in [('from+x',(-1.0,-2.0),(-1,0)),('from+y',(-1.9,-1.0),(0,-1)),('from+x low',(-1.0,-2.27),(-1,0)),('diag',(-1.2,-1.3),(-1/math.sqrt(2),-1/math.sqrt(2)))]:
  for rot in [0,2]:
    obs,_=env.reset(seed=s)
    for _ in range(rot): obs,*_=step((0,0,0),(0,0,0.4))
    obs=goto(1,-1.0,start[1],obs); obs=goto(1,*start,obs)
    assert math.hypot(rov(obs)[1][0]-start[0],rov(obs)[1][1]-start[1])<1e-4, rov(obs)
    obs=push(1,d,obs,tol=1e-5); x,y,t=rov(obs)[1]
    print(name,'theta',round(t,2),'stop',round(x,5),round(y,5),'dx',round(x-L[0],5),'dy',round(y-L[1],5),'dist',round(math.hypot(x-L[0],y-L[1]),5))
