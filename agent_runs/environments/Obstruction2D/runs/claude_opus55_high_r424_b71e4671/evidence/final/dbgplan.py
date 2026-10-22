import sys, itertools
from env_client import make_env
import approach as A
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=A.GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
print("legs", ap.legs)
robot, block, surface, obst = ap._parse(obs)
sr=A._rect(obs,surface); br=A._rect(obs,block)
orects={o.name:A._rect(obs,o) for o in obst}
start=(A._g(obs,robot,'x'),A._g(obs,robot,'y'))
for k in range(len(orects)+1):
    for R in itertools.permutations(orects,k):
        print(R, ap._plan_subset(start,R,orects,br,(sr[0],sr[1]),ap._assembly()), getattr(ap,"_why",None))
env.close()
# instrument
import numpy as np
R=('obstruction0','obstruction1')
n='obstruction0'; r=orects[n]
others=[(q[0],q[1],q[3]) for m,q in orects.items() if m!=n]+[(br[0],br[1],br[3])]
print("dopts", ap._d_options(r), [ap._pick_ok(r,v,others) for v in ap._d_options(r)])
print("block dopts", [ap._pick_ok(br,v,[(q[0],q[1],q[3]) for q in orects.values()]) for v in ap._d_options(br)])
