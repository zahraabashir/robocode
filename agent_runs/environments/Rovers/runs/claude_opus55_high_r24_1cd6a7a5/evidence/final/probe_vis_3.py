from probe_vis_lib import *
import time
t=time.time()
print(scan(2,'objective2',-np.pi/2,2.1,1.8,0.01,via=[(-0.492,-1.75)]))
print(time.time()-t)
