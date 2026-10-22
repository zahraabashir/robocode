from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV='rover0'
seed=2; name='objective0'; pill=np.array([0.735,0.444])
reset(seed); o=objpos(name)[:2]
r=float(sys.argv[1]); thd=float(sys.argv[2]); s0,s1,ds=map(float,sys.argv[3:6])
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
goto([(1.0,-1.75),(0.9,-1.75)]); turn(np.deg2rad(thd))
res=[]
for s in np.arange(s0,s1+1e-9,ds):
    p=o+r*u+s*n; q=goto([tuple(p)])
    if np.linalg.norm(q[:2]-p)>1e-4: res.append((round(s,3),'X')); continue
    c=cal()
    if c>0.5: step(op=-1/6)
    res.append((round(s,3),int(c)))
print(r,thd,' '.join(f"{a}:{b}" for a,b in res))
