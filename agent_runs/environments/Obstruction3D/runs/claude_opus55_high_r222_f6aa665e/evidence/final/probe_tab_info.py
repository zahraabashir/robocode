from env_client import make_env
from kin import *
import numpy as np
env = make_env()
for seed in [0,1,2]:
    obs, info = env.reset(seed=seed)
    for o in obs:
        pass
    print(type(obs))
    try:
        names=[o.name for o in obs]
    except Exception as e: names=None; print(e)
    print(names)
    for n in names or []:
        o=obs.get_object_from_name(n)
        f=[k for k in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z'] ]
        try: print(n,[round(float(obs.get(o,k)),3) for k in f])
        except Exception as e: print(n,e)
st=env.get_state(); print(type(st), str(st)[:300])
env.close()
