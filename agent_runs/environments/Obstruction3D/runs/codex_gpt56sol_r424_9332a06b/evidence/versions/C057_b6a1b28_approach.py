"""Feedback manipulation policy for Obstruction3D."""
import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives): self.action_space=action_space
    @staticmethod
    def _v(s,n,f): return s.get(s.get_object_from_name(n),f)
    def _xyz(self,s,n): return np.array([self._v(s,n,"pose_"+c) for c in "xyz"])
    def reset(self,state,info):
        self.region=self._xyz(state,"target_region"); self.object_name="target_block"
        self.mode="pick"; self.pick_i=self.pick_t=0
        self.B=np.zeros((11,5)); self.B[0,0]=1.; self.B[1,1]=1.; self.B[4,2]=1.
        self.B[6,3]=1.; self.B[8,4]=1.
        self.J=np.zeros((6,5)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
        self.last_delta=0.; self.move_count=0; self.waypoint=0
        rx,ry,_=self.region; rhx=self._v(state,"target_region","half_extent_x"); rhy=self._v(state,"target_region","half_extent_y")
        self.region_hx,self.region_hy=rhx,rhy
        blockers=[]
        for n in state.get_object_names():
            if not n.startswith("obstruction"): continue
            x,y,_=self._xyz(state,n); hx=self._v(state,n,"half_extent_x"); hy=self._v(state,n,"half_extent_y")
            if abs(x-rx)<hx+rhx and abs(y-ry)<hy+rhy: blockers.append(n)
        blockers.sort(key=lambda n:self._v(state,n,"pose_z")+self._v(state,n,"half_extent_z"),reverse=True)
        self.tasks=blockers+["target_block"]; self.task_i=0
        self._setup(state,self.tasks[0])

    def _setup(self,state,name):
        self.object_name=name; self.mode="pick"; self.pick_i=self.pick_t=0; self.waypoint=0
        self.approach_t=0
        self.opening_wrong=False
        self.resetting=self.task_i>0
        self.reset_t=0
        self.cal_i=0; self.cal_sign=1; self.last_delta=0.; self.move_count=0; self.release_t=0
        x=self._v(state,name,"pose_x"); self.start_x=x
        pick_bx=-.12
        model_x=x
        if name=="target_block" and self.region[0]>x+.15:
            # Pick with the base retracted and the arm extended.  The stored base
            # travel then supplies forward workspace during transport.
            pick_bx=-.30; model_x=x+.18
        if model_x<.23: base=(.18,-2.50,-.75)
        else: base=(.35+2*(model_x-.336),-2.20+1.5*(model_x-.336),-.60+.8*(model_x-.336))
        triples=[(base[0]-.10,base[1],base[2]),base,(base[0]+.08,base[1],base[2]),
                 (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10),
                 (base[0],base[1],base[2]-.18),(base[0],base[1],base[2]+.18)]
        if model_x<.23:
            for q2 in (.10,.20,.30,.40):
                for q4 in (-2.50,-2.35,-2.20):
                    for q6 in (-.90,-.75,-.60): triples.append((q2,q4,q6))
        self.pick_poses=[]
        for q2,q4,q6 in triples:
            self.pick_poses.append((np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]),.00135,pick_bx))
        if name!="target_block":
            # A second, highly folded grasp family reaches the tiny obstructions.
            q=np.array([-1.6368,2.41,-2.6184,2.66,-1.0464,2.23,-1.8828])
            bx=min(-.12,-.12+x-.219855)
            for d in [0.,-.12,.12]:
                qq=q.copy(); qq[5]+=d; self.pick_poses.append((qq,.196424,bx))
        if name=="target_block": self.dest=self.region[:2].copy(); self.rest_z=.110
        else:
            k=self.task_i; self.dest=np.array([.16+.07*(k%4),-.36 if k%2==0 else .36])
            self.rest_z=.075+self._v(state,name,"half_extent_z")
    def _held(self,s): return self._v(s,self.object_name,"grasp_active")>.5
    def _feat(self,s):
        o=self.object_name
        return np.r_[self._xyz(s,o), .18*np.array([self._v(s,o,"pose_q"+c) for c in "xyz"])]
    def _start_calibration(self,s):
        self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
        self.last_pos=self._feat(s); self.last_delta=0.
    def get_action(self,state):
        a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
        if self.mode=="pick" and self.opening_wrong:
            if self._v(state,"robot","grasp_active")>.5: a[10]=1.; return a
            self.opening_wrong=False
        if self.mode=="pick" and self._v(state,"robot","grasp_active")>.5 and not self._held(state):
            self.opening_wrong=True; a[10]=1.; self.pick_t=0; self.approach_t=0
            self.pick_i=(self.pick_i+1)%len(self.pick_poses); return a
        if self.mode=="reserve":
            a[0]=-.20; a[10]=-1.; self._start_calibration(state); return a
        if self.mode=="pick" and self.resetting:
            safe=np.array([0.,-.35,-np.pi,-2.50,0.,-.87,np.pi/2])
            rob=state.get_object_from_name("robot")
            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
            a[3:10]=np.clip(safe-cur,-.2,.2); a[10]=1.
            self.reset_t+=1
            if np.max(np.abs(safe-cur))<.03 or self.reset_t>=25: self.resetting=False
            return a
        if self.mode=="release" and not self._held(state):
            if self.object_name=="target_block":
                # A callback after release means the drop missed the strict goal;
                # retry from the observed block pose rather than idling forever.
                self._setup(state,"target_block")
            else:
                self.task_i+=1
                if self.task_i<len(self.tasks): self._setup(state,self.tasks[self.task_i])
                else: return a
        if self.mode not in ("pick","release") and not self._held(state):
            # Recover if contact is lost during a transfer.
            self._setup(state,self.object_name)
        if self._held(state) and self.mode=="pick": self._start_calibration(state)
        if self.mode=="pick":
            x,y,z=self._xyz(state,self.object_name); target,yoff,bx=self.pick_poses[self.pick_i]
            rob=state.get_object_from_name("robot")
            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
            a[1]=np.clip(y-yoff-self._v(state,"robot","pos_base_y"),-.2,.2)
            if bx is not None: a[0]=np.clip(bx-self._v(state,"robot","pos_base_x"),-.2,.2)
            a[3:10]=np.clip(target-cur,-.2,.2)
            err=max(np.max(np.abs(target-cur)),abs(y-yoff-self._v(state,"robot","pos_base_y")))
            if bx is not None: err=max(err,abs(bx-self._v(state,"robot","pos_base_x")))
            self.approach_t+=1
            if err<.035 or self.approach_t>=12: a[10]=-1.; self.pick_t+=1
            else: a[10]=1.; self.pick_t=0
            if self.pick_t>=5 or self.approach_t>=18:
                self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
                self.approach_t=0
            return a
        pos=self._xyz(state,self.object_name); feat=self._feat(state)
        if self.mode=="calibrate" and self.last_delta:
            col=(feat-self.last_pos)/self.last_delta
            if self.cal_sign<0:
                self.J[:,self.cal_i]=.5*(self.J[:,self.cal_i]+col); self.cal_i+=1; self.cal_sign=1
            else: self.J[:,self.cal_i]=col; self.cal_sign=-1
            self.last_delta=0.
        if self.mode=="calibrate":
            if self.cal_i>=5: self.mode="move"; self.move_count=0
            else:
                d=.04*self.cal_sign; a += self.B[:,self.cal_i]*d; a[10]=-1.
                self.last_pos=feat; self.last_delta=d; return a
        if self.mode=="release":
            needs_push=(self.object_name!="target_block" or self.release_t>=2)
            if needs_push and self.release_t<60:
                gz=self.rest_z-.005 if self.object_name!="target_block" else self.release_z+.04
                g=np.array([self.release_x,self.dest[1],gz])
                er=np.r_[g-pos,-feat[3:]]
                u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(er,-.03,.03))
                a += self.B@np.clip(u,-.05,.05)
            a[10]=1.; self.release_t+=1; return a
        clearance=.19
        goals=[np.array([pos[0],pos[1],clearance]),np.array([self.dest[0],self.dest[1],clearance]),
               np.array([self.dest[0],self.dest[1],self.rest_z+.005])]
        goal=goals[self.waypoint]; poserr=goal-pos
        err=np.r_[poserr, -feat[3:]]
        if self.waypoint==1:
            # At clearance height, temporarily exploit all redundant arm motion;
            # upright orientation is restored during the final descent.
            err[3:]=0.
        tol=.012 if self.waypoint<2 else .004
        arrived=(np.linalg.norm(poserr)<tol)
        if self.waypoint==2:
            arrived=(np.linalg.norm(poserr[:2])<.004 and pos[2]<self.rest_z+.012)
        if arrived and np.linalg.norm(feat[3:])<.025:
            self.waypoint+=1
            # The last waypoint seats the object before opening the fingers.
            if self.waypoint>=3:
                self.mode="release"; self.release_t=0; self.release_x=pos[0]; self.release_z=pos[2]
            else: self._start_calibration(state)
            a[10]=-1.; return a
        u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
        u=np.clip(u,-.10,.10)
        a += self.B@u
        a[10]=-1.; self.move_count+=1
        if self.move_count>=7: self._start_calibration(state)
        return a
