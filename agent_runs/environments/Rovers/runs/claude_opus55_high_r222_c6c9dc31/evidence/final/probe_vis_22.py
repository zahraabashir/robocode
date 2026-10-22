from probe_vis_util import *
r=R(1)
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(-2.1,1.0)])
r.act(1,'calibrate'); r.act(1,'image'); r.act(1,'send'); print(r.objst())
r.act(1,'calibrate'); print('cal after only-visible objective received:',r.rv(1)['calibrated'])
r.act(1,'image'); print('image ->',r.rv(1)['calibrated'],r.objst())
r.act(1,'send'); print('send holding already-received image ->',r.objst(),r.rv(1)['calibrated'])
