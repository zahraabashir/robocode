from probe_send_lib import *
e=E(1)
ox,oy=e.g('objective1','x'),e.g('objective1','y'); print('obj',ox,oy)
for p in [(-1.2,0.5),(-1.4,1.3),(-1.5,1.5)]:
    print('nav',p,nav(e,1,p),e.pose(1))
    for th in [None,np.arctan2(oy-p[1],ox-p[0]),0.0]:
        if th is not None: e.turn(1,th)
        f0=e.flags(); e.act(1,(0,0,0),SEL['cal']); d1=diff(f0,e.flags())
        f0=e.flags(); e.act(1,(0,0,0),SEL['image']); d2=diff(f0,e.flags())
        print(' th',e.pose(1)[2],'cal',d1,'img',d2)
