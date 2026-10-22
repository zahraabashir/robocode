from env_client import make_env

env = make_env()
for seed in range(2):
    obs, info = env.reset(seed=seed)
    print("SEED", seed, "info", info, "max", env.max_steps)
    print("types", env.observation_space.types)
    for name in obs.get_object_names():
        obj = obs.get_object_from_name(name)
        typ = obj.type.name if hasattr(obj.type, "name") else str(obj.type)
        feats = env.observation_space.type_features[obj.type]
        print(name, typ, {f: float(obs.get(obj, f)) for f in feats})
env.close()
