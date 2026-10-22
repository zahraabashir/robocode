from probe_vis_util import *
import sys
th=float(sys.argv[1]); ang=math.radians(float(sys.argv[2])); ds=eval(sys.argv[3])
r=R(1)
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(-2.1,1.0)])
r.act(1,'calibrate'); r.act(1,'image')
print(r.objst())
L=(-1.9,-2.0)
for d in ds:
    ok=r.goto(1,L[0]+d*math.cos(ang),L[1]+d*math.sin(ang),tol=1e-6)
    if not ok: print('blocked',d,r.rv(1)); break
    r.turn(1,th)
    r.act(1,'send')
    if r.objst()['objective1'][2]>0: print('th',th,'sent at d=%.4f'%d); break
else: print('never')
