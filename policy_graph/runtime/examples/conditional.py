"""Only the positive-input call performs one-step lookahead."""


def get_action(obs):
    if obs > 0:
        return min([-1, 1], key=lambda a: abs(obs + a))
    return 0
