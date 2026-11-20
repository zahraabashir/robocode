"""A policy split across files: approach.py plus its own helper modules.

Agent-written policies often keep the search in a helper (``from planner import
plan``). The helper is instrumented like approach.py, so the split policy must give
the same evidence and numbers as the same code in one file.
"""

import tempfile
import textwrap
import unittest
from pathlib import Path

from robocode.planning_explanations.search.policy_discovery import (
    discover_policy,
    validate_policy,
)
from robocode.planning_explanations.search.policy_domains import DiscWorld
from robocode.planning_explanations.search.policy_fixtures import (
    _FOLLOW,
    _HEADER,
    _PLANNER,
    PLAN_ONCE,
)
from robocode.planning_explanations.search.policy_runner import (
    PolicyProgram,
    local_modules,
    own_object,
    policy_callable,
    site_order,
)

DEVELOPMENT = ((1, 0), (3, 1))
VALIDATION = ((3, 100),)

# PLAN_ONCE with its A* moved, unchanged, into planner.py as a module function.
SPLIT_PLANNER = "import heapq\nimport math\n\n" + textwrap.dedent(_PLANNER).replace(
    "def _plan(self, ", "def plan("
)
SPLIT_APPROACH = "from planner import plan\n" + _HEADER + _FOLLOW + """
    def reset(self, state, info):
        self.goal = tuple(state["goal"])
        self.path = plan(state["robot"], self.goal, state["obstacles"])

    def get_action(self, state):
        return self._follow(state)
"""


class SplitPolicyTest(unittest.TestCase):
    """The same search in planner.py or in approach.py: same parts, same numbers."""

    results: dict = {}

    @classmethod
    def setUpClass(cls):
        cls.results = {}
        for name, program in (
            ("inline", PolicyProgram(PLAN_ONCE)),
            (
                "split",
                PolicyProgram(SPLIT_APPROACH, modules={"planner": SPLIT_PLANNER}),
            ),
        ):
            bank = discover_policy(program, DiscWorld(), DEVELOPMENT, VALIDATION)
            cls.results[name] = (
                program,
                bank,
                validate_policy(program, DiscWorld(), bank),
            )

    def search_parts(self, name: str) -> dict:
        """Sites the bank holds as searches."""
        _, bank, _ = self.results[name]
        return {s: p for s, p in bank.parts.items() if p["status"] == "search"}

    def test_helper_search_is_a_part_named_after_its_file(self):
        """The A* loop in planner.py is found, explained and named planner.py:..."""
        program, _, _ = self.results["split"]
        (site,) = self.search_parts("split")
        self.assertTrue(site.startswith("planner.py:"), site)
        self.assertEqual(program.sites[site]["file"], "planner.py")
        self.assertEqual(program.sites[site]["function"], "plan")
        (inline,) = self.search_parts("inline")
        self.assertNotIn("file", self.results["inline"][0].sites[inline])

    def test_split_policy_gives_the_same_numbers(self):
        """Every validation number matches the single-file policy."""
        inline = self.results["inline"][2]["summary"]
        split = self.results["split"][2]["summary"]
        self.assertTrue(inline["complete"])
        self.assertEqual(split["mean"], inline["mean"])
        self.assertEqual(split["max"], inline["max"])
        self.assertGreater(split["mean"]["planning_events"], 0)

    def test_digest_covers_helpers_and_keeps_single_file_digest(self):
        """A helper edit changes the program's digest; one file keeps its old one."""
        split = PolicyProgram(SPLIT_APPROACH, modules={"planner": SPLIT_PLANNER})
        edited = PolicyProgram(
            SPLIT_APPROACH, modules={"planner": SPLIT_PLANNER + "\n# edit\n"}
        )
        self.assertNotEqual(split.digest, edited.digest)
        self.assertEqual(
            PolicyProgram(PLAN_ONCE).digest, PolicyProgram(PLAN_ONCE, modules={}).digest
        )


class HelperModuleTest(unittest.TestCase):
    """Loading rules for helper modules."""

    def test_only_imported_siblings_are_loaded(self):
        """approach -> planner -> geometry are loaded; unrelated files are not."""
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "approach.py").write_text("import math\nfrom planner import plan\n")
            (root / "planner.py").write_text(
                "def plan():\n    from geometry import area\n    return area()\n"
            )
            (root / "geometry.py").write_text("def area():\n    return 1.0\n")
            (root / "test_planner.py").write_text("import planner\n")
            modules = local_modules(root / "approach.py")
        self.assertEqual(sorted(modules), ["geometry", "planner"])

    def test_helpers_get_the_simulated_clock_and_count_as_policy_code(self):
        """A helper's `time` is the analyzer's clock; its classes and functions are
        the policy's own."""
        helper = (
            "import time\n"
            "CLOCK = time\n"
            "class Tree:\n"
            "    def __init__(self):\n"
            "        self.nodes = []\n"
            "def grow(tree):\n"
            "    tree.nodes.append(1)\n"
        )
        approach = (
            "from tree import Tree, grow\n"
            "class GeneratedApproach:\n"
            "    def __init__(self, action_space, observation_space, primitives):\n"
            "        self.tree = Tree()\n"
            "        grow(self.tree)\n"
        )
        program = PolicyProgram(approach, modules={"tree": helper})
        policy = program.policy_class()(None, None, {})
        main, module = program.recorder.random.namespaces
        self.assertIs(module["CLOCK"], program.clock.module)
        self.assertTrue(own_object(policy.tree))
        self.assertTrue(policy_callable(main["grow"]))
        self.assertEqual(policy.tree.nodes, [1])

    def test_sites_sort_approach_first_then_helpers_by_line(self):
        """Report order: approach.py's sites, then each helper file's."""
        sites = [
            "planner.py:12:8:While",
            "40:8:While",
            "geometry.py:3:4:For",
            "7:8:For",
        ]
        self.assertEqual(
            sorted(sites, key=site_order),
            ["7:8:For", "40:8:While", "geometry.py:3:4:For", "planner.py:12:8:While"],
        )


if __name__ == "__main__":
    unittest.main()
