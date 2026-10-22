from probe_ops_lib import *
reset(0)
last=None
for k in range(60):
    step(0,-0.02,0); x=pos(0)[0]
    if last is not None and abs(x-last)<1e-6: break
    last=x
print('r0 stops at',pos(0)[:2])
for k in range(30):
    step(1,0.02,0); 
print('r1 at',pos(1)[:2])
reset(1)
# approach sample1 from +x in tiny steps on its y
sx,sy=get('sample1')[:2]
goto(1,sx+0.4,sy)
for k in range(40):
    x=pos(1)[0]; step(1,-0.005,0); 
    if abs(pos(1)[0]-x)<1e-6: print('blocked at dist',pos(1)[0]-sx); break
else: print('no block, dist',pos(1)[0]-sx)
