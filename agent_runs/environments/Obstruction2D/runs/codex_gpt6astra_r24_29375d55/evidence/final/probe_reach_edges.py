from env_client import make_env
from approach import GeneratedApproach
import json
edge=[];inaccessible=[]
for seed in range(500,1000):
 e=make_env();s,i=e.reset(seed=seed);a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i)
 for o in a.obstacles(s)+[a.block]:
  x,y,w,h=a.rect(s,o)
  if x>1.52 or x+w<.10:edge.append((seed,o.name,x,w))
  if not a.offsets(x,x,w):inaccessible.append((seed,o.name,x,y,w,h))
 e.close()
print(json.dumps({'inaccessible':inaccessible,'edges':edge}));
