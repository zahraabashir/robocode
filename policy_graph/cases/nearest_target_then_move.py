# expect: reactive
# Greedy: choose the nearest target, then compute the action from it with a rule.
import numpy as np


class Policy:
    def get_action(self, obs):
        t = min(obs["targets"], key=lambda t: abs(t - obs["pos"]))
        return np.sign(t - obs["pos"])
