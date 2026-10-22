import numpy as np
from env_client import make_env
SEL=dict(sample=-0.8333,calibrate=-0.5,image=-0.1667,noop=0,send=0.5,drop=0.8333)
env=make_env()
class S: obs=None; te=False; tr=False; n=0
def reset(seed):
    S.obs,info=env.reset(seed=seed); S.n=0; return info
def g(name,f): o=S.obs.get_object_from_name(name); return float(S.obs.get(o,f))
def R(i): return [round(g(f'rover{i}',f),3) for f in ['x','y','theta','store_full','calibrated','at_home']]
def SM(j): return [round(g(f'sample{j}',f),3) for f in ['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis']]
def step(a0=(0,0,0),s0='noop',a1=(0,0,0),s1='noop'):
    a=list(a0)+[SEL[s0]]+list(a1)+[SEL[s1]]
    S.obs,r,te,tr,info=env.step(np.array(a,dtype=np.float32)); S.n+=1
    S.te,S.tr=te,tr; return r,te,tr
def goto(i,x,y,th=None,maxn=200):
    for _ in range(maxn):
        p=R(i); dx=x-p[0]; dy=y-p[1]; dt=0 if th is None else (th-p[2]+np.pi)%(2*np.pi)-np.pi
        if abs(dx)<1e-3 and abs(dy)<1e-3 and abs(dt)<1e-3: return True
        m=(np.clip(dx,-.2,.2),np.clip(dy,-.2,.2),np.clip(dt,-.2,.2))
        if i==0: step(m)
        else: step(a1=m)
        q=R(i)
        if q[:3]==p[:3]: print('stuck',i,p); return False
    return False
