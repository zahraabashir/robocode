import numpy as np, sys
from env_client import make_env
from approach import GeneratedApproach
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=int(sys.argv[1]), options={'object_count':int(sys.argv[2])})
ap.reset(obs, info)
r, rects = ap._parse(obs); ap.r = r
blk=rects['target_block']; surf=rects['target_surface']
print(ap._grasp_xs(blk, rects))
c, held, gx, gy = ap._place_candidates_target(blk, surf, rects)
print(len(c), c[:3], gx)
print(ap._plan(rects))
