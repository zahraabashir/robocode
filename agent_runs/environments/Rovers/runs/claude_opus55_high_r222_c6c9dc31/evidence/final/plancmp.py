import sys
from env_client import make_env
import approach, approach_rot
env=make_env(); tot=[0,0]
for s in range(int(sys.argv[1]),int(sys.argv[2])):
    obs,info=env.reset(seed=s); out=[]
    for i,m in enumerate([approach, approach_rot]):
        ap=m.GeneratedApproach(env.action_space, env.observation_space,{}); ap.reset(obs,info)
        v=max(len(p) for p in ap.plans.values()); tot[i]+=v; out.append(v)
    if out[0]!=out[1]: print(s,out)
print(tot)
