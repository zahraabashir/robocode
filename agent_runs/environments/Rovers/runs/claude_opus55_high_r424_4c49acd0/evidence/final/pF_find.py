from pE_lib import *
for seed in range(40):
    s=Sim(seed); P=[];S=[]
    for n in s.obs.get_object_names():
        o=s.obs.get_object_from_name(n); v=s.obs.vec([o])
        if str(n).startswith('obstacle') and abs(float(s.obs.get(o,'half_x'))-0.05)<1e-3: P.append(v[:2])
        if str(n).startswith('sample'): S.append(v[:2])
    for p in P:
        if 0.6<p[0]<1.7 and -1.3<p[1]<1.2:
            d=min([np.hypot(*(p-q)) for q in P if np.hypot(*(p-q))>1e-6]+[np.hypot(*(p-q)) for q in S])
            if d>0.75: print(seed,p.round(3),round(d,3),flush=True)
    s.env.close()
