from probe_vis_lib import *
from probe_vis_geo import *
import sys
e=E(4)
ob=e.objs()['objective2']; o=(ob['x'],ob['y'])
e.path(1,[(-1.0,-1.0),(-1.0,0.75),(float(sys.argv[1]),0.75)])
out=[]
for k in range(32):
    th=-math.pi+k*2*math.pi/32
    e.turn(1,th)
    r=[]
    for rep in range(2):
        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img'); r.append(int(c))
    st=e.rs(1)
    out.append('%d%d'%tuple(r)); print(k,round(st['theta'],5),st['x'],st['y'],r)
print(sys.argv[1],' '.join(out), st['x'],st['y'])
