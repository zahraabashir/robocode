import numpy as np
from probe_vis_geo import cam, segd
b=(0.81,0.083); o=(0.44,1.845); p=(0.735,0.444)
s="-180:0 -165:0 -150:1 -135:1 -120:1 -105:1 -90:1 -75:1 -60:1 -45:1 -30:1 -15:1 0:1 15:0 30:0 45:0 60:0 75:0 90:0 105:0 120:0 135:0 150:1 165:0"
for kv in s.split():
    t,v=map(int,kv.split(':')); c=cam(b,np.deg2rad(t))
    print(t,v,f"{segd(c,o,p)[1]:+.4f}", c.round(3), round(np.linalg.norm(c-np.array(o)),3))
