from env_client import make_env
env = make_env()
for seed in [0,1]:
    obs, info = env.reset(seed=seed)
    print("seed", seed, info)
    for t in obs.get_objects(None) if False else []: pass
    for name in obs.get_object_names():
        o = obs.get_object_from_name(name)
        tname = o.type.name if hasattr(o.type,'name') else o.type
        feats = env.observation_space.type_features[env.observation_space.get_type(tname)] if False else None
        print(name, tname, end=' ')
        for typ in ['rover','lander','objective','sample','obstacle']:
            pass
        print()
    for typ in env.observation_space.types:
        for o in obs.get_objects(typ):
            print(o.name, [round(float(obs.get(o,f)),3) for f in env.observation_space.type_features[typ]])
env.close()
