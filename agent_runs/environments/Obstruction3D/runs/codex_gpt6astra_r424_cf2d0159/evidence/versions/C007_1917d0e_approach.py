import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation

_ORIGINS = [([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
_ORIGINS = [(np.array(p),Rotation.from_euler('x',a).as_matrix()) for p,a in _ORIGINS]
def fk(q):
    p=np.zeros(3); r=np.eye(3)
    for a,(v,rot) in zip(q,_ORIGINS):
        p+=r@v
        c,s=np.cos(a),np.sin(a)
        r=r@rot@np.array([[c,-s,0],[s,c,0],[0,0,1.]])
    p+=r@np.array([0,0,-.061525])
    r=r@np.diag([1.,-1.,-1.])
    return p+r@np.array([0,0,.12]),r

def ik(x,z):
    def residual(a):
        q=np.array([0,a[0],-np.pi,a[1],0,a[2],np.pi/2])
        p,r=fk(q)
        return [p[0]-x,p[2]-z,r[0,2]]
    sol=least_squares(residual,[-.1,-1.7,-1.3],max_nfev=80)
    return np.array([0,sol.x[0],-np.pi,sol.x[1],0,sol.x[2],np.pi/2])

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space=action_space
        self.observation_space=observation_space
        self.robot_type=observation_space.get_type('Kinematic3DRobot')
        self.cube_type=observation_space.get_type('Kinematic3DCuboid')
    def reset(self,state,info):
        self.phase=0
        self.steps=0
        self.qhigh=ik(.45,.30)
        self.qlow=ik(.45,.1)
    def get_action(self,state):
        self.steps+=1
        robot=next(iter(state.get_objects(self.robot_type)))
        q=np.array([state.get(robot,'joint_'+str(i)) for i in range(1,8)])
        b=np.array([state.get(robot,'pos_base_x'),state.get(robot,'pos_base_y')])
        cubes=list(state.get_objects(self.cube_type))
        target=next(o for o in cubes if o.name=='target_block')
        region=next(o for o in cubes if o.name=='target_region')
        tp=np.array([state.get(target,'pose_'+a) for a in 'xyz'])
        rp=np.array([state.get(region,'pose_'+a) for a in 'xyz'])
        action=np.zeros(11)
        if self.phase==0:
            action[3:10]=self.qhigh-q
            if np.max(abs(action[3:10]))<.001:self.phase=1
        elif self.phase==1:
            action[:2]=tp[:2]-[.45,.001]-b
            if np.max(abs(action[:2]))<.001:self.phase=2
        elif self.phase==2:
            action[3:10]=self.qlow-q
            if np.max(abs(action[3:10]))<.001:self.phase=3
        elif self.phase==3:
            action[10]=-1
            self.phase=4
        elif self.phase==4:
            action[3:10]=self.qhigh-q
            if np.max(abs(action[3:10]))<.001:self.phase=5
        elif self.phase==5:
            action[:2]=rp[:2]-[.45,.001]-b
            if np.max(abs(action[:2]))<.001:self.phase=6
        elif self.phase==6:
            action[3:10]=ik(.45,.11)-q
            if np.max(abs(action[3:10]))<.001:self.phase=7
        else:action[10]=1
        return np.clip(action,self.action_space.low,self.action_space.high).astype(np.float32)
