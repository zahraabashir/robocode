"""Two three-step predictions in reset; three actions consume the cached plan."""


class GeneratedApproach:
    def __init__(self, action_space=None, observation_space=None, primitives=None):
        self.plan = []

    def reset(self, state, info):
        def score(plan):
            predicted = state
            for action in plan:
                predicted += action
            return abs(predicted)

        self.plan = list(min([[-1, -1, -1], [1, 1, 1]], key=score))

    def get_action(self, state):
        return self.plan.pop(0)
