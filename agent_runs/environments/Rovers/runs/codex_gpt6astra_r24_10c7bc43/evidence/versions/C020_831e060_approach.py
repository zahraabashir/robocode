import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.space = observation_space
    def objects(self, s, t):
        return s.get_objects(self.space.get_type(t))
    def xy(self,s,o):
        return np.array([s.get(o,'x'),s.get(o,'y')])
    def reset(self,state,info):
        self.rovers=[state.get_object_from_name('rover'+str(i)) for i in range(2)]
        self.homes=[self.xy(state,r) for r in self.rovers]
        self.objs=self.objects(state,'objective'); self.samples=self.objects(state,'sample')
        self.lander=self.xy(state,self.objects(state,'lander')[0])
        self.boxes=np.array([[state.get(o,k) for k in ['x','y','half_x','half_y']] for o in self.objects(state,'obstacle')]+[[0,0,0.05,2.5]])
        self.axis=np.arange(-2.3,2.301,0.1)
        self.n=len(self.axis)
        self.points=np.array([(x,y) for x in self.axis for y in self.axis])
        self.valid=self.free(self.points)
        self.bad=np.zeros((2,len(self.points),len(self.objs)),dtype=bool)
        self.send_bad=np.zeros((2,len(self.points)),dtype=bool)
        self.prev=None; self.step=0
        self.make_graph()
        self.image_masks=[self.visible(self.points,self.xy(state,o),2) for o in self.objs]
        self.sample_masks=[np.linalg.norm(self.points-self.xy(state,o),axis=1)<.245 for o in self.samples]
        self.radio_mask=self.visible(self.points,self.lander,4)
        self.home_dist=[dijkstra(self.graph,indices=self.nearest(h)) for h in self.homes]
    def free(self,p):
        p=np.atleast_2d(p)
        d=np.abs(p[:,None,:]-self.boxes[None,:,:2])-self.boxes[None,:,2:]
        ok=np.all(np.sum(np.maximum(d,0)**2,axis=2) > 0.228**2,axis=1)
        ok &= np.linalg.norm(p-self.lander,axis=1)>.55
        ok &= np.max(np.abs(p),axis=1)<2.271
        return ok
    def make_graph(self):
        rows=[]; cols=[]
        for i in np.flatnonzero(self.valid):
            x,y=divmod(i,self.n)
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                xx,yy=x+dx,y+dy
                if 0<=xx<self.n and 0<=yy<self.n:
                    j=xx*self.n+yy
                    if self.valid[j]: rows.append(i);cols.append(j)
        self.graph=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(self.points),len(self.points)))
    def visible(self,p,target,limit):
        p=np.atleast_2d(p); target=np.asarray(target)
        ok=np.linalg.norm(p-target,axis=1)<limit-.025
        # Low mounds do not occlude the camera, but pillars and wall do.
        boxes=self.boxes[:-1][(self.boxes[:-1,2]<.2)]
        delta=target-p
        for b in boxes:
            lo=b[:2]-b[2:];hi=b[:2]+b[2:]
            with np.errstate(divide='ignore',invalid='ignore'):
                t1=(lo-p)/delta;t2=(hi-p)/delta
            near=np.maximum(np.min(np.stack([t1,t2]),axis=0).max(axis=1),.001)
            far=np.minimum(np.max(np.stack([t1,t2]),axis=0).min(axis=1),.999)
            ok &= near>far
        return ok
    def nearest(self,p):
        ds=np.sum((self.points-p)**2,axis=1);ds[~self.valid]=np.inf
        return int(np.argmin(ds))
    def pending_count(self,s,i):
        return sum(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs)+sum(s.get(o,'analyzed_rover'+str(i)) and not s.get(o,'received_analysis') for o in self.samples)
    def get_action(self,s):
        self.step+=1
        pos=[self.xy(s,r) for r in self.rovers]
        if self.prev is not None:
            for i in range(2):
                old,move,op,idx,had=self.prev[i]
                if np.linalg.norm(move)>.02 and np.linalg.norm(pos[i]-old)<.001:
                    q=old+move
                    ids=np.linalg.norm(self.points-q,axis=1)<.085
                    self.valid[ids]=False
                    self.make_graph()
                if op==.5 and self.pending_count(s,i)>=had:
                    self.send_bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.23]=True
                if op in [-.5,-1/6] and idx is not None:
                    if (op==-.5 and not s.get(self.rovers[i],'calibrated')) or (op==-1/6 and not s.get(self.objs[idx],'have_image_rover'+str(i))):
                        self.bad[i,np.linalg.norm(self.points-pos[i],axis=1)<.16,idx]=True
        action=np.zeros(8,np.float32); records=[]; assigned=set(); kinds=set()
        received=[any(s.get(o,'is_soil')==k and s.get(o,'received_analysis') for o in self.samples) for k in [0,1]]
        acquired=[any(s.get(o,'is_soil')==k and (s.get(o,'analyzed_rover0') or s.get(o,'analyzed_rover1')) for o in self.samples) for k in [0,1]]
        for i,r in enumerate(self.rovers):
            p=pos[i]; start=self.nearest(p)
            dist,pred=dijkstra(self.graph,indices=start,return_predecessors=True)
            candidates=[]
            for k in [0,1]:
                if not acquired[k] and k not in kinds and not s.get(r,'store_full'):
                    for oi,o in enumerate(self.samples):
                        if int(s.get(o,'is_soil'))==k:
                            mask=self.sample_masks[oi]
                            candidates.append((mask,'sample',o,k))
            for j,o in enumerate(self.objs):
                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]) and j not in assigned:
                    mask=self.image_masks[j]&~self.bad[i,:,j]
                    candidates.append((mask,'image',o,j))
            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
            if pending: candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
            best=None; score=np.inf
            for mask,task,o,j in candidates:
                dd=dist+.001*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
                target=int(np.argmin(dd)); cost=dd[target]
                if task=='send': cost+=5 if any(c[1]!='send' for c in candidates) else 0
                if cost<score: score=cost;best=(target,task,o,j)
            if best is None: best=(self.nearest(self.homes[i]),'home',None,None)
            target,task,o,j=best
            if task=='sample': kinds.add(j)
            if task=='image': assigned.add(j)
            targetpos=self.points[target]
            if task=='home': targetpos=self.homes[i]
            path=[target];cur=target
            for _ in range(len(self.points)):
                if cur==start:break
                cur=int(pred[cur])
                if cur<0:break
                path.append(cur)
            path=path[::-1]
            goal=targetpos
            for node in path:
                q=self.points[node]
                if np.max(np.abs(q-p))<=.20001: goal=q
                else: break
            if np.max(np.abs(targetpos-p))<=.2:goal=targetpos
            move=np.clip(goal-p,-.2,.2)
            if np.linalg.norm(p+move-pos[1-i])<.43:move=np.zeros(2)
            q=p+move; op=0.;idx=None
            if task=='sample' and np.linalg.norm(q-self.xy(s,o))<.249:op=-5/6
            else:
                useful=[jj for jj,oo in enumerate(self.objs) if not s.get(oo,'received_image') and not any(s.get(oo,'have_image_rover'+str(a)) for a in [0,1]) and self.visible(q,self.xy(s,oo),2)[0]]
                if useful:
                    idx=min(useful,key=lambda jj:np.linalg.norm(q-self.xy(s,self.objs[jj])))
                    op=-1/6 if s.get(r,'calibrated') else -.5
            if op==0 and pending and self.visible(q,self.lander,4)[0] and not self.send_bad[i,self.nearest(q)]:op=.5
            elif op==0 and s.get(r,'store_full'):op=5/6
            action[4*i:4*i+2]=move;action[4*i+3]=op
            records.append((p,move,op,idx,self.pending_count(s,i)))
        self.prev=records
        return action
