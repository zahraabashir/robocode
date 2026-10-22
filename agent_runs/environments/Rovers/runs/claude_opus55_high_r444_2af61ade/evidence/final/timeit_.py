import sys, time
from env_client import make_env
from approach import GeneratedApproach
import cProfile, pstats
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1])); env.close()
ap=GeneratedApproach(None,None,{})
t=time.time()
cProfile.run('ap.reset(obs,info)','prof.out')
print('time',time.time()-t)
pstats.Stats('prof.out').sort_stats('cumtime').print_stats(12)
