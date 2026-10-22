from pC_lib import *
import numpy as np
reset(11)
sx,sy=g('sample0','x'),g('sample0','y'); goto(1,-1.5,-1.0); goto(1,sx,sy); step(s1='sample')
# obstacle11 (-0.742,-0.793); put rover1 behind it on line from lander
L=np.array([-1.9,-2.0]); O=np.array([-0.742,-0.793]); u=(O-L)/np.linalg.norm(O-L)
for k in [0.45,0.6]:
    p=O+k*u; print(goto(1,*p),R(1)); step(s1='send'); print('behind obstacle',k,SM(0)[6])
