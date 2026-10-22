import sys, numpy as np
from test_approach import *
from concurrent.futures import ThreadPoolExecutor
def trial(tx,ty):
    env = make_env(); obs, info = env.reset(seed=SEED)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    for t in range(NST):
        obs,*_=env.step(ap.get_action(obs))
    r0=obs.get_object_from_name('rover0')
    for k in range(40):
        x,y=obs.get(r0,'x'),obs.get(r0,'y')
        d=np.array([tx-x,ty-y])
        if np.abs(d).max()<1e-6: break
        a=np.zeros(8,dtype=np.float32); a[:2]=np.clip(d,-0.2,0.2); a[3]=0.1667; a[7]=0.1667
        obs,*_=env.step(a)
        nx,ny=obs.get(r0,'x'),obs.get(r0,'y')
        if abs(nx-x)+abs(ny-y)<1e-9: return (tx,ty,'blocked',round(x,3),round(y,3))
    a=np.zeros(8,dtype=np.float32); a[3]=0.5; a[7]=0.1667
    obs,*_=env.step(a)
    s=[obs.get(o,'received_analysis') for o in obs.get_objects(obs.get_object_from_name('sample0').type)]+[obs.get(o,'received_image') for o in obs.get_objects(obs.get_object_from_name('objective0').type)]
    env.close()
    return (tx,ty,round(math.degrees(math.atan2(ty+2,tx+1.9)),1),max(s))
import math
SEED=int(sys.argv[1]); NST=int(sys.argv[2]); R=float(sys.argv[3])
pts=[(round(-1.9+R*math.cos(math.radians(b)),3), round(-2.0+R*math.sin(math.radians(b)),3)) for b in range(0,50,3)]
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(lambda p: trial(*p), pts): print(r)
