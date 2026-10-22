import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
OC=int(sys.argv[3]) if len(sys.argv)>3 else None
obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None)); ap.reset(obs, info)
r0,objs,surf=ap._parse(obs)
print("surf",surf); [print(o) for o in objs.values()]
prev=None
for step in range(N):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    rb=ap._parse(obs)[0]
    key=(ap.mode,ap.cur)
    if key!=prev or step%50==0: print(step,key,[round(v,3) for v in (rb['x'],rb['y'],rb['th'],rb['arm'],rb['vac'])],np.round(a,3))
    prev=key
    if term: print("DONE",step+1);break
env.close()
