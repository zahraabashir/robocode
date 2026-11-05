"""The static baseline keeps this path; an execution never takes it."""


def get_action(obs):
    if obs > 0:
        if obs < 0:
            return min([-1, 1], key=lambda a: abs(obs + a))
    return 0
