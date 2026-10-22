"""Build the offline A/B test bank for a study config.

Rolls out every policy in the configured environments on every candidate seed,
keeps pair tests that are non-trivial (same outcome, distinguishable behaviour),
grades their difficulty and renders the videos. This uses no LLM and no
explanation, so the questions are independent of the explanation generator.

    python experiments/explanations/build_test_bank.py \
        --config experiments/explanations/conf/demo_mock.yaml [key=value ...]
"""

import argparse
import collections
import logging

from robocode.explanations.policy_provider import PolicyProvider, RolloutEngine
from robocode.explanations.study import load_config, test_bank_config
from robocode.explanations.understanding import build_test_bank


def main() -> None:
    """Build and summarize the test bank."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("overrides", nargs="*", help="key=value config overrides")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    cfg = load_config(args.config, args.overrides)
    provider = PolicyProvider(
        cfg.policy_root, envs=list(cfg.envs) if cfg.get("envs") else None
    )
    bank = build_test_bank(
        provider, RolloutEngine(), test_bank_config(cfg), cfg.test_bank_dir
    )
    counts = collections.Counter(
        (t.env_name, t.difficulty) for t in bank.tests.values()
    )
    print(f"Wrote {len(bank.tests)} pair tests to {bank.root}")
    for (env, difficulty), n in sorted(counts.items()):
        print(f"  {env:15s} {difficulty:7s} {n}")
    untested = sorted(
        {p.policy_id for p in provider.list_policies()} - set(bank.policy_ids())
    )
    if untested:
        print(
            "Policies without any test (excluded from studies):", *untested, sep="\n  "
        )


if __name__ == "__main__":
    main()
