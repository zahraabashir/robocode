from geom_lib import *
from geom_wall import corners
P=Prober()
seed=20
o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
d=M@np.array([0,-1.0])
P.nav(c+M@np.array([0,0.5]))
for k in range(150):
    prev=P.obs.copy(); P.step(d*0.03)
    if np.abs(P.obs[0:3]-prev[0:3]).max()>0.2 or k%10==0:
        cs=corners(P.obs); print(k,'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'vel',np.round(P.obs[3:6],2),'cmin',np.round(cs.min(0),3),'cmax',np.round(cs.max(0),3))
    if np.abs(P.obs[0:3]-prev[0:3]).max()>0.2: break
