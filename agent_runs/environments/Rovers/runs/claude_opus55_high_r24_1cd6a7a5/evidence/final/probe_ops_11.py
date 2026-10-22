from probe_ops_lib import *
reset(0)
for wp in [(-0.5,-1.2),(-0.45,-0.2),(-0.3,0.6)]: print(goto(1,*wp),[round(v,2) for v in pos(1)[:2]])
x,y=pos(1)[:2]
for n in names('objective'): o=get(n); print(n,'dist',round(math.hypot(o[0]-x,o[1]-y),2))
step(1,op='calibrate'); print('cal',pos(1)[4])
if pos(1)[4]: step(1,op='image'); print(dump('objective'))
# move closer to wall & up
for wp in [(-0.3,1.2)]:
    print(goto(1,*wp)); x,y=pos(1)[:2]
    for n in names('objective'): o=get(n); print(n,'dist',round(math.hypot(o[0]-x,o[1]-y),2))
    step(1,op='calibrate'); print('cal',pos(1)[4])
    if pos(1)[4]: step(1,op='image'); print(dump('objective'))
