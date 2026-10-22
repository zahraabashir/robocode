from probe_ops_lib import *
import sys
reset(21)
print(goto(0,0.62,-0.92+0.1))
step(0,op='sample'); print('after sample', dump('sample')['sample3'], pos(0))
cands=[(1.0,-1.75),(0.62,-0.82),(0.3,-1.75),(0.3,-2.25),(0.3,-1.0),(0.3,0.0),(0.3,1.0),(1.5,-1.0)]
for c in cands:
    ok=goto(0,*c)
    for th in [None]:
        step(0,op='send')
    print(c, ok, [round(v,2) for v in pos(0)], 'recv', dump('sample')['sample3'][-1], S.info if S.n<3 else '')
    if dump('sample')['sample3'][-1]>0: break
