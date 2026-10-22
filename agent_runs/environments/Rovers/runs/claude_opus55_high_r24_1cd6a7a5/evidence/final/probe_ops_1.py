from probe_ops_lib import *
reset(1)
# test move semantics: is dx world frame? rover1 theta=0
print(pos(1)); step(1,0.1,0); print(pos(1)); step(1,dth=0.4); step(1,0.1,0); print(pos(1))
# sample1 at (-1.49,-1.37); approach to various distances
sx,sy=get('sample1')[:2]
for d in [0.4,0.3,0.27,0.25,0.23,0.2,0.15,0.1]:
    goto(1,sx+d,sy)
    step(1,op='sample'); p=pos(1)
    print('d',d,'pos',[round(v,3) for v in p],'dist',round(math.hypot(p[0]-sx,p[1]-sy),3),'s1',[round(v,2) for v in get('sample1')] if 'sample1' in names('sample') else 'GONE')
    if p[3]==1: break
print(dump('sample'))
