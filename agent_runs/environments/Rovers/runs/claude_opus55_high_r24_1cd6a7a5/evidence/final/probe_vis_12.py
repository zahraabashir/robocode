from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV='rover0'
seed=2; name='objective0'; pill=np.array([0.735,0.444])
r=float(sys.argv[1]); s=float(sys.argv[2]); ths=eval(sys.argv[3])
reset(seed); o=objpos(name)[:2]
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
p=o+r*u+s*n; q=goto([(1.0,-1.75),(p[0],-1.75),tuple(p)])
brg=np.degrees(np.arctan2(*(o-q[:2])[::-1]))
print('at',q.round(4),'bearing',round(brg,2))
out=[]
for thd in ths:
    turn(np.deg2rad(thd)); c=cal()
    if c>0.5: step(op=-1/6)
    rel=(brg-thd+180)%360-180
    out.append(f"{thd}({rel:.0f}):{int(c)}")
print(' '.join(out))
