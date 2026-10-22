import sys, numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach, _rect_bbox
seed=int(sys.argv[1])
env=make_env(); obs,info=env.reset(seed=seed)
ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
# monkeypatch path cost to print
orig=ap._path_cost
log=[]
def pc(p0,p1,o,c):
    v=orig(p0,p1,o,c); log.append((p0,p1,v)); return v
ap._path_cost=pc
orig_fs=ap._find_spot
def fs(o):
    log.clear(); r=orig_fs(o)
    for i in range(0,len(log),3):
        print("cand rx=%.3f ry=%.3f  c1=%d c2=%d c3=%d"%(log[i][1][0],log[i][1][1],log[i][2],log[i+1][2],log[i+2][2]))
    print("chosen",r); return r
ap._find_spot=fs
for t in range(200):
    a=ap.get_action(obs); obs,r,term,tr,_=env.step(a)
    if term: print("steps",t+1); break
