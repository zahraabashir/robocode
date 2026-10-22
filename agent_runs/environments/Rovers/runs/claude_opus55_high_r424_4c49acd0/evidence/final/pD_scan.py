from pB_lib import *
env=make_env()
for seed in range(60):
    obs,_=env.reset(seed=seed)
    P=[]; O=[]
    for n in obs.get_object_names():
        v=obs.vec([obs.get_object_from_name(n)])
        if n.startswith('obstacle') and abs(v[3]-0.05)<1e-3: P.append((round(v[0],2),round(v[1],2)))
        if n.startswith('objective'): O.append((round(v[0],2),round(v[1],2)))
    bad=[p for p in P if -2.1<p[0]<1.3 and -2.3<p[1]<0.5]
    if len(bad)==0: print(seed,'objs',O,'pillars',P)
