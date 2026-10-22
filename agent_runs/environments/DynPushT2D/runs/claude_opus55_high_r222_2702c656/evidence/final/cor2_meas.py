import sys, math, json
import numpy as np
from env_client import make_env
from approach import GeneratedApproach, Block, R_ROBOT, MAXS, LO, HI
from concurrent.futures import ThreadPoolExecutor
def wrap(a): return (a+math.pi)%(2*math.pi)-math.pi
def prims(B):
    w,Lh,Lv=B.w,B.Lh,B.Lv; a=Lh/2-0.04; tipy=-(w+Lv)+0.04; sy=-(w+0.7*Lv)
    return {'Rtopm+':((Lh/4,0),(0,-1)),'Rtopm-':((-Lh/4,0),(0,-1)),
     'Rbotm+':((Lh/4,-w),(0,1)),'Rbotm-':((-Lh/4,-w),(0,1)),
     'Rend+':((Lh/2,-w/2),(-1,0)),'Rend-':((-Lh/2,-w/2),(1,0)),
     'Rslm':((-w/2,sy),(1,0)),'Rsrm':((w/2,sy),(-1,0)),
     'Rtop+':((a,0),(0,-1)),'Rtop-':((-a,0),(0,-1)),'Rbot+':((a,-w),(0,1)),'Rbot-':((-a,-w),(0,1)),
     'Rsl':((-w/2,tipy),(1,0)),'Rsr':((w/2,tipy),(-1,0))}
NAMES=list(prims(Block(np.zeros(20)+0.2)).keys())
def run(args):
    seed,name=args
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    B=Block(obs)
    if min(B.x,B.y,5-B.x,5-B.y)<0.6+0: pass
    p,n=prims(B)[name]; p=np.array(p,float); n=np.array(n,float)
    pre=B.to_world(p-n*0.14)
    if not (np.all(pre>LO) and np.all(pre<HI)): return None
    # check block far from walls: all corners
    for (x0,x1,y0,y1) in B.rects:
        for c in ((x0,y0),(x0,y1),(x1,y0),(x1,y1)):
            wc=B.to_world(c)
            if np.any(wc<0.6) or np.any(wc>5-0.6): return None
    ok=False
    for t in range(300):
        B=Block(obs); rp=obs[16:18]
        pre=B.to_world(p-n*0.14)
        if np.linalg.norm(rp-pre)<0.01: ok=True; break
        tg=ap.nav_step(B,rp,pre)
        if tg is None: return None
        a=np.clip(ap._move_to(rp,tg),-MAXS,MAXS)
        obs,_,term,trunc,_=env.step(a.astype(np.float32))
        if term or trunc: return None
    if not ok: return None
    cors=[]; th0=obs[2]; travel=0; rl=[]; contact=0
    for t in range(17):
        B=Block(obs); rp=obs[16:18].copy()
        tgt=B.to_world(p-n*0.098)+B.dir_world(n)*MAXS
        a=np.clip(ap._move_to(rp,tgt),-MAXS,MAXS)
        obs2,_,term,trunc,_=env.step(a.astype(np.float32))
        travel+=np.linalg.norm(obs2[16:18]-rp)
        dth=wrap(obs2[2]-obs[2])
        if abs(dth)>0.004:
            v=B.Rm.T@(obs2[0:2]-obs[0:2]); u=v/dth; cors.append((-u[1],u[0]))
        B2=Block(obs2); rl.append(B2.to_local(obs2[16:18]).tolist())
        if B2.dist(obs2[16:18])<R_ROBOT+0.01: contact+=1
        obs=obs2
        if term or trunc: break
    return dict(seed=seed,name=name,w=B.w,Lh=B.Lh,Lv=B.Lv,cors=cors,dth=wrap(obs[2]-th0),travel=travel,rl=rl,contact=contact,p=p.tolist(),n=n.tolist())
jobs=[(s,nm) for nm in NAMES for s in range(3000,3060)]
with ThreadPoolExecutor(16) as ex: res=[r for r in ex.map(run,jobs) if r]
json.dump(res,open('cor2_data.json','w'))
print(len(res))
