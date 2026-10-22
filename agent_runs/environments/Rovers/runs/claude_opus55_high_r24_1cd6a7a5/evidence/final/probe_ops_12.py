from probe_ops_lib import *
reset(14)
ox,oy=get('objective0')[:2]; px,py=get('obstacle7')[:2]
dd=math.hypot(px-ox,py-oy); ux,uy=(px-ox)/dd,(py-oy)/dd
goto(0,1.0,0.0)
for L in [1.6,1.45,1.4,1.36]:
    tx,ty=ox+L*ux,oy+L*uy
    ok=goto(0,tx,ty,tol=0.005); x,y=pos(0)[:2]
    step(0,op='calibrate'); c=pos(0)[4]
    if c: step(0,op='image')
    print('L',L,ok,'pos',round(x,3),round(y,3),'distpillar',round(math.hypot(px-x,py-y),3),'cal',c)
