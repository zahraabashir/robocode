from env_client import make_env
import numpy as np
env = make_env()
def dump(obs):
    for n in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(n)
        feats = obs.type_features[o.type] if o.type in obs.type_features else obs.type_features[o.type.name]
        print(n, {f: round(float(obs.get(o,f)),4) for f in feats})
for seed in [0,1,2]:
    obs, info = env.reset(seed=seed)
    dump(obs); print()
env.close()
