# expect: planning
# One-step look-ahead written as a best-so-far loop over actions.
class Policy:
    def get_action(self, obs):
        best, choice = 1e9, None
        for a in (-1, 1):
            c = abs(self.goal - (obs + a))
            if c < best:
                best, choice = c, a
        return choice
