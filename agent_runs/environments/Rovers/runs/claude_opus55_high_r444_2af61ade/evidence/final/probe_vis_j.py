from probe_vis_lib import *
import sys, json
th=float(sys.argv[1]); y=float(sys.argv[2])
e=E(4)
e.path(1,[(-1.0,-1.0),(-1.0,y),(-2.3,y)]); e.turn(1,th)
res=[]
x=-2.3
while x<-1.55:
    ok=e.goto(1,x,y,tol=1e-7); st=e.rs(1)
    if ok:
        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img'); res.append((st['x'],st['y'],st['theta'],int(c)))
    x+=0.005
json.dump(res,open('probe_vis_j_%s_%s.json'%(sys.argv[1],sys.argv[2]),'w'))
s=''.join(str(r[3]) for r in res); print(th, res[0][0], s)
