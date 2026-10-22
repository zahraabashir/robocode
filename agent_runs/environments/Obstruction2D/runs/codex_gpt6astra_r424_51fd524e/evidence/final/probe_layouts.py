from env_client import make_env
import json
e=make_env(); out=[]
for count in [0,1,2,3,5,10,20]:
 for seed in range(10):
  s,i=e.reset(seed=seed,options={'object_count':count})
  rows=[]
  for o in s.get_objects(e.observation_space.get_type('rectangle')):
   rows.append(dict(name=o.name,**{f:s.get(o,f) for f in ['x','y','width','height','theta']}))
  out.append(dict(seed=seed,count=count,rows=rows))
 print('count',count,'last actual',len(rows)-2,flush=True)
json.dump(out,open('layouts.json','w'));e.close()
