"""Command-line choices: episode sets and the KinDER environment."""

import argparse
import json
import unittest

from robocode.planning_explanations.search.policy_cli import episode_list
from robocode.planning_explanations.search.policy_domains import (
    POLICIES,
    KinderDomain,
)

OBSTRUCTION2D = {
    "_target_": "robocode.environments.variable_object_count_env."
    "VariableObjectCountEnv",
    "constant_object_env_path": "kinder.envs.kinematic2d.obstruction2d:"
    "Obstruction2DEnv",
    "count_kwarg": "num_obstructions",
    "count_object_prefix": "obstruction",
    "design_counts": [0, 1, 2],
    "eval_counts": [0, 1, 2, 3, 4],
    "bilevel_env_name": "obstruction2d",
}


class EpisodeListTest(unittest.TestCase):
    """--development / --validation values."""

    def test_parses_count_seed_pairs(self):
        """ "0:0,1:1,2:2" is three (count, seed) episodes, in order."""
        self.assertEqual(episode_list("0:0,1:1,2:2"), ((0, 0), (1, 1), (2, 2)))

    def test_rejects_malformed_or_repeated_episodes(self):
        """A missing seed or a repeated episode is an argument error."""
        for text in ("1,2", "1:0,1:0", "a:1", ""):
            with self.assertRaises(argparse.ArgumentTypeError):
                episode_list(text)


class KinderDomainNameTest(unittest.TestCase):
    """Reports and banks name the environment they ran in."""

    def test_default_config_keeps_its_name(self):
        """ClutteredRetrieval2D keeps the name its frozen banks were made with."""
        config = json.loads(
            (POLICIES / "clutteredretrieval2d_env_config.json").read_text()
        )
        self.assertEqual(KinderDomain(config).name, "kinder-clutteredretrieval2d")

    def test_other_environment_is_named_after_its_class(self):
        """Obstruction2D runs are named kinder-obstruction2d and reset by count."""
        domain = KinderDomain(OBSTRUCTION2D)
        self.assertEqual(domain.name, "kinder-obstruction2d")
        state, _ = domain.reset((2, 0))
        names = {str(o.name) for o in state}
        self.assertTrue({"obstruction0", "obstruction1"} <= names)
        self.assertEqual(domain.max_steps((2, 0)), 600)


if __name__ == "__main__":
    unittest.main()
