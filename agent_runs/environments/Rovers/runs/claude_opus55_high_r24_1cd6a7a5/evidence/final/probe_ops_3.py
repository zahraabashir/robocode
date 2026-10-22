from probe_ops_lib import *
reset(0)
for y in [-1.75,-1.0,0.5,1.5,2.4]:
    goto(0,1.0,y); goto(0,-0.5,y,maxn=30); print('r0 wall test y',y,[round(v,3) for v in pos(0)[:2]])
reset(0)
goto(1,-0.27,-1.75); goto(1,0.5,-1.75,maxn=20); print('r1 rightmost',pos(1)[:2])
# sample4 at -0.27,-2.04
sx,sy=get('sample4')[:2]
goto(1,sx-0.2,sy); step(1,op='sample'); print('r1 sampled',pos(1)[3],get('sample4'))
step(1,op='drop'); goto(1,sx-0.4,sy+0.3)
goto(0,0.3,-1.75); goto(0,sx+0.22,sy); print('r0 pos',pos(0)[:2],'dist',math.hypot(pos(0)[0]-sx,pos(0)[1]-sy))
step(0,op='sample'); print('r0 sampled',pos(0)[3],get('sample4'))
