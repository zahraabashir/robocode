import sys, time
from env_client import make_env
from approach import GeneratedApproach
a,b=int(sys.argv[1]),int(sys.argv[2])
env=make_env(); ts=[]
for s in range(a,b):
    obs,info=env.reset(seed=s)
    ap=GeneratedApproach(env.action_space,env.observation_space,{})
    t0=time.time(); ap.reset(obs,info); ts.append((time.time()-t0,s))
ts.sort(); print("max",[(round(t,2),s) for t,s in ts[-5:]],"mean",sum(t for t,_ in ts)/len(ts))
