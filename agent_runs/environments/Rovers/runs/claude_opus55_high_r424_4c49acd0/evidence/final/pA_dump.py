from env_client import make_env
import numpy as np,sys
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0)
for n in sorted(obs.get_object_names()):
    o=obs.get_object_from_name(n)
    fs=[f for f in ['x','y','z','theta','half_x','half_y','half_z','store_full','calibrated','at_home'] ]
    vals={}
    for f in fs:
        try: vals[f]=round(float(obs.get(o,f)),3)
        except Exception: pass
    print(n,vals)
