import numpy as np
from env_client import make_env
env=make_env()
from collections import Counter
c={}
for s in range(51):
    obs,info=env.reset(seed=s)
    c[s]=info.get('object_count')
print(Counter(c.values()))
print({k:v for k,v in c.items() if v==min(c.values())})
print(info.keys(), getattr(env,'max_steps',None))
obs,info=env.reset(seed=0)
for n in sorted(obs.get_object_names()): print(n)
