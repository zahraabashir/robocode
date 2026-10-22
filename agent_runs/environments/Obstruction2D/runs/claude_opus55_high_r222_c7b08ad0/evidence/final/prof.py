import cProfile, pstats, sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=int(sys.argv[1])); ap.reset(obs, info)
def run():
    global obs
    for t in range(200):
        a = ap.get_action(obs); obs, r, term, *_ = env.step(a)
        if term: break
cProfile.run('run()', 'prof.out')
pstats.Stats('prof.out').sort_stats('cumulative').print_stats(15)
