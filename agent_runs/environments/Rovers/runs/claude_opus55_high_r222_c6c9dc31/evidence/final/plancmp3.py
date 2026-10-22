import sys
from env_client import make_env
import approach
env=make_env(); tot=[0]*6
for s in range(int(sys.argv[1]),int(sys.argv[2])):
    obs,info=env.reset(seed=s); out=[]
    for i,aset in enumerate([[0],[4],[8],[12],[2],[14]]):
        ap=approach.GeneratedApproach(env.action_space, env.observation_space,{})
        approach.ROT=True
        orig=ap._plan
        ap.reset(obs,info) if False else None
        # set angset before reset planning
        ap.__dict__['angset_fixed']=aset
        oldreset=ap.reset
        approach_reset=approach.GeneratedApproach.reset
        def patched_plan(state, ap=ap, aset=aset, orig=orig):
            ap.angset=aset; return orig(state)
        ap._plan=patched_plan
        ap.reset(obs,info)
        v=max(len(p) for p in ap.plans.values()) if ap.rot else 99; out.append(v)
    print(s,out, flush=True)
