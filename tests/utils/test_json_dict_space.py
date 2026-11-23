"""Tests for dict observations in black-box mode (JSONDictSpace and its plumbing)."""

import json

import numpy as np
import pytest

from robocode import prompts
from robocode.environments.maze_env import MazeEnv
from robocode.mcp import MCP_TOOLS_SYSTEM_PROMPT_SUFFIX_JSON_DICT, mcp_tool_descriptions
from robocode.utils.env_client import JSONDictSpaceInfo
from robocode.utils.env_server import decode, encode, serialize_space
from robocode.utils.json_dict_space import JSONDictSpace


def test_contains_only_json_dicts() -> None:
    """A JSON dict is a member; non-dicts and non-JSON values are not."""
    space = JSONDictSpace("layout")
    assert space.contains({"a": [1, 2.5, {"b": None}], "c": "x", "d": True})
    assert not space.contains([1, 2])
    assert not space.contains({"a": float("nan")})
    assert not space.contains({"a": np.zeros(2)})
    with pytest.raises(NotImplementedError):
        space.sample()


def test_serialize_and_client_mirror() -> None:
    """The sandbox learns only that observations are dicts, plus the summary."""
    spec = serialize_space(JSONDictSpace("layout summary"))
    assert spec == {"type": "JSONDict", "description": "layout summary"}
    info = JSONDictSpaceInfo(json.loads(json.dumps(spec)))
    assert info.description == "layout summary"
    with pytest.raises(NotImplementedError):
        info.sample()


def test_dict_observation_crosses_the_wire_unchanged() -> None:
    """Encode/decode pass a plain dict observation through as-is."""
    obs = {"world": {"objects": {"Ball": {"position": [1.5, 2]}}}, "history": []}
    assert decode(json.loads(json.dumps(encode(obs)))) == obs


def test_restrict_to_synthesis_defaults_to_no_op() -> None:
    """Envs without held-out instances are unaffected by the env server's hook."""
    env = MazeEnv(3, 3, 3, 3)
    env.restrict_to_synthesis()
    env.reset(seed=0)


def test_strict_spec_describes_dict_observations() -> None:
    """The strict spec documents dicts, not vectors or object-centric states."""
    spec = prompts.blackbox_interaction_spec(strict=True, dict_obs=True)
    assert "plain Python dicts" in spec
    assert "env.render_state(state=obs)" in spec
    assert "fixed-length numpy arrays" not in spec
    assert "ObjectCentricState" not in spec
    # Strict still drops the snapshot lines and adds the import allowlist.
    assert "env.get_state()" not in spec
    assert "may import only" in spec


def test_dict_obs_overrides_render_state_tool_text() -> None:
    """render_state's MCP text drops the list-of-floats state mode for dicts."""
    desc = mcp_tool_descriptions("codex", blackbox=True, strict_blackbox=True)
    dict_desc = mcp_tool_descriptions(
        "codex", blackbox=True, strict_blackbox=True, dict_obs=True
    )
    assert "obs.tolist()" in desc["render_state"]
    assert "obs.tolist()" not in dict_desc["render_state"]
    assert "env.render_state(state=obs)" in dict_desc["render_state"]
    assert "options={'object_count': object_count}" in dict_desc["render_state"]


def test_system_prompt_uses_dict_mcp_suffix() -> None:
    """With MCP tools, a dict-observation env gets the dict rendering guidance."""
    system = prompts.build_system_prompt(
        intro="",
        blackbox=True,
        backend_name="codex",
        timeout=60,
        mcp_tools=("render_state", "render_policy"),
        blackbox_strict=True,
        dict_obs=True,
    )
    assert MCP_TOOLS_SYSTEM_PROMPT_SUFFIX_JSON_DICT in system
    assert "obs.tolist()" not in system
