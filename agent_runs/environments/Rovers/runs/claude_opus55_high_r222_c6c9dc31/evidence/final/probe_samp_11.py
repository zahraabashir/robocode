from probe_samp_util import *
hx,hy,hth=1,-1.75,math.pi
for sgn in [1,-1]:
  D=Driver(1)
  for k in range(20,41):
    dth=0.01*k; D.turn(0,hth+sgn*dth)
    if rov(D.obs,0)['at_home']<0.5: print('theta lost at',sgn*dth); break
for d in [0.248,0.25,0.252,0.255]:
  D=Driver(1); D.goto(0,hx+d/math.sqrt(2),hy+d/math.sqrt(2),tol=1e-6); p=rov(D.obs,0)
  print('diag d',d,round(math.hypot(p['x']-hx,p['y']-hy),5),p['at_home'])
# combined: d=0.2 and dth 0.25
D=Driver(1); D.goto(0,hx+0.2,hy); D.turn(0,hth+0.25); print('combo',rov(D.obs,0)['at_home'])
