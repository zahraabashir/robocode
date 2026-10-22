import sys, numpy as np, collections
from env_client import make_env
from approach import GeneratedApproach
cnt=collections.Counter(); env=make_env(); tot=0
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    for t in range(1000):
        a = ap.get_action(obs)
        c = ap.cur
        tag = "grip" if c is None else (c[0] if c[0]!="move" else c[3])
        if tag=="travel": tag += "-J" if (ap.jplan is not None and ap.jplan is not False) else "-C"
        cnt[tag]+=1; tot+=1
        obs, r, term, trunc, info = env.step(a)
        if term: break
print(tot, cnt.most_common())
