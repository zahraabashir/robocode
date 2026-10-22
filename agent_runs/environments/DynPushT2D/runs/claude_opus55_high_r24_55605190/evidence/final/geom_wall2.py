from geom_lib import *
from geom_wall import corners
P=Prober()
for seed in [12,20,24,31]:
    o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
    d=M@np.array([0,-1.0])  # stem direction
    P.nav(c+M@np.array([0,0.5]))
    lo,hi=[],[]
    for k in range(150):
        P.step(d*0.03)
        cs=corners(P.obs); lo.append(cs.min(0)); hi.append(cs.max(0))
    lo=np.min(lo,0); hi=np.max(hi,0)
    print('seed',seed,'stemdir',np.round(d,2),'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'corner min',np.round(lo,3),'max',np.round(hi,3))
