import numpy as np
from kin import ik, Q0

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space=action_space
        self.observation_space=observation_space
    def reset(self,state,info):
        self.t=0
        self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
        self.block=state.get_object_from_name('target_block')
    def get_action(self,state):
        self.t+=1;r=self.robot
        x=state.get(self.block,'pose_x');y=state.get(self.block,'pose_y')
        z=max(.112,.25-max(0,self.t-10)*.002)
        q=ik(x-state.get(r,'pos_base_x'),z)
        a=np.zeros(11,dtype=np.float32)
        a[1]=y-.001-state.get(r,'pos_base_y')
        a[3:10]=q-np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
        a[10]=-1 if self.t>=10 else 0
        return np.clip(a,self.action_space.low,self.action_space.high)
