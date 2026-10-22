from pC_lib import *
import numpy as np
reset(11)
def O(): return [round(g('objective0',f),3) for f in ['have_image_rover0','have_image_rover1','received_image']]
goto(1,-1.5,-1.0); goto(1,-1.5,1.0)
for th in [np.pi/2, 2.0, 2.5, np.pi, 0, -np.pi/2]:
  for y in [1.0,1.3,1.4]:
    ok=goto(1,-2.0,y,th); step(s1='calibrate'); c=R(1)[4]
    step(s1='image'); print(th,y,ok,R(1),O())
