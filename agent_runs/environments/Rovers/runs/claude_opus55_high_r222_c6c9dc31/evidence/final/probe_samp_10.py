from probe_samp_util import *
for i,(hx,hy,hth) in enumerate([(1,-1.75,math.pi),(-1,-1.75,0.0)]):
  for ddir in [(1,0),(0,1),(-1,0),(0,-1)]:
    D=Driver(1); last=None
    for k in range(1,40):
      d=0.01*k; D.goto(i,hx+ddir[0]*d,hy+ddir[1]*d,tol=1e-5)
      h=rov(D.obs,i)['at_home']
      if h<0.5: print('rover',i,'dir',ddir,'at_home lost at d=',round(d,3)); break
  D=Driver(1)
  for dth in [0.05,0.1,0.2,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.1]:
    D.turn(i,hth+dth); print('rover',i,'dth',dth,'at_home',rov(D.obs,i)['at_home'],end='; ')
  print()
