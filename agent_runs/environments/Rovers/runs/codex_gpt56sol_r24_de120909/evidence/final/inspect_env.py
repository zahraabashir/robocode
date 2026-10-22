from env_client import make_env

for seed in range(4):
    env = make_env()
    s, info = env.reset(seed=seed)
    print("SEED", seed, "max", env.max_steps, "info", info)
    for name in sorted(s.get_object_names()):
        o = s.get_object_from_name(name)
        fs = s.type_features[o.type]
        print(name, dict(zip(fs, [s.get(o, f) for f in fs])))
    env.close()
