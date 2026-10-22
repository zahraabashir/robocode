from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
sx,sy=0.547,-1.348
# fine radius, facing away (theta=0, rover west of sample => sample is east... choose rover east of sample facing east=away)
for th in [0.0, math.pi/2]:
  D=Driver(1); D.turn(0,th)
  for d in [0.252,0.25,0.249,0.248,0.246,0.244]:
    D.goto(0,sx+d,sy,tol=1e-5); D.act(0,'sample'); p=rov(D.obs,0)
    print('th',th,'d',d,'actual',round(math.hypot(p['x']-sx,p['y']-sy),5),'store',p['store_full'])
    if p['store_full']: break
  # sample again while full
  before=S(D.obs,'sample3'); D.act(0,'sample'); print('resample full', rov(D.obs,0)['store_full'], S(D.obs,'sample3'))
  # drop far away
  D.goto(0,1.5,-1.0); D.act(0,'drop'); print('drop far', D.last[0], rov(D.obs,0), S(D.obs,'sample3'))
  D.act(0,'drop'); print('drop empty', rov(D.obs,0)['store_full'])
