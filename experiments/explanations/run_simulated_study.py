"""Run a study end-to-end with simulated participants (no human, no UI).

Each persona x repeat is one simulated user, run in every configured condition
with an isolated memory per (user, condition). With the mock LLM this runs
offline; point ``explainer_llm`` / ``updater_llm`` at a real provider to test
the real prompts against simulated feedback.

    python experiments/explanations/run_simulated_study.py \
        --config experiments/explanations/conf/demo_mock.yaml [key=value ...]
"""

import argparse
import logging

from robocode.explanations.runner import run_simulated_session
from robocode.explanations.simulated_user import PERSONAS, SimulatedParticipant
from robocode.explanations.study import StudyContext, load_config


def main() -> None:
    """Run every simulated user in every condition."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("overrides", nargs="*", help="key=value config overrides")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    cfg = load_config(args.config, args.overrides)
    ctx = StudyContext.from_config(cfg)
    for persona_name in cfg.simulation.personas:
        for rep in range(int(cfg.simulation.repeats)):
            user_id = f"sim-{persona_name}-{rep}"
            for condition in cfg.conditions:
                # Same seed in every condition: identical simulated person.
                participant = SimulatedParticipant(
                    PERSONAS[persona_name], seed=int(cfg.study_seed) * 1000 + rep
                )
                session = ctx.make_session(user_id, condition, participant.info())
                records = run_simulated_session(session, participant, ctx.bank)
                if records:
                    acc = sum(r["answer"]["correct"] for r in records) / len(records)
                    rating = sum(r["feedback"]["rating"] for r in records) / len(
                        records
                    )
                    print(
                        f"{user_id:32s} {condition:26s} acc={acc:.2f} "
                        f"mean_rating={rating:.2f}"
                    )
    print(f"Logs in {ctx.logger.study_dir}")


if __name__ == "__main__":
    main()
