from env_client import make_env
import numpy as np, sys
env=make_env()
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
def goto(env,obs,tgt,step=0.049):
    r=obs[16:18].copy()
    while True:
        d=tgt-r; n=np.linalg.norm(d)
        if n<1e-9: return obs
        a=d if n<=step else d/n*step
        obs,_,_,_,_=env.step(np.clip(a,-0.0499,0.0499)); r=obs[16:18].copy()
        if np.linalg.norm(tgt-r)>=n-1e-9 and n>1e-6: print("stuck",r,tgt); return obs
def probe(seed,p_loc,d_loc,back=0.5,Rc=1.7):
    obs,_=env.reset(seed=seed); b0=obs[0:3].copy(); c=b0[:2]; th=b0[2]
    p=c+R(th)@np.array(p_loc); d=R(th)@np.array(d_loc,float); d/=np.linalg.norm(d)
    start=p-d*back
    # navigate: radial out to Rc, around circle, then in to start
    r=obs[16:18]; a0=np.arctan2(*(r-c)[::-1]); a1=np.arctan2(*(start-c)[::-1])
    path=[c+Rc*np.array([np.cos(a0),np.sin(a0)])]
    da=(a1-a0+np.pi)%(2*np.pi)-np.pi
    for k in range(1,21): a=a0+da*k/20; path.append(c+Rc*np.array([np.cos(a),np.sin(a)]))
    path.append(start)
    for w in path: obs=goto(env,obs,w,0.02)
    if np.abs(obs[0:3]-b0).max()>1e-6: return None,"moved during nav"
    r=obs[16:18].copy()
    for i in range(1500):
        prev=obs[16:18].copy()
        obs,_,_,_,_=env.step(d*0.001 if i>0 else d*0.0)
        if np.abs(obs[0:3]-b0).max()>1e-7:
            loc=R(th).T@(prev-c); return loc, obs[0:3]-b0
    return None,"no contact"
if __name__=="__main__":
    for s in map(int,sys.argv[1:]):
        o,_=env.reset(seed=s); w,Lh,Lv=o[12:15]
        print("seed",s,"pose",o[0:3],"w,Lh,Lv",w,Lh,Lv)
        probes={"top":((0,0.4),(0,-1)),"rightend":((Lh/2+0.3,-w/2),(-1,0)),"leftend":((-Lh/2-0.3,-w/2),(1,0)),
                "under_r":((0.4,-0.7),(0,1)),"stemtip":((0,-Lv-0.4),(0,1)),"stemside":((0.5,-0.7),(-1,0))}
        for k,(p,d) in probes.items():
            loc,res=probe(s,p,d)
            print(f"  {k}: robot_local={loc} dblock={res}")
