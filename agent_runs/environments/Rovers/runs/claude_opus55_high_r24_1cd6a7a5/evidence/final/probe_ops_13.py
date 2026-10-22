from probe_ops_lib import *
reset(14)
for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: print(goto(0,*wp),[round(v,2) for v in pos(0)[:2]])
step(0,op='sample'); print('store',pos(0)[3],get('sample5'))
step(0,op='calibrate'); step(0,op='image'); print('img',get('objective0'))
for wp in [(2.2,1.2),(2.2,0.6)]: print(goto(0,*wp))
lx,ly=get('lander')[:2]
turn_to(0,0.56); print('theta',pos(0)[2])
x,y=pos(0)[:2]; d=math.hypot(lx-x,ly-y); ux,uy=(lx-x)/d,(ly-y)/d
for k in range(40):
    step(0,op='send'); x,y=pos(0)[:2]
    r1=get('objective0')[5]; r2=get('sample5')[6]
    if r1 or r2: print('send ok at dist',round(math.hypot(lx-x,ly-y),3),'img recv',r1,'ana recv',r2,'store',pos(0)[3],'theta',pos(0)[2]); break
    step(0,0.05*ux,0.05*uy)
print(dump('rover'))
