# horizontal approach probe: python calib_2.py seed yaw zoff
from calib_u import *
import sys
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); zfk=float(sys.argv[3])
e=R(); res=[]
for ang in [0,90,180,270]:
    d=np.array([np.cos(np.radians(ang)),np.sin(np.radians(ang)),0])
    e.reset(seed); b=e.blk(); c=b[:3].copy(); c[2]=zfk
    s=0.25
    e.go(c-d*s+[0,0,0.1],yaw); ok=e.go(c-d*s,yaw)
    if not ok: res.append((ang,'startblk')); continue
    for step in [0.01,0.001]:
        while s>-0.25:
            r=e.go(c-d*(s-step),yaw)
            if r is None: print('ikfail'); break
            if not r: break
            s-=step
    res.append(s)
# contact positions along axis: EE coordinate at contact relative to block center
xa=-res[0]; xb=res[2]; ya=-res[1]; yb=res[3]
b=e.blk()
print(f"seed {seed} yaw {yaw:.2f} z {zfk} blk {np.round(b[:2],3)} he {np.round(b[3:5],3)} | x: {xa:.3f} {xb:.3f} ctr {-(xa+xb)/2:+.3f} w {xb-xa-2*b[3]:.3f} | y: {ya:.3f} {yb:.3f} ctr {-(ya+yb)/2:+.3f} w {yb-ya-2*b[4]:.3f}",flush=True)
