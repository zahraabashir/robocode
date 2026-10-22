from probe_coll_util import *
for s in range(30):
    obs,_=env.reset(seed=s)
    P=[v for v in obst(obs).values() if v[2]<0.1]
    okR=all(not(-0.1<p[0]<1.4 and -2.5<p[1]<2.5 and not (p[0]>1.25)) for p in P)
    okL=all(not(-1.4<p[0]<0.1) for p in P)
    if okR or okL: print(s,okR,okL)
