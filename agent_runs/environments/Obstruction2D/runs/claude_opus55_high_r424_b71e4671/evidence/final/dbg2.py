import sys, numpy as np
from env_client import make_env
import approach as A
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=A.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
robot, block, surface, obst = ap._parse(obs)
sr=A._rect(obs,surface); br=A._rect(obs,block)
orects={o.name:A._rect(obs,o) for o in obst}
print("surf",sr[:2],"block",br)
orig=ap._place_any
def pa(br_,d,lefts,obstacles):
    r=orig(br_,d,lefts,obstacles); print("place_any d",d,"obst",np.round(obstacles,3).tolist(),"->",r); return r
ap._place_any=pa
start=(A._g(obs,robot,'x'),A._g(obs,robot,'y'))
R=tuple(sys.argv[2].split(','))
print(ap._plan_subset(start,R,orects,br,(sr[0],sr[1]),ap._assembly()), ap._why)
env.close()
