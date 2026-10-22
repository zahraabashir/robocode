from env_client import make_env
import numpy as np
E=make_env()
s,i=E.reset(seed=0)
print('INFO',i,'MAX',E.max_steps)
for typ in E.observation_space.types:
 print('TYPE',typ)
 for obj in s.get_objects(typ):
  print(obj, {f:s.get(obj,f) for f in E.observation_space.type_features[typ]})
E.close()
