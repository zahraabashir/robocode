import sys, math
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
for t in ['lander','obstacle']:
  for o in obs.get_objects(env.observation_space.get_type(t)):
    print(o.name, [round(obs.get(o,f),3) for f in ['x','y']], end=' | ')
print()
