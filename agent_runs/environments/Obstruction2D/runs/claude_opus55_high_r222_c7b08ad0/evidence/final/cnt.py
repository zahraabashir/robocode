import numpy as np, sys
from env_client import make_env
from approach import GeneratedApproach
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
multi=0; tot=0
for seed in range(6000, 6060):
    obs, info = env.reset(seed=seed, options={'object_count':int(sys.argv[1])})
    ap.reset(obs, info)
    r, rects = ap._parse(obs); ap.r = r
    blk=rects['target_block']; surf=rects['target_surface']
    c, held, gx, gy = ap._place_candidates_target(blk, surf, rects)
    k = c[0][0]
    sets = set(tuple(sorted(x[4])) for x in c if x[0]==k)
    tot+=1; multi += len(sets)>1
    if len(sets)>1: print(seed, k, sets)
print(multi, tot)
