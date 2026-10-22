import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); DZ=float(sys.argv[2])
class P(GeneratedApproach):
    def _plan_place(self, state, boxes, name, place_xy, bottom):
        if name=="target_block": bottom=bottom+DZ
        return super()._plan_place(state, boxes, name, place_xy, bottom)
    def _blocking(self, boxes): return []
env=make_env(); obs,info=env.reset(seed=seed, options={"object_count":0})
ap=P(env.action_space, env.observation_space, {}); ap.reset(obs,info)
rob=ap._robot(obs); r_=ap._boxes(obs)["target_region"]
for t in range(40):
    a=ap.get_action(obs)
    obs,r,term,trunc,info=env.step(a)
    bb=ap._boxes(obs)["target_block"]
    print(t, "a10",round(float(a[10]),2),"grasp",obs.get(rob,"grasp_active"),"blkg",bb["g"],"bottom-regtop",round(bb["z"]-bb["hz"]-r_["z"]-r_["hz"],4),"term",term, ap.cur[0] if ap.cur else None)
    if term: break
