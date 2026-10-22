from env_client import make_env
import json
edge=[];far=[]
for seed in range(400,600):
 e=make_env();s,i=e.reset(seed=seed,options={'object_count':3})
 for o in s.get_objects(e.observation_space.get_type('rectangle')):
  if s.get(o,'static'):continue
  x,y,w,h=[s.get(o,f) for f in ['x','y','width','height']]
  if x>1.5398:edge.append((seed,o.name,x,y,w,h))
  if x>1.5518:far.append((seed,o.name,x,y,w,h))
 e.close()
print(json.dumps({'far':far,'edges':edge}),flush=True)
