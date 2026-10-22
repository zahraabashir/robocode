from probe_samp_util import *
for y in [-2.3,-1.0,0.0,1.0,1.8,2.3]:
  D=Driver(1); D.goto(0,1.0,y) if y>-1.75 else D.goto(0,1.0,y)
  ok,p=goto_fine(D,0,-1.0,y); print('r0 west at y',y,ok,[round(v,3) for v in p])
