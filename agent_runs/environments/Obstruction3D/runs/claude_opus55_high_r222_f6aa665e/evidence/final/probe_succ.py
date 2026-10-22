import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); DX=float(sys.argv[2]); DY=float(sys.argv[3]); DZ=float(sys.argv[4]) if len(sys.argv)>4 else 0.0
N=int(sys.argv[5]) if len(sys.argv)>5 else 600
class P(GeneratedApproach):
    def _plan_place(self, state, boxes, name, place_xy, bottom):
        if name=="target_block":
            place_xy=(place_xy[0]+DX, place_xy[1]+DY); bottom=bottom+DZ
        return super()._plan_place(state, boxes, name, place_xy, bottom)
    def _blocking(self, boxes): return []
env=make_env(); obs,info=env.reset(seed=seed, options={"object_count":0})
ap=P(env.action_space, env.observation_space, {}); ap.reset(obs,info)
b=ap._boxes(obs); r_=b["target_region"]; t_=b["target_block"]
print("reg", {k:round(v,6) for k,v in r_.items()}); print("blk", {k:round(v,6) for k,v in t_.items()})
rob=ap._robot(obs); opened=None; res="NOTERM"
for t in range(N):
    a=ap.get_action(obs); g0=obs.get(rob,"grasp_active")
    obs,r,term,trunc,info=env.step(a)
    b=ap._boxes(obs); bb=b["target_block"]; g=obs.get(rob,"grasp_active")
    if g0>0.5 and g<0.5 and opened is None and bb["z"]<0.3: opened=t
    if term or (opened is not None and t-opened>=1):
        res="TERM" if term else "NOTERM"
        print(res, "t",t,"opened",opened,"grasp",g,"blkg",bb["g"],"off", round(bb["x"]-r_["x"],6), round(bb["y"]-r_["y"],6),
              "bottom-regtop", round(bb["z"]-bb["hz"]-(r_["z"]+r_["hz"]),4), "yaw", round(bb["yaw"],3),"r",r); break
else: print("timeout", "opened", opened)
