from probe_col_lib import R
from probe_col_bounds import approach, rot
import numpy as np
c=np.array([0.654,-0.199])
r=R(0)
r.goto(0,1.0,-1.0); r.goto(0,*(c+[0.25,0.08]))
print('A',r.pos(0)[:2]-c)
q=r.step(0,-0.17,0.17); print('diag step through corner -> rel',q[:2]-c)
# rotation in contact
r.goto(0,1.3,-1.0); r.goto(0,1.3,c[1]); p=approach(r,0,c); print('contact rel',p[:2]-c,p[2])
for d in [0.4,-0.4,0.2,-0.2]:
    q=r.step(0,0,0,d); print('rot',d,'->th %.4f pos'%q[2],q[:2]-c)
# rover-rover: simultaneous moves both toward wall at same y
r.goto(1,-1.0,-1.75); 
a=np.array([0,0,0,0,0,0,0,0],np.float32)
print(r.pos(0),r.pos(1))
r.env.close()
