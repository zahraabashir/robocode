from probe_ops_lib import *
reset(14)
for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: goto(0,*wp)
step(0,op='sample')
ox,oy=get('objective0')[:2]
# calibrate threshold: move away to 2.1, approach in 0.005 steps
for wp in [(2.2,1.2),(2.2,0.6)]: goto(0,*wp)
x,y=pos(0)[:2]; d=math.hypot(ox-x,oy-y); ux,uy=(ox-x)/d,(oy-y)/d
goto(0,ox-2.05*ux,oy-2.05*uy,tol=0.002)
for k in range(30):
    step(0,op='calibrate'); x,y=pos(0)[:2]
    if pos(0)[4]: print('cal at 2D',round(math.hypot(ox-x,oy-y),4)); break
    step(0,0.005*ux,0.005*uy)
step(0,op='image')
lx,ly=get('lander')[:2]
x,y=pos(0)[:2]; d=math.hypot(lx-x,ly-y); ux,uy=(lx-x)/d,(ly-y)/d
goto(0,lx-4.12*ux,ly-4.12*uy,tol=0.002)
for k in range(30):
    step(0,op='send'); x,y=pos(0)[:2]
    if get('objective0')[5]: print('send at 2D',round(math.hypot(lx-x,ly-y),4)); break
    step(0,0.005*ux,0.005*uy)
step(0,op='drop'); print('after drop',pos(0))
goto(0,1.0,0.0); goto(0,1.0,-1.75,tol=0.001)
r,term,trunc=step(0); print('home',pos(0),'r',r,'term',term,'n',S.n, dump('sample'),dump('objective'), S.info)
for (x,y) in [(1.2,-1.75),(1.0,-1.4)]:
    goto(0,x,y,tol=0.001); r,term,trunc=step(0); print((x,y),'at_home',pos(0)[5],r,term)
