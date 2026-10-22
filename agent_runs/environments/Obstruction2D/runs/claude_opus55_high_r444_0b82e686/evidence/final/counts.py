import time
from env_client import make_env
from collections import Counter
env=make_env(); c=Counter(); t=time.time()
for s in range(30):
    o,i=env.reset(seed=s); c[i['object_count']]+=1
print(c, time.time()-t)
