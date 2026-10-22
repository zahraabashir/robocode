from pB_lib import *
import numpy as np
P=(0.654,-0.199)
for th in [0,np.pi/4,np.pi/2]:
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        s=Sim(0); start=(P[0]+0.6*d[0],P[1]+0.6*d[1])
        ok=gp(s,0,[(1.2,-1.75),(1.2,start[1]) if d[1]==0 else (1.2,-1.75),start],th=th)
        if not ok: print('fail reach',th,d,s.r(0)); continue
        for k in range(200):
            p=s.r(0); s.act(a0=(-0.003*d[0],-0.003*d[1],0,'noop'))
            if s.r(0)==p: break
        c=s.r(0); print(round(th,2),d,'gap',round(abs(c['x']-P[0])+abs(c['y']-P[1]),3))
