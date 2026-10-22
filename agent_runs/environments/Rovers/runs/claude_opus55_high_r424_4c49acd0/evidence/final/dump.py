from env_client import make_env
import sys
env = make_env()
seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
obs, info = env.reset(seed=seed)
print(info)
for t in env.observation_space.types:
    feats = env.observation_space.type_features[t]
    for o in obs.get_objects(t):
        print(o.name, {f: round(float(obs.get(o,f)),3) for f in feats})
env.close()
