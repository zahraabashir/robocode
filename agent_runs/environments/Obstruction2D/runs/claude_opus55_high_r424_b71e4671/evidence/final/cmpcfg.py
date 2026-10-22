import sys, time
from env_client import make_env
from approach import GeneratedApproach
a,b=int(sys.argv[1]),int(sys.argv[2])
cfgs=[(20,3,3),(60,5,5),(150,8,8)]
env=make_env()
tot=[0]*len(cfgs); tm=[0]*len(cfgs)
for s in range(a,b):
    obs,info=env.reset(seed=s)
    row=[]
    for i,(n,kd,kp) in enumerate(cfgs):
        ap=GeneratedApproach(env.action_space,env.observation_space,{})
        ap.n_sim,ap.k_drop,ap.k_place=n,kd,kp
        t0=time.time(); ap.reset(obs,info); dt=time.time()-t0
        k=getattr(ap,'_best_key',(0,0))[0]; tot[i]+=k; tm[i]=max(tm[i],dt); row.append((k,round(dt,1)))
    print(s,row,flush=True)
print("tot",tot,"maxt",tm)
