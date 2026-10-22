import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); C=int(sys.argv[2]) if len(sys.argv)>2 else None
env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':C} if C else None)
for n in sorted(obs.get_object_names()):
    o=obs.get_object_from_name(n)
    print(n, {f: round(float(obs.get(o,f)),3) for f in (["x","y","width","height"] if n!='robot' else ['x','y'])})
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
pv=0
R=obs.get_object_from_name('robot')
for t in range(1000):
    a = ap.get_action(obs)
    prev=obs
    obs, r, term, trunc, info = env.step(a)
    if a[4]!=pv or term:
        moved=[n for n in obs.get_object_names() if n!='robot' and abs(obs.get(obs.get_object_from_name(n),'y')-prev.get(prev.get_object_from_name(n),'y'))+abs(obs.get(obs.get_object_from_name(n),'x')-prev.get(prev.get_object_from_name(n),'x'))>1e-6]
        print(t, "vac" , a[4], "R=(%.3f,%.3f)"%(obs.get(R,'x'),obs.get(R,'y')), moved, [(n, round(obs.get(obs.get_object_from_name(n),'x'),3), round(obs.get(obs.get_object_from_name(n),'y'),3)) for n in moved])
        pv=a[4]
    if term: print("TERM", t+1); break
