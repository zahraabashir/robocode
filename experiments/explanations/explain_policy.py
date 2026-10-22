"""Explain a policy for one person using a profile learned in a study.

No learning happens here: the profile is read, never updated, and there is no
test or rating. The prompt is the same one the study used, so a profile behaves
the same way it did during the study.

    python experiments/explanations/explain_policy.py \
        --config experiments/explanations/conf/pilot.yaml \
        --profile STUDY_DIR/memory/understanding_preference/1/profile.json \
        --policy Obstruction2D/claude_opus55_high_r42_820cc0f3 \
        --baseline --out explanation.md

``--policy`` is a policy id from the archive (``<Env>/<run>``) or a path to any
``approach.py`` (add ``--task task.md`` if it has no task description next to it).
``--config`` supplies only the LLM settings (``explainer_llm``) and archive root.
The profile is plain JSON and can be edited by hand before use.
"""

import argparse
import json
from pathlib import Path

from robocode.explanations.explanation_generator import (
    Explanation,
    ExplanationGenerator,
)
from robocode.explanations.policy_provider import PolicyProvider, policy_from_path
from robocode.explanations.study import load_config, make_llm, public_model_info


def _section(title: str, expl: Explanation) -> str:
    return (
        f"## {title}\n\n"
        f"*{expl.word_count} words; profile version {expl.profile_version}; "
        f"{expl.model.get('provider')} {expl.model.get('model', '')}*\n\n"
        f"{expl.text}\n"
    )


def main() -> None:
    """Generate the explanation(s) and print or save them."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--config", required=True, help="study config (for explainer_llm)"
    )
    parser.add_argument(
        "--profile", type=Path, help="learned profile.json (omit for none)"
    )
    parser.add_argument(
        "--policy", required=True, help="policy id or path to approach.py"
    )
    parser.add_argument(
        "--task", type=Path, help="task description, if not found automatically"
    )
    parser.add_argument(
        "--baseline", action="store_true", help="also explain without the profile"
    )
    parser.add_argument(
        "--out", type=Path, help="write Markdown here instead of printing"
    )
    parser.add_argument("overrides", nargs="*", help="key=value config overrides")
    args = parser.parse_args()

    cfg = load_config(args.config, args.overrides)
    if Path(args.policy).is_file():
        policy = policy_from_path(args.policy, args.task)
    else:
        policy = PolicyProvider(cfg.policy_root).get(args.policy)
    profile = (
        json.loads(args.profile.read_text(encoding="utf-8")) if args.profile else None
    )
    generator = ExplanationGenerator(
        make_llm(cfg.explainer_llm), model_info=public_model_info(cfg.explainer_llm)
    )

    parts = [f"# Explanation of {policy.policy_id}\n"]
    if profile is not None:
        parts.append(f"Profile: `{args.profile}` (version {profile.get('version')}).\n")
    parts.append(
        _section(
            "For this person" if profile else "Explanation",
            generator.generate(policy, profile),
        )
    )
    if args.baseline and profile is not None:
        parts.append(
            _section("Without the profile (baseline)", generator.generate(policy, None))
        )
    text = "\n".join(parts)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
