from probe_vis_util import *
r=R(1)
o=r.obs.get_object_from_name('objective1'); ox,oy=float(r.obs.get(o,'x')),float(r.obs.get(o,'y'))
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(ox,0.3)])
N=48
for d in [1.90,1.92,1.94,1.96,1.98,2.0,2.02,2.04,2.06,2.08]:
    r.goto(1,ox,oy-d,tol=1e-6)
    res=[]
    for k in range(N):
        r.turn(1,-math.pi+k*2*math.pi/N)
        r.act(1,'calibrate'); c=r.rv(1)['calibrated']
        if c: r.act(1,'image')
        res.append(int(c))
    print('d %.3f'%d,''.join(map(str,res)))
