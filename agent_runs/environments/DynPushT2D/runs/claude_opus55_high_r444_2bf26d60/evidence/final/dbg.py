import numpy as np, sys
from env_client import make_env
from approach import *
np.set_printoptions(precision=3, suppress=True)
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
orig=ap.plan_push
def pp(pose,robot):
    r=orig(pose,robot); print("PLAN pose",pose,"rob",robot,"cost %.3f score %.4f k %d here %d"%(r[4],r[3],r[2],r[5]), "start",r[0],"dir",r[1]); return r
ap.plan_push=pp
for i in range(int(sys.argv[2])):
    a=ap.get_action(obs)
    obs,r,te,tr,_=env.step(a)
    if te: print("DONE",i); break
print("goal", ap.goal)
