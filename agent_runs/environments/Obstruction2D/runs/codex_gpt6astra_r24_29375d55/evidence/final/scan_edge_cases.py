from env_client import make_env
import json
for seed in range(600,1100):
 e=make_env();s,i=e.reset(seed=seed,options={'object_count':3})
 edge=[(o.name,s.get(o,'x'),s.get(o,'width')) for o in s.get_objects(e.observation_space.get_type('rectangle')) if o.type.name!='target_surface' and (s.get(o,'x')>1.5518 or s.get(o,'x')+s.get(o,'width')<.0662)]
 if edge:print(json.dumps({'seed':seed,'edge':edge}),flush=True)
 e.close()
print('completed',flush=True)
