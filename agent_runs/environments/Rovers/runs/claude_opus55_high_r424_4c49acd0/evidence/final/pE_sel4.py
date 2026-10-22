from pE_lib import *
s=Sim(12)
drive(s,0,0.65,0.45); print(info(s,0)); act1(s,0,'cal'); act1(s,0,'img'); print('after r0 img',[o[2:] for o in objs(s)])
for pos in [(0.65,0.45),(1.0,-1.75),(0.5,-1.0)]:
    drive(s,0,*pos); act1(s,0,'send'); print('send at',pos,[o[2:] for o in objs(s)],s.r(0))
    if objs(s)[1][4]>0.5: break
drive(s,0,0.65,0.45); print(info(s,0))
act1(s,0,'cal'); act1(s,0,'img'); print('re-img',[o[2:] for o in objs(s)])
drive(s,1,-0.3,1.1); print(info(s,1)); act1(s,1,'cal'); act1(s,1,'img'); print('r1 img after received',[o[2:] for o in objs(s)])
