# expect: reactive
# A rule on the current observation and a goal remembered from reset.
class Policy:
    def reset(self, obs):
        self.goal = obs + 10

    def get_action(self, obs):
        d = self.goal - obs
        if d > 0:
            a = 1
        else:
            a = -1
        return self.clip(a)

    def clip(self, x):
        return max(-1, min(1, x))
