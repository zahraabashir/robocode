"""Import shim for the ``tool-games`` submodule (the Virtual Tools Game).

``third-party/tool-games`` is k-r-allen/tool-games, the code and levels of Allen,
Smith & Tenenbaum (PNAS 2020). It ships only a Python-2-era distutils ``setup.py``,
so, like ss-pybullet (:mod:`robocode.environments.ss_pybullet`), it is imported off
``sys.path``. This module does that once; no other robocode module touches the path.

Only the game's JavaScript route is used. ``ToolPicker`` simulates a placement in the
game's own engine (Chipmunk-JS 6.1.1, the engine human participants and the SSUP model
ran on) inside node.js through PyExecJS. The package's Python copy of the physics
(``pyGameWorld.world``, built on pymunk) is never built: it predates pymunk 7, which
KinDER pins, and fails there. So a ``ToolPicker`` must be created with
``checkThruPy=False``, and nothing may call ``pyGameWorld.loadFromDict`` or the
package's pygame viewer (pygame is imported at package import, but never used).
"""

# The sys.path bootstrap below must run before the pyGameWorld import, so that import
# cannot sit at the top of the module (see ss_pybullet.py for why isort forces this).
# pylint: disable=wrong-import-position

from __future__ import annotations

import os
import sys
from pathlib import Path

TOOL_GAMES_ROOT = Path(__file__).resolve().parents[3] / "third-party" / "tool-games"
_PACKAGE_ROOT = TOOL_GAMES_ROOT / "environment"
# Level files: TRIALS_DIR / "<Original|Validation>" / "<name>.json".
TRIALS_DIR = _PACKAGE_ROOT / "Trials"


def _ensure_on_path() -> None:
    """Put the tool-games package directory on ``sys.path`` (idempotent)."""
    if not (_PACKAGE_ROOT / "pyGameWorld").is_dir():
        raise ImportError(
            f"tool-games is not checked out at {TOOL_GAMES_ROOT}. Run "
            "`git submodule update --init third-party/tool-games`."
        )
    entry = str(_PACKAGE_ROOT)
    if entry not in sys.path:
        sys.path.insert(0, entry)


def require_node() -> None:
    """Fail early, with a fix, if PyExecJS or a node.js runtime is missing."""
    try:
        import execjs  # type: ignore[import-untyped]  # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise ImportError(
            "The Virtual Tools env needs PyExecJS: `uv sync --extra virtualtools`."
        ) from exc
    try:
        execjs.get()
    except execjs.RuntimeUnavailableError as exc:
        raise RuntimeError(
            "The Virtual Tools env runs the game's JavaScript physics in node.js, "
            "but no JavaScript runtime was found. Install node.js and put `node` on "
            "PATH."
        ) from exc


_ensure_on_path()
# pygame prints a banner to stdout on import; the env never uses pygame.
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

# On sys.path only at run time, so static checkers cannot resolve it.
# pylint: disable-next=import-error
from pyGameWorld import ToolPicker  # type: ignore[import-not-found]  # noqa: E402

__all__ = ["TOOL_GAMES_ROOT", "TRIALS_DIR", "ToolPicker", "require_node"]
