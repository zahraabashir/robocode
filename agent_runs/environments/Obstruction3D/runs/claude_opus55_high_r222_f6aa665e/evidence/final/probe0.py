from env_client import make_env
import numpy as np
env = make_env()
def dump(obs):
    for o in sorted(obs.data, key=lambda o:o.name):
        f = obs.type_features[o.type]
        print(o.name, {k: round(float(v),4) for k,v in zip(f, obs.data[o])})
for seed in [0,1,2]:
    obs, info = env.reset(seed=seed)
    print("seed",seed); dump(obs)
env.close()
