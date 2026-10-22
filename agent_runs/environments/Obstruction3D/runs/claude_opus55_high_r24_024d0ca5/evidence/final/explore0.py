from env_client import make_env
import numpy as np
env = make_env()
for seed in [0,1]:
    obs, info = env.reset(seed=seed)
    print("info", info)
    for n in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(n) if isinstance(n,str) else n
        name = n if isinstance(n,str) else n.name
        t = o.type if hasattr(o,'type') else None
        print(name, t, {f: round(float(obs.get(o,f)),4) for f in env.observation_space.get_type(t.name if hasattr(t,'name') else t).features} if False else "")
    print(type(obs), dir(obs)[:60])
env.close()
