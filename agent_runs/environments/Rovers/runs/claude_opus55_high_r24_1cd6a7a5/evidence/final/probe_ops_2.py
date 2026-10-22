from probe_ops_lib import *
reset(1)
sx,sy=get('sample3')[:2]
goto(0,sx+0.3,sy); print(pos(0))
for k in range(20):
    step(0,-0.005,0,op='sample'); p=pos(0)
    if p[3]==1: print('sampled at dist',round(math.hypot(p[0]-sx,p[1]-sy),4),'theta',p[2]); break
# small move test
x0=pos(0)[0]; step(0,0.01,0); print('small move dx', pos(0)[0]-x0)
# drop
step(0,op='drop'); print('after drop',[round(v,2) for v in pos(0)], get('sample3'))
# sample again same sample with rover0
step(0,op='sample'); print('resample', pos(0)[3], get('sample3'))
step(0,op='drop')
# rover1: go to sample3? wall in middle; try sample1 by rover1 then rover0 can't. Instead try rover1 sampling sample1, drop, then sample again
sx1,sy1=get('sample1')[:2]
goto(1,sx1+0.2,sy1); step(1,op='sample'); print('r1 sample1',pos(1)[3],get('sample1'))
