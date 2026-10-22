exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
import math
L=np.array([-1.9,-2.0])
for yy in [-2.1,-2.3,-1.5]:
    if yy==-1.5:
        pts=[(x,yy) for x in np.arange(2.2,1.6,-0.003)]
        r=scan((0,0),pts,lambda: goto(1,-1.0,-1.0))
    else:
        pts=[(x,yy) for x in np.arange(2.2,1.8,-0.003)]
        r=scan((0,0),pts)
    q=pos(0)[:2]; print(yy, np.round(q,4), 'dist', round(math.hypot(q[0]-L[0],q[1]-L[1]),4))
