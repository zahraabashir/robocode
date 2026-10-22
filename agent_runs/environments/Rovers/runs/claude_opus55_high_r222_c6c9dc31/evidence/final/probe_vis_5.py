from probe_vis_util import *
def ex(r,name):
    o=r.obs.get_object_from_name(name); return [float(r.obs.get(o,f)) for f in ['x','y','z']]
r=R(1)
O=ex(r,'objective1'); O0=ex(r,'objective0')
ox,oy=O[0],O[1]
print(path(r,1,[(-0.9,-0.5),(-1.0,0.0),(-0.7,0.2),(-0.3,1.3)]))
a=math.radians(-20); u=np.array([math.cos(a),math.sin(a)])
for d in np.arange(1.95,2.3,0.01):
    p=np.array([ox,oy])+u*d
    ok=r.goto(1,p[0],p[1],tol=1e-6)
    r.act(1,'calibrate'); c=r.rv(1)['calibrated']
    if c: r.act(1,'image')
    q=r.rv(1); 
    print('d %.3f cal %s ok %s pos %.3f %.3f d1 %.3f d0 %.3f'%(d,c,ok,q['x'],q['y'],math.hypot(q['x']-ox,q['y']-oy),math.hypot(q['x']-O0[0],q['y']-O0[1])), r.objst())
