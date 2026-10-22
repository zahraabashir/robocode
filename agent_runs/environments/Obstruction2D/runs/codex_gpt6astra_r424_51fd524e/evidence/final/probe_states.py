from env_client import make_env
import json
e=make_env()
print('limit',e.max_steps)
for seed in range(5):
 s,i=e.reset(seed=seed)
 print('SEED',seed,'INFO',i)
 for n in sorted(s.get_object_names()):
  o=s.get_object_from_name(n)
  print(n,o.type.name,{f:round(s.get(o,f),4) for f in e.observation_space.type_features[o.type] if not f.startswith('color') and f!='z_order'})
e.close()
