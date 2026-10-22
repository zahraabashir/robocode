from env_client import make_env
import numpy as np
env=make_env()
for s in range(6):
    obs,_=env.reset(seed=s)
    print('seed',s)
    for o in obs:
        t=o.type.name
        if t=='obstacle':
            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','z','half_x','half_y','half_z']])
        elif t=='objective':
            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','z']])
        elif t=='sample':
            print(' ',o.name,[round(obs.get(o,f),3) for f in ['x','y','is_soil']])
env.close()
