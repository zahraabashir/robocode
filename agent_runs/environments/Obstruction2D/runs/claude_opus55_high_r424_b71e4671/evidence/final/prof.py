import cProfile, pstats, sys
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(env.action_space, env.observation_space, {})
cProfile.run('ap.reset(obs,info)','prof.out')
pstats.Stats('prof.out').sort_stats('cumtime').print_stats(12)
