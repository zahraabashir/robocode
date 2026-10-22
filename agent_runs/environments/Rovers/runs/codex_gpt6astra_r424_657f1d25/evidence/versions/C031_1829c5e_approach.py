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
        self.pillars = []
        for o in self.objects(state, 'obstacle'):
            p = self.xy(state, o)
            h = np.array([state.get(o, 'half_x'), state.get(o, 'half_y')])
            if state.get(o, 'half_z') > .1:
                self.occluders.append((p-h, p+h))
                self.pillars.append(p)
            else:
                self.rects.append((p-h, p+h))
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
        self.masks[('send',1)] = self.masks[('send',0)].copy()
        self.good_radio = [[],[]]
        self.tasks = [None,None]
        self.paths = [[],[]]
        self.previous = [None,None]
        self.fail = [0,0]
        self.tick = 0
        self.last_op = [None, None]
        self.schedule = assign_tasks(self,state)
        self.loose_views = set()
        self.rejected_views = {}
        self.still = [0,0]
        self.signatures = [None,None]

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
        for center in self.pillars:
            delta=np.abs(pts-center)
            good &= ~((delta[...,0]<.265)&(delta[...,1]<.25)&(np.sum(delta,axis=-1)<.405))
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
            if self.pending(s,r) and s.get(self.rovers[r],'at_home')>.5:
                best=('send',r)
                mask=self.masks[best]
                if self.good_radio[r]:
                    known=np.zeros(len(self.points),dtype=bool)
                    for point in self.good_radio[r]:known |= np.linalg.norm(self.points-point,axis=1)<.075
                    pp,cost=self.route(p,known & self.free,other)
                    if cost<1e5:mask=known & self.free
                self.masks[best]=mask
                path,_=self.route(p,mask,other)
            else:
                best=('home',r)
                mask=np.linalg.norm(self.points-self.home[r],axis=1)<.24
                path,_=self.route(p,mask,other)
                if s.get(self.rovers[r],'at_home')>.5:path=[]
        self.tasks[r]=best;self.paths[r]=path

    def radio_evidence(self,s,r):
        evidence=[]
        for objects,own,received in ((self.objectives,'have_image_rover','received_image'),(self.samples,'analyzed_rover','received_analysis')):
            for o in objects:
                if s.get(o,own+str(r))>.5 and s.get(o,own+str(1-r))<.5 and s.get(o,received)<.5:
                    evidence.append((o,received))
        return evidence

    def result_count(self, s, r):
        return sum(s.get(o, 'have_image_rover%d'%r) for o in self.objectives) + sum(s.get(o, 'analyzed_rover%d'%r) for o in self.samples)

    def replan(self,s,r,p,other,explore=False):
        task=self.tasks[r]
        kind,k=task
        mask=(np.linalg.norm(self.points-self.home[r],axis=1)<.24) if kind=='home' else self.masks[task]
        path,_=self.route(p,mask,other)
        if kind in ('image','send') and (explore or not path):
            # If the conservative sight model runs out of positions, use
            # direct operator feedback to explore nearby untested viewpoints.
            target=self.xy(s,self.objectives[k]) if kind=='image' else self.lander
            radius=1.9 if kind=='image' else 3.8
            mask=self.free & (np.linalg.norm(self.points-target,axis=1)<radius)
            for failed in self.rejected_views.get(task,[]):
                mask &= np.linalg.norm(self.points-failed,axis=1)>.085
            self.masks[task]=mask
            self.loose_views.add(task)
            path,_=self.route(p,mask,other)
        self.paths[r]=path
        if not path and kind!='home':
            self.schedule=None
            self.tasks[r]=None
            self.choose(s,r,p,other)

    def get_action(self, state):
        s=state; self.tick+=1
        action=np.zeros(8,dtype=np.float32)
        pos=[self.xy(s,r) for r in self.rovers]
        for r in range(2):
            p=pos[r];rob=self.rovers[r]
            signature=(tuple(p),s.get(rob,'store_full'),s.get(rob,'calibrated'),self.result_count(s,r))
            self.still[r]=self.still[r]+1 if signature==self.signatures[r] else 0
            self.signatures[r]=signature
            if self.previous[r] is not None and np.linalg.norm(p-self.previous[r][0])<1e-5 and np.linalg.norm(self.previous[r][1])>.01:
                self.fail[r]+=1
            else:self.fail[r]=0
            task=self.tasks[r]
            last=self.last_op[r]
            if last is not None:
                old_task, old_p, old_op, old_count, old_evidence = last
                if old_op==.5 and any(s.get(obj,feature)>.5 for obj,feature in old_evidence):
                    if all(np.linalg.norm(p-v)>.1 for v in self.good_radio[r]):self.good_radio[r].append(p.copy())
                failed = ((old_task[0]=='image' and old_op == -.5 and s.get(rob,'calibrated')<.5) or
                          (old_task[0]=='image' and old_op == -1/6 and self.result_count(s,r)<=old_count) or
                          (old_op == .5 and old_task[0]=='send' and self.pending(s,r)))
                if failed and task==old_task and task[0] in ('image','send'):
                    self.rejected_views.setdefault(task,[]).append(p.copy())
                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>(.085 if task in self.loose_views else .22)
                    self.replan(s,r,p,pos[1-r])
                    task=self.tasks[r]
            if task is None or self.completed(s,r,task):
                self.choose(s,r,p,pos[1-r]);task=self.tasks[r]
            if self.fail[r]>=2:
                self.paths[r]=[]
                # Infer blocked configuration and route around it.
                blocked=p+self.previous[r][1]
                self.free[np.linalg.norm(self.points-blocked,axis=1)<.12]=False
                self.replan(s,r,p,pos[1-r]);task=self.tasks[r]
                self.fail[r]=0
            if self.still[r]>=6 and not self.completed(s,r,task):
                if task[0]=='sample':
                    self.masks[task] &= np.linalg.norm(self.points-p,axis=1)>.12
                self.replan(s,r,p,pos[1-r],explore=True);task=self.tasks[r]
                self.still[r]=0
            path=self.paths[r]
            while path and np.max(np.abs(path[0]-p))<.025:path.pop(0)
            dest=p.copy()
            selected=-1
            for pi,point in enumerate(path[:5]):
                d=point-p
                if np.max(np.abs(d))>.20001:
                    if pi:break
                    point=p+np.clip(d,-.2,.2)
                    d=point-p
                probes=p+np.linspace(0,1,5)[:,None]*d
                if (np.all(self.valid(probes)) or (not self.valid(p[None,:])[0] and self.valid(point[None,:])[0])) and np.linalg.norm(point-pos[1-r])>.4:dest=point.copy();selected=pi
                else:break
            if selected>0:del path[:selected]
            d=np.clip(dest-p,-.2,.2)
            q=p+d
            op=0.
            kind,k=task
            if kind=='sample' and s.get(rob,'store_full')<.5 and self.sample_safe(s,q[None,:],k)[0]:op=-5/6
            elif kind=='image' and ((task in self.loose_views and np.linalg.norm(q-self.xy(s,self.objectives[k]))<1.99) or self.visible(q[None,:],self.xy(s,self.objectives[k]),1.99)[0]):
                op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
                if path and np.linalg.norm(q-path[-1])>.06 and last is not None and last[0]==task and last[2] in (-.5,-1/6):op=0.
            elif kind=='send' and ((task in self.loose_views and np.linalg.norm(q-self.lander)<3.85) or self.visible(q[None,:],self.lander,3.85)[0]):
                op=.5
                if path and np.linalg.norm(q-path[-1])>.06:op=0.
            if op==0 and s.get(rob,'store_full')>.5:op=5/6
            elif op==0 and self.pending(s,r) and self.visible(q[None,:],self.lander,3.85)[0]:op=.5
            # Use otherwise idle travel steps for camera work.
            if op in (0.,.5) and np.linalg.norm(d)>.01:
                visible=[]
                for j,o in enumerate(self.objectives):
                    if s.get(o,'have_image_rover%d'%r)<.5 and self.visible(q[None,:],self.xy(s,o),1.97)[0]:
                        visible.append((float(np.linalg.norm(q-self.xy(s,o))),j))
                if visible:
                    _,j=min(visible)
                    if not self.have(s,j):op=-1/6 if s.get(rob,'calibrated')>.5 else -.5
            action[r*4:r*4+2]=d;action[r*4+3]=op
            self.previous[r]=(p.copy(),d.copy())
            self.last_op[r]=(task,q.copy(),op,self.result_count(s,r),self.radio_evidence(s,r) if op==.5 else [])
        return action
