import time, numpy as np
from env_client import make_env
import approach, navgrid
env=make_env(); obs,_=env.reset(seed=5)
m=approach.Model(obs)
t=time.time(); g=navgrid.NavGrid(m,obs[0:2],obs[2],0.115); src,d,pr=g.from_source(obs[16:18]); print("t",time.time()-t)
print(np.isfinite(d).sum(), g.free.sum(), d[navgrid.cell_of(obs[0:2]+np.array([0,0.4]))])
