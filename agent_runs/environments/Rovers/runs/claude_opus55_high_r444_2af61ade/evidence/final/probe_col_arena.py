from probe_col_lib import R
import numpy as np
r=R(0)
# rover0: push +x at y=-1.75, -y, then to +y along x=1.0 (avoid obstacles)
print('r0 +x', r.push(0,1,0))
print('r0 -y', r.push(0,0,-1))
r.path(0,[(1.0,-1.75),(1.0,0.5)])
print('r0 +y at x=1.0',r.push(0,0,1))
r.path(0,[(1.0,0.5),(0.3,-1.75)])
print('r0 -x at y=-1.75',r.push(0,-1,0))
# rover1
print('r1 -x', r.push(1,-1,0))
print('r1 -y', r.push(1,0,-1))
r.path(1,[(-1.0,-1.75),(-1.0,1.3)])
print('r1 +y at x=-1',r.push(1,0,1))
r.path(1,[(-1.0,1.3),(-0.3,-1.75)])
print('r1 +x at y=-1.75',r.push(1,1,0))
