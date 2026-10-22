from pA_lib import P
import numpy as np
p=P(0)
for th in [0,np.pi/4,np.pi/2]:
    p.goto(1,-0.8,-1.0); s=p.goto(1,-0.8,-2.0,th); q=p.bisect(1,-1,0); print('th',round(th,2),'start',np.round(s,3),'lander +x side dx',round(q[0]+1.9,4))
    p.goto(1,-0.8,-1.0); p.goto(1,-1.2,-1.0); s=p.goto(1,-1.2,-1.0,th); q=p.bisect(1,0,-1); print('   start',np.round(s,3),'x=-1.2 from +y dy',round(q[1]+2.0,4))
    p.goto(1,-0.8,-1.0); p.goto(1,-1.5,-1.2); s=p.goto(1,-1.5,-1.2,th); q=p.bisect(1,0,-1); print('   start',np.round(s,3),'x=-1.5 from +y dy',round(q[1]+2.0,4))
