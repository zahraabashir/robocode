import numpy as np, math
data={1.5708:4.07,0.7854:4.065,0.0:4.015,2.3562:4.0275,-3.1416:3.96,-0.7854:3.9475,-2.3562:3.91,-1.5708:3.905}
ang=math.radians(80); u=np.array([math.cos(ang),math.sin(ang)])
best=[]
for R in np.arange(3.95,4.05,0.0025):
  for rho in np.arange(0.05,0.12,0.0025):
    for phi in np.radians(np.arange(170,206,1.0)):
      e=0
      for th,d in data.items():
        c=d*u+rho*np.array([math.cos(th+phi),math.sin(th+phi)])
        e=max(e,abs(np.linalg.norm(c)-R))
      best.append((round(e,4),round(R,4),round(rho,4),round(math.degrees(phi))))
best.sort(); print(best[:6])
