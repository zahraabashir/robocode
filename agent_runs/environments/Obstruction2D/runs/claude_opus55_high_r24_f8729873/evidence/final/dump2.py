from env_client import make_env
import sys
env = make_env()
seed=int(sys.argv[1]); cnt=int(sys.argv[2]) if len(sys.argv)>2 else None
obs, info = env.reset(seed=seed, options={'object_count':cnt} if cnt else None)
for n in sorted(obs.get_object_names()):
    o=obs.get_object_from_name(n)
    fs=["x","y","width","height"] if n!='robot' else ['x','y']
    print(n, {f: round(float(obs.get(o,f)),3) for f in fs})
