# expect: planning
# One-step look-ahead with the prediction in a helper method.
class Policy:
    def predict(self, s, a):
        return s + a

    def get_action(self, obs):
        actions = [-1, 1]
        future = [self.predict(obs, a) for a in actions]
        scores = [abs(self.goal - s) for s in future]
        return actions[scores.index(min(scores))]
