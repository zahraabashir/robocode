from env_client import make_env
env = make_env()
for seed in [0,1,2]:
    obs, info = env.reset(seed=seed)
    print("seed", seed, info)
    for name in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(name) if isinstance(name,str) else name
        t = o.type if hasattr(o,'type') else None
        print(name, t, {f: round(obs.get(o,f),3) for f in env.observation_space.get_type(t.name if hasattr(t,'name') else t).__dict__.get('feature_names', [])} if False else '')
    print(obs)
env.close()
