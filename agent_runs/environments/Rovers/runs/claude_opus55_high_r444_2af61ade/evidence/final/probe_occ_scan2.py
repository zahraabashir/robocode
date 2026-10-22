from probe_send_lib import *
from concurrent.futures import ThreadPoolExecutor
def f(seed):
    e=E(seed); pil=[];sm=[]
    for o in e.obs:
        n=o.name
        if o.type.name=='obstacle' and e.g(n,'half_x')<0.1: pil.append((round(e.g(n,'x'),2),round(e.g(n,'y'),2)))
        if o.type.name=='sample': sm.append((round(e.g(n,'x'),2),round(e.g(n,'y'),2)))
    e.env.close()
    bad=[p for p in pil if p[0]<1.0 and p[1]<0.3]
    rs=[s for s in sm if s[0]>0.1 and s[1]<0.5]
    return seed,len(bad),rs,bad
with ThreadPoolExecutor(12) as ex:
    for r in ex.map(f,range(6,66)):
        if r[1]<=1 and r[2]: print(r)
