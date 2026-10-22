import sys, cProfile, pstats, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); K=int(sys.argv[2])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for k in range(K):
    a = ap.get_action(obs); obs, *_ = env.step(a)
cProfile.run("ap.get_action(obs)", "p.out")
pstats.Stats("p.out").sort_stats("cumtime").print_stats(12)
