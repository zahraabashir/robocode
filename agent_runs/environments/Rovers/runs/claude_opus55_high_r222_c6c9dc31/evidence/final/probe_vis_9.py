from probe_vis_util import *
import sys
seed=int(sys.argv[1]); oname=sys.argv[2]; i=int(sys.argv[3]); beta=math.radians(float(sys.argv[4]))
wps=eval(sys.argv[5])
r=R(seed)
o=r.obs.get_object_from_name(oname); ox,oy=float(r.obs.get(o,'x')),float(r.obs.get(o,'y'))
print(path(r,i,wps))
N=48
for d in [1.90,1.92,1.94,1.96,1.98,2.0,2.02,2.04,2.06,2.08,2.10]:
    ok=r.goto(i,ox-d*math.cos(beta),oy-d*math.sin(beta),tol=1e-6)
    if not ok: print('blocked',d); break
    res=[]
    for k in range(N):
        r.turn(i,-math.pi+k*2*math.pi/N)
        r.act(i,'calibrate'); c=r.rv(i)['calibrated']
        if c: r.act(i,'image')
        res.append(int(c))
    print('%.3f'%d,''.join(map(str,res)))
