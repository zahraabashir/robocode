import sys, copy, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); T=int(sys.argv[2])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
acts=[]
for t in range(T):
    a = ap.get_action(obs); acts.append(a); obs, *_ = env.step(a)
a = ap.get_action(obs)
print("seg", ap.cur[0], ap.cur[3], "act", np.round(a,3))
def trial(aa, tag):
    e2 = make_env(); o,_ = e2.reset(seed=seed)
    for x in acts: o,*_ = e2.step(x)
    q0 = ap._q(o); b0=ap._base(o)
    o2,*_ = e2.step(aa)
    print(tag, "moved" if (np.abs(ap._q(o2)-q0).max()>1e-7 or np.abs(ap._base(o2)-b0).max()>1e-7) else "REJECTED")
trial(a, "full")
b = a.copy(); b[0:3]=0; trial(b, "arm only")
b = a.copy(); b[3:10]=0; trial(b, "base only")
b = a.copy(); b[3:10]*=0.3; b[0:3]*=0.3; trial(b, "0.3 scaled")
b = np.zeros(11,dtype=np.float32); b[0:3]=[0,0.02,0]; trial(b, "base y small")
