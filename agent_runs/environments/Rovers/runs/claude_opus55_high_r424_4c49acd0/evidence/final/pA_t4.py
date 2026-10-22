from pA_lib import P
import numpy as np
p=P(0)
p.goto(1,-1.08,-1.0); s=p.goto(1,-1.08,1.42,0); print('reached',np.round(s,3))
u=np.array([1,1])/np.sqrt(2); q=p.bisect(1,*u); print('mound corner dist',round(np.linalg.norm(q[:2]-np.array([-0.75,1.75])),4),np.round(q[:2],4))
