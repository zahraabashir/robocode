import math
import heapq
import numpy as np

class DensePlanner:
    def __init__(self, action_space, observation_space, primitives):
        self.space=observation_space
        self.action_space=action_space

    def reset(self,state,info):
        self.robot=next(iter(state.get_objects(self.space.get_type('crv_robot'))))
        targets=list(state.get_objects(self.space.get_type('target_region')))
        self.target=targets[0]
        self.obstacles=[tuple(float(state.get(o,f)) for f in ('x','y','width','height','theta')) for o in state.get_objects(self.space.get_type('rectangle')) if o not in targets]
        self.target_data=tuple(float(state.get(self.target,f)) for f in ('x','y','width','height','theta'))
        self.obstacles=[(x+min(w,0)*math.cos(t)-min(h,0)*math.sin(t),y+min(w,0)*math.sin(t)+min(h,0)*math.cos(t),abs(w),abs(h),t) for x,y,w,h,t in self.obstacles]
        self.radius=float(state.get(self.robot,'base_radius'))+1e-5
        walls=sorted(set((x,x+w) for x,y,w,h,t in self.obstacles if abs(math.sin(t))<1e-8))
        corridor_width=min((b[0]-a[1] for a,b in zip(walls,walls[1:]) if b[0]>a[1]),default=float('inf'))
        self.heading=math.pi/2 if corridor_width<2*self.radius+.01 else 0.
        self.ghx=float(state.get(self.robot,'gripper_height' if self.heading else 'gripper_width'))/2+1e-5
        self.ghy=float(state.get(self.robot,'gripper_width' if self.heading else 'gripper_height'))/2+1e-5
        self.arm=.1
        self.goffx=0. if self.heading else self.arm
        self.goffy=self.arm if self.heading else 0.
        self.path=[]
        self.last=None
        self.stuck=0
        self.plan(state)

    def clear(self,points):
        p=np.asarray(points).reshape(-1,2);r=self.radius
        px,py=p[:,0],p[:,1];gx,gy=px+self.goffx,py+self.goffy
        good=(px>=r)&(px<=2.5-r)&(py>=r)&(py<=2.5-r)&(gy+self.ghy<=2.5)&(gx+self.ghx<=2.5)&(gy-self.ghy>=0)&(gx-self.ghx>=0)
        for x,y,w,h,t in self.obstacles:
            c,s=math.cos(t),math.sin(t)
            dx,dy=px-x,py-y
            u,v=c*dx+s*dy,-s*dx+c*dy
            ex=np.maximum(np.maximum(-u,u-w),0);ey=np.maximum(np.maximum(-v,v-h),0)
            good &= ex*ex+ey*ey>r*r
            # SAT: vertical gripper against arbitrary oriented obstacle.
            ocx=x+c*w/2-s*h/2;ocy=y+s*w/2+c*h/2
            dx,dy=gx-ocx,gy-ocy
            sep=(np.abs(dx)>self.ghx+abs(c)*w/2+abs(s)*h/2)|(np.abs(dy)>self.ghy+abs(s)*w/2+abs(c)*h/2)
            sep|=(np.abs(c*dx+s*dy)>w/2+abs(c)*self.ghx+abs(s)*self.ghy)|(np.abs(-s*dx+c*dy)>h/2+abs(s)*self.ghx+abs(c)*self.ghy)
            good &= sep
        return good

    def segment_clear(self,a,b):
        n=max(2,int(np.max(np.abs(b-a))/.002)+2)
        return bool(np.all(self.clear(np.linspace(a,b,n))))

    def plan(self,state):
        pos=np.array([state.get(self.robot,'x'),state.get(self.robot,'y')])
        x,y,w,h,t=self.target_data
        xs=list(np.arange(.1,2.401,.02))+[pos[0],x+.001,x+w-.001,x+w/2]
        ys=list(np.arange(.1,2.401,.02))+[pos[1],y+.001,y+h-.001,y+h/2,self.radius+.00001,2.5-max(self.radius,self.goffy+self.ghy)-.00001]
        boundaries=[.0,2.5]
        for ox,oy,ow,oh,ot in self.obstacles:
            if abs(ot)<1e-8:
                xs += [ox-self.radius-.00001,ox+ow+self.radius+.00001]
                ys += [oy-max(self.radius,self.goffy+self.ghy)-.00001,oy+oh+self.radius+.00001,(oy+2.5)/2,(oy+oh+2.5)/2]
                boundaries += [ox,ox+ow]
        walls=sorted(set(boundaries))
        xs += [(a+b)/2 for a,b in zip(walls,walls[1:]) if b-a>2*self.radius]
        xa=np.unique(np.array(xs));ya=np.unique(np.array(ys))
        xa=xa[(xa>=self.radius)&(xa<=2.5-self.radius)];ya=ya[(ya>=self.radius)&(ya<=2.5-self.radius)]
        xx,yy=np.meshgrid(xa,ya,indexing='ij');nx,ny=xx.shape
        free=self.clear(np.stack([xx.ravel(),yy.ravel()],axis=-1)).reshape(nx,ny)
        c,s=math.cos(t),math.sin(t);u=c*(xx-x)+s*(yy-y);v=-s*(xx-x)+c*(yy-y)
        goal=free&(u>.0001)&(u<w-.0001)&(v>.0001)&(v<h-.0001)
        start=(int(np.argmin(abs(xa-pos[0]))),int(np.argmin(abs(ya-pos[1]))));free[start]=True
        # Distance to goal bounding rectangle is an admissible Euclidean heuristic.
        heuristic=np.maximum(np.maximum(np.maximum(x-xx,xx-x-w),0),np.maximum(np.maximum(y-yy,yy-y-h),0))
        dist=np.full((nx,ny),np.inf);parents=np.full((nx,ny),-1,np.int32);dist[start]=0
        heap=[(float(heuristic[start]),0,*start)];end=None
        while heap:
            _,negative_d,i,j=heapq.heappop(heap)
            d=-negative_d
            if d>dist[i,j]+1e-10:continue
            if goal[i,j]:end=(i,j);break
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                ni,nj=i+di,j+dj
                if ni<0 or ni>=nx or nj<0 or nj>=ny or not free[ni,nj]:continue
                if di and dj and not(free[i,nj] and free[ni,j]):continue
                nd=d+max(abs(xa[ni]-xa[i]),abs(ya[nj]-ya[j]))
                if nd<dist[ni,nj]-1e-10:
                    dist[ni,nj]=nd;parents[ni,nj]=i*ny+j
                    heapq.heappush(heap,(nd+heuristic[ni,nj],-nd,ni,nj))
        if end is None:
            self.path=[];self.solved_plan=False;return
        rev=[]
        while end!=start:
            i,j=end;rev.append(np.array([xa[i],ya[j]]));idx=int(parents[end]);end=(idx//ny,idx%ny)
        raw=list(reversed(rev));self.path=[];a=pos
        while raw:
            k=len(raw)-1
            while k>0 and not self.segment_clear(a,raw[k]):k-=1
            a=raw[k];self.path.append(a);raw=raw[k+1:]
        self.solved_plan=True

    def get_action(self,state):
        theta=float(state.get(self.robot,'theta'));turn=(self.heading-theta+math.pi)%(2*math.pi)-math.pi
        if abs(turn)>1e-6:return np.array([0,0,np.clip(turn,-.19634954,.19634954),-.1,0],np.float32)
        pos=np.array([state.get(self.robot,'x'),state.get(self.robot,'y')])
        while self.path and np.max(abs(self.path[0]-pos))<1e-6:self.path.pop(0)
        if not self.path:return np.array([0,0,0,-.1,0],np.float32)
        delta=self.path[0]-pos;delta*=min(1,.05/max(1e-10,float(np.max(abs(delta)))))
        return np.array([*delta,0,-.1,0],np.float32)
