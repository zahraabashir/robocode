from probe_vis_lib import *
import probe_vis_lib as L, sys
seed=2; name='objective2'
R=float(sys.argv[1]); a0=float(sys.argv[2]); a1=float(sys.argv[3]); da=float(sys.argv[4]); thd=float(sys.argv[5])
reset(seed); c=objpos(name)[:2]
P=lambda a: tuple(c+R*np.array([np.cos(np.deg2rad(a)),np.sin(np.deg2rad(a))]))
s=P(a0); goto([(-1.0,-1.75),(-1.0,s[1]),s]); turn(np.deg2rad(thd))
cal(); step(op=-1/6); print('pre',imaged())
n=int(round(abs(a1-a0)/da))+1
for i in range(n):
    a=a0+(a1-a0)*i/(n-1); q=goto([P(a)])
    cal(); step(op=-1/6)
    if name in imaged():
        print('visible at ang',a,q.round(4)); break
else: print('never')
