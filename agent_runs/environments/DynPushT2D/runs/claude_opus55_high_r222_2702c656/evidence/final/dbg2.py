import sys, math
import numpy as np
from env_client import make_env
from approach import GeneratedApproach, Block
seed=int(sys.argv[1]); N=int(sys.argv[2])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(N):
    a = ap.get_action(obs)
    if t>=N-5:
        B=Block(obs); name,p,n,k,tq=ap.push
        pre=B.to_world(p-n*(0.14)); rp=obs[16:18]
        print(t, ap.mode, name, 'a',a,'rp',rp,'pre',pre,'dist',B.dist(rp), 'wp', ap.nav_step(B,rp,pre))
    obs, r, term, trunc, info = env.step(a)
