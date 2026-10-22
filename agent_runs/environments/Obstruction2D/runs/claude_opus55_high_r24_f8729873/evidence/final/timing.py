import time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=1)
ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info); ap.state=obs
robot,block,surf,obst=ap._objs()
obstacles=ap._others_bboxes([])+[ap._others_bboxes([])[0]]
t=time.time()
for _ in range(20): r=ap._dp_path(0.389,0.826,1.09,0.38,obstacles,None)
print("dp ms", (time.time()-t)/20*1000, r[0])
t=time.time()
for _ in range(5): ap._find_spot(obst[0])
print("find_spot ms", (time.time()-t)/5*1000)
