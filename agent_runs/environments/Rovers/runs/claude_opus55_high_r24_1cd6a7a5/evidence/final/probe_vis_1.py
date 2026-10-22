from probe_vis_lib import *
import probe_vis_lib as L
t=time.time()
for th in [0,np.pi/2,np.pi,-np.pi/2]:
  for p in [(-1.5,0.25),(-1.57,0.31)]:
    reset(2); goto([(-1.0,p[1]),p]); q=turn(th); c=cal()
    print(p,th,L.pos().round(4),c)
print(time.time()-t)
