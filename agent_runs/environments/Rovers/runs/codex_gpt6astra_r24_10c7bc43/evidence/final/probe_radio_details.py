from env_client import make_env
from approach import GeneratedApproach
from scipy.sparse.csgraph import dijkstra
import numpy as np

def trial(seed,j,target):
 e=make_env();s,_=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
 r=p.rovers[j]
 def xy():return p.xy(s,r)
 def step(move,op):
  nonlocal s
  a=np.zeros(8);a[4*j:4*j+2]=move;a[4*j+3]=op;s,*_=e.step(a)
 def go(t,im=False):
  end=p.nearest(np.array(t))
  for k in range(120):
   q=xy();start=p.nearest(q)
   if np.linalg.norm(q-p.points[end])<.02:break
   dist,pred=dijkstra(p.graph,indices=start,return_predecessors=True)
   path=[end]
   while path[-1]!=start:
    z=int(pred[path[-1]])
    if z<0:return False
    path.append(z)
   dest=p.points[path[-2] if len(path)>1 else end]
   move=np.clip(dest-q,-.2,.2)
   op=(-1/6 if s.get(r,'calibrated') else -.5) if im else 0
   step(move,op)
   if np.linalg.norm(xy()-q)<1e-6:return False
  return True
 go((1 if j==0 else -1.8,.9),True)
 for k in range(2):step([0,0],-1/6 if s.get(r,'calibrated') else -.5)
 have=sum(s.get(o,'have_image_rover'+str(j)) for o in p.objs)
 ok=go(target)
 step(np.clip(np.array(target)-xy(),-.2,.2),0)
 step([0,0],.5)
 rec=sum(s.get(o,'received_image') for o in p.objs)
 print(seed,j,target,'actual',xy(),'have',have,'received',rec,'go',ok,flush=True)
 if seed==2 and target==(-2.2,0):
  print('obs',p.boxes.tolist(),flush=True)
 e.close()
for t in [(1,.62),(1,.625),(1,.63),(1,.635),(1,.64),(.9,.74),(1.1,.505)]:trial(0,0,t)
