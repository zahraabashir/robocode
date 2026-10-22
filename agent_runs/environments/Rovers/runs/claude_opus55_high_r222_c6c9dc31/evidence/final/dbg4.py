import sys, math
import numpy as np
from env_client import make_env
from approach import seg_hits_box
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
T=lambda n: env.observation_space.get_type(n)
cx,cy=float(sys.argv[2]),float(sys.argv[3]); on=sys.argv[4]
ob=[o for o in obs.get_objects(T('objective')) if o.name==on][0]
ox,oy=obs.get(ob,'x'),obs.get(ob,'y')
for p in obs.get_objects(T('obstacle')):
    px,py,hx,hy=[obs.get(p,f) for f in ('x','y','half_x','half_y')]
    for m in (0.0,0.012):
        if seg_hits_box(np.array(cx),np.array(cy),ox,oy,px,py,hx+m,hy+m):
            # fraction along
            L=math.hypot(ox-cx,oy-cy); s=((px-cx)*(ox-cx)+(py-cy)*(oy-cy))/L**2
            print(p.name,'margin',m,'s=',round(s,3),'perp',round(abs((px-cx)*(oy-cy)-(py-cy)*(ox-cx))/L,3), 'hz',obs.get(p,'half_z'))
