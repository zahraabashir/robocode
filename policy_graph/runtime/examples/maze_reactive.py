"""A minimal reactive policy for the small_maze CLI example; ignores obstacles."""

# The constructor/reset signatures follow RoboCode's GeneratedApproach contract.
# pylint: disable=unused-argument


class GeneratedApproach:
    """Move toward the goal using the current observation only."""

    def __init__(self, action_space, observation_space, primitives):
        pass

    def reset(self, state, info):
        """This policy has no persistent state to reset."""

    def get_action(self, state):
        """Choose a direction without predicting successor states."""
        row, column = state.agent
        goal_row, goal_column = state.goal
        if column < goal_column:
            return 3
        if column > goal_column:
            return 2
        if row < goal_row:
            return 1
        return 0
