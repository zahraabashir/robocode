from env_client import make_env
import numpy as np
env = make_env()
SP = env.observation_space
def objs(obs,t): return obs.get_objects(SP.get_type(t))
def rov(obs):
    r={o.name:o for o in objs(obs,'rover')}
    return [(float(obs.get(r[n],'x')),float(obs.get(r[n],'y')),float(obs.get(r[n],'theta'))) for n in ['rover0','rover1']]
def obst(obs):
    return {o.name:[float(obs.get(o,f)) for f in ['x','y','half_x','half_y']] for o in objs(obs,'obstacle')}
def act(a0=(0,0,0),a1=(0,0,0)):
    return np.array([a0[0],a0[1],a0[2],0,a1[0],a1[1],a1[2],0],dtype=np.float32)
def step(a0=(0,0,0),a1=(0,0,0)):
    obs,r,te,tr,info=env.step(act(a0,a1)); return obs,r,te,tr,info
def push(i,d,obs,big=0.2,tol=1e-4,maxn=200):
    """move rover i in unit direction d until blocked; refine step. returns obs"""
    s=big; n=0
    while s>tol and n<maxn:
        n+=1
        before=rov(obs)[i]
        a=(d[0]*s,d[1]*s,0)
        obs,*_=step(a,(0,0,0)) if i==0 else step((0,0,0),a)
        after=rov(obs)[i]
        if abs(after[0]-before[0])<1e-9 and abs(after[1]-before[1])<1e-9: s/=2
    return obs
def goto(i,x,y,obs,maxn=100):
    for _ in range(maxn):
        p=rov(obs)[i]; dx=np.clip(x-p[0],-.2,.2); dy=np.clip(y-p[1],-.2,.2)
        if abs(x-p[0])<1e-6 and abs(y-p[1])<1e-6: break
        a=(dx,dy,0); obs,*_=step(a,(0,0,0)) if i==0 else step((0,0,0),a)
    return obs
