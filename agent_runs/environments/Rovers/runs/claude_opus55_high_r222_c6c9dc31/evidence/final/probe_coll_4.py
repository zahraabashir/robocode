from probe_coll_util import *
obs,_=env.reset(seed=0)
obs=goto(0,0.654,0.4,obs); print(rov(obs)[0])
for i in range(8):
    obs,*_=step((0,-0.2,0)); print(rov(obs)[0])
for i in range(8):
    obs,*_=step((0,0.2,0)); print('up',rov(obs)[0])
