import math, numpy as np
A,B,D=-0.087,-0.0125,1.99758
def cam(x,y,th): return (x+A*math.cos(th)-B*math.sin(th), y+A*math.sin(th)+B*math.cos(th))
def seg_box_dist(p,q,c,h):
    # distance between segment pq and axis-aligned box center c half h (0 if intersect), via dense sampling + exact
    best=1e9
    for t in np.linspace(0,1,4001):
        x=p[0]+t*(q[0]-p[0]); y=p[1]+t*(q[1]-p[1])
        dx=max(abs(x-c[0])-h[0],0); dy=max(abs(y-c[1])-h[1],0)
        # signed penetration
        if dx==0 and dy==0: d=-min(h[0]-abs(x-c[0]),h[1]-abs(y-c[1]))
        else: d=math.hypot(dx,dy)
        best=min(best,d)
    return best
def seg_pt_dist(p,q,c):
    px,py=q[0]-p[0],q[1]-p[1]; t=((c[0]-p[0])*px+(c[1]-p[1])*py)/(px*px+py*py); t=min(1,max(0,t))
    return math.hypot(p[0]+t*px-c[0],p[1]+t*py-c[1])
