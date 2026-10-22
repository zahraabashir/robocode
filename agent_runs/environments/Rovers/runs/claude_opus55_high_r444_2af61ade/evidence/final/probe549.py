import sys, numpy as np
from test_approach import *
from concurrent.futures import ThreadPoolExecutor
def trial(tx,ty):
    env = make_env(); obs, info = env.reset(seed=549)
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    for t in range(12):
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
    s=[obs.get(obs.get_object_from_name(f'sample{i}'),'received_analysis') for i in (1,4)]
    env.close()
    return (tx,ty,s)
pts=[(x,y) for x in (0.4,1.0,1.6,2.2) for y in (-2.2,-1.8,-1.4,-1.0,-0.6,-0.2,0.2,0.6)]
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(lambda p: trial(*p), pts): print(r)
