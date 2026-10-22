import numpy as np
from approach import *
pose=np.array([3.846,1.935,-0.482]); 
for rx in [3.277,3.326]:
    pl=to_local(np.array([[rx,1.95]]),pose); print(pl, dist_to_T_local(pl, rects_local(0.141,1.102,1.137)))
