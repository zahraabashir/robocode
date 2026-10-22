from probe_vis_util import *
r=R(1)
print(path(r,1,[(-0.9,-0.5),(-1.6,0.0),(-2.1,1.0)]), r.rv(1))
r.act(1,'image'); print('image uncal', r.rv(1)['calibrated'], r.objst())
r.act(1,'calibrate'); print('calib', r.rv(1)['calibrated'], r.last[0])
r.act(1,'calibrate'); print('calib2', r.rv(1)['calibrated'])
r.act(1,'image'); print('image', r.rv(1)['calibrated'], r.objst())
r.act(1,'image'); print('image2', r.rv(1)['calibrated'], r.objst())
r.act(1,'send'); print('send', r.objst(), r.last)
