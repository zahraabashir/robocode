from kin import *
import numpy as np
q0=np.array([0,0.26,3.14,-2.27,0,0.96,1.57])  # generic seed
xs=np.round(np.arange(-0.3,0.95,0.05),3); ys=np.round(np.arange(-0.8,0.85,0.05),3)
for yaw in [0,np.pi/2]:
  for z in [0.23,0.40]:
    print("yaw",round(yaw,2),"z",z,"  cols y from",ys[0],"to",ys[-1])
    for x in xs[::-1]:
        row=""
        for y in ys:
            best=9
            for s in [q0, np.array([0,0.5,0,1.8,0,1.0,0]), np.array([np.arctan2(y,x),0.3,3.14,-2.0,0,0.9,1.57])]:
                q,e=ik(s,np.array([x,y,z]),down_R(yaw),(0,0,0)); best=min(best,e)
                if best<1e-3: break
            row+="#" if best<1e-3 else "."
        print("%+.2f "%x+row)
