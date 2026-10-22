from probe_motion_lib import *
import sys
seed=int(sys.argv[1])
obs,_=env.reset(seed=seed)
print('pillars/mounds', [(n,v[0],v[1],v[3]) for n,v in obstacles(obs)])
for i,sx,ux in [(0,1.0,-1),(1,-1.0,1)]:
  res=[]
  for y in np.arange(-2.25,2.26,0.05):
    obs,_=env.reset(seed=seed)
    p=goto(i,sx,-1.75); p=goto(i,sx,y)
    if abs(p[1]-y)>1e-3: res.append((round(y,2),'unreach')); continue
    p=approach(i,ux,0,steps=(0.2,0.05,0.01))
    res.append((round(y,2),round(p[0],3)))
  print('rover',i,res)
