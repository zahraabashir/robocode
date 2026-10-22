"""Feedback manipulation policy for Obstruction3D."""
import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives): self.action_space=action_space
    @staticmethod
    def _v(s,n,f): return s.get(s.get_object_from_name(n),f)
    def _xyz(self,s,n): return np.array([self._v(s,n,"pose_"+c) for c in "xyz"])
    def reset(self,state,info):
        self.region=self._xyz(state,"target_region"); self.object_name="target_block"
        self.mode="pick"; self.pick_i=self.pick_t=0; self.controls=[1,4,6,8]
        self.J=np.zeros((3,4)); self.cal_i=0; self.cal_sign=1; self.last_pos=None
        self.last_delta=0.; self.move_count=0; self.waypoint=0
        x=self._v(state,self.object_name,"pose_x")
        if x<.23: base=(.18,-2.50,-.75)
        else: base=(.35+2*(x-.336),-2.20+1.5*(x-.336),-.60+.8*(x-.336))
        self.pick_poses=[base,(base[0]-.08,base[1],base[2]),(base[0]+.08,base[1],base[2]),
                         (base[0],base[1]-.10,base[2]-.10),(base[0],base[1]+.10,base[2]+.10)]
    def _held(self,s): return self._v(s,"robot","grasp_active")>.5
    def _start_calibration(self,s):
        self.mode="calibrate"; self.cal_i=0; self.cal_sign=1
        self.last_pos=self._xyz(s,self.object_name); self.last_delta=0.
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
        pos=self._xyz(state,self.object_name)
        if self.mode=="calibrate" and self.last_delta:
            col=(pos-self.last_pos)/self.last_delta
            if self.cal_sign<0:
                self.J[:,self.cal_i]=.5*(self.J[:,self.cal_i]+col); self.cal_i+=1; self.cal_sign=1
            else: self.J[:,self.cal_i]=col; self.cal_sign=-1
            self.last_delta=0.
        if self.mode=="calibrate":
            if self.cal_i>=len(self.controls): self.mode="move"; self.move_count=0
            else:
                d=.04*self.cal_sign; a[self.controls[self.cal_i]]=d; a[10]=-1.
                self.last_pos=pos; self.last_delta=d; return a
        goals=[np.array([pos[0],pos[1],.24]),np.array([self.region[0],self.region[1],.24]),
               np.array([self.region[0],self.region[1],.115])]
        goal=goals[self.waypoint]; err=goal-pos; tol=.012 if self.waypoint<2 else .004
        if np.linalg.norm(err)<tol:
            self.waypoint+=1
            if self.waypoint>=3: self.mode="release"
            else: self._start_calibration(state)
            a[10]=-1.; return a
        if self.mode=="release": a[10]=1.; return a
        JJ=self.J@self.J.T+1e-5*np.eye(3)
        u=self.J.T@np.linalg.solve(JJ,np.clip(err,-.06,.06)); u=np.clip(u,-.12,.12)
        for k,idx in enumerate(self.controls): a[idx]=u[k]
        a[10]=-1.; self.move_count+=1
        if self.move_count>=7: self._start_calibration(state)
        return a
