from env_client import make_env
from probe_base_fk import fk
import numpy as np
def ik(p, q, tool=0.12, it=300):
    q=np.array(q,float)
    for _ in range(it):
        def err(q):
            T=fk(q,tool); return np.concatenate([T[:3,3]-p, 0.3*(T[:3,2]-np.array([0,0,-1]))])
        e=err(q)
        if np.linalg.norm(e)<1e-5: break
        J=np.zeros((6,7))
        for i in range(7):
            dq=np.zeros(7); dq[i]=1e-5; J[:,i]=(err(q+dq)-e)/1e-5
        q=q-J.T@np.linalg.solve(J@J.T+1e-4*np.eye(6),e)
    return q, np.linalg.norm(e)
env=make_env()
def goto(obs,R,qt):
    """move joints to qt in steps<=0.1; return (obs, rejected_flag)"""
    for _ in range(200):
        q=np.array([obs.get(R,f"joint_{i}") for i in range(1,8)])
        d=np.clip(qt-q,-0.1,0.1)
        if np.abs(d).max()<1e-6: return obs,False
        a=np.zeros(11,np.float32); a[3:10]=d; a[10]=1
        obs,*_=env.step(a)
        q2=np.array([obs.get(R,f"joint_{i}") for i in range(1,8)])
        if np.allclose(q2,q): return obs,True
    return obs,False
def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
for seed in [1,0,2]:
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
    TB=obs.get_object_from_name("target_block")
    tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
    for label,xy in [("above block",tb),("empty spot",tb+np.array([0,0.15 if tb[1]<0 else -0.15]))]:
        obs,_=env.reset(seed=seed); o0=objs(obs)
        rel=xy-base
        qh=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2])
        obs,rj=goto(obs,R,qh)
        q=qh; last=None
        for zr in np.arange(0.40,-0.6,-0.01):
            qt,err=ik(np.array([rel[0],rel[1],zr]),q)
            if err>1e-3: print("ik fail",zr); break
            obs,rj=goto(obs,R,qt); q=qt
            if rj: break
            last=zr
        o=objs(obs)
        mv={k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6}
        print(f"seed{seed} {label} xy={np.round(xy,3)}: lowest ok z_rel={last}, rejected={rj}, moved={mv}")
env.close()
