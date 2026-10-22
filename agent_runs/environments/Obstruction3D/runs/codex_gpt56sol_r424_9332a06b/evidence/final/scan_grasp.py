import concurrent.futures
import itertools
import numpy as np
from env_client import make_env

def v(s,n,f): return s.get(s.get_object_from_name(n),f)

def trial(cfg):
    q2,q4,q6=cfg
    e=make_env(); s,_=e.reset(seed=0)
    target=np.array([0,q2,-np.pi,q4,0,q6,np.pi/2])
    for t in range(12):
        r=s.get_object_from_name('robot')
        cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)])
        a=np.zeros(11,np.float32)
        a[1]=np.clip(v(s,'target_block','pose_y')-.00135-v(s,'robot','pos_base_y'),-.2,.2)
        a[3:10]=np.clip(target-cur,-.2,.2)
        if t>=7:a[10]=-1
        s,_,_,_,_=e.step(a)
        if v(s,'robot','grasp_active')>.5:
            e.close(); return cfg,True
    e.close(); return cfg,False

configs=list(itertools.product([.25,.35,.45,.55,.65],[-2.2,-2.0,-1.8],[-1.2,-1.0,-.8,-.6,-.4]))
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
    for cfg,ok in ex.map(trial,configs):
        if ok: print('SUCCESS',cfg,flush=True)
