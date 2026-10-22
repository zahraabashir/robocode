import numpy as np
import scipy.ndimage as ndi
import json
import approach
from env_client import make_env
approach.assign_tasks=lambda policy,state: None
E=make_env();out=[]
for seed in range(5000,6000):
 s,info=E.reset(seed=seed);A=approach.GeneratedApproach(E.action_space,E.observation_space,{});A.reset(s,info)
 labels,_=ndi.label(A.free.reshape(A.size,A.size));labels=labels.ravel();reachable=np.zeros(len(labels),bool);why=[]
 for r in range(2):
  if not A.valid(A.home[r][None,:])[0]:why.append('home%d_inside_margin'%r)
  root=np.argmin(np.linalg.norm(A.points-A.home[r],axis=1)+(~A.free)*100)
  reachable |= labels==labels[root]
 for k,o in enumerate(A.objectives):
  if not np.any(A.masks[('image',k)]&reachable):why.append('image%d_unreachable'%k)
 for soil in range(2):
  if not any(np.any(A.masks[('sample',k)]&reachable) for k,o in enumerate(A.samples) if int(s.get(o,'is_soil'))==soil):why.append('sample%d_unreachable'%soil)
 if why:
  print(seed,why,flush=True);out.append((seed,why))
 if seed%100==0:print('PROGRESS',seed,flush=True)
open('scan_results.json','w').write(json.dumps(out));E.close();print('DONE',len(out),flush=True)
