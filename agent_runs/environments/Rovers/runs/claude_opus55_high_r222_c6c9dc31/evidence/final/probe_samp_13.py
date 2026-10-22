from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
D=Driver(1)
D.act(0,'calibrate'); D.act(1,'calibrate'); print('calib at start',rov(D.obs,0)['calibrated'],rov(D.obs,1)['calibrated'])
D.goto(0,0.747,-1.348); D.act(0,'sample'); goto_fine(D,0,0.8,-2.0); D.act(0,'send'); print('s3',S(D.obs,'sample3'))
D.goto(1,-1.285,-1.367); D.act(1,'sample'); D.act(1,'send'); print('s1',S(D.obs,'sample1'))
print(goto_fine(D,0,1,-1.75), goto_fine(D,1,-1,-1.75)); D.turn(0,math.pi); D.turn(1,0)
print('home',rov(D.obs,0),rov(D.obs,1),'term',D.last[1:],'R',D.R,'steps',D.steps)
D.act(0,'drop'); D.act(1,'drop'); print('after drop term',D.last[1:])
