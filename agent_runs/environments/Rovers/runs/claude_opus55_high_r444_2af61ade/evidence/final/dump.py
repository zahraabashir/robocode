from env_client import make_env
env = make_env()
for seed in [0,1]:
    obs, info = env.reset(seed=seed)
    print("seed",seed, info)
    for o in obs:
        print(o.name, o.type.name, [round(float(v),3) for v in obs.data[o]])
env.close()
