import sys, numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach
seed=int(sys.argv[1])
env=make_env(); ap=GeneratedApproach(None,None,{})
obs,info=env.reset(seed=seed); ap.reset(obs,info)
orig=ap.plan_push
def pp(s, look=0):
    p=orig(s, look)
    print('t',t,'pose',np.round(s[0:3],3),'goal',np.round(s[29:32],3),'robot',np.round(s[16:18],2), 'plan', None if p is None else (len(p['path']), np.round(p['u'],2), round(p['L'],2), round(p['E0'],3), round(p['Epred'],3)))
    return p
ap.plan_push=pp
import builtins
for t in range(int(sys.argv[2])):
    a=ap.get_action(obs); obs,r,te,tr,_=env.step(a)
    if te: print('done',t); break
