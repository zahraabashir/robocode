from env_client import make_env
import json
cases=[]
for seed in range(1000,2500):
 e=make_env();s,i=e.reset(seed=seed);b=next(iter(s.get_objects(e.observation_space.get_type('target_block'))));g=next(iter(s.get_objects(e.observation_space.get_type('target_surface'))))
 x,w=s.get(b,'x'),s.get(b,'width');gx,gw=s.get(g,'x'),s.get(g,'width')
 possible=False
 for dest in (gx+.002,gx+gw-w-.002):
  low=max(.1002-x,.1002-dest,-.022);high=min(1.5178-x,1.5178-dest,w+.022)
  possible |= low<=high
 if not possible:
  row={'seed':seed,'block':[x,w],'surface':[gx,gw]};cases.append(row);print(json.dumps(row),flush=True)
 e.close()
print('FOUND',len(cases),flush=True)
