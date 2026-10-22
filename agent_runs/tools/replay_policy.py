"""Replay one agent's final policy and save a GIF of the episode.

Rebuilds the environment from the run's saved config and runs its frozen
evidence/final/approach.py, the same program that was scored.

    python agent_runs/tools/replay_policy.py \
        agent_runs/environments/Obstruction2D/runs/claude_opus55_high_r42_820cc0f3 [seed]

Writes <run>_seed<seed>.gif in the current directory. Run from the robocode
repository root inside its virtual environment (uv sync --dev).
"""

import sys
from pathlib import Path

import yaml
from hydra.utils import instantiate
from omegaconf import OmegaConf

from robocode.utils.episode import load_generated_approach, save_video


def main() -> None:
    """Replay the run given on the command line."""
    run = Path(sys.argv[1])
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    cfg = OmegaConf.create(yaml.safe_load((run / "evidence/config.yaml").read_text()))
    env = instantiate(cfg.environment)
    policy = load_generated_approach(
        run / "evidence/final/approach.py", env.action_space, env.observation_space, {}
    )
    obs, info = env.reset(seed=seed)
    policy.reset(obs, info)
    frames = [env.render()]
    terminated, step = False, 0
    for step in range(1, int(cfg.max_steps) + 1):
        obs, _, terminated, truncated, info = env.step(policy.get_action(obs))
        frames.append(env.render())
        if terminated or truncated:
            break
    print(f"{run.name}: {'solved' if terminated else 'not solved'} in {step} steps")
    save_video(frames, Path(f"{run.name}_seed{seed}.gif"))


if __name__ == "__main__":
    main()
