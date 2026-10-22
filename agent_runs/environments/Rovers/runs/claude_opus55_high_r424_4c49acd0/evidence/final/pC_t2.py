from pC_lib import *
import numpy as np
reset(11)
sx,sy=g('sample3','x'),g('sample3','y'); print('sample exact',sx,sy)
goto(0,1.0,sy)
# fine threshold along x, theta pi
for d in [0.252,0.251,0.2505,0.25,0.2495,0.249]:
    goto(0,sx+d,sy); step(s0='sample'); print(d, g('rover0','x')-sx, R(0)[3])
    if R(0)[3]: break
print('after sample',SM(3))
step(s0='drop'); print('drop',R(0),SM(3))
# theta dependence: rotate to 0 and test at 0.24
goto(0,sx+0.24,sy,th=0.0); step(s0='sample'); print('theta0 d.24',R(0),SM(3))
step(s0='drop')
goto(0,sx+0.24,sy,th=1.57); step(s0='sample'); print('theta1.57 d.24',R(0))
step(s0='drop')
# y offset direction
goto(0,sx+0.3,sy+0.3); goto(0,sx,sy+0.24); step(s0='sample'); print('above d.24',R(0)); step(s0='drop')
# sit on top
ok=goto(0,sx,sy); print('on top reached',ok,R(0)); step(s0='sample'); print('ontop sample',R(0),SM(3))
step(s0='drop')
# same-step motion: from d=0.40 move -0.2 with sample -> ends at 0.20
goto(0,sx+0.40,sy); step((-0.2,0,0),'sample'); print('move+sample end d',g('rover0','x')-sx,R(0))
step(s0='drop')
# reverse: from 0.2 move +0.2 to 0.4
goto(0,sx+0.20,sy); step((0.2,0,0),'sample'); print('start in range, move out: d',g('rover0','x')-sx,R(0))
