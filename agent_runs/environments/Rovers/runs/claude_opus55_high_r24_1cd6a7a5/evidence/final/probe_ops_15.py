from probe_ops_lib import *
reset(14)
for wp in [(-1.0,-1.2),(-1.5,-1.2),(-1.47,-0.65)]: print(goto(1,*wp))
step(1,op='sample'); print('r1 store',pos(1)[3])
for wp in [(-1.5,0.0),(-1.5,2.25)]: print(goto(1,*wp,tol=0.002),pos(1)[:2])
lx,ly=get('lander')[:2]
for k in range(80):
    step(1,op='send'); x,y=pos(1)[:2]
    if get('sample2')[6]: print('send at 2D',round(math.hypot(lx-x,ly-y),4),'pos',x,y); break
    yy=pos(1)[1]; step(1,0,-0.005)
    if abs(pos(1)[1]-yy)<1e-6: print('blocked'); break
print(S.n)
