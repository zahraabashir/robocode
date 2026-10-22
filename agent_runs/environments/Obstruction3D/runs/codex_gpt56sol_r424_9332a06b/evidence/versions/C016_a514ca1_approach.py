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
        x=self._v(state,self.object_name,"pose_x")
        if x<.23: base=(.18,-2.50,-.75)
        else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
        self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10)]
        rx=self.region[0]
        if rx<.23: self.lower_pose=(.18,-2.50,-.75)
        else: self.lower_pose=(.35+2*(rx-.336),-2.20+1.5*(rx-.336),-.60+.8*(rx-.336))
        # With an object in the fingers the nominal pickup pose leaves its bottom
        # about 2 cm high; this coupled correction lowers without shifting x.
        self.lower_pose=(self.lower_pose[0]+.10,self.lower_pose[1]-.027,
                         self.lower_pose[2]+.10)
        self.lower_t=0
        self.release_t=0
    def _held(self,s): return self._v(s,"robot","grasp_active")>.5
    def _feat(self,s):
        o=self.object_name
        return np.r_[self._xyz(s,o), .18*np.array([self._v(s,o,"pose_q"+c) for c in "xyz"])]
    def _start_calibration(self,s):
        self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
        self.last_pos=self._feat(s); self.last_delta=0.
    def get_action(self,state):
        a=np.zeros(self.action_space.shape,dtype=self.action_space.dtype)
        if self._held(state) and self.mode=="pick": self._start_calibration(state)
        if self.mode=="pick":
            x,y,z=self._xyz(state,self.object_name); q2,q4,q6=self.pick_poses[self.pick_i]
            target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2]); rob=state.get_object_from_name("robot")
            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
            a[1]=np.clip(y-.00135-self._v(state,"robot","pos_base_y"),-.2,.2)
            a[3:10]=np.clip(target-cur,-.2,.2); a[10]=1. if self.pick_t<7 else -1.
            self.pick_t+=1
            if self.pick_t>=12:
                self.pick_t=0; self.pick_i=(self.pick_i+1)%len(self.pick_poses); a[10]=1.
            return a
        pos=self._xyz(state,self.object_name); feat=self._feat(state)
        if self.mode=="lower":
            q2,q4,q6=self.lower_pose; target=np.array([0.,q2,-np.pi,q4,0.,q6,np.pi/2])
            rob=state.get_object_from_name("robot")
            cur=np.array([state.get(rob,"joint_%d"%j) for j in range(1,8)])
            a[1]=np.clip(self.region[1]-.00135-self._v(state,"robot","pos_base_y"),-.12,.12)
            a[3:10]=np.clip(target-cur,-.10,.10); a[10]=-1.; self.lower_t+=1
            if self.lower_t>=15: self.mode="release"; self.release_t=0
            return a
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
            a[10]=1.; self.release_t+=1; return a
        goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
               np.array([self.region[0],self.region[1],.115])]
        goal=goals[self.waypoint]; poserr=goal-pos
        err=np.r_[poserr, -feat[3:]]
        tol=.012 if self.waypoint<2 else .004
        if np.linalg.norm(poserr)<tol and np.linalg.norm(feat[3:])<.025:
            self.waypoint+=1
            # Dropping from the clear waypoint avoids wedging the fingers against
            # the tabletop; gravity preserves the accurately controlled x/y.
            if self.waypoint>=3: self.mode="release"; self.release_t=0
            else: self._start_calibration(state)
            a[10]=-1.; return a
        u=np.linalg.solve(self.J.T@self.J+1e-5*np.eye(5),self.J.T@np.clip(err,-.06,.06))
        u=np.clip(u,-.10,.10)
        a += self.B@u
        a[10]=-1.; self.move_count+=1
        if self.move_count>=7: self._start_calibration(state)
        return a
