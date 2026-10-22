# descend-grid in TCP coords (tool=0.12): python calib_5.py seed yaw dy -> TCP z where descent stopped, over dx
from calib_u import *
import sys
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); dy=float(sys.argv[3]); T=0.12
e=R(); row=[]
for dx in np.arange(-0.08,0.081,0.01):
    e.reset(seed); b=e.blk(); z=0.25
    r0=e.go([b[0]+dx,b[1]+dy,z],yaw,tool=T)
    while z>0.06:
        r=e.go([b[0]+dx,b[1]+dy,z-0.0025],yaw,tool=T)
        if not r: break
        z-=0.0025
    M=e.ee(T); err=np.linalg.norm(M[:3,:3]-kin.down_R(yaw))
    row.append(z if (r is not None and err<0.05) else -1)
print(f"{dy:+.2f} "+" ".join(f"{v:.3f}" for v in row),flush=True)
