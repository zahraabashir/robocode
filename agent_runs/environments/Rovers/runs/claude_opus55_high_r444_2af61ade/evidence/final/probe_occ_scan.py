from probe_send_lib import *
import time
t=time.time()
for seed in range(6):
    e=E(seed)
    out=[]
    for o in e.obs:
        if o.type.name in('sample','obstacle'):
            out.append((o.name[:6],round(e.g(o.name,'x'),2),round(e.g(o.name,'y'),2)))
    print(seed,out)
print(e.feats('rover0'), [o.name for o in e.obs][:3], time.time()-t)
for o in e.obs:
    if o.type.name=='sample': print(o.name, e.feats(o.name)); break
