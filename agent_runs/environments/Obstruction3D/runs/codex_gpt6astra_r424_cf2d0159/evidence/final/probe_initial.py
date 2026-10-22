from env_client import make_env
import numpy as np
E=make_env(); s,info=E.reset(seed=0)
print('info',info,'max',E.max_steps)
for t in E.observation_space.types:
 for o in s.get_objects(t):
  print(o.name,{f:round(s.get(o,f),6) for f in E.observation_space.type_features[t]})
E.close()
