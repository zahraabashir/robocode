from probe_coll_util import *
for seed in [0,1]:
    obs,_=env.reset(seed=seed)
    print('seed',seed,{k:[round(x,3) for x in v] for k,v in obst(obs).items() if v[2]<0.1})
    # rover0 right
    obs=push(0,(1,0),obs); print('r0 +x',rov(obs)[0])
    obs=push(0,(0,-1),obs); print('r0 -y',rov(obs)[0])
    obs=push(0,(-1,0),obs); print('r0 -x along bottom',rov(obs)[0])
    obs=push(1,(0,-1),obs); print('r1 -y',rov(obs)[1])
    obs=push(1,(-1,0),obs); print('r1 -x',rov(obs)[1])
