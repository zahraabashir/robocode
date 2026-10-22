from env_client import make_env
import numpy as np
env=make_env()
for s in range(60):
    o,_=env.reset(seed=s)
    if 1.7<o[0]<3.3 and 1.7<o[1]<3.3: print(s, np.round(o[[0,1,2,12,13,14,16,17]],4))
