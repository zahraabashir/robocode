from probe_send_lib import *
import numpy as np
for x in [0.25,0.5,1.0,1.5]:
    r=test([(x,y) for y in np.arange(-1.6,-2.45,-0.01)])
    print(x, r[-2:])
for y in [-2.25,-2.4,-2.1]:
    r=test([(x,y) for x in np.arange(2.3,0.5,-0.01)])
    print(y, r[-2:])
