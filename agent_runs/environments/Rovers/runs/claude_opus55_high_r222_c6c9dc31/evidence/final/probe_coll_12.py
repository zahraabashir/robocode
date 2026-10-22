from probe_coll_util import *
obs,_=env.reset(seed=3)
obs=goto(0,0.3,-1.75,obs); print('r0 at',rov(obs))
obs,*_=step((-0.1,0.1,0.3),(0.1,0.1,0.3)); print('after (-.1,.1,.3) both:',rov(obs))
obs,*_=step((-0.1,0.0,0.0),(0,0,0)); print('after -.1 x only',rov(obs))
obs,*_=step((0,0.0,0.4),(0,0,0)); print('rot only at wall',rov(obs))
obs,_=env.reset(seed=3); n=0
while True:
    obs,r,te,tr,info=env.step(act()); n+=1
    if te or tr: print('ended at step',n,'term',te,'trunc',tr,'r',r); break
    if n>1200: print('no end by 1200'); break
