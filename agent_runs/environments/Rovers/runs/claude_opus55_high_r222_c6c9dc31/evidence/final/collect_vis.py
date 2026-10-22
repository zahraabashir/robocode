import sys, math, json
import numpy as np
from env_client import make_env
env=make_env(); T=lambda n: env.observation_space.get_type(n)
seeds=[int(s) for s in sys.argv[1:]]
out=open('vis_data_%d.jsonl'%seeds[0],'w')
for seed in seeds:
    obs,info=env.reset(seed=seed)
    if info['object_count']!=1: continue
    ob=list(obs.get_objects(T('objective')))[0]; ox,oy=obs.get(ob,'x'),obs.get(ob,'y')
    rovers={o.name:o for o in obs.get_objects(T('rover'))}
    for rname,k in (('rover0',0),('rover1',4)):
        rv=rovers[rname]
        x0=obs.get(rv,'x'); side=1 if x0>0 else -1
        xs=np.arange(0.25,2.26,0.1)*side
        ys=np.arange(-2.2,2.21,0.1)
        pts=[]
        for i,x in enumerate(xs):
            col=[(x,y) for y in (ys if i%2==0 else ys[::-1]) if math.hypot(x-ox,y-oy)<2.15]
            pts+=col
        if not pts: continue
        def step(dx,dy,sel):
            global obs
            a=np.zeros(8,np.float32); a[k]=dx;a[k+1]=dy;a[k+3]=sel
            obs,*_=env.step(a)
        for (tx,ty) in pts:
            ok=True
            for _ in range(40):
                x,y=obs.get(rv,'x'),obs.get(rv,'y')
                if abs(tx-x)<1e-4 and abs(ty-y)<1e-4: break
                step(float(np.clip(tx-x,-.2,.2)),float(np.clip(ty-y,-.2,.2)),1/6)
                x2,y2=obs.get(rv,'x'),obs.get(rv,'y')
                if abs(x2-x)<1e-7 and abs(y2-y)<1e-7: ok=False; break
            if not ok: continue
            step(0,0,-0.5)
            c=float(obs.get(rv,'calibrated'))
            if c>0.5: step(0,0,-1/6)
            out.write(json.dumps(dict(seed=seed,r=rname,x=float(obs.get(rv,'x')),y=float(obs.get(rv,'y')),th=float(obs.get(rv,'theta')),vis=c,ox=ox,oy=oy))+'\n'); out.flush()
