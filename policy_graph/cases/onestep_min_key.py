# expect: planning
# One-step look-ahead: each action is scored by the state it leads to; the best is returned.
class Policy:
    def get_action(self, obs):
        return min([-1, 1], key=lambda a: abs(self.goal - (obs + a)))
