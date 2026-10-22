from probe_col_lib import R
import numpy as np
px,py=0.654,-0.199; h=0.05
def run(start,u,dth=None,label=''):
    r=R(0)
    r.path(0,[(1.0,-1.0),(1.6,-1.0),(1.6,0.6)] if start[1]>-0.2 else [(1.0,-1.0)])
    if dth is not None:
        r.step(0,0,0,dth)
    if not r.path(0,[start]): return
    p=r.push(0,*u)
    # dist from rover center to box
    cx=np.clip(p[0],px-h,px+h); cy=np.clip(p[1],py-h,py+h)
    print(label,'stop',np.round(p,4),'dbox=%.4f'%np.hypot(p[0]-cx,p[1]-cy),'dx=%.4f dy=%.4f'%(abs(p[0]-px)-h,abs(p[1]-py)-h))
    r.env.close()
run((px,-0.8),(0,1),label='from below')
run((1.3,py),(-1,0),label='from right')
run((1.3,py),(-1,0),dth=0.4,label='from right th rot')
run((px,0.4),(0,-1),label='from above')
d=0.5
run((px+h+d,py-h-d),(-1,1),label='diag to corner BR')
run((px+h+d,py-h-d),(-1,1),dth=0.4,label='diag to corner BR rot')
run((px+h+d,py-h-d),(-1,1),dth=-0.4,label='diag to corner BR rot-')
run((px+h+0.4,py-h-0.2),(-2,1),label='dir(-2,1) to corner BR')
