import numpy as np
from kin import fk, ik, down_R
class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives): pass
    def reset(self, state, info):
        R = state.get_object_from_name('robot'); B = state.get_object_from_name('target_block')
        self.R=R
        base=(state.get(R,'pos_base_x'), state.get(R,'pos_base_y'), state.get(R,'pos_base_rot'))
        q=np.array([state.get(R,f'joint_{i}') for i in range(1,8)])
        p=np.array([state.get(B,'pose_x'),state.get(B,'pose_y'),0.24])
        self.qt,_=ik(q,p,down_R(0),base)
    def get_action(self, state):
        q=np.array([state.get(self.R,f'joint_{i}') for i in range(1,8)])
        d=(self.qt-q+np.pi)%(2*np.pi)-np.pi
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); return a
