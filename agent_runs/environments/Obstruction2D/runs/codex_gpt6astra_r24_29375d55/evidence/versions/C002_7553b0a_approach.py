import math
import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.types = {t.name: t for t in observation_space.types}
    def reset(self, state, info):
        self.phase = 0
        self.obj = None
    def get_action(self, state):
        r = next(iter(state.get_objects(self.types['crv_robot'])))
        b = next(iter(state.get_objects(self.types['target_block'])))
        x, y = state.get(r,'x'), state.get(r,'y')
        tx = state.get(b,'x') + state.get(b,'width') / 2
        ty = state.get(b,'y') + state.get(b,'height') + .3
        return np.array([np.clip(tx-x,-.05,.05),np.clip(ty-y,-.05,.05),0,0,1],dtype=np.float32)
