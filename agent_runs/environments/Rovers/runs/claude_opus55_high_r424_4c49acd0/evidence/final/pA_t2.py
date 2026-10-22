from pA_lib import P
import numpy as np
p=P(0)
# mound obstacle3 (-0.5,2) half .25
for th in [0,np.pi/4,np.pi/2]:
    p.goto(1,-0.5,1.0,th); q=p.bisect(1,0,1); print('mound from below th',round(th,2),'contact y',round(q[1],4),'gap',round(1.75-q[1],4))
    p.goto(1,-1.2,1.3); p.goto(1,-1.2,2.0); q=p.bisect(1,1,0); print('  mound from left contact x',round(q[0],4),'gap',round(-0.75-q[0],4))
    p.goto(1,-1.2,1.3)
p.goto(1,-0.6,1.0,0); q=p.bisect(1,1,0); print('wall at y=1, x lim',round(q[0],5))
# sample collision? sample5 (-0.997,0.732)
p.goto(1,-0.997,0.4); p.goto(1,-0.997,0.732); print('on sample5',np.round(p.pos(1),3))
# lander careful
for th in [0,np.pi/4,np.pi/2]:
    p.goto(1,-0.8,-1.0); p.goto(1,-0.8,-2.0,th); q=p.bisect(1,-1,0); print('lander from +x th',round(th,2),'dx',round(q[0]+1.9,4))
    p.goto(1,-0.8,-1.0); p.goto(1,-1.3,-1.0); p.goto(1,-1.3,-1.6,th); q=p.bisect(1,0,-1); print('   from +y at x=-1.3 dy',round(q[1]+2.0,4))
