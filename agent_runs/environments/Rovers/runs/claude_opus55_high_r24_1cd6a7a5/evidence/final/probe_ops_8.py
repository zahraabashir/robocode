from probe_ops_lib import *
reset(1)
for wp in [(-1.0,-1.2),(-1.7,-1.2)]: goto(1,*wp)
ox,oy=get('objective1')[:2]
def d(): x,y=pos(1)[:2]; return math.hypot(ox-x,oy-y)
step(1,op='image'); print('image w/o cal ->',get('objective1')[3:6])
# scan calibrate far->near
while pos(1)[1]<1.0:
    step(1,op='calibrate')
    if pos(1)[4]==1: print('calibrated at dist',round(d(),3),pos(1)[:2]); break
    step(1,0,0.05)
# move back far keeping cal
goto(1,-1.7,-1.2); print('cal after moving',pos(1)[4])
while pos(1)[1]<1.0:
    step(1,op='image')
    if get('objective1')[4]==1: print('image at dist',round(d(),3),'cal now',pos(1)[4]); break
    if pos(1)[4]==0: print('cal lost at',d()); break
    step(1,0,0.05)
