import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2]); C=int(sys.argv[3]) if len(sys.argv)>3 else None
env = make_env(); obs, info = env.reset(seed=seed, options={'object_count':C} if C else None)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
names=sorted(obs.get_object_names())
for t in range(N):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    R=obs.get_object_from_name('robot')
    line=f"{t} a={np.round(a,3)} R=({obs.get(R,'x'):.3f},{obs.get(R,'y'):.3f},{obs.get(R,'arm_joint'):.2f})"
    for n in names:
        if n in('robot','target_surface'):continue
        o=obs.get_object_from_name(n); line+=f" {n[:4]}{n[-1]}=({obs.get(o,'x'):.3f},{obs.get(o,'y'):.3f})"
    print(line)
    if term: print("TERM"); break
