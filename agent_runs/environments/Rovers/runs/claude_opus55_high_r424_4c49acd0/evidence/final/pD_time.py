import time
from pD_lib import *
S=(0.4,-0.6,np.pi); t=time.time()
print(trial((S,pos_on_line(S,0.5,0.0,0))), time.time()-t)
