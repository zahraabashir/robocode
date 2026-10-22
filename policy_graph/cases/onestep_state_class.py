# expect: planning
# One-step look-ahead with the predicted state as an object.
class State:
    def __init__(self, x):
        self.x = x

    def moved(self, a):
        return State(self.x + a)


class Policy:
    def get_action(self, obs):
        actions = [-1, 1]
        future = [State(obs).moved(a) for a in actions]
        scores = [abs(self.goal - s.x) for s in future]
        return actions[scores.index(min(scores))]
