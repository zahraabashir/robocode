from env_client import make_env


def objects(obs, space, typ):
    t = next(t for t in space.types if t.name == typ)
    out = []
    for o in obs.get_objects(t):
        out.append((o.name, {f: float(obs.get(o, f)) for f in space.type_features[t]}))
    return out


for seed in range(5):
    env = make_env()
    obs, info = env.reset(seed=seed)
    print("SEED", seed, "max", env.max_steps, "info", info)
    for typ in ("rover", "lander", "objective", "sample", "obstacle"):
        print(typ, objects(obs, env.observation_space, typ))
    env.close()
