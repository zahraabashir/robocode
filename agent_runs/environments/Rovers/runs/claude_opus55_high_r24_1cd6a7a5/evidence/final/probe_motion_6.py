from probe_motion_lib import *
import math
for ang in [0,90,180,270]:
    obs,_=env.reset(seed=0); ux,uy=math.cos(math.radians(ang)),math.sin(math.radians(ang))
    d=0
    for k in range(200):
        obs,*_=step(0,0.005*ux,0.005*uy); r=rov(obs,0)
        if r[5]<0.5: print('dir',ang,'at_home->0 at dist',round(math.hypot(r[0]-1,r[1]+1.75),4)); break
obs,_=env.reset(seed=0); n=0
while True:
    obs,r,te,tr,inf=env.step(act(0)); n+=1
    if te or tr or n>1100: print('ended at',n,te,tr); break
