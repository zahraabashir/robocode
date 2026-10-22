from pE_lib import *
s=Sim(12)
print(objs(s))
drive(s,0,0.65,0.45); act1(s,0,'cal'); act1(s,0,'img'); print('after r0 img',[o[2:] for o in objs(s)])
drive(s,1,-0.3,1.1); print(info(s,1))
act1(s,1,'cal'); act1(s,1,'img'); print('after r1 img',[o[2:] for o in objs(s)])
act1(s,1,'cal'); act1(s,1,'img'); print('after r1 img2',[o[2:] for o in objs(s)])
act1(s,1,'cal'); act1(s,1,'img'); print('after r1 img3',[o[2:] for o in objs(s)],'cal',s.r(1)['calibrated'])
