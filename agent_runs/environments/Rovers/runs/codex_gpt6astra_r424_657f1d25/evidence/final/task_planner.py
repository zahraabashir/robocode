"""Small cooperative task-tour planner using grid distance transforms."""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra


def assign_tasks(policy, state):
    # Keep planning bounded if a future variant adds many more objectives.
    if len(policy.objectives)>5:
        return None
    n=policy.size
    free=policy.free.reshape(n,n)
    ids=np.arange(n*n).reshape(n,n)
    rows=[];cols=[];weights=[]
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
        ya=slice(max(0,-dy),min(n,n-dy));xa=slice(max(0,-dx),min(n,n-dx))
        yb=slice(max(0,dy),min(n,n+dy));xb=slice(max(0,dx),min(n,n+dx))
        ok=free[ya,xa]&free[yb,xb]
        if dx and dy:ok &= free[ya,xb]&free[yb,xa]
        src=ids[ya,xa][ok];dst=ids[yb,xb][ok]
        rows.extend(src);cols.extend(dst);weights.extend([.5+(.0005 if dx and dy else 0.)]*len(src))
    graph=csr_matrix((weights,(rows,cols)),shape=(n*n,n*n))
    tasks=[('image',k) for k in range(len(policy.objectives))]+[('soil',0),('soil',1)]
    masks=[]
    for kind,k in tasks:
        if kind=='image':masks.append(policy.masks[(kind,k)])
        else:
            mask=np.zeros(n*n,dtype=bool)
            for j,o in enumerate(policy.samples):
                if int(state.get(o,'is_soil'))==k:mask |= policy.masks[('sample',j)]
            masks.append(mask)
    def field(mask):
        goals=np.flatnonzero(mask & policy.free)
        if len(goals)==0:return np.full(n*n,np.inf),np.zeros(n*n,dtype=int)
        d,_,sources=dijkstra(graph,directed=False,indices=goals,return_predecessors=True,min_only=True)
        return d,sources
    fields=[field(m) for m in masks]
    count=len(tasks)
    full=(1<<count)-1
    results=[]
    for r in range(2):
        back,_=field(np.linalg.norm(policy.points-policy.home[r],axis=1)<.24)
        root=int(np.argmin(np.linalg.norm(policy.points-policy.home[r],axis=1)+(~policy.free)*100))
        best=np.full(1<<count,np.inf);paths=[[] for _ in best];cache={}
        def visit(at, mask, cost, seq):
            total=cost+back[at]
            if total<best[mask]:best[mask]=total;paths[mask]=seq
            for k,(dist,target) in enumerate(fields):
                if mask & (1<<k) or not np.isfinite(dist[at]):continue
                nxt=int(target[at]);bits=mask|(1<<k)
                service=1.2 if tasks[k][0]=='image' else .2
                new=cost+max(0.,dist[at])+service
                key=(nxt,bits)
                if new>=cache.get(key,1e20):continue
                cache[key]=new
                visit(nxt,bits,new,seq+[tasks[k]])
        visit(root,0,0.,[])
        results.append((best,paths))
    options=[]
    for mask in range(full+1):
        c0=results[0][0][mask];c1=results[1][0][full^mask]
        if np.isfinite(c0+c1):options.append((max(c0,c1)+.05*(c0+c1),mask))
    if not options:return None
    _,mask=min(options)
    return [results[0][1][mask],results[1][1][full^mask]]
