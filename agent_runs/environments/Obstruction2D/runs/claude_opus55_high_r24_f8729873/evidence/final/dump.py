from env_client import make_env
import sys
env = make_env()
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    obs, info = env.reset(seed=seed)
    print("seed", seed, type(obs))
    for n in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(n) if isinstance(n,str) else n
        print(" ", o, {f: round(float(obs.get(o, f)),3) for f in ["x","y","theta","width","height","static"] if True} if 'robot' not in str(o) else {f: round(float(obs.get(o,f)),3) for f in env.observation_space.type_features[env.observation_space.get_type('crv_robot')] } )
env.close()
