# expect: planning
# One-step look-ahead: predicts obs + a for each action and returns the best one.
def get_action(self, obs):
    actions = [-1, 1]
    future = [obs + a for a in actions]
    scores = [abs(self.goal - s) for s in future]
    return actions[scores.index(min(scores))]