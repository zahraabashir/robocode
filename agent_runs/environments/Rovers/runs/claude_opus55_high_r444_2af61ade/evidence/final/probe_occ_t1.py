from probe_occ_lib import *
import time
t=time.time()
r=sweep(44,(0.6,-0.35),math.pi,(-1.0,-1.406),0.0,(0,1),step=0.01,n=40)
print(r,time.time()-t)
