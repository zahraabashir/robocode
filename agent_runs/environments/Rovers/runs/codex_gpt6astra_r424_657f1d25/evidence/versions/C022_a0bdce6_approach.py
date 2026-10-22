import math
import heapq
import numpy as np
from task_planner import assign_tasks


class GeneratedApproach:
    """Feedback navigation and task allocation for the two rovers."""
    def __init__(self, action_space, observation_space, primitives):
        self.space = observation_space
        self.types = {t.name: t for t in observation_space.types}

    def objects(self, state, kind):
        return sorted(state.get_objects(self.types[kind]), key=lambda o: o.name)

    def xy(self, state, obj):
        return np.array([state.get(obj, 'x'), state.get(obj, 'y')], dtype=float)

    def reset(self, state, info):
        self.rovers = self.objects(state, 'rover')
        self.objectives = self.objects(state, 'objective')
        self.samples = self.objects(state, 'sample')
        self.home = [self.xy(state, r) for r in self.rovers]
        self.lander = self.xy(state, self.objects(state, 'lander')[0])
        self.rects = []
        self.occluders = []
        for o in self.objects(state, 'obstacle'):
            p = self.xy(state, o)
            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
            self.rects.append((p-h, p+h))
            if state.get(o, 'half_z') > .1:
                self.occluders.append((p-h, p+h))
        self.rects.append((np.array([-.05, -3.]), np.array([.05, 3.])))
        self.rects.append((self.lander-np.array([.510,.334]),self.lander+np.array([.510,.334])))
        axis = np.arange(-2.2, 2.201, .1)
        self.size = len(axis)
        xx, yy = np.meshgrid(axis, axis)
        self.points = np.column_stack([xx.ravel(), yy.ravel()])
        self.free = self.valid(self.points)
        self.masks = {}
        for k, o in enumerate(self.objectives):
            self.masks[('image',k)] = self.free & self.visible(self.points,self.xy(state,o),1.97)
        for k, o in enumerate(self.samples):
            self.masks[('sample',k)] = self.free & self.sample_safe(state,self.points,k)
        self.masks[('send',0)] = self.free & self.visible(self.points,self.lander,3.8)
        self.tasks = [None,None]
        self.paths = [[],[]]
        self.previous = [None,None]
        self.fail = [0,0]
        self.tick = 0
        self.last_op = [None, None]
        self.bad_views = {}
        self.schedule = assign_tasks(self,state)

    def sample_safe(self, state, pts, k):
        target=self.samples[k]
        good=np.linalg.norm(pts-self.xy(state,target),axis=1)<.242
        for obj in self.samples:
            if state.get(obj,'is_soil')!=state.get(target,'is_soil'):
                good &= np.linalg.norm(pts-self.xy(state,obj),axis=1)>.255
        return good

    def valid(self, pts):
        good = np.all(np.abs(pts) <= 2.265, axis=-1)
        for lo,hi in self.rects:
            good &= np.linalg.norm(np.maximum(np.maximum(lo-pts,pts-hi),0),axis=-1) > .182
        return good

    def visible(self, pts, target, radius):
        good = np.linalg.norm(pts-target,axis=1)<radius
        d = target-pts
        length2 = np.maximum(np.sum(d*d,axis=1),1e-12)
        for lo,hi in self.occluders:
            center=(lo+hi)*.5
            t=np.clip(np.sum((center-pts)*d,axis=1)/length2,0,1)
            closest=pts+t[:,None]*d
            clearance=min(.155,float(np.linalg.norm(target-center))*.85)
            good &= np.linalg.norm(closest-center,axis=1)>clearance
        return good

    def route(self, start, mask, other=None):
        # A multi-goal Dijkstra on a small occupancy grid.
        free=self.free.copy()
        if other is not None:
            free &= np.linalg.norm(self.points-other,axis=1)>.4
        starts=np.argsort(np.linalg.norm(self.points-start,axis=1))[:20]
        root=next((int(j) for j in starts if free[j]),int(starts[0]))
        dist={root:0.}; parent={}; queue=[(0.,root)]
        n=self.size
        end=None
        while queue:
            cost,j=heapq.heappop(queue)
            if cost!=dist[j]: continue
            if mask[j]: end=j;break
            x=j%n;y=j//n
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
                nx=x+dx;ny=y+dy
                if nx<0 or nx>=n or ny<0 or ny>=n:continue
                k=ny*n+nx
                if not free[k]:continue
                if dx and dy and (not free[y*n+nx] or not free[ny*n+x]):continue
                v=cost+1.+(.001 if dx and dy else 0.)
                if v<dist.get(k,1e9):
                    dist[k]=v;parent[k]=j;heapq.heappush(queue,(v,k))
        if end is None:return [],1e6
        path=[end]
        while path[-1]!=root:path.append(parent[path[-1]])
        return [self.points[j].copy() for j in path[::-1]],dist[end]*.5

    def have(self,s,k):
        o=self.objectives[k]
        return any(s.get(o,f)>0.5 for f in ('received_image','have_image_rover0','have_image_rover1'))

    def needed(self,s):
        return [not any(s.get(o,'is_soil')==soil and any(s.get(o,f)>.5 for f in ('received_analysis','analyzed_rover0','analyzed_rover1')) for o in self.samples) for soil in (0,1)]

    def pending(self,s,r):
        return any(s.get(o,'have_image_rover%d'%r)>.5 and s.get(o,'received_image')<.5 for o in self.objectives) or any(s.get(o,'analyzed_rover%d'%r)>.5 and s.get(o,'received_analysis')<.5 for o in self.samples)

    def completed(self,s,r,task):
        kind,k=task
        if kind=='image':return self.have(s,k)
        if kind=='sample':return not self.needed(s)[int(s.get(self.samples[k],'is_soil'))]
        if kind=='send':return not self.pending(s,r)
        return s.get(self.rovers[r],'at_home')>.5

    def choose(self,s,r,p,other):
        candidates=[]
        reserved=self.tasks[1-r]
        need=self.needed(s)
        for k,o in enumerate(self.objectives):
            if not self.have(s,k) and reserved!=('image',k):candidates.append(('image',k))
        if True:
            for k,o in enumerate(self.samples):
                soil=int(s.get(o,'is_soil'))
                if need[soil] and not (reserved and reserved[0]=='sample' and int(s.get(self.samples[reserved[1]],'is_soil'))==soil):candidates.append(('sample',k))
        if self.schedule is not None:
            schedule=self.schedule[r]
            while schedule:
                kind,k=schedule[0]
                if (kind=='image' and self.have(s,k)) or (kind=='soil' and not need[k]):schedule.pop(0)
                else:break
            if schedule:
                kind,k=schedule[0]
                planned=[t for t in candidates if t==schedule[0] or (kind=='soil' and t[0]=='sample' and int(s.get(self.samples[t[1]],'is_soil'))==k)]
                if planned:candidates=planned
            else:candidates=[]
        best=None;score=1e9;path=[]
        for task in candidates:
            pp,cost=self.route(p,self.masks[task],other)
            cost+=2 if task[0]=='image' else 0
            if cost<score and cost<1e5:best=task;score=cost;path=pp
        if best is None and candidates and self.schedule is not None:
            self.schedule=None
            self.choose(s,r,p,other)
            return
        if best is None:
            if self.pending(s,r):best=('send',0);path,_=self.route(p,self.masks[best],other)
            else:
                best=('home',r)
                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
                path,_=self.route(p,mask,other)
                if s.get(self.rovers[r],'at_home')>.5:path=[]
        self.tasks[r]=best;self.paths[r]=path

    def result_count(self, s, r):
        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)

    def get_action(self, state):
        s=state; self.tick+=1
        action=np.zeros(8,dtype=np.float32)
        pos=[self.xy(s,r) for r in self.rovers]
        for r in range(2):
            p=pos[r];rob=self.rovers[r]
            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
                self.fail[r]+=1
            else:self.fail[r]=0
            task=self.tasks[r]
            last=self.last_op[r]
            if last is not None:
                old_task, old_p, old_op, old_count = last
                failed = ((old_op == -.5 and s.get(rob,'calibrated')<.5) or
                          (old_op == -1/6 and self.result_count(s,r)<=old_count) or
                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
                if failed and task==old_task and task[0] in ('image','send'):
                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.22
                    self.paths[r],_=self.route(p,self.masks[task],pos[1-r])
            if task is None or self.completed(s,r,task):
                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
            if self.fail[r]>=2:
                self.paths[r]=[]
                # Infer blocked configuration and route around it.
                blocked=p+self.previous[r][1]
                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
                if task[0]=='home':mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
                else:mask=self.masks[task]
                self.paths[r],_=self.route(p,mask,pos[1-r])
                if task[0]!='home' and not self.paths[r]:
                    self.tasks[r]=None
                    self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
                self.fail[r]=0
            path=self.paths[r]
            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
            dest=p.copy()
            selected=-1
            for pi,point in enumerate(path[:5]):
                d=point-p
                if np.max(np.abs(d))>.20001:break
                probes=p+np.linspace(0,1,5)[:,None]*d
                if np.all(self.valid(probes)) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
                else:break
            if selected>0:del path[:selected]
            d=np.clip(dest-p,-.2,.2)
            q=p+d
            op=0.
            kind,k=task
            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
            elif kind=='image' and self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]:
                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
            elif kind=='send' and self.visible(q[None,:],self.lander,3.85)[0]:
                op=.5
                if path and np.linalg.norm(q-path[-1])>.06:op=0.
            if op==0 and s.get(rob,'store_full')>.5:op=5/6
            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
            action[r*4:r*4+2]=d;action[r*4+3]=op
            self.previous[r]=(p.copy(),d.copy())
            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r))
        return action
