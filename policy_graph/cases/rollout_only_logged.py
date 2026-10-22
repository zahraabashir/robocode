# expect: reactive
# The same rollout, but its result is only logged; the action is a rule.
class Policy:
    def reset(self, obs):
        self.log = []

    def model(self, s, a):
        return s + a

    def get_action(self, obs):
        for a in (-1, 0, 1):
            s = obs
            for _ in range(5):
                s = self.model(s, a)
            self.log.append(s)
        return -1 if obs > 0 else 1
