from env_client import make_env
import numpy as np
SEL=dict(sample=-0.8333,cal=-0.5,image=-0.1667,noop=0.0,send=0.5,drop=0.8333)
class E:
    def __init__(s,seed=0):
        s.env=make_env(); s.obs,s.info=s.env.reset(seed=seed); s.t=0; s.last=None
    def g(s,name,f): return float(s.obs.get(s.obs.get_object_from_name(name),f))
    def objs(s,typ): return [o.name for o in s.obs if o.type.name==typ]
    def feats(s,name): o=s.obs.get_object_from_name(name); return [round(float(v),4) for v in s.obs.data[o]]
    def pose(s,k): r=f'rover{k}'; return (round(s.g(r,'x'),4),round(s.g(r,'y'),4),round(s.g(r,'theta'),4))
    def step(s,a0=(0,0,0,0),a1=(0,0,0,0)):
        a=np.array(list(a0)+list(a1),dtype=np.float32)
        s.obs,r,te,tr,inf=s.env.step(a); s.t+=1; s.last=(r,te,tr,inf); return s.last
    def act(s,k,mv=(0,0,0),sel=0.0):
        a=list(mv)+[sel]; z=[0,0,0,0]
        return s.step(a,z) if k==0 else s.step(z,a)
    def goto(s,k,x,y,tol=0.002,maxit=300):
        for i in range(maxit):
            px,py,_=s.pose(k); dx,dy=x-px,y-py
            if abs(dx)<tol and abs(dy)<tol: return True
            mx,my=np.clip(dx,-0.2,0.2),np.clip(dy,-0.2,0.2)
            s.act(k,(mx,my,0))
            nx,ny,_=s.pose(k)
            if abs(nx-px)<1e-6 and abs(ny-py)<1e-6:
                # blocked: try axis separately
                s.act(k,(mx,0,0)); s.act(k,(0,my,0))
                nx2,ny2,_=s.pose(k)
                if abs(nx2-px)<1e-6 and abs(ny2-py)<1e-6: return False
        return False
    def turn(s,k,th):
        for i in range(50):
            d=(th-s.pose(k)[2]+np.pi)%(2*np.pi)-np.pi
            if abs(d)<1e-4: return
            s.act(k,(0,0,np.clip(d,-0.4,0.4)))
    def flags(s):
        out={}
        for o in s.obs:
            if o.type.name in ('rover','objective','sample'):
                out[o.name]=s.feats(o.name)
        return out
def diff(a,b):
    return {k:(a[k],b[k]) for k in a if a[k]!=b[k]}

import heapq
def plan(e,k,goal,clr=0.27,res=0.05):
    obs=[]
    for o in e.obs:
        if o.type.name=='obstacle':
            n=o.name; obs.append((e.g(n,'x'),e.g(n,'y'),e.g(n,'half_x'),e.g(n,'half_y')))
    def free(x,y):
        if abs(x)>2.5-0.2 or abs(y)>2.5-0.2: return False
        if k==0 and x<0.24: return False
        if k==1 and x>-0.24: return False
        for ox,oy,hx,hy in obs:
            if abs(x-ox)<hx+clr and abs(y-oy)<hy+clr: return False
        return True
    st=e.pose(k)[:2]
    toi=lambda p:(int(round(p[0]/res)),int(round(p[1]/res)))
    s=toi(st); g=toi(goal)
    pq=[(0,s)]; came={s:None}; cost={s:0}
    while pq:
        _,c=heapq.heappop(pq)
        if c==g: break
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx==dy==0: continue
                n=(c[0]+dx,c[1]+dy)
                if not free(n[0]*res,n[1]*res) and n!=g: continue
                nc=cost[c]+np.hypot(dx,dy)
                if n not in cost or nc<cost[n]:
                    cost[n]=nc; came[n]=c; heapq.heappush(pq,(nc+np.hypot(n[0]-g[0],n[1]-g[1]),n))
    if g not in came: return None
    path=[]; c=g
    while c: path.append((c[0]*res,c[1]*res)); c=came[c]
    return path[::-1]
def nav(e,k,goal,clr=0.27):
    path=plan(e,k,goal,clr)
    if path is None: return False
    # compress: follow points
    for p in path[1:]:
        e.goto(k,*p,maxit=5)
    return e.goto(k,*goal,maxit=20)
