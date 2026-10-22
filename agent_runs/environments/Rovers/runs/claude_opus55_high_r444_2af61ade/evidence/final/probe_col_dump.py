from env_client import make_env
import numpy as np, sys
env=make_env()
for s in [0,1,2]:
    obs,info=env.reset(seed=s)
    print('seed',s)
    for o in obs:
        feats={}
        for f in ['x','y','z','theta','half_x','half_y']:
            try: feats[f]=round(float(obs.get(o,f)),3)
            except Exception: pass
        print(' ',o.name,o.type.name,feats)
env.close()
