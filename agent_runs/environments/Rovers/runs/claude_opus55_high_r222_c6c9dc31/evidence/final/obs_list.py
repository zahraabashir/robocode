import sys
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
for o in obs.get_objects(env.observation_space.get_type('obstacle')):
    print(o.name, [round(float(obs.get(o,f)),3) for f in env.observation_space.type_features[env.observation_space.get_type('obstacle')]])
