import numpy as np, heapq
from env_client import make_env
M=0.0499
R=0.1
def rot(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
def rects_local(w,Lh,Lv):
    # (x0,x1,y0,y1): bar then stem; origin = top-center of bar
    return [(-Lh/2,Lh/2,-w,0.0),(-w/2,w/2,-w-Lv,-w)]
def to_world(pose,P): return np.asarray(P)@rot(pose[2]).T+pose[:2]
def to_local(pose,p): return (np.asarray(p)-pose[:2])@rot(pose[2])
def block_dist_many(obs,pts):
    pose=obs[0:3]; w,Lh,Lv=obs[12],obs[13],obs[14]
    pl=to_local(pose,np.atleast_2d(pts))
    ds=[]
    for x0,x1,y0,y1 in rects_local(w,Lh,Lv):
        dx=np.maximum(np.maximum(x0-pl[:,0],pl[:,0]-x1),0); dy=np.maximum(np.maximum(y0-pl[:,1],pl[:,1]-y1),0)
        ds.append(np.hypot(dx,dy))
    return np.min(ds,axis=0)
def plan(obs,goal,clear=0.2,h=0.05,lo=0.13,hi=4.87):
    start=obs[16:18].copy(); goal=np.asarray(goal,float)
    xs=np.arange(lo,hi+1e-9,h); n=len(xs)
    X,Y=np.meshgrid(xs,xs,indexing='ij')
    free=(block_dist_many(obs,np.stack([X.ravel(),Y.ravel()],1))>clear).reshape(n,n)
    def idx(p): return (int(np.clip(round((p[0]-lo)/h),0,n-1)),int(np.clip(round((p[1]-lo)/h),0,n-1)))
    s,g=idx(start),idx(goal)
    free[s]=True; free[g]=True
    pq=[(0,s)]; came={s:None}; cost={s:0}
    while pq:
        _,c=heapq.heappop(pq)
        if c==g: break
        for di in (-1,0,1):
            for dj in (-1,0,1):
                if di==dj==0: continue
                nb=(c[0]+di,c[1]+dj)
                if not(0<=nb[0]<n and 0<=nb[1]<n) or not free[nb]: continue
                nc=cost[c]+np.hypot(di,dj)
                if nb not in cost or nc<cost[nb]:
                    cost[nb]=nc; came[nb]=c
                    heapq.heappush(pq,(nc+np.hypot(nb[0]-g[0],nb[1]-g[1]),nb))
    if g not in came: return None
    path=[]; c=g
    while c is not None: path.append(np.array([xs[c[0]],xs[c[1]]])); c=came[c]
    path=path[::-1][1:]
    # shortcut: prune waypoints whose straight segment is clear
    pts=[start]+path+[goal]; out=[]; i=0
    while i<len(pts)-1:
        j=len(pts)-1
        while j>i+1:
            seg=pts[i]+np.linspace(0,1,40)[:,None]*(pts[j]-pts[i])
            if (block_dist_many(obs,seg)>clear-0.03).all(): break
            j-=1
        out.append(pts[j]); i=j
    return out
def goto(env,obs,pt,max_step=M):
    for _ in range(400):
        d=pt-obs[16:18]
        if np.linalg.norm(d)<1e-6: break
        a=d if np.max(np.abs(d))<=max_step else d/np.max(np.abs(d))*max_step
        obs,*_=env.step(a)
    return obs
def navigate(env,obs,goal,clear=0.2):
    path=plan(obs,goal,clear)
    if path is None: return obs,False
    b0=obs[0:3].copy()
    for wp in path:
        obs=goto(env,obs,wp)
    moved=np.abs(obs[0:3]-b0).max()>1e-6
    return obs,(not moved) and np.linalg.norm(obs[16:18]-goal)<1e-3
def backoff(env,obs,clear=0.2):
    for _ in range(40):
        p=obs[16:18]; d0=block_dist_many(obs,p)[0]
        if d0>=clear+0.01: break
        eps=1e-4
        g=np.array([block_dist_many(obs,p+[eps,0])[0]-d0,block_dist_many(obs,p+[0,eps])[0]-d0])
        g=g/(np.linalg.norm(g)+1e-12)
        if p[0]<0.3: g[0]=max(g[0],0.3)
        if p[1]<0.3: g[1]=max(g[1],0.3)
        if p[0]>4.7: g[0]=min(g[0],-0.3)
        if p[1]>4.7: g[1]=min(g[1],-0.3)
        obs,*_=env.step(g/np.linalg.norm(g)*0.03)
    return obs
_nav_old=navigate
def navigate(env,obs,goal,clear=0.2):
    obs=backoff(env,obs,clear)
    return _nav_old(env,obs,goal,clear)
