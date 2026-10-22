from probe_send_lib import *
import time
t=time.time()
# move along x=0.3 downward from -1.75 to -2.25 in steps
print(test([(0.3,y) for y in [-1.8,-1.85,-1.9,-1.95,-2.0,-2.05,-2.1,-2.15,-2.2,-2.25]]))
print(time.time()-t)
print(test([(x,-2.25) for x in [2.0,1.8,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.3]]))
