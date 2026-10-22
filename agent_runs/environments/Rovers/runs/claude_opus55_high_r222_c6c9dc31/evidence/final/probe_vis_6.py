from probe_vis_util import *
def ex(r,name):
    o=r.obs.get_object_from_name(name); return [float(r.obs.get(o,f)) for f in ['x','y','z']]
r=R(1)
O=ex(r,'objective1'); ox,oy=O[0],O[1]
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(ox,0.3)])
print('theta cols: k*pi/8 - pi, k=0..15')
for d in np.arange(1.2,2.15,0.05):
    r.goto(1,ox,oy-d,tol=1e-6)
    res=[]
    for k in range(16):
        r.turn(1,-math.pi+k*math.pi/8)
        r.act(1,'calibrate'); c=r.rv(1)['calibrated']
        if c: r.act(1,'image')
        res.append(int(c))
    print('d %.3f'%(oy-r.rv(1)['y']),''.join(map(str,res)))
