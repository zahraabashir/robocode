from probe_vis_lib import *
import probe_vis_lib as L
objs=None
for p in [(-1.5,0.25),(-1.57,0.31)]:
    reset(2); objs=L.obs.get_objects(L.T['objective'])
    goto([(-1.0,p[1]),p])
    for k in range(3):
        c=cal(); step(op=-1/6)
        print(p,k,'cal',c,[int(L.obs.get(o,'have_image_rover1')) for o in objs],'cal after',L.obs.get(L.r1,'calibrated'))
