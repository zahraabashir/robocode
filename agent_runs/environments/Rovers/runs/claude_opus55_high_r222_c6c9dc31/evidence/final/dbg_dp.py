import sys, numpy as np
from env_client import make_env
import approach
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=approach.GeneratedApproach(env.action_space, env.observation_space,{})
orig_plan=ap._plan
def pp(state):
    ap.angset=[4]; return orig_plan(state)
ap._plan=pp
orig=ap._theta_dp
def dp(state):
    ok=orig(state)
    if ap.rot:
        for r,p in ap.plans.items():
            print(r, [(t,op) for t,(c,op) in enumerate(p) if op!='none'], len(p), r in ap.thplan)
    return ok
ap._theta_dp=dp
ap.reset(obs,info)
r,allow,cost,plan,res=ap._dbg
for t in range(len(allow)): print(t, ''.join('1' if a else '.' for a in allow[t]), ''.join('x' if np.isfinite(c) else '.' for c in cost[t]))
X,Y=res['X'],res['Y']
(x,y),op=plan[12]
i=np.unravel_index(np.argmin(np.abs(X-x)+np.abs(Y-y)), X.shape)
print(op, x,y, X[i],Y[i], res['send'][i], [int(sl[i]) for sl in res['send_l']], len(res['send_l']))
