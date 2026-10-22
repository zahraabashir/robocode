from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
# seed 1: sample3 soil (0.547,-1.348); rover0 at (1,-1.75)
sx,sy=0.547,-1.348
for ang in [0.0, math.pi/2]:
  D=Driver(1)
  for d in [0.6,0.5,0.45,0.4,0.35,0.3,0.28,0.26,0.25,0.24,0.22,0.2,0.15,0.1]:
    tx,ty=sx+d*math.cos(ang-0.9),sy+d*math.sin(ang-0.9)
    ok=D.goto(0,tx,ty)
    D.act(0,'sample'); p=rov(D.obs,0)
    print('ang',round(ang,2),'d',d,'ok',ok,'dist',round(math.hypot(p['x']-sx,p['y']-sy),3),'th',round(p['theta'],2),'store',p['store_full'],S(D.obs,'sample3'),D.last[0],D.last[3])
    if p['store_full']: break
  print('rover0',rov(D.obs,0))
