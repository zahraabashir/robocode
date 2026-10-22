import numpy as np
class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
    def reset(self, state, info):
        pass
    def get_action(self, state):
        return np.array([0,0,0,0,0], dtype=np.float32)
