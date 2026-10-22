# expect: planning
# Predicts 5 steps ahead for each action and picks the best predicted outcome.
class Policy:
    def model(self, s, a):
        return s + a

    def get_action(self, obs):
        scores = {}
        for a in (-1, 0, 1):
            s = obs
            for _ in range(5):
                s = self.model(s, a)
            scores[a] = abs(s)
        return min(scores, key=scores.get)
