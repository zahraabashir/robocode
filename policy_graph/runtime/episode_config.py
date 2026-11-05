"""Reuse RoboCode environment/run configuration for a single traced episode."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ENVIRONMENTS = Path(__file__).resolve().parents[2] / "experiments/conf/environment"


@dataclass
class EpisodeSpec:
    """Resolved environment and primitive settings; no synthesis or training."""

    environment: dict[str, Any]
    max_steps: int
    primitive_names: list[str]
    blackbox: bool
    metadata: dict[str, Any]

    def make_env(self):
        """Construct the same environment class as the experiment runner."""
        from hydra.utils import instantiate  # pylint: disable=import-outside-toplevel

        return instantiate(self.environment)

    def make_primitives(self, env):
        """Build only the primitives granted by the selected configuration."""
        if not self.primitive_names:
            return {}
        # Primitive dependencies are optional for policies that do not use them.
        # pylint: disable=import-outside-toplevel
        from robocode.primitives import build_primitives

        return build_primitives(env, self.primitive_names, blackbox=self.blackbox)


def _saved_config(path):
    for parent in Path(path).resolve().parents:
        hydra = parent / ".hydra/config.yaml"
        if hydra.is_file():
            return hydra
        # Frozen archive: evidence/final/approach.py + evidence/config.yaml.
        if parent.name == "evidence" and (parent / "config.yaml").is_file():
            return parent / "config.yaml"
    return None


def load_episode_spec(
    path, *, env=None, run_config=None, max_steps=None, primitives=None
):
    """Resolve a named environment, explicit saved run, or nearby run metadata."""
    from omegaconf import OmegaConf  # pylint: disable=import-outside-toplevel

    if env is not None:
        source = ENVIRONMENTS / f"{env}.yaml"
        if Path(env).name != env or not source.is_file():
            choices = ", ".join(sorted(p.stem for p in ENVIRONMENTS.glob("*.yaml")))
            raise ValueError(f"Unknown environment {env!r}. Available: {choices}")
        cfg = OmegaConf.create({"environment": OmegaConf.load(source)})
    else:
        source = Path(run_config).resolve() if run_config else _saved_config(path)
        if source is None:
            raise ValueError(
                "No saved run configuration found beside this policy. "
                "Specify --env NAME (for example small_maze) or --run-config PATH. "
                "No scenario JSON is needed for an environment episode."
            )
        cfg = OmegaConf.load(source)
    if not OmegaConf.is_dict(cfg) or not OmegaConf.is_dict(cfg.get("environment")):
        raise ValueError(f"{source} must contain a resolved environment with _target_")
    environment = OmegaConf.to_container(cfg.environment, resolve=True)
    if not isinstance(environment, dict) or "_target_" not in environment:
        raise ValueError(f"{source} must contain a resolved environment with _target_")
    steps = max_steps if max_steps is not None else int(cfg.get("max_steps", 1000))
    if steps <= 0:
        raise ValueError("max_steps must be positive")
    granted = primitives if primitives is not None else cfg.get("primitives", [])
    if isinstance(granted, str):
        raise ValueError("primitives must be a list of names, not a string")
    names = list(granted)
    if not all(isinstance(name, str) for name in names):
        raise ValueError("Primitive names must be strings")
    blackbox = bool((cfg.get("approach") or {}).get("blackbox", False))
    return EpisodeSpec(
        environment,
        steps,
        names,
        blackbox,
        {
            "mode": "episode",
            "environment_config": environment,
            "environment_name": env,
            "episode_config": str(source.resolve()),
            "episode_config_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "primitive_names": names,
            "blackbox": blackbox,
        },
    )
