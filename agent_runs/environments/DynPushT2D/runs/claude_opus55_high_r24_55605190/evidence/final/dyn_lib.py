from env_client import make_env
import numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=200)
def R(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
def to_body(obs,p): return R(obs[2]).T@(np.asarray(p)-obs[0:2])
def to_world(obs,pb): return obs[0:2]+R(obs[2])@np.asarray(pb)
class E:
    def __init__(s,seed=0):
        s.env=make_env(); s.obs,_=s.env.reset(seed=seed); s.n=0
    def step(s,a):
        a=np.clip(np.asarray(a,float),-0.049,0.049)
        s.obs,r,te,tr,_=s.env.step(a); s.n+=1; return s.obs
    def goto(s,tgt,maxstep=0.049,n=400):
        for _ in range(n):
            d=np.asarray(tgt)-s.obs[16:18]
            if np.linalg.norm(d)<1e-7: break
            m=np.max(np.abs(d)); a=d if m<=maxstep else d*maxstep/m
            s.step(a)
        return s.obs
    def goto_safe(s,tgt_body):
        # move radially out to radius 1.6 from block center, go around circle, then to target (in body frame)
        o=s.obs; c=o[0:2]; p=o[16:18]
        tw=to_world(o,tgt_body)
        Rr=1.7
        v=p-c; a0=np.arctan2(v[1],v[0])
        if np.linalg.norm(v)<Rr: s.goto(c+Rr*np.array([np.cos(a0),np.sin(a0)]))
        vt=tw-c; a1=np.arctan2(vt[1],vt[0])
        da=(a1-a0+np.pi)%(2*np.pi)-np.pi
        for k in range(1,21):
            a=a0+da*k/20; s.goto(c+Rr*np.array([np.cos(a),np.sin(a)]))
        s.goto(tw); return s.obs
