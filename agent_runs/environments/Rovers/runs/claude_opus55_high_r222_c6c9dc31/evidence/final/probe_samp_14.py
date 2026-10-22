from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
ox,oy=-2.114,2.096
D=Driver(1)
for wp in [(-1.7,-1.0),(-1.7,0.0)]: print(goto_fine(D,1,*wp))
for y in [0.0,0.3,0.6,0.9,1.2,1.4,1.5]:
  ok,p=goto_fine(D,1,-1.7,y); th=math.atan2(oy-p[1],ox-p[0]); D.turn(1,th)
  D.act(1,'calibrate'); c=rov(D.obs,1)['calibrated']; D.act(1,'image')
  print('pos',[round(v,2) for v in p],'dist',round(math.hypot(ox-p[0],oy-p[1]),2),'calib',c,'img',S(D.obs,'objective1')['have_image_rover1'],'calib after',rov(D.obs,1)['calibrated'])
