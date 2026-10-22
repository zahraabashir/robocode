from env_client import make_env
import numpy as np, math
env=make_env()
T={t.name:t for t in env.observation_space.types}
F={'rover':['x','y','theta','store_full','calibrated','at_home'],'lander':['x','y','z'],'objective':['x','y','z','have_image_rover0','have_image_rover1','received_image'],'sample':['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis'],'obstacle':['x','y','z','half_x','half_y','half_z']}
SEL={'sample':-5/6,'calibrate':-0.5,'image':-1/6,'noop':1/6,'send':0.5,'drop':5/6}
class S:
    obs=None; term=False; info=None; n=0
def reset(seed):
    S.obs,S.info=env.reset(seed=seed); S.n=0; return S.obs
def get(name):
    o=S.obs.get_object_from_name(name)
    return [float(S.obs.get(o,f)) for f in F[o.type.name]]
def names(t): return [o.name for o in S.obs.get_objects(T[t])]
def dump(t):
    return {n:[round(v,2) for v in get(n)] for n in names(t)}
def step(i=0,dx=0,dy=0,dth=0,op='noop',op2='noop'):
    a=np.zeros(8,dtype=np.float32)
    a[3]=SEL['noop']; a[7]=SEL['noop']
    a[4*i:4*i+3]=[dx,dy,dth]; a[4*i+3]=SEL[op]
    a[4*(1-i)+3]=SEL[op2]
    S.obs,r,term,trunc,S.info=env.step(a); S.n+=1; S.term=term
    return r,term,trunc
def pos(i): return get(f'rover{i}')
def goto(i,tx,ty,tol=0.02,maxn=200):
    import random
    stuck=0
    for k in range(maxn):
        x,y=pos(i)[:2]; d=math.hypot(tx-x,ty-y)
        if d<tol: return True
        s=min(0.2,d); dx=(tx-x)/d*s; dy=(ty-y)/d*s
        step(i,dx,dy)
        x2,y2=pos(i)[:2]
        if math.hypot(x2-x,y2-y)<1e-4:
            # detour
            moved=False
            for ang in [math.pi/2,-math.pi/2,math.pi/4,-math.pi/4,3*math.pi/4,-3*math.pi/4]:
                c,sn=math.cos(ang),math.sin(ang)
                ddx=(dx*c-dy*sn); ddy=(dx*sn+dy*c)
                n=0.2/max(1e-9,math.hypot(ddx,ddy))
                for _ in range(2): step(i,ddx*n,ddy*n)
                x3,y3=pos(i)[:2]
                if math.hypot(x3-x,y3-y)>1e-3: moved=True; break
            if not moved: return False
    return False
def turn_to(i,th):
    for _ in range(40):
        t=pos(i)[2]; e=(th-t+math.pi)%(2*math.pi)-math.pi
        if abs(e)<1e-3: return
        step(i,dth=max(-0.4,min(0.4,e)))
