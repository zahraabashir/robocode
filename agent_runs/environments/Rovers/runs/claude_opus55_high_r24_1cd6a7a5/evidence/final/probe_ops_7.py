from probe_ops_lib import *
reset(1)
for wp in [(-1.0,-1.2),(-1.7,-1.2),(-1.7,0.9)]:
    print(goto(1,*wp), [round(v,2) for v in pos(1)])
ox,oy=get('objective1')[:2]
x,y=pos(1)[:2]; bearing=math.atan2(oy-y,ox-x); print('bearing',bearing,'dist',math.hypot(ox-x,oy-y))
th0=pos(1)[2]
for k in range(17):
    step(1,op='calibrate'); c=pos(1)[4]
    msg=''
    if c==1:
        step(1,op='image'); msg='img->'+str(get('objective1')[3:6])+' cal '+str(pos(1)[4])
    rel=(pos(1)[2]-bearing+math.pi)%(2*math.pi)-math.pi
    print('theta',round(pos(1)[2],2),'rel',round(rel,2),'cal',c,msg)
    step(1,dth=0.4)
