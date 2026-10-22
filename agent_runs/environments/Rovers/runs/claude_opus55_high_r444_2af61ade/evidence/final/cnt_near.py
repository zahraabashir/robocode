from test_approach import make_env
import numpy as np
env=make_env(); c=[]
for s in range(0,800,4):
    o,_=env.reset(seed=s)
    T=o.get_object_from_name('sample0').type
    d=min(np.hypot(o.get(x,'x')+1.9,o.get(x,'y')+2.0) for x in o.get_objects(T))
    if d<0.3: c.append((s,round(d,3)))
print(len(c),c)
