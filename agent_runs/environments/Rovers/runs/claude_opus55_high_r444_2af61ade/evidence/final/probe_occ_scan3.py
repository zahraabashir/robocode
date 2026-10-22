from probe_send_lib import *
for seed in (44,54,61):
    e=E(seed)
    print(seed,[(round(e.g(o.name,'x'),2),round(e.g(o.name,'y'),2)) for o in e.obs if o.type.name=='obstacle' and e.g(o.name,'half_x')<0.1])
    o=e.obs.get_object_from_name('sample0'); print(e.obs.data[o].shape, [f for f in ['x','y','z']])
    e.env.close()
