import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
    def reset(self, state, info):
        self.t = 0
    def get_action(self, state):
        self.t += 1
        return np.zeros(11, dtype=np.float32)
