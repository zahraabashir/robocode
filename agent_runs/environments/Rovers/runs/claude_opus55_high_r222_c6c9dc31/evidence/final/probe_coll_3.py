from probe_coll_util import *
import math
ox,oy=0.654,-0.199
for th_steps in [0,2]:  # rotate 0 or 0.8 rad
  for name,start,d in [('from+x',(1.3,oy),(-1,0)),('from-y',(ox,-0.8),(0,1)),('from+y',(ox,0.4),(0,-1)),('diag ++',(1.2,0.35),(-1/math.sqrt(2),-1/math.sqrt(2))),('diag +-',(1.2,-0.75),(-1/math.sqrt(2),1/math.sqrt(2)))]:
    obs,_=env.reset(seed=0)
    for _ in range(th_steps): obs,*_=step((0,0,0.4))
    obs=goto(0,*start,obs)
    assert abs(rov(obs)[0][0]-start[0])<1e-5, rov(obs)
    obs=push(0,d,obs,tol=2e-5)
    x,y,t=rov(obs)[0]
    # dist from box
    ddx=max(abs(x-ox)-0.05,0); ddy=max(abs(y-oy)-0.05,0)
    print(th_steps,name,round(x,5),round(y,5),'theta',round(t,3),'dist_to_box',round(math.hypot(ddx,ddy),5),'center dist',round(math.hypot(x-ox,y-oy),5))
