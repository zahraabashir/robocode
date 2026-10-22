from kin import *
import numpy as np
q0=np.array([0,0.26,3.14,-2.27,0,0.96,1.57])
pts=[(0.51,0.41),(0.51,-0.41),(0.09,0.41),(0.09,-0.41),(0.55,0),(0.6,0.3),(0.3,0),(0.12,0.0)]
for yaw in [0,np.pi/2]:
  for z in [0.23,0.40]:
    r=[]
    for x,y in pts:
        s=np.array([np.arctan2(y,x),0.3,3.14,-2.0,0,0.9,1.57])
        e=min(ik(s,np.array([x,y,z]),down_R(yaw),(0,0,0))[1], ik(q0,np.array([x,y,z]),down_R(yaw),(0,0,0))[1])
        r.append("%.0e"%e)
    print(round(yaw,2),z,r,flush=True)
