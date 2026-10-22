from pC_lib import *
import numpy as np
reset(11)
def O(): return [round(g('objective0',f),3) for f in ['have_image_rover0','have_image_rover1','received_image']]
goto(1,-1.5,-1.0); goto(1,-2.0,1.0,np.pi/2); step(s1='calibrate'); step(s1='image'); print(O(),R(1))
r=step(s1='send'); print('send img',r,O(),R(1))
goto(1,-1.5,-1.0); r=goto(1,-1.0,-1.75,0.0); print('home',R(1),S.te,S.tr,S.n)
# sample soil(sample5 left) and rock(sample0 left) via rover1
for j in [0,5]:
    sx,sy=g(f'sample{j}','x'),g(f'sample{j}','y')
    goto(1,-1.5,sy); goto(1,sx,sy); r=step(s1='sample'); print(j,R(1),SM(j)); r=step(s1='send'); print('send',r,SM(j)); r=step(s1='drop'); print(r)
goto(1,-1.5,-1.0); goto(1,-1.0,-1.75,0.0); print('home',R(1),S.te,S.tr,S.n)
r=step(); print(r)
