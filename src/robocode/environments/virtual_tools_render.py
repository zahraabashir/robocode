"""Draw a Virtual Tools observation as an RGB image, straight from its dict.

Uses only Pillow: the game's own viewer goes through its pymunk copy of the physics,
which does not run under pymunk 7 (see :mod:`robocode.environments.tool_games`).

The scene is drawn at its initial poses. When the latest step was an accepted
placement, its outcome is drawn on top: each moving object's trajectory, a faint copy
at its start pose, and its final pose. Each path entry gives positions and rotations
sampled every ``path_dt`` seconds, so a pose at sample ``k`` is the start geometry
moved rigidly: ``v_k = p_k + R(rot_k - rot_0) (v_0 - p_0)``. A rejected placement is
drawn as a red outline. Earlier placements are numbered markers.
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
from numpy.typing import NDArray
from PIL import Image, ImageColor, ImageDraw, ImageFont

_PANEL_WIDTH = 170
_TOOL_RGB = (40, 40, 220)
_REJECT_RGB = (220, 30, 30)
_Shape = tuple[Any, ...]


def _rgb(name: Any, default: tuple[int, int, int] = (0, 0, 0)) -> tuple[int, ...]:
    try:
        return ImageColor.getrgb(str(name))[:3]
    except ValueError:
        return default


def _lighten(rgb: tuple[int, ...], amount: float) -> tuple[int, ...]:
    return tuple(int(c + (255 - c) * amount) for c in rgb)


def _object_shapes(obj: dict[str, Any]) -> list[_Shape]:
    """The object's geometry at its initial pose, in world coordinates."""
    kind = obj["type"]
    if kind in ("Poly", "Goal"):
        return [("poly", obj["vertices"])]
    if kind == "Compound":
        return [("poly", poly) for poly in obj["polys"]]
    if kind == "Ball":
        return [("ball", obj["position"], obj["radius"])]
    if kind == "Container":
        return [("container", obj["points"], obj["width"])]
    raise ValueError(f"Unknown Virtual Tools object type {kind!r}")


def _move(points: list[Any], p0: Any, pk: Any, angle: float) -> list[tuple[float, ...]]:
    c, s = math.cos(angle), math.sin(angle)
    moved: list[tuple[float, ...]] = []
    for x, y in points:
        dx, dy = x - p0[0], y - p0[1]
        moved.append((pk[0] + c * dx - s * dy, pk[1] + s * dx + c * dy))
    return moved


def _move_shapes(shapes: list[_Shape], p0: Any, pk: Any, angle: float) -> list[_Shape]:
    out: list[_Shape] = []
    for shape in shapes:
        if shape[0] == "ball":
            out.append(("ball", _move([shape[1]], p0, pk, angle)[0], shape[2]))
        elif shape[0] == "poly":
            out.append(("poly", _move(shape[1], p0, pk, angle)))
        else:
            out.append((shape[0], _move(shape[1], p0, pk, angle), shape[2]))
    return out


class _Canvas:
    """World-to-pixel drawing helpers (world y points up, pixel y points down)."""

    def __init__(self, width: int, height: int) -> None:
        self.height = height
        self.image = Image.new("RGB", (width + _PANEL_WIDTH, height), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    def px(self, p: Any) -> tuple[float, float]:
        """Pixel coordinates of world point ``p``."""
        return (float(p[0]), float(self.height - p[1]))

    def shapes(
        self,
        shapes: list[_Shape],
        fill: Any,
        outline: Any = None,
        inner: Any = None,
    ) -> None:
        """Fill polygons and balls; draw containers as thick polylines."""
        for shape in shapes:
            if shape[0] == "poly":
                pts = [self.px(v) for v in shape[1]]
                self.draw.polygon(pts, fill=fill, outline=outline)
            elif shape[0] == "ball":
                (x, y), r = self.px(shape[1]), shape[2]
                self.draw.ellipse(
                    [x - r, y - r, x + r, y + r], fill=fill, outline=outline
                )
            else:
                pts = [self.px(v) for v in shape[1]]
                if inner is not None:
                    self.draw.polygon(pts, fill=inner)
                self.draw.line(
                    pts, fill=fill, width=int(round(shape[2])), joint="curve"
                )

    def trace(self, positions: list[Any], color: Any) -> None:
        """Draw a trajectory as a polyline."""
        if len(positions) > 1:
            self.draw.line([self.px(p) for p in positions], fill=color, width=3)

    def text(self, xy: tuple[float, float], message: str, color: Any = "black") -> None:
        """Write a label at pixel coordinates."""
        self.draw.text(xy, message, fill=color, font=self.font)


def _tool_shapes(tool: list[Any], position: Any) -> list[_Shape]:
    return [
        ("poly", [(position[0] + x, position[1] + y) for x, y in poly]) for poly in tool
    ]


def _draw_scene(canvas: _Canvas, world: dict[str, Any], attempt: Any) -> None:
    """Draw blocks and objects; objects moved by ``attempt`` are drawn at its end."""
    for block in world.get("blocks", {}).values():
        pts = [canvas.px(v) for v in block["vertices"]]
        canvas.draw.polygon(pts, fill=_lighten(_rgb(block.get("color", "grey")), 0.6))
    objects = world["objects"]
    paths = attempt["paths"] if attempt is not None else {}
    # Goal regions first, then static objects, then dynamic ones on top.
    order = sorted(
        objects,
        key=lambda n: (objects[n]["type"] != "Goal", objects[n].get("density", 1) != 0),
    )
    for name in order:
        obj = objects[name]
        shapes = _object_shapes(obj)
        color = _rgb(obj.get("color", "black"))
        if obj["type"] == "Container":
            color = _rgb(obj.get("outerColor", obj.get("color", "black")))
        inner = _rgb(obj["innerColor"]) if "innerColor" in obj else None
        if obj["type"] == "Goal":
            color = _lighten(color, 0.3)
        if name in paths:
            pos, rot = paths[name]["pos"], paths[name]["rot"]
            canvas.trace(pos, _lighten(color, 0.55))
            canvas.shapes(shapes, _lighten(color, 0.75))
            shapes = _move_shapes(shapes, pos[0], pos[-1], rot[-1] - rot[0])
        canvas.shapes(shapes, color, inner=inner)


def _draw_attempts(canvas: _Canvas, obs: dict[str, Any]) -> None:
    """Draw the latest placement and number the earlier ones."""
    history = obs["history"]
    for i, entry in enumerate(history[:-1]):
        x, y = canvas.px(entry["position"])
        color = (120, 120, 120) if entry["accepted"] else _REJECT_RGB
        canvas.draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=color)
        canvas.text((x + 4, y - 12), str(i + 1), color)
    if not history:
        return
    last = history[-1]
    tool = obs["tools"][last["tool"]]
    shapes = _tool_shapes(tool, last["position"])
    if not last["accepted"]:
        canvas.shapes(shapes, None, outline=_REJECT_RGB)
        return
    placed = last["paths"].get("PLACED")
    if placed is not None:
        canvas.trace(placed["pos"], _lighten(_TOOL_RGB, 0.55))
        canvas.shapes(shapes, _lighten(_TOOL_RGB, 0.75))
        pos, rot = placed["pos"], placed["rot"]
        shapes = _move_shapes(shapes, pos[0], pos[-1], rot[-1] - rot[0])
    canvas.shapes(shapes, _TOOL_RGB)


def _draw_panel(canvas: _Canvas, obs: dict[str, Any], width: int) -> None:
    """Tool boxes labelled by action index, plus the attempt counters."""
    draw = canvas.draw
    draw.rectangle(
        [width, 0, width + _PANEL_WIDTH, canvas.height], fill=(235, 235, 235)
    )
    box = (_PANEL_WIDTH - 20) / 2
    for index, tool in enumerate(obs["tools"]):
        cx, cy = width + _PANEL_WIDTH / 2, 100 + index * 170
        draw.rectangle(
            [cx - box, cy - 75, cx + box, cy + 75],
            outline=(150, 150, 150),
            fill="white",
        )
        canvas.text((cx - box + 5, cy - 72), f"tool {index}")
        for poly in tool:
            draw.polygon([(cx + x, cy - y) for x, y in poly], fill=_TOOL_RGB)
    canvas.text(
        (width + 8, canvas.height - 40),
        f"attempts {obs['attempts_used']}/{obs['max_attempts']}",
    )
    canvas.text(
        (width + 8, canvas.height - 24),
        f"rejected {obs['rejected_placements']}/{obs['max_rejected_placements']}",
    )


def _headline(obs: dict[str, Any]) -> str:
    if not obs["history"]:
        return "no placement yet"
    last = obs["history"][-1]
    where = (
        f"tool {last['tool']} at ({last['position'][0]:.0f}, {last['position'][1]:.0f})"
    )
    if not last["accepted"]:
        return f"{where}: placement rejected (overlaps something or out of bounds)"
    outcome = "SUCCESS" if last["success"] else "failure"
    attempt = obs["attempts_used"]
    return f"attempt {attempt}: {where}: {outcome} at t={last['sim_time']:.1f}s"


def render_observation(obs: dict[str, Any]) -> NDArray[np.uint8]:
    """Render a Virtual Tools observation as an ``(H, W, 3)`` uint8 image."""
    world = obs["world"]
    width, height = (int(d) for d in world["dims"])
    canvas = _Canvas(width, height)
    last = obs["history"][-1] if obs["history"] else None
    accepted = last if last is not None and last["accepted"] else None
    _draw_scene(canvas, world, accepted)
    _draw_attempts(canvas, obs)
    _draw_panel(canvas, obs, width)
    canvas.text((6, 4), _headline(obs))
    return np.asarray(canvas.image, dtype=np.uint8)
