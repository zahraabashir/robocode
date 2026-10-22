from env_client import make_env
from approach import GeneratedApproach
from scipy.sparse.csgraph import dijkstra
import numpy as np
for seed in range(200):
 e=make_env();s,_=e.reset(seed=seed)
 samples=sorted(s.get_objects(e.observation_space.get_type('sample')),key=lambda o:o.name)
 coords=np.array([[s.get(o,'x'),s.get(o,'y')] for o in samples])
 pairs=[(i,j) for i in range(3) for j in range(3,6) if np.linalg.norm(coords[i]-coords[j])<.44]
 if not pairs:e.close();continue
 p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
 found=False
 for stone,soil in pairs:
  d1=np.linalg.norm(p.points-coords[stone],axis=1);d2=np.linalg.norm(p.points-coords[soil],axis=1)
  ids=np.flatnonzero(p.valid&(d1<.245)&(d2<d1-.025))
  for end in ids:
   j=0 if p.points[end,0]>0 else 1;r=p.rovers[j]
   dist,pred=dijkstra(p.graph,indices=p.nearest(p.homes[j]),return_predecessors=True)
   if np.isfinite(dist[end]):found=True;break
  if found:break
 if not found:e.close();continue
 print('seed',seed,'pair',stone,soil,'coords',coords.tolist(),'target',p.points[end].tolist(),'dist',d1[end],d2[end],flush=True)
 def step(move,op):
  global s
  a=np.zeros(8);a[4*j:4*j+2]=move;a[4*j+3]=op;s,*_=e.step(a)
 for k in range(130):
  q=p.xy(s,r);start=p.nearest(q)
  if np.linalg.norm(q-p.points[end])<.01:break
  dist,pred=dijkstra(p.graph,indices=start,return_predecessors=True);path=[end]
  while path[-1]!=start:
   z=int(pred[path[-1]])
   if z<0:break
   path.append(z)
  dest=p.points[path[-2] if len(path)>1 else end];step(np.clip(dest-q,-.2,.2),0)
  if np.linalg.norm(p.xy(s,r)-q)<1e-7:break
 print('arrived',p.xy(s,r).tolist(),flush=True)
 for rep in range(3):
  step([0,0],-5/6)
  print('sample',rep,'full',s.get(r,'store_full'),'analyzed',[o.name for o in samples if s.get(o,'analyzed_rover'+str(j))],flush=True)
  step([0,0],5/6)
 e.close()
 break
