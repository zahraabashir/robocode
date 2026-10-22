import numpy as np
import math
import heapq

def wrap(a):
    return (a+math.pi)%(2*math.pi)-math.pi

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.reset(None, {})

    def reset(self, state, info):
        self.steps=0
        self.contact=None
        self.age=0
        self.last=None

    def geometry(self,s):
        w,h,v=s[12:15]
        self.rects=[np.array([-h/2,h/2,-w,0]),np.array([-w/2,w/2,-v-w,-w])]
        # Sample exposed surfaces with inward normals.
        points=[]; normals=[]
        def edge(a,b,n,count):
            for t in np.linspace(.04,.96,count):
                points.append(np.array(a)*(1-t)+np.array(b)*t); normals.append(n)
        edge([-h/2,0],[h/2,0],[0,-1],15)
        edge([-h/2,-w],[-h/2,0],[1,0],3)
        edge([h/2,-w],[h/2,0],[-1,0],3)
        edge([-h/2,-w],[-w/2,-w],[0,1],6)
        edge([w/2,-w],[h/2,-w],[0,1],6)
        edge([-w/2,-v-w],[-w/2,-w],[1,0],13)
        edge([w/2,-v-w],[w/2,-w],[-1,0],13)
        edge([-w/2,-v-w],[w/2,-v-w],[0,1],3)
        self.pts=np.array(points); self.normals=np.array(normals)

    def free(self,a,b,margin):
        for rect in self.rects:
            lo=rect[[0,2]]-margin; hi=rect[[1,3]]+margin
            dd=b-a; t0=0.; t1=1.
            for j in range(2):
                if abs(dd[j])<1e-10:
                    if a[j]<=lo[j] or a[j]>=hi[j]: t1=-1.; break
                else:
                    z=(lo[j]-a[j])/dd[j]; zz=(hi[j]-a[j])/dd[j]
                    t0=max(t0,min(z,zz)); t1=min(t1,max(z,zz))
            if t0<t1-1e-7: return False
        return True

    def navigate(self,a,b,radius):
        margin=radius+.009
        if self.free(a,b,margin): return b
        # Axis-aligned expanded rectangles give a small visibility graph.
        vertices=[a,b]
        for rect in self.rects:
            x0,x1,y0,y1=rect+np.array([-1,1,-1,1])*(margin+.006)
            for x,y in [(x0,y0),(x0,y1),(x1,y0),(x1,y1)]:
                p=np.array([x,y])
                if self.free(p,p,margin) and np.all((p@self.R.T+self.origin>.105)&(p@self.R.T+self.origin<4.895)): vertices.append(p)
        # If touching, first move out along the nearest boundary.
        if not self.free(a,a,margin):
            choices=[]
            for rect in self.rects:
                lo=rect[[0,2]]-margin-.008; hi=rect[[1,3]]+margin+.008
                for j in range(2):
                    for v in [lo[j],hi[j]]:
                        p=a.copy(); p[j]=v
                        if self.free(p,p,margin): choices.append(p)
            if choices: return min(choices,key=lambda p:np.linalg.norm(p-a))
        n=len(vertices); dist=[1e9]*n; prev=[-1]*n; dist[0]=0; heap=[(0,0)]
        while heap:
            d,i=heapq.heappop(heap)
            if d>dist[i]+1e-8: continue
            if i==1: break
            for j in range(1,n):
                if i!=j and self.free(vertices[i],vertices[j],margin):
                    nd=d+np.linalg.norm(vertices[i]-vertices[j])
                    if nd<dist[j]: dist[j]=nd;prev[j]=i;heapq.heappush(heap,(nd,j))
        j=1
        if prev[j]<0:return b
        while prev[j]>0:j=prev[j]
        return vertices[j]

    def get_action(self,state):
        s=np.asarray(state); self.steps+=1
        self.geometry(s)
        self.origin=s[:2]
        c,ss=math.cos(s[2]),math.sin(s[2]); R=np.array([[c,-ss],[ss,c]])
        self.R=R
        robot=(s[16:18]-s[:2])@R
        delta=(s[29:31]-s[:2])@R; angle=wrap(s[31]-s[2])
        # Approximate generalized displacement due to unit normal force.
        w,h,v=s[12:15]
        cy=-(h*w/2+v*(w+v/2))/(h+v)
        com=np.array([0.,cy])
        inertia=(h*((h*h+w*w)/12+(-w/2-cy)**2)+v*((w*w+v*v)/12+(-w-v/2-cy)**2))/(h+v)
        rr=self.pts-com
        torque=rr[:,0]*self.normals[:,1]-rr[:,1]*self.normals[:,0]
        omega=torque/(inertia+np.sum(rr*rr,axis=1))
        vel=self.normals-omega[:,None]*np.column_stack((-self.pts[:,1],self.pts[:,0]))
        desired=np.r_[delta,angle]
        J=np.column_stack((vel,omega))
        weights=np.array([1.,1.,.6])
        dot=(J*weights)@desired
        norm=np.sum(J*J*weights,axis=1)
        gain=np.maximum(0,dot)**2/norm
        staging=self.pts-self.normals*(s[28]+.045)
        distances=np.linalg.norm(staging-robot,axis=1)
        score=gain/(.20+distances*.28)
        world_stage=staging@R.T+s[:2]
        score[np.any((world_stage<.115)|(world_stage>4.885),axis=1)]=0.
        for i in range(len(score)):
            cp=self.pts[i]-self.normals[i]*(s[28]+.002)
            if not self.free(cp,cp,s[28]-.001) or not self.free(staging[i],staging[i],s[28]+.009): score[i]=0.
        best=int(np.argmax(score))
        if self.contact is None:
            self.contact=best; self.age=0
        else:
            self.age+=1
            cur=self.contact
            if score[cur]<=0 or dot[cur]<=0 or (self.age>8 and score[best]>score[cur]*1.5) or self.age>70:
                self.contact=best; self.age=0
        k=self.contact; n=self.normals[k]; p=self.pts[k]
        stage=staging[k]
        along=np.dot(robot-p,n); lateral=np.linalg.norm(robot-p-along*n)
        if lateral<.035 and along<-.06 and along>-(s[28]+.10):
            step=min(.045,max(.004,dot[k]/norm[k]*.45))
            target=p-n*(s[28]-.008)+n*step
        else:
            target=self.navigate(robot,stage,s[28])
        a=(target-robot)@R.T
        a*=min(1.,.049/max(np.max(np.abs(a)),1e-9))
        self.last=s.copy()
        return a
