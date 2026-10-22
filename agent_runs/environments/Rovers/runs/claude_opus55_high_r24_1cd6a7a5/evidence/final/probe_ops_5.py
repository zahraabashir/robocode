from probe_ops_lib import *
for y in [-1.75,-1.2]:
    reset(0)
    if y!=-1.75:
        for k in range(3): step(1,0,0.2)
    for k in range(80):
        x=pos(1)[0]; step(1,0.02,0)
        if abs(pos(1)[0]-x)<1e-6: break
    print('r1 stops',pos(1)[:2])
    for k in range(80):
        x=pos(0)[0]; step(0,-0.02,0)
        if abs(pos(0)[0]-x)<1e-6: break
    print('r0 stops',pos(0)[:2])
