from env_client import make_env
import numpy as np
env=make_env()
obs,info=env.reset(seed=1)
print(type(obs)); print(env._primitive_manifest)
for o in obs: print(o, [ (f,round(obs.get(o,f),4)) for f in env.observation_space.type_features[o.type]] if hasattr(env.observation_space,'type_features') else '')
print(info)
s=env.get_state(); print(type(s))
