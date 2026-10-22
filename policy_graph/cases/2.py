def get_action(self, obs):
    scores = []
    for a in [-1, 1]:
        score = 0
        for k in range(3):
            score += abs(obs - a) / (k + 1)
        scores.append(score)
    return [-1, 1][scores.index(min(scores))]