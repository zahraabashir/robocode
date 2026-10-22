from probe_coll_util import *
ox,oy=0.654,-0.199
obs,_=env.reset(seed=0)
obs=goto(0,1.3,oy,obs); obs=push(0,(-1,0),obs,tol=1e-5); print('contact',rov(obs)[0])
for d in [0.1,0.4,0.4,-0.4]:
    obs,*_=step((0,0,d)); print('rot',d,rov(obs)[0])
