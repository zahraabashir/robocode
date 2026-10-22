from probe_vis_util import *
import sys
mode=sys.argv[1]
r=R(0)
if mode in 'BC':
    path(r,1,[(-0.5,-1.0),(-0.4,0.0),(-0.3,0.6)]); r.act(1,'calibrate'); r.act(1,'image')
    if mode=='C': r.act(1,'send')
    print('after rover1',r.objst())
path(r,0,[(1.2,0.0),(1.2,1.6)])
for k in range(3):
    r.act(0,'calibrate'); c=r.rv(0)['calibrated']; r.act(0,'image'); print(mode,'cal',c,'calafter',r.rv(0)['calibrated'],r.objst())
r.act(0,'send'); print('send',r.objst())
r.act(0,'calibrate'); print('cal when all received:',r.rv(0)['calibrated'])
