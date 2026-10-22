import sys,numpy as np
from env_client import make_env
env=make_env()
seed=int(sys.argv[1])
obs,info=env.reset(seed=seed)
def dump(obs):
    for n in sorted(obs.get_object_names()):
        o=obs.get_object_from_name(n)
        fs=env.observation_space.type_features[o.type] if hasattr(env.observation_space,'type_features') else None
        print(n,o.type.name,[ (f,round(float(obs.get(o,f)),3)) for f in fs])
dump(obs); print(info)
