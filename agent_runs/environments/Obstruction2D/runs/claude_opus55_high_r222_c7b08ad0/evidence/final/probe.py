from env_client import make_env
import sys
env = make_env()
tf = env.observation_space.type_features
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    obs, info = env.reset(seed=seed)
    print("seed", seed, info)
    for n in sorted(obs.get_object_names()):
        o = obs.get_object_from_name(n)
        print(" ", n, o.type.name, {f: round(float(obs.get(o,f)),3) for f in tf[o.type]})
env.close()
