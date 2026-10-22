from env_client import make_env


def f(state, obj, name):
    return float(state.get(obj, name))


for seed in range(12):
    env = make_env()
    state, info = env.reset(seed=seed)
    print("SEED", seed, "max_steps", env.max_steps, "info", info)
    print("names", len(state.get_object_names()), state.get_object_names())
    for typ in env.observation_space.types:
        objs = state.get_objects(typ)
        print(" TYPE", typ.name if hasattr(typ, "name") else typ, "n", len(objs))
        for o in objs:
            vals = {x: f(state, o, x) for x in env.observation_space.type_features[typ]}
            print("  ", o.name if hasattr(o, "name") else o, vals)
    env.close()
