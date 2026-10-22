from env_client import make_env
import numpy as np
from common import *
env = make_env()
mins={}; maxs={}; counts=[]; rots=0; bases=set()
for s in range(60):
    obs,info=env.reset(seed=s)
    names=obs.get_object_names(); counts.append(len(names)-3)
    bases.add(tuple(np.round(getbase(obs),3)))
    for n in names:
        if n=='robot': continue
        d=objd(obs,n); k=n.rstrip('0123456789')
        v=np.array([d['pose_x'],d['pose_y'],d['pose_z']])
        mins[k]=np.minimum(mins.get(k,v),v); maxs[k]=np.maximum(maxs.get(k,v),v)
        if abs(d['pose_qw'])<0.9999: rots+=1
print('counts',sorted(set(counts)), np.bincount(counts)); print('rotated',rots); print('bases',bases)
for k in mins: print(k, np.round(mins[k],3), np.round(maxs[k],3))
