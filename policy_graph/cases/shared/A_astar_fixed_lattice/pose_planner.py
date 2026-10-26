import heapq
import math
import time
import numpy as np


class PosePlanner:
    """Spatial and angular lattice fallback for very narrow passages."""
    def __init__(self,action_space,observation_space,primitives):
        self.action_space=action_space;self.space=observation_space

    def reset(self,state,info):
        self.robot=next(iter(state.get_objects(self.space.get_type('crv_robot'))))
        targets=list(state.get_objects(self.space.get_type('target_region')))
        self.target=targets[0]
        self.target_data=tuple(float(state.get(self.target,f)) for f in ('x','y','width','height','theta'))
        self.obstacles=[]
        for o in state.get_objects(self.space.get_type('rectangle')):
            if o in targets:continue
            x,y,w,h,t=(float(state.get(o,f)) for f in ('x','y','width','height','theta'))
            c,s=math.cos(t),math.sin(t)
            self.obstacles.append((x+min(w,0)*c-min(h,0)*s,y+min(w,0)*s+min(h,0)*c,abs(w),abs(h),t))
        self.radius=float(state.get(self.robot,'base_radius'))+1e-5
        self.gw=float(state.get(self.robot,'gripper_width'))/2+1e-5
        self.gh=float(state.get(self.robot,'gripper_height'))/2+1e-5
        self.arm=.1;self.path=[];self.solved_plan=False
        self.plan(state)

    def clear(self,points,theta=None):
        p=np.asarray(points).reshape(-1,2);px,py=p.T;r=self.radius
        good=(px>=r)&(px<=2.5-r)&(py>=r)&(py<=2.5-r)
        if theta is not None:
            c,s=np.cos(theta),np.sin(theta);gx=px+self.arm*c;gy=py+self.arm*s
            hx=np.abs(c)*self.gw+np.abs(s)*self.gh;hy=np.abs(s)*self.gw+np.abs(c)*self.gh
            good&=(gx>=hx)&(gx<=2.5-hx)&(gy>=hy)&(gy<=2.5-hy)
        for x,y,w,h,t in self.obstacles:
            oc,os=math.cos(t),math.sin(t);dx,dy=px-x,py-y
            u,v=oc*dx+os*dy,-os*dx+oc*dy
            ex=np.maximum(np.maximum(-u,u-w),0);ey=np.maximum(np.maximum(-v,v-h),0)
            good&=ex*ex+ey*ey>r*r
            if theta is None:continue
            dx=gx-(x+oc*w/2-os*h/2);dy=gy-(y+os*w/2+oc*h/2)
            ac=np.abs(c*oc+s*os);ass=np.abs(s*oc-c*os)
            sep=(np.abs(oc*dx+os*dy)>w/2+self.gw*ac+self.gh*ass)|(np.abs(-os*dx+oc*dy)>h/2+self.gw*ass+self.gh*ac)
            sep|=(np.abs(c*dx+s*dy)>self.gw+w/2*ac+h/2*ass)|(np.abs(-s*dx+c*dy)>self.gh+w/2*ass+h/2*ac)
            good&=sep
        return good

    def segment_clear(self,a,b):
        da=(b[2]-a[2]+math.pi)%(2*math.pi)-math.pi
        n=max(2,int(max(abs(b[0]-a[0]),abs(b[1]-a[1]))/.002)+2,int(abs(da)/.025)+2)
        f=np.linspace(0,1,n)
        return bool(np.all(self.clear(a[:2][None,:]+f[:,None]*(b[:2]-a[:2])[None,:],a[2]+f*da)))

    def plan(self,state):
        begun=time.monotonic();pos=np.array([float(state.get(self.robot,f)) for f in ('x','y','theta')]);r=self.radius
        x,y,w,h,t=self.target_data
        xs=list(np.arange(r,2.5-r,.025))+[pos[0],x+.001,x+w-.001,x+w/2,2.5-r-.00001]
        ys=list(np.arange(r,2.5-r,.025))+[pos[1],y+.001,y+h-.001,y+h/2,2.5-r-.00001]
        boundaries=[0.,2.5]
        for ox,oy,ow,oh,ot in self.obstacles:
            if abs(ot)<1e-8:
                xs += [ox-r-.00001,ox+ow+r+.00001]
                ys += [oy-r-.00001,oy+oh+r+.00001,oy-.10502,oy+oh+.10502]
                boundaries += [ox,ox+ow]
        bs=sorted(set(boundaries));xs += [(a+b)/2 for a,b in zip(bs,bs[1:]) if b-a>2*r]
        xa=np.unique(xs);ya=np.unique(ys);xa=xa[(xa>=r)&(xa<=2.5-r)];ya=ya[(ya>=r)&(ya<=2.5-r)]
        xx,yy=np.meshgrid(xa,ya,indexing='ij');nx,ny=xx.shape;n=nx*ny
        pts=np.stack([xx.ravel(),yy.ravel()],axis=-1);base=self.clear(pts).reshape(nx,ny)
        c,s=math.cos(t),math.sin(t);u=c*(xx-x)+s*(yy-y);v=-s*(xx-x)+c*(yy-y)
        goal=base&(u>.0001)&(u<w-.0001)&(v>.0001)&(v<h-.0001)
        start=(int(np.argmin(abs(xa-pos[0]))),int(np.argmin(abs(ya-pos[1]))));base[start]=True
        # A reverse translational search supplies a maze-aware lower bound.
        neighbors=[[] for _ in range(n)]
        for i,j in np.argwhere(base):
            idx=int(i*ny+j)
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                ni,nj=i+di,j+dj
                if not(0<=ni<nx and 0<=nj<ny and base[ni,nj]):continue
                if di and dj and not(base[i,nj] and base[ni,j]):continue
                neighbors[idx].append((int(ni*ny+nj),max(abs(xa[ni]-xa[i]),abs(ya[nj]-ya[j]))/.05))
        heuristic=np.full(n,np.inf);heap=[]
        for idx in np.flatnonzero(goal.ravel()):heuristic[idx]=0;heap.append((0,int(idx)))
        heapq.heapify(heap)
        while heap:
            d,idx=heapq.heappop(heap)
            if d>heuristic[idx]+1e-8:continue
            for ni,cost in neighbors[idx]:
                nd=d+cost
                if nd<heuristic[ni]-1e-8:heuristic[ni]=nd;heapq.heappush(heap,(nd,ni))
        si=start[0]*ny+start[1]
        if not np.isfinite(heuristic[si]):return
        angles=np.arange(32)*math.pi/16
        free=np.stack([self.clear(pts,a) for a in angles]);startk=int(round(pos[2]/(math.pi/16)))%32
        sid=startk*n+si;free[startk,si]=True
        dist=np.full(32*n,np.inf);parent=np.full(32*n,-1,np.int32);dist[sid]=0
        heap=[(heuristic[si]*1.12,0,sid)];end=None;expanded=0
        while heap:
            _,d,idx=heapq.heappop(heap)
            if d>dist[idx]+1e-8:continue
            expanded+=1
            if expanded%1024==0 and time.monotonic()-begun>12:break
            k,loc=divmod(idx,n)
            if goal.ravel()[loc]:end=idx;break
            # Rotation in place and translation with optional simultaneous rotation.
            for nk in [k,(k-1)%32,(k+1)%32]:
                candidates=neighbors[loc] if nk==k else [(loc,0)]+neighbors[loc]
                for nl,cost in candidates:
                    if not free[nk,nl]:continue
                    nd=d+max(cost,0 if nk==k else 1)
                    ni=nk*n+nl
                    if nd>=dist[ni]-1e-8:continue
                    if nk!=k:
                        midpoint=(pts[loc]+pts[nl])/2
                        midangle=angles[k]+((angles[nk]-angles[k]+math.pi)%(2*math.pi)-math.pi)/2
                        if not self.clear(midpoint,midangle)[0]:continue
                    dist[ni]=nd;parent[ni]=idx
                    heapq.heappush(heap,(nd+1.12*heuristic[nl],nd,ni))
        self.expanded=expanded;self.plan_seconds=time.monotonic()-begun
        if end is None:return
        rev=[]
        while end!=sid:
            k,loc=divmod(end,n);rev.append(np.array([*pts[loc],angles[k]]));end=int(parent[end])
        raw=[np.array([*pts[si],angles[startk]])]+list(reversed(rev));a=pos
        while raw:
            # Limit greedy checks: long angular moves are rarely useful.
            candidate=min(len(raw)-1,80)
            while candidate>0 and not self.segment_clear(a,raw[candidate]):candidate-=1
            a=raw[candidate];self.path.append(a);raw=raw[candidate+1:]
        self.solved_plan=True

    def get_action(self,state):
        pos=np.array([float(state.get(self.robot,f)) for f in ('x','y','theta')])
        while self.path:
            p=self.path[0];delta=p-pos;delta[2]=(delta[2]+math.pi)%(2*math.pi)-math.pi
            if np.max(abs(delta))<1e-6:self.path.pop(0)
            else:break
        if not self.path:return np.array([0,0,0,-.1,0],np.float32)
        scale=min(1,.05/max(1e-12,abs(delta[0]),abs(delta[1])),.19634954/max(1e-12,abs(delta[2])))
        delta*=scale
        return np.array([*delta,-.1,0],np.float32)
