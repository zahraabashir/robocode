"""What a coding agent's own tests said at each checkpoint, against a fixed re-run.

During synthesis an agent tests its policy many times, on scenes it chooses. This
script recovers those tests and puts them next to an independent measurement:

``extract``
    Reads every command the agent and its subagents ran (Codex session files in
    ``sandbox/.agent_sessions``) and every result file it committed, attaches each
    to the checkpoint it tested (a commit that changed ``approach.py`` or a file it
    imports, such as ``planner.py``), labels what kind of test it was
    (environment probe, component test, single-episode trace, timing, pass rate)
    and turns printed results into per-episode records. Writes ``tests.json``
    (every command) and ``believed.json`` (per checkpoint: episodes the agent ran
    and how many it solved).
``replay``
    Re-runs each checkpoint ``--repeats`` times on the first ``--episodes``
    instances of the run's own evaluation suite (the harness's seeds and object
    counts, never seen during synthesis), with the harness's timed episode runner
    and per-instance timeout. Writes ``replay/v<NN>-r<K>.json`` (checkpoint NN, run
    K); resumable, and saved runs on a different suite are redone. Policies that
    stop searching on a clock give different results run to run and with machine
    load, so keep ``--workers`` at or below the number of fast cores.
``plot``
    ``believed_vs_measured.png``, ``seen_timeline.png`` and ``summary.md``.
    Re-runs are shown as the mean over runs with the min-max range.

Usage (``<run>`` is the folder holding ``sandbox/``, e.g. ``.../replicate_424`` or
``.../run``):

    python experiments/test_history.py extract --run <run> --out <dir>
    python experiments/test_history.py replay --run <run> --out <dir> \
        [--episodes 100] [--repeats 1] [--workers 3]
    python experiments/test_history.py plot --out <dir>

Codex runs only for now (Claude Code transcripts live in ``stream.jsonl``).
"""

from __future__ import annotations

import argparse
import ast
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from collections import Counter, defaultdict
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
JS_STRING = r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'|`((?:[^`\\]|\\.)*)`'
COMMAND = re.compile(r"[\"']?cmd[\"']?\s*:\s*(?:" + JS_STRING + ")", re.S)
SESSION = re.compile(r"session_id\s*:\s*(\d+)")
# A command still running reports its session, as text or inside a JSON chunk.
STARTED = re.compile(r"SESSION_ID=(\d+)|\"session_id\"\s*:\s*(\d+)")
COMMIT = re.compile(r"git commit[^\n]*?-m\s*(['\"])(.+?)\1")
# Rough test labels (kind_of), from the structure of the code a command runs.
WRITTEN = re.compile(
    r"cat\s*>+\s*([\w./-]+)\s*<<-?\s*['\"]?(\w+)['\"]?\n.*?\n\2\b", re.S
)
POLICY_USE = re.compile(
    r"^[ \t]*(?:from[ \t]+approach\w*[ \t]+import|import[ \t]+approach)"
    r"|GeneratedApproach\(|load_generated_approach\(",
    re.M,
)
ENV_USE = re.compile(r"make_env\(|env_client|gym(?:nasium)?\.make\(")
EPISODE_RUN = re.compile(r"\.reset\(.*?\.step\(", re.S)
MANY_EPISODES = re.compile(
    # a for-loop whose indented body resets an environment (one way to split each
    # line: "[ \t]+[^\n]*" would backtrack exponentially)
    r"for[ \t]+\w+[ \t]+in\b[^\n]*(?:\n[ \t][^\n]*)*?\.reset\(|sys\.argv\[1:\]"
    r"|Pool\(|Executor\(",
)
# "from planner import plan", "import geometry as g, kin" (also inside functions)
LOCAL_IMPORT = re.compile(
    r"^[ \t]*(?:from[ \t]+([\w.]+)[ \t]+import|import[ \t]+([\w., \t]+))", re.M
)
SCRIPT = re.compile(r"python[^\n|;&]*?\s([\w./-]+\.py)\b")
# Saved results: any data or log file except traces and debug output.
RESULT_FILE = re.compile(
    r"^(?!.*(?:trace|debug|env_spaces)).*\.(json|jsonl|log|txt|out)$"
)
# Kinds of test, in the order they are checked.
KINDS = (
    "planner component",
    "timing",
    "pass rate",
    "single-episode trace",
    "environment probe",
)


# ----------------------------------------------------------------------- helpers


def _git(sandbox: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(sandbox), *args], capture_output=True, text=True, check=True
    ).stdout


def _js_string(groups: tuple) -> str:
    raw = next(g for g in groups if g is not None)
    try:
        return json.loads('"' + raw.replace("\n", "\\n") + '"')
    except json.JSONDecodeError:
        return raw.encode().decode("unicode_escape", errors="replace")


def _text(output: Any) -> str:
    if isinstance(output, list):
        return "".join(x.get("text", "") for x in output if isinstance(x, dict))
    return str(output or "")


def _unwrap(output: str) -> str:
    """Codex sometimes wraps command output in JSON chunks; keep the text."""
    pieces = []
    for match in re.finditer(
        r'\{"chunk_id"[^\n]*?"output":"((?:[^"\\]|\\.)*)"', output
    ):
        try:
            pieces.append(json.loads('"' + match.group(1) + '"'))
        except json.JSONDecodeError:
            pieces.append(match.group(1))
    return "\n".join(pieces) if pieces else output


def _imported_files(text: str, tree: set[str]) -> set[str]:
    """Sandbox files a Python file imports (``x.py`` or ``x/__init__.py``)."""
    found = set()
    for source, plain in LOCAL_IMPORT.findall(text):
        names = (
            [source]
            if source
            else [n.split(" as ")[0].strip() for n in plain.split(",")]
        )
        for name in names:
            parts = name.lstrip(".").split(".")
            for k in range(len(parts), 0, -1):
                stem = "/".join(parts[:k])
                found |= {f"{stem}.py", f"{stem}/__init__.py"} & tree
    return found


def _policy_files(sandbox: Path, sha: str) -> set[str]:
    """approach.py and every sandbox file it imports, directly or not, at a commit."""
    tree = set(_git(sandbox, "ls-tree", "-r", "--name-only", sha).splitlines())
    if "approach.py" not in tree:
        return set()
    files: set[str] = set()
    todo = ["approach.py"]
    while todo:
        name = todo.pop()
        if name in files:
            continue
        files.add(name)
        todo.extend(_imported_files(_git(sandbox, "show", f"{sha}:{name}"), tree))
    return files


def versions(sandbox: Path) -> list[dict]:
    """Every commit that changed the policy's code, oldest first.

    The policy is approach.py plus the sandbox files it imports, directly or through
    another of them (e.g. planner.py). A commit that changes only such a helper is a
    checkpoint too; ``files`` lists what each checkpoint changed.
    """
    rows = []
    before: set[str] = set()
    log = _git(
        sandbox, "log", "--reverse", "--name-only", "--format=%x00%H%x09%ct%x09%s"
    )
    for block in log.split("\x00")[1:]:
        header, *changed = block.strip().split("\n")
        sha, when, subject = header.split("\t", 2)
        policy = _policy_files(sandbox, sha)
        # files of the policy before or after this commit (a removed import counts)
        touched = sorted({c for c in changed if c} & (policy | before))
        before = policy
        if touched:
            rows.append(
                {"sha": sha, "time": float(when), "subject": subject, "files": touched}
            )
    for index, row in enumerate(rows, 1):
        row["index"] = index
    return rows


def _version_of(command: str, started: float, history: list[dict]) -> int:
    """The checkpoint a command tested: the commit it made, else the latest before."""
    made = COMMIT.search(command)
    if made:
        hits = [v["index"] for v in history if v["subject"] == made.group(2)]
        if hits:
            return hits[0]
    before = [v["index"] for v in history if v["time"] <= started]
    return before[-1] if before else 0


# ----------------------------------------------------------------------- extract


def codex_commands(sandbox: Path) -> list[dict]:
    """Every shell command of every agent thread, with its output and start time."""
    records = []
    pattern = str(sandbox / ".agent_sessions/codex/**/*.jsonl")
    for path in sorted(glob.glob(pattern, recursive=True)):
        thread, calls, outputs = None, [], {}
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                event = json.loads(line)
                payload = event.get("payload", {})
                if event.get("type") == "session_meta" and thread is None:
                    source = payload.get("source")
                    spawn = (
                        source.get("subagent", {}).get("thread_spawn", {})
                        if isinstance(source, dict)
                        else {}
                    )
                    thread = spawn.get("agent_path", "/main").rsplit("/", 1)[-1]
                if (
                    payload.get("type") == "custom_tool_call"
                    and payload.get("name") == "exec"
                ):
                    calls.append(
                        (event["timestamp"], payload["call_id"], payload["input"])
                    )
                if payload.get("type") == "custom_tool_call_output":
                    outputs[payload["call_id"]] = _text(payload.get("output"))
        # A long command's output continues in later write_stdin calls.
        continued: dict[str, str] = defaultdict(str)
        for _, call_id, code in calls:
            for sid in SESSION.findall(code):
                continued[sid] += outputs.get(call_id, "")
        for when, call_id, code in calls:
            for match in COMMAND.finditer(code):
                output = outputs.get(call_id, "")
                for sid in {a or b for a, b in STARTED.findall(output)}:
                    output += continued.get(sid, "")
                records.append(
                    {
                        "time": when,
                        "started": datetime.fromisoformat(
                            when.replace("Z", "+00:00")
                        ).timestamp(),
                        "thread": thread or "main",
                        "command": _js_string(match.groups()),
                        "output": _unwrap(output),
                    }
                )
    records.sort(key=lambda r: r["started"])
    return records


def codex_outputs(sandbox: Path) -> list[dict]:
    """Every tool output as it reached an agent: time, thread, text."""
    rows = []
    pattern = str(sandbox / ".agent_sessions/codex/**/*.jsonl")
    for path in sorted(glob.glob(pattern, recursive=True)):
        thread = None
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                event = json.loads(line)
                payload = event.get("payload", {})
                if event.get("type") == "session_meta" and thread is None:
                    source = payload.get("source")
                    spawn = (
                        source.get("subagent", {}).get("thread_spawn", {})
                        if isinstance(source, dict)
                        else {}
                    )
                    thread = spawn.get("agent_path", "/main").rsplit("/", 1)[-1]
                if payload.get("type") == "custom_tool_call_output":
                    when = event["timestamp"]
                    rows.append(
                        {
                            "time": datetime.fromisoformat(
                                when.replace("Z", "+00:00")
                            ).timestamp(),
                            "thread": thread or "main",
                            "text": _unwrap(_text(payload.get("output"))),
                        }
                    )
    rows.sort(key=lambda r: r["time"])
    return rows


def _seen(episodes: list[dict], outputs: list[dict], history: list[dict]) -> None:
    """When each result first reached an agent: the first output, after the test
    was launched, that contains its result line. Never read: seen_at is None."""
    for episode in episodes:
        episode["seen_at"] = episode["seen_time"] = episode["seen_by"] = None
        line = episode.get("line")
        if not line:
            continue
        for output in outputs:
            if output["time"] >= episode["launched"] - 1 and line in output["text"]:
                before = [v["index"] for v in history if v["time"] <= output["time"]]
                episode["seen_at"] = before[-1] if before else 0
                episode["seen_time"] = output["time"]
                episode["seen_by"] = output["thread"]
                break


def _script_text(sandbox: Path, name: str, sha: str | None) -> str:
    name = name.removeprefix("./")
    if sha:
        try:
            return _git(sandbox, "show", f"{sha}:{name}")
        except subprocess.CalledProcessError:
            pass
    path = sandbox / Path(name).name
    return path.read_text(errors="ignore") if path.exists() else ""


def runs_policy_or_env(command: str, code: str) -> bool:
    """A command whose printed results are read as the agent's test results: it
    runs Python and mentions the policy or the environment."""
    return "python" in command and bool(
        re.search(
            r"GeneratedApproach|from approach\w* import|import approach|"
            r"make_env|env_client",
            code,
        )
    )


def _run_text(command: str, code: str) -> str:
    """The code a command runs: the body of a file it writes but never runs (such
    as approach.py itself, written with ``cat > file <<EOF``) is left out."""

    def keep(match: re.Match) -> str:
        name = re.escape(Path(match.group(1)).name)
        ran = re.search(rf"python[^\n|;&]*\s[\w./-]*{name}\b", command)
        return match.group(0) if ran else f"cat > {match.group(1)}"

    return WRITTEN.sub(keep, code)


def kind_of(command: str, code: str) -> str | None:
    """A rough, not yet validated label of what a command tests.

    From the structure of the code it runs, not from function names: never loads
    the policy -> environment probe (if it makes an environment); loads the policy
    but never steps an environment -> component test; times the policy -> timing;
    runs episodes in a loop or over given seeds -> pass rate; else one episode ->
    single-episode trace. Commands that only write, edit or compile files are not
    tests.
    """
    if "python" not in command:
        return None
    code = _run_text(command, code)
    if not POLICY_USE.search(code):
        return "environment probe" if ENV_USE.search(code) else None
    if not EPISODE_RUN.search(code):
        return "planner component"
    if re.search(r"policy_time|max_action_time", code):
        return "timing"
    if MANY_EPISODES.search(code):
        return "pass rate"
    return "single-episode trace"


def _count_arg(command: str) -> int | None:
    match = re.search(r"--count\s+(\d+)|object_count['\"]?\s*[:=]\s*(\d+)", command)
    return int(next(g for g in match.groups() if g)) if match else None


FLAGS = ("success", "solved", "done")
TEXT_RESULTS = (
    # Sol: "7 (True, 207, -207.0)"
    re.compile(r"^(\d+) \((True|False), \d+,"),
    # "3 {'object_count': 5} steps 47 success True ..."
    re.compile(r"^(\d+) (\{[^}]*\}) steps \d+ success (True|False)"),
    # "15 success True steps 115 ...", "seed 3 solved=True", "4 done: false"
    re.compile(
        r"^(?:seed[=: ]*)?(\d+)\b.*?\b(?:success|solved|done)['\"]?\s*[=:]?\s*"
        r"(True|False|true|false)\b",
        re.I,
    ),
    # "13 False 3300 55.0 ...": a seed followed by its outcome
    re.compile(r"^(\d+)[ ,]+(True|False)\b"),
)
# A result line may start with a label: "RESULT 6 None {'object_count': 1} 111 True
# False 2.89", "RESULT 1 False 1000 3.47". Only result-like labels: "ACTION 3 -1.0
# False False" is a step of a trace, not an episode.
RESULT_LABEL = re.compile(r"^results?\b[:=]?\s+(?=\d)", re.I)
# After the label: the seed, optionally None, the reset options, a step count and a
# decimal (a return: "RESULT 0 1000 -1000.0 False"), then the outcome, perhaps named
# ("RESULT 1 {...} done True steps 452"). A line with no step count besides the
# leading number is left unread: "RESULT 487 False lower_place" leads with a step
# count, not a seed.
LABELLED_RESULT = re.compile(
    r"^(\d+)\s+(?:None\s+)?(?:\{[^}]*\}\s+)?(\d+\s+)?(?:-?\d+\.\d+\s+)?"
    r"(?:(?:done|success|solved)[:=]?\s+)?(True|False|true|false)\b(.*)$"
)
# Lines that look like an episode result; those not read are reported by extract.
RESULT_LIKE = re.compile(
    r"\b(?:result|success|solved)\b.*\b(?:True|False|true|false)\b"
    r"|\b(?:True|False)\b.*\b(?:success|solved)\b",
    re.I,
)
UNREAD: Counter = Counter()  # shape of an unread result-like line -> how often
UNREAD_EXAMPLES: dict[str, str] = {}


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _json_episode(item, count=None, raw: str | None = None) -> dict | None:
    """One saved result: a dict with a success/solved/done flag, or a list
    [seed, (count,) flag, ...]."""
    if isinstance(item, dict):
        flag = next((item[k] for k in FLAGS if isinstance(item.get(k), bool)), None)
        if flag is None:
            return None
        found = item.get("count") if _is_int(item.get("count")) else None
        for key in ("n", "info", "options"):
            nested = item.get(key)
            if found is None and isinstance(nested, dict):
                found = nested.get("object_count")
        if found is None and _is_int(item.get("object_count")):
            found = item["object_count"]
        return {
            "seed": item["seed"] if _is_int(item.get("seed")) else None,
            "count": found if _is_int(found) else count,
            "solved": flag,
            "line": raw or json.dumps(item),
        }
    if isinstance(item, list) and item and _is_int(item[0]):
        flags = [x for x in item[1:4] if isinstance(x, bool)]
        if flags:
            return {
                "seed": item[0],
                "count": item[1] if len(item) > 1 and _is_int(item[1]) else count,
                "solved": flags[0],
                "line": raw or json.dumps(item),
            }
    return None


def _walk(value, count=None):
    """Every result record anywhere inside a JSON document."""
    episode = _json_episode(value, count)
    if episode:
        yield episode
        return
    if isinstance(value, dict):
        for child in value.values():
            yield from _walk(child, count)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child, count)


def _literal(text: str):
    """A printed dict or list: JSON, or Python's own printing ("{'seed': 2, ...}").

    Python-printed dicts count only when they name the scene (a ``seed`` key), so
    per-step state dumps are not taken for episodes.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    try:
        value = ast.literal_eval(text)
    except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
        return None
    return value if isinstance(value, dict) and "seed" in value else None


def _line_episode(line: str, count) -> dict | None:
    text = line.strip()
    # "file.log:{...}" from a search over several files
    text = re.sub(r"^[\w./-]+:(?=[{\[])", "", text)
    if text[:1] in ("{", "[") and text[-1:] in ("}", "]"):
        value = _literal(text)
        if value is not None:
            return _json_episode(value, count, raw=text)
    label = RESULT_LABEL.match(text)
    if label:
        match = LABELLED_RESULT.match(text[label.end() :])
        if match and (match.group(2) or re.search(r"\b\d+\b", match.group(4))):
            seed, _, flag, _ = match.groups()
            nested = re.search(r"'object_count': (\d+)", text)
            return {
                "seed": int(seed),
                "count": int(nested.group(1)) if nested else count,
                "solved": flag.lower() == "true",
                "line": text,
            }
    for pattern in TEXT_RESULTS:
        match = pattern.match(text)
        if not match:
            continue
        groups = match.groups()
        found = count
        if len(groups) == 3:
            nested = re.search(r"'object_count': (\d+)", groups[1])
            found = int(nested.group(1)) if nested else count
        return {
            "seed": int(groups[0]),
            "count": found,
            "solved": groups[-1].lower() == "true",
            "line": text,
        }
    return None


def parse_episodes(output: str, command: str) -> tuple[list[dict], list[tuple]]:
    """Per-episode results printed by a test, and bare "solved X / Y" summaries."""
    count = _count_arg(command)
    episodes = []
    for line in output.splitlines():
        episode = _line_episode(line, count)
        if episode:
            episodes.append(episode)
        elif len(line) < 300 and RESULT_LIKE.search(line):
            shape = re.sub(r"-?\d+(?:\.\d+)?(?:e-?\d+)?", "N", line.strip())[:80]
            UNREAD[shape] += 1
            UNREAD_EXAMPLES.setdefault(shape, line.strip()[:200])
    summaries = []
    if not episodes:
        summaries = [
            (int(s), int(n)) for s, n in re.findall(r"solved (\d+) / (\d+)", output)
        ]
    return episodes, summaries


def parse_file(text: str) -> list[dict]:
    """Results in a saved file: one JSON document, or line by line."""
    try:
        return list(_walk(json.loads(text)))
    except json.JSONDecodeError:
        return parse_episodes(text, "")[0]


def _writes(command: str, name: str) -> bool:
    """Does this command produce the result file ``name``?

    Either by writing it by name (``> batch_20_objects.log``, ``tee``) or, for a file
    named after the run's arguments (``results_100_110_n20.json`` from
    ``batch_test.py 100 110 20``), by those arguments in order.
    """
    base = Path(name).name
    if re.search(rf"(?:>>?|\btee\s+(?:-a\s+)?)\s*(?:\./)?{re.escape(base)}\b", command):
        return True
    numbers = re.findall(r"\d+", Path(base).stem)
    return bool(numbers) and bool(
        re.search(r"\.py\s+" + r"\s+".join(numbers) + r"(?!\S)", command)
    )


def committed_results(
    sandbox: Path, history: list[dict], launches: list[dict]
) -> list[dict]:
    """Result files the agent committed: per-episode records with their checkpoint.

    A test running in the background keeps writing its file while later commits
    happen, and it imported the policy once, at launch. So a file counts for the
    checkpoint of the latest command before the commit that produces it; only when
    no command does, for the checkpoint the commit itself belongs to.
    """
    shas = [v["sha"] for v in history]
    rows = []
    for line in _git(sandbox, "log", "--reverse", "--format=%H %ct").splitlines():
        sha, committed = line.split()
        changed = [
            f
            for f in _git(sandbox, "show", "--name-only", "--format=", sha).split()
            if RESULT_FILE.search(f)
        ]
        if not changed:
            continue
        ancestors = set(_git(sandbox, "rev-list", sha).split())
        at_commit = sum(1 for s in shas if s in ancestors)
        for name in changed:
            started = [
                c
                for c in launches
                if c["started"] <= float(committed) and _writes(c["command"], name)
            ]
            version = started[-1]["version"] if started else at_commit
            launched = started[-1]["started"] if started else float(committed)
            try:
                text = _git(sandbox, "show", f"{sha}:{name}")
            except subprocess.CalledProcessError:
                continue
            episodes = parse_file(text)
            for episode in episodes:
                rows.append(
                    {
                        **episode,
                        "version": version,
                        "launched": launched,
                        "source": f"{name}@{sha[:7]}",
                    }
                )
    return rows


def extract(args: argparse.Namespace) -> None:
    """tests.json and believed.json for one run."""
    UNREAD.clear()
    UNREAD_EXAMPLES.clear()
    sandbox = args.run / "sandbox"
    history = versions(sandbox)
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    tests = []
    episodes = []
    launches = []
    for command in codex_commands(sandbox):
        version = _version_of(command["command"], command["started"], history)
        launches.append({**command, "version": version})
        sha = history[version - 1]["sha"] if version else None
        code = command["command"] + "".join(
            "\n" + _script_text(sandbox, name, sha)
            for name in SCRIPT.findall(command["command"])
        )
        kind = kind_of(command["command"], code)
        found, summaries = (
            parse_episodes(command["output"], command["command"])
            if runs_policy_or_env(command["command"], code)
            else ([], [])
        )
        tests.append(
            {
                "time": command["time"],
                "thread": command["thread"],
                "version": version,
                "kind": kind,
                "command": command["command"][:2000],
                "episodes": found,
                "summaries": summaries,
            }
        )
        for episode in found:
            episodes.append(
                {
                    **episode,
                    "version": version,
                    "launched": command["started"],
                    "source": f"transcript {command['time']}",
                }
            )
        for solved, total in summaries:
            episodes.extend(
                {
                    "seed": None,
                    "count": _count_arg(command["command"]),
                    "solved": i < solved,
                    "version": version,
                    "launched": command["started"],
                    "line": f"solved {solved} / {total}",
                    "source": f"summary {command['time']}",
                }
                for i in range(total)
            )
    episodes += committed_results(sandbox, history, launches)
    # A reset without an explicit count draws it from the seed (the env's own rule).
    design = json.loads((args.run / "env_config.json").read_text()).get("design_counts")
    if design:
        import numpy as np  # pylint: disable=import-outside-toplevel

        for episode in episodes:
            if episode["count"] is None and episode["seed"] is not None:
                episode["count"] = int(
                    np.random.default_rng(episode["seed"]).choice(design)
                )
    _seen(episodes, codex_outputs(sandbox), history)
    # One result per (checkpoint, seed, count): a rerun of the same scene counts
    # once, and it was first seen when any copy of it was.
    unique: dict[tuple, dict] = {}
    anonymous = []
    for episode in episodes:
        if episode["seed"] is None:
            anonymous.append(episode)
            continue
        key = (episode["version"], episode["seed"], episode["count"])
        kept = unique.setdefault(key, episode)
        if episode["seen_time"] is not None and (
            kept["seen_time"] is None or episode["seen_time"] < kept["seen_time"]
        ):
            for field in ("seen_at", "seen_time", "seen_by"):
                kept[field] = episode[field]
    believed: dict[int, dict] = defaultdict(
        lambda: {"episodes": 0, "solved": 0, "by_count": defaultdict(lambda: [0, 0])}
    )
    for episode in list(unique.values()) + anonymous:
        row = believed[episode["version"]]
        row["episodes"] += 1
        row["solved"] += episode["solved"]
        cell = row["by_count"][str(episode["count"])]
        cell[0] += episode["solved"]
        cell[1] += 1
    kinds = defaultdict(Counter)
    for test in tests:
        if test["kind"]:
            kinds[test["version"]][test["kind"]] += 1
    (out / "versions.json").write_text(json.dumps(history, indent=1))
    (out / "episodes.json").write_text(
        json.dumps(
            [
                {
                    "tested_at": e["version"],
                    "seen_at": e["seen_at"],
                    "seen_by": e["seen_by"],
                    "seed": e["seed"],
                    "count": e["count"],
                    "solved": bool(e["solved"]),
                    "source": e["source"],
                }
                for e in list(unique.values()) + anonymous
            ],
            indent=1,
        )
    )
    (out / "tests.json").write_text(json.dumps(tests, indent=1))
    (out / "believed.json").write_text(
        json.dumps(
            {
                str(v): {
                    **row,
                    "by_count": dict(row["by_count"]),
                    "kinds": dict(kinds[v]),
                }
                for v, row in sorted(believed.items())
            }
            | {
                str(v): {"episodes": 0, "solved": 0, "by_count": {}, "kinds": dict(k)}
                for v, k in kinds.items()
                if v not in believed
            },
            indent=1,
        )
    )
    total = Counter(t["kind"] for t in tests if t["kind"])
    print(
        f"{len(tests)} commands, {sum(total.values())} tests ({dict(total)}), "
        f"{sum(r['episodes'] for r in believed.values())} episode results over "
        f"{len(believed)} of {len(history)} checkpoints -> {out}"
    )
    (out / "unread_lines.json").write_text(
        json.dumps(
            [
                {"lines": n, "shape": shape, "example": UNREAD_EXAMPLES[shape]}
                for shape, n in UNREAD.most_common()
            ],
            indent=1,
        )
    )
    if UNREAD:
        print(
            f"warning: {sum(UNREAD.values())} lines that look like episode results "
            f"({len(UNREAD)} shapes) were not read; see unread_lines.json"
        )
    save_official(args.run, out, history)


def save_official(run: Path, out: Path, history: list[dict]) -> None:
    """``official.json``: the harness's own evaluation of the final code, per episode.

    The final code is the last checkpoint unless policy files were left uncommitted,
    which is recorded. Episodes are in suite order, so they line up with re-runs.
    """
    path = run / "results.json"
    if not path.exists() or not history:
        return
    results = json.loads(path.read_text())
    sandbox = run / "sandbox"
    policy = _policy_files(sandbox, "HEAD")
    dirty = {
        line[3:].strip() for line in _git(sandbox, "status", "--porcelain").splitlines()
    }
    (out / "official.json").write_text(
        json.dumps(
            {
                "sha": history[-1]["sha"],
                "uncommitted": sorted(dirty & policy),
                "solve_rate": results.get("solve_rate"),
                "episodes": [
                    {
                        "count": e.get("object_count"),
                        "solved": bool(e.get("solved")),
                        "steps": e.get("num_steps"),
                    }
                    for e in results.get("per_episode", [])
                ],
            },
            indent=1,
        )
    )


# ------------------------------------------------------------------------ replay


def _config(run: Path) -> dict:
    import yaml  # pylint: disable=import-outside-toplevel

    return yaml.safe_load((run / ".hydra/config.yaml").read_text())


def suite(run: Path, episodes: int) -> list[dict]:
    """The first instances of the run's own evaluation suite (seed, object count)."""
    import numpy as np  # pylint: disable=import-outside-toplevel

    config = _config(run)
    env = json.loads((run / "env_config.json").read_text())
    rng = np.random.default_rng(int(config["eval_seed"]))
    seeds = [int(rng.integers(0, 2**63)) for _ in range(episodes)]
    pool = env.get("eval_counts")
    return [
        {"seed": seed, "count": pool[i % len(pool)] if pool else None}
        for i, seed in enumerate(seeds)
    ]


def replay_one(args: argparse.Namespace) -> None:
    """Worker: one checkpoint's tree, every suite episode, JSON on stdout."""
    import importlib  # pylint: disable=import-outside-toplevel

    from robocode.approaches.base_approach import (  # pylint: disable=import-outside-toplevel
        BaseApproach,
    )
    from robocode.utils.episode import (  # pylint: disable=import-outside-toplevel
        load_generated_approach,
        run_episode_with_timeout,
    )

    config = _config(args.run)
    env_config = json.loads((args.run / "env_config.json").read_text())
    module, name = env_config.pop("_target_").rsplit(".", 1)
    env = getattr(importlib.import_module(module), name)(**env_config)
    strict = bool(config.get("approach", {}).get("blackbox_strict", False))
    generated = load_generated_approach(
        args.tree / "approach.py",
        env.action_space,
        env.observation_space,
        {},
        strict_imports=strict,
    )

    class Loaded(BaseApproach):  # pylint: disable=too-few-public-methods
        """The harness's view of a generated policy: reset, step, update."""

        def __init__(self):  # pylint: disable=super-init-not-called
            self._last_state = None

        def reset(self, state, info):
            self._last_state = state
            generated.reset(state, info)

        def update(self, state, reward, done, info):
            self._last_state = state
            if hasattr(generated, "update"):
                generated.update(state, reward, done, info)

        def _get_action(self):
            return generated.get_action(self._last_state)

    results = []
    for episode in json.loads(args.episodes_json):
        count = episode["count"]
        steps = (
            env.max_steps_for_count(count)
            if count is not None and hasattr(env, "max_steps_for_count")
            else int(config.get("max_steps", 1000))
        )
        start = time.perf_counter()
        try:
            metrics, _, _ = run_episode_with_timeout(
                env, Loaded(), episode["seed"], steps, timeout=args.timeout, count=count
            )
            results.append(
                {
                    **episode,
                    "solved": bool(metrics["solved"]),
                    "timed_out": bool(metrics.get("timed_out", False)),
                    "steps": metrics.get("num_steps"),
                    "seconds": round(time.perf_counter() - start, 1),
                }
            )
        except Exception as error:  # pylint: disable=broad-exception-caught
            results.append(
                {
                    **episode,
                    "solved": False,
                    "crashed": f"{type(error).__name__}: {error}"[:200],
                    "seconds": round(time.perf_counter() - start, 1),
                }
            )
    if args.result:
        Path(args.result).write_text(json.dumps(results), encoding="utf-8")
    print(json.dumps(results))


RESULT_NAME = "_replay_results.json"


def _worker_results(path: Path, stdout: str) -> list[dict]:
    """A worker's results: its result file, else the last JSON list it printed.

    Simulators can print to the same output without a newline (pybullet:
    ``base_root[{...}]``), so the printed list is searched for, not expected at a
    line start.
    """
    if path.exists():
        return json.loads(path.read_text())
    for line in reversed(stdout.splitlines()):
        start = line.find("[{")
        if start >= 0:
            try:
                return json.loads(line[start:])
            except json.JSONDecodeError:
                continue
    return []


def _worker_error(stderr: str) -> str:
    """The most telling line of a failed worker's error output."""
    lines = [l for l in stderr.strip().splitlines() if l.strip()] or ["no output"]
    errors = [l for l in lines if re.search(r"Error|Exception|Killed", l)]
    return (errors or lines)[-1][:300]


def _scenes(results: list[dict]) -> list[tuple]:
    return [(r["seed"], r["count"]) for r in results]


def _saved_runs(folder: Path) -> list[dict]:
    """Every readable re-run file in ``replay/`` that has results, oldest first."""
    rows = []
    paths = folder.glob("v*.json") if folder.exists() else []
    for path in sorted(paths, key=lambda p: p.stat().st_mtime):
        try:
            row = json.loads(path.read_text())
        except (OSError, ValueError):
            continue
        if row.get("results"):
            rows.append(row)
    return rows


def replay(args: argparse.Namespace) -> None:
    """Every checkpoint on the same suite episodes, ``--repeats`` times each.

    One job per (checkpoint, run), all checkpoints' first run before any second, so
    a stopped replay still has every checkpoint once.
    """
    sandbox = args.run / "sandbox"
    history = versions(sandbox)
    chosen = [v for v in history if not args.versions or v["index"] in args.versions]
    episodes = suite(args.run, args.episodes)
    target = args.out / "replay"
    target.mkdir(parents=True, exist_ok=True)
    (args.out / "suite.json").write_text(json.dumps(episodes, indent=1))
    # Runs already saved for this suite, by commit and run number (not by file
    # name: checkpoint numbers change when helper-only commits are added).
    done = {
        (row.get("sha"), row["repeat"])
        for row in _saved_runs(target)
        if "repeat" in row and _scenes(row["results"]) == _scenes(episodes)
    }
    jobs = [
        (r, v)
        for r in range(1, args.repeats + 1)
        for v in chosen
        if args.force or (v["sha"], r) not in done
    ]

    def one(job: tuple[int, dict]) -> None:
        repeat, version = job
        path = target / f"v{version['index']:02d}-{version['sha'][:7]}-r{repeat}.json"
        start = time.time()
        load = os.getloadavg()[0]
        # ".noindex": keep macOS Spotlight from indexing each unpacked checkpoint
        with tempfile.TemporaryDirectory(suffix=".noindex") as tree:
            archive = subprocess.run(
                ["git", "-C", str(sandbox), "archive", version["sha"]],
                capture_output=True,
                check=True,
            ).stdout
            subprocess.run(["tar", "-x", "-C", tree], input=archive, check=True)
            done = subprocess.run(
                [
                    sys.executable,
                    __file__,
                    "replay-one",
                    "--run",
                    str(args.run),
                    "--tree",
                    tree,
                    "--timeout",
                    str(args.timeout),
                    "--episodes-json",
                    json.dumps(episodes),
                    "--result",
                    str(Path(tree) / RESULT_NAME),
                ],
                capture_output=True,
                text=True,
                cwd=REPO,
                check=False,
                env={
                    **os.environ,
                    "PYTHONPATH": str(REPO / "src"),
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
            )
            results = _worker_results(Path(tree) / RESULT_NAME, done.stdout)
        error = "" if results else _worker_error(done.stderr)
        path.write_text(
            json.dumps(
                {
                    **version,
                    "repeat": repeat,
                    "results": results,
                    "error": error,
                    "seconds": round(time.time() - start),
                    # 1-minute load average at start and end, to spot busy runs
                    "load": [round(load, 1), round(os.getloadavg()[0], 1)],
                    "workers": args.workers,
                },
                indent=1,
            )
        )
        solved = sum(r["solved"] for r in results)
        timeouts = sum(bool(r.get("timed_out")) for r in results)
        print(
            f"v{version['index']:02d} run {repeat}/{args.repeats}: "
            f"{solved}/{len(results)} solved ({timeouts} timeouts) "
            f"in {round(time.time() - start)} s {error}",
            flush=True,
        )

    with ThreadPoolExecutor(args.workers) as pool:
        list(pool.map(one, jobs))


# -------------------------------------------------------------------------- plot

DESIGN_MAX = 10  # counts above this are beyond the design range (1, 3, 5, 10)
COLORS = {"believed": "#eb6834", "measured": "#2a78d6"}
KIND_COLORS = {
    "pass rate": "#2a78d6",
    "single-episode trace": "#a9a8a3",
    "environment probe": "#1baf7a",
    "planner component": "#eb6834",
    "timing": "#8f6ad8",
}


def _load(out: Path) -> tuple[list[dict], dict, dict[int, list[dict]]]:
    """Checkpoints, the agent's own results, and every re-run per checkpoint.

    Re-runs are matched to checkpoints by commit, since numbering changes when
    checkpoints are added. Only re-runs on the current suite (``suite.json``) count.
    A single re-run saved before repeats existed is used when no numbered run is.
    """
    history = json.loads((out / "versions.json").read_text())
    believed = {
        int(k): v for k, v in json.loads((out / "believed.json").read_text()).items()
    }
    suite_path = out / "suite.json"
    scenes = (
        _scenes(json.loads(suite_path.read_text())) if suite_path.exists() else None
    )
    index_of = {v["sha"]: v["index"] for v in history}
    numbered: dict[int, dict[int, dict]] = defaultdict(dict)
    single: dict[int, list[dict]] = {}
    for row in _saved_runs(out / "replay"):  # oldest first: a redone run replaces
        index = index_of.get(row.get("sha"))
        if index is None or (scenes and _scenes(row["results"]) != scenes):
            continue
        if "repeat" in row:
            numbered[index][row["repeat"]] = row
        else:
            single[index] = [row]
    runs = {i: [r[k] for k in sorted(r)] for i, r in numbered.items()}
    return history, believed, {**single, **runs}


def _run_rates(runs: list[dict], keep) -> list[float]:
    """Solve rate of each re-run on the episodes ``keep`` selects (by count)."""
    rates = []
    for run in runs:
        chosen = [r for r in run["results"] if keep(str(r["count"]))]
        if chosen:
            rates.append(sum(r["solved"] for r in chosen) / len(chosen))
    return rates


def _flaky(runs: list[dict]) -> list[tuple[int, list[dict]]]:
    """Suite episodes solved in some re-runs and not others: (position, results)."""
    by_episode = zip(*(run["results"] for run in runs))
    return [
        (i, list(results))
        for i, results in enumerate(by_episode)
        if len({r["solved"] for r in results}) > 1
    ]


def _official_check(
    out: Path, history: list[dict], measured: dict[int, list[dict]]
) -> dict | None:
    """The official evaluation on the re-run scenes, against each re-run of the final
    checkpoint, episode by episode. None without ``official.json`` or ``suite.json``,
    or when the official episodes are not in suite order."""
    path, suite_path = out / "official.json", out / "suite.json"
    if not path.exists() or not suite_path.exists():
        return None
    official = json.loads(path.read_text())
    scenes = json.loads(suite_path.read_text())
    index = {v["sha"]: v["index"] for v in history}.get(official["sha"])
    episodes = official["episodes"][: len(scenes)]
    if (
        index is None
        or len(episodes) < len(scenes)
        or [e["count"] for e in episodes] != [s["count"] for s in scenes]
    ):
        return None
    runs = []
    for run in measured.get(index, []):
        pairs = list(zip(run["results"], episodes))
        runs.append(
            {
                "solved": sum(r["solved"] for r, _ in pairs),
                "same_outcome": sum(r["solved"] == e["solved"] for r, e in pairs),
                "same_steps": sum(r.get("steps") == e["steps"] for r, e in pairs),
                "differ": [
                    i for i, (r, e) in enumerate(pairs) if r["solved"] != e["solved"]
                ],
            }
        )
    return {
        "index": index,
        "official": episodes,
        "runs": runs,
        "uncommitted": official.get("uncommitted", []),
    }


def _official_text(check: dict | None) -> str:
    """The summary's check of re-runs against the official evaluation."""
    if not check:
        return (
            "No comparison: the run has no `results.json`, `extract` has not been run "
            "since this check was added, or the official episodes are not in the order "
            "of the re-run suite."
        )
    n, v = len(check["official"]), check["index"]
    lines = [
        f"The official evaluation ran the final code (v{v}) on these same {n} scenes "
        f"and solved {sum(e['solved'] for e in check['official'])}/{n}. Re-running v{v} "
        "here should give the same outcomes; if it does not, this machine runs the "
        "policies differently and every re-run point is suspect."
    ]
    if check["uncommitted"]:
        lines.append(
            f"\n**Warning:** the evaluated code had uncommitted changes to "
            f"{', '.join(check['uncommitted'])}, so v{v} is not exactly what was "
            "evaluated."
        )
    if not check["runs"]:
        lines.append(f"\nv{v} has not been re-run yet.")
        return "\n".join(lines)
    lines += [
        "",
        f"| Re-run of v{v} | Solved | Same outcome as official | Same number of steps |",
        "| --- | --- | --- | --- |",
    ]
    for k, r in enumerate(check["runs"], 1):
        lines.append(
            f"| run {k} | {r['solved']}/{n} | {r['same_outcome']}/{n} | "
            f"{r['same_steps']}/{n} |"
        )
    differ = sorted({i for r in check["runs"] for i in r["differ"]})
    if not differ:
        lines.append(
            "\nEvery outcome matches, so re-runs on this machine reproduce the "
            "official evaluation. (Step counts can differ where the policy's search "
            "stops on a clock.)"
        )
    else:
        listed = ", ".join(
            f"{i + 1} ({check['official'][i]['count']} obstacles, official "
            f"{'solved' if check['official'][i]['solved'] else 'failed'})"
            for i in differ[:15]
        )
        lines.append(
            f"\n**{len(differ)} episode(s) differ from the official outcome** in at "
            f"least one re-run: {listed}{' …' if len(differ) > 15 else ''}. One or two "
            "can be flaky scenes (see below); many, or crashes, mean this machine runs "
            "the policy differently from the evaluation machine."
        )
    return "\n".join(lines)


def _nearest(count: int, centers: list[int]) -> int:
    """The eval count a tested count is grouped with (a tie goes to the smaller)."""
    return min(centers, key=lambda c: (abs(c - count), c))


def gap_breakdown(
    history: list[dict],
    believed: dict,
    measured: dict[int, list[dict]],
    scenes: list[dict],
) -> list[dict]:
    """Per checkpoint: where the gap between the agent's tests and our re-run is from.

    The agent's tests are grouped by the nearest eval obstacle count (17 -> 15,
    30 -> 25, 0 -> 1). Four pass rates, each changing one thing:
    A the agent's tests as run; B its per-range rates in the eval's mix, over the
    ranges it tested; C our re-run on those ranges, same mix; D our re-run on every
    scene. Mix = A - B, same-count = B - C, coverage = C - D; they add up to A - D.
    """
    mix = Counter(s["count"] for s in scenes)
    if not mix or None in mix:
        return []
    centers = sorted(mix)
    rows = []
    for v in history:
        cells = believed.get(v["index"], {}).get("by_count", {})
        known = {int(c): x for c, x in cells.items() if c not in ("None", "null")}
        runs = measured.get(v["index"], [])
        if not known or not runs:
            continue
        agent: dict[int, list[int]] = defaultdict(lambda: [0, 0])
        for count, (solved, tested) in known.items():
            agent[_nearest(count, centers)][0] += solved
            agent[_nearest(count, centers)][1] += tested
        ours = {}
        for c in centers:
            results = [r for run in runs for r in run["results"] if r["count"] == c]
            ours[c] = sum(r["solved"] for r in results) / len(results)
        covered = [c for c in centers if c in agent]
        weight = sum(mix[c] for c in covered)
        a = sum(s for s, _ in agent.values()) / sum(n for _, n in agent.values())
        b = sum(mix[c] * agent[c][0] / agent[c][1] for c in covered) / weight
        c_same = sum(mix[c] * ours[c] for c in covered) / weight
        d = sum(mix[c] * ours[c] for c in centers) / sum(mix.values())
        rows.append(
            {
                "checkpoint": v["index"],
                "agent_tests": round(100 * a, 1),
                "agent_eval_mix": round(100 * b, 1),
                "ours_same_ranges": round(100 * c_same, 1),
                "ours_all": round(100 * d, 1),
                "mix": round(100 * (a - b), 1),
                "same_count": round(100 * (b - c_same), 1),
                "coverage": round(100 * (c_same - d), 1),
                "total_gap": round(100 * (a - d), 1),
                "never_tested": [c for c in centers if c not in agent],
                "per_range": {
                    str(c): {
                        "agent": agent[c],
                        "ours": round(100 * ours[c], 1),
                        "tested_counts": sorted(
                            n for n in known if _nearest(n, centers) == c
                        ),
                    }
                    for c in covered
                },
                "re_runs": len(runs),
            }
        )
    return rows


def gap_summary(rows: list[dict], history: list[dict]) -> dict:
    """The run in one line: averages over checkpoints of the gap and its parts, the
    average size of the gap ignoring its sign, and the gap on the final code."""
    if not rows:
        return {}

    def mean(values: list[float]) -> float:
        return round(sum(values) / len(values), 1)

    final = next((r for r in rows if r["checkpoint"] == history[-1]["index"]), None)
    return {
        "checkpoints": len(rows),
        "average_gap": mean([r["total_gap"] for r in rows]),
        "mix": mean([r["mix"] for r in rows]),
        "same_count": mean([r["same_count"] for r in rows]),
        "coverage": mean([r["coverage"] for r in rows]),
        "average_size": mean([abs(r["total_gap"]) for r in rows]),
        "final_checkpoint": final["total_gap"] if final else None,
    }


def _signed(value: float | None) -> str:
    if value is None:
        return "—"
    return "0" if value == 0 else f"{value:+.1f}".replace("-", "−")


def _ranges(rows: list[dict]) -> list[int]:
    return sorted(
        {int(c) for r in rows for c in r["per_range"]}
        | {c for r in rows for c in r["never_tested"]}
    )


def _gap_text(rows: list[dict], summary: dict) -> str:
    """The summary's gap section: the run in one line, then per checkpoint and per
    obstacle range (the table view of ``gap_breakdown.png``)."""
    if not rows:
        return (
            "No breakdown: it needs the agent's tests with known obstacle counts and "
            "a re-run of the same checkpoint on scenes with obstacle counts."
        )
    lines = [
        "![gap breakdown](gap_breakdown.png)",
        "",
        "| Average gap | Mix | Same-count | Coverage | Average size "
        "| Final checkpoint |",
        "| --- | --- | --- | --- | --- | --- |",
        f"| {_signed(summary['average_gap'])} | {_signed(summary['mix'])} | "
        f"{_signed(summary['same_count'])} | {_signed(summary['coverage'])} | "
        f"{summary['average_size']:.1f} | {_signed(summary['final_checkpoint'])} |",
        "",
        "How to read it, in percentage points: positive means the agent's tests "
        "looked better than our re-run on every evaluation scene, negative that they "
        "looked worse.",
        "",
        f"- **Average gap**: the agent's pass rate minus ours, averaged over the "
        f"{summary['checkpoints']} checkpoints below.",
        "- **Mix, same-count, coverage**: where the gap comes from; they add up to it "
        "(up to rounding). *Mix*: its choice of easier or harder obstacle counts. "
        "*Same-count*: its tests against ours on the same counts. *Coverage*: counts "
        "it never tested.",
        "- **Average size**: the gap ignoring its sign. Larger than the average gap "
        "means it was off in both directions.",
        "- **Final checkpoint**: the gap on the code that was evaluated.",
        "",
        "Looking worse is not necessarily wrong: the agent's tests may have found real "
        "failures that our re-run did not sample, or run under harsher rules than the "
        "evaluation (fewer steps, a shorter timeout, harder scenes).",
        "",
        "### Per checkpoint",
        "",
        "| Checkpoint | Agent's tests | Our re-run | Mix | Same-count | Coverage "
        "| Total gap |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        lines.append(
            f"| v{r['checkpoint']} | {r['agent_tests']:.1f}% | {r['ours_all']:.1f}% | "
            f"{_signed(r['mix'])} | {_signed(r['same_count'])} | "
            f"{_signed(r['coverage'])} | **{_signed(r['total_gap'])}** |"
        )
    ranges = _ranges(rows)
    lines += [
        "",
        "### Per obstacle range",
        "",
        "The agent's tests (solved / tested) against our re-run's rate on the same "
        "range; — = the agent never tested that range (the coverage part). Counts "
        "that are not evaluation counts are grouped with the nearest one.",
        "",
        "| Checkpoint | " + " | ".join(str(c) for c in ranges) + " |",
        "| --- |" + " --- |" * len(ranges),
    ]
    grouped = []
    for r in rows:
        cells = []
        for c in ranges:
            x = r["per_range"].get(str(c))
            cells.append(
                f"{x['agent'][0]}/{x['agent'][1]} vs {x['ours']:.0f}%" if x else "—"
            )
            if x and x["tested_counts"] != [c]:
                grouped.append(
                    f"v{r['checkpoint']}: {', '.join(map(str, x['tested_counts']))} "
                    f"in {c}"
                )
        lines.append(f"| v{r['checkpoint']} | " + " | ".join(cells) + " |")
    if grouped:
        lines += ["", "Grouped: " + "; ".join(grouped) + "."]
    lines += [
        "",
        "Checkpoints without agent tests of known count, or without a re-run, are "
        "left out.",
    ]
    return "\n".join(lines)


GAP_PARTS = (  # stacked in this order; colours validated for colour-blind readers
    ("coverage", "coverage: obstacle ranges it never tested", "#6250d6"),
    ("same_count", "same-count: its tests vs ours on the same ranges", "#eda100"),
    ("mix", "mix: its choice of easier or harder counts", "#1baf7a"),
)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"


def plot_gap(
    plt, out: Path, rows: list[dict], summary: dict, label: str
) -> Path | None:
    """gap_breakdown.png: the gap per checkpoint split into its three parts, and
    the agent's tests against our re-run per obstacle range."""
    if not rows:
        return None
    import numpy as np  # pylint: disable=import-outside-toplevel
    from matplotlib.colors import (  # pylint: disable=import-outside-toplevel
        LinearSegmentedColormap,
    )
    from matplotlib.patches import Rectangle  # pylint: disable=import-outside-toplevel

    xs = list(range(len(rows)))
    ranges = _ranges(rows)
    fig, (top, bottom) = plt.subplots(
        2,
        1,
        figsize=(max(9.0, 0.8 * len(rows) + 3.5), 9.5),
        sharex=True,
        gridspec_kw={"height_ratios": [1.15, 1]},
    )
    for ax in (top, bottom):
        ax.set_facecolor(SURFACE)
    above = [0.0] * len(rows)
    below = [0.0] * len(rows)
    for key, name, color in GAP_PARTS:
        values = [r[key] for r in rows]
        top.bar(
            xs,
            values,
            bottom=[a if v >= 0 else b for v, a, b in zip(values, above, below)],
            color=color,
            width=0.6,
            edgecolor=SURFACE,
            linewidth=1.5,
            label=name,
            zorder=2,
        )
        above = [a + max(v, 0) for a, v in zip(above, values)]
        below = [b + min(v, 0) for b, v in zip(below, values)]
    totals = [r["total_gap"] for r in rows]
    top.scatter(
        xs, totals, marker="D", s=40, color=INK, zorder=3, label="total gap (the sum)"
    )
    limit = max(5.0, *above, *(-b for b in below), *(abs(t) for t in totals)) * 1.3
    top.set_ylim(-limit, limit)
    top.axhline(0, color=INK_2, linewidth=1, zorder=1)
    top.grid(axis="y", alpha=0.25, zorder=0)
    top.set_ylabel("Agent's tests minus our re-run\n(percentage points)")
    for y, text, va in (
        (0.98, "↑ the agent's tests looked better than the re-run", "top"),
        (0.02, "↓ the agent's tests looked worse than the re-run", "bottom"),
    ):
        top.text(
            0.005, y, text, transform=top.transAxes, va=va, fontsize=8.5, color=INK_2
        )
    top.legend(
        loc="lower left",
        bbox_to_anchor=(0, 1.0),
        ncol=2,
        frameon=False,
        fontsize=8.5,
    )
    # Per range: colour = agent's rate - our rate; hatched = never tested.
    grid = np.full((len(ranges), len(rows)), np.nan)
    for j, r in enumerate(rows):
        for c, x in r["per_range"].items():
            solved, tested = x["agent"]
            i = ranges.index(int(c))
            grid[i, j] = 100 * solved / tested - x["ours"]
            bottom.text(
                j,
                i,
                f"{solved}/{tested}\n{x['ours']:.0f}%",
                ha="center",
                va="center",
                fontsize=7,
                color="white" if abs(grid[i, j]) > 35 else INK,
                zorder=3,
            )
    cmap = LinearSegmentedColormap.from_list("gap", ["#2a78d6", "#f0efec", "#e34948"])
    image = bottom.imshow(
        grid,
        cmap=cmap,
        vmin=-50,
        vmax=50,
        aspect="auto",
        origin="lower",
        extent=(-0.5, len(rows) - 0.5, -0.5, len(ranges) - 0.5),
        zorder=1,
    )
    for i, j in zip(*np.where(np.isnan(grid))):
        bottom.add_patch(
            Rectangle(
                (j - 0.5, i - 0.5),
                1,
                1,
                facecolor=SURFACE,
                hatch="////",
                edgecolor="#d6d5d0",
                linewidth=0,
                zorder=2,
            )
        )
    bottom.set_yticks(range(len(ranges)), [str(c) for c in ranges])
    bottom.set_ylabel("Obstacles\n(agent's tests grouped\nto the nearest count)")
    bottom.set_xticks(xs, [f"v{r['checkpoint']}" for r in rows])
    bottom.set_xlabel("Checkpoint")
    scale = fig.colorbar(
        image, ax=bottom, orientation="horizontal", fraction=0.06, pad=0.2, aspect=50
    )
    scale.set_ticks([-50, 0, 50], labels=["−50 or less", "0", "+50 or more"])
    scale.set_label(
        "Agent's pass rate minus ours on that range (points); "
        "cells: agent solved/tested, our rate; hatched: never tested",
        fontsize=8.5,
    )
    fig.suptitle(
        f"{label}: where the gap between the agent's tests and our re-run comes from",
        x=0.01,
        ha="left",
        fontweight="bold",
    )
    fig.text(
        0.01,
        0.945,
        f"Average gap {_signed(summary['average_gap'])} "
        f"(mix {_signed(summary['mix'])}, same-count {_signed(summary['same_count'])}, "
        f"coverage {_signed(summary['coverage'])}) · average size "
        f"{summary['average_size']:.1f} · final checkpoint "
        f"{_signed(summary['final_checkpoint'])}",
        fontsize=9.5,
        color=INK_2,
    )
    fig.subplots_adjust(top=0.86, hspace=0.12)
    path = out / "gap_breakdown.png"
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    return path


def _outcome(result: dict) -> str:
    if result["solved"]:
        return "solved"
    if result.get("timed_out"):
        return "timeout"
    return "crash" if result.get("crashed") else "fail"


def _spread_text(values: Sequence[float]) -> str:
    """'4.3 (3–6)' over several runs, or the single value."""
    mean = sum(values) / len(values)
    text = f"{mean:.1f}".removesuffix(".0")
    return text if len(set(values)) == 1 else f"{text} ({min(values)}–{max(values)})"


def _runs_text(runs: list[dict], keep) -> str:
    """Mean solved / episodes over re-runs, with the lowest and highest run."""
    counts = []
    total = 0
    for run in runs:
        chosen = [r for r in run["results"] if keep(str(r["count"]))]
        counts.append(sum(r["solved"] for r in chosen))
        total = len(chosen)
    if not total:
        return "—"
    mean = f"{sum(counts) / len(counts):.1f}".removesuffix(".0")
    spread = f" ({min(counts)}–{max(counts)})" if len(set(counts)) > 1 else ""
    return f"{mean}/{total}{spread}"


def _rate(cells: dict, keep) -> tuple[float | None, int]:
    solved = sum(s for c, (s, n) in cells.items() if keep(c))
    total = sum(n for c, (s, n) in cells.items() if keep(c))
    return (solved / total if total else None), total


def _design(count: str) -> bool:
    return count not in ("None", "null") and int(count) <= DESIGN_MAX


def _beyond(count: str) -> bool:
    return count not in ("None", "null") and int(count) > DESIGN_MAX


def _seen_table(out: Path, history: list[dict]) -> list[str]:
    """Per checkpoint: results first seen while it was current, and never seen."""
    path = out / "episodes.json"
    if not path.exists():
        return ["(run extract again to add when results were seen)"]
    episodes = json.loads(path.read_text())
    rows = [
        "| Checkpoint | Results first seen (solved / episodes) | Tested on | "
        "Seen by |",
        "| --- | --- | --- | --- |",
    ]
    for v in history:
        seen = [e for e in episodes if e["seen_at"] == v["index"]]
        if not seen:
            continue
        tested = Counter(f"v{e['tested_at']}" for e in seen)
        threads = Counter(e["seen_by"] for e in seen)
        rows.append(
            f"| v{v['index']} | {sum(e['solved'] for e in seen)}/{len(seen)} | "
            + ", ".join(f"{k} ({n})" for k, n in sorted(tested.items()))
            + " | "
            + ", ".join(f"{k} ({n})" for k, n in threads.most_common())
            + " |"
        )
    never = [e for e in episodes if e["seen_at"] is None]
    unseen_fails = sum(not e["solved"] for e in never)
    rows.append(
        f"\n{len(never)} of {len(episodes)} results were never shown to the agent "
        f"line by line ({unseen_fails} of them failures). Agents often read only a "
        "log's last lines or search it for failures (e.g. `rg 'false' log`), so "
        "they may know a success only as the absence of a failure."
    )
    return rows


def plot(args: argparse.Namespace) -> None:
    """Believed vs measured pass rate, tested counts, and kinds of test."""
    import matplotlib  # pylint: disable=import-outside-toplevel

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # pylint: disable=import-outside-toplevel

    history, believed, measured = _load(args.out)
    label = args.label or args.out.name
    xs = [v["index"] for v in history]
    fig, axes = plt.subplots(
        3,
        1,
        figsize=(11, 9.5),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1.6, 1.6]},
    )
    ax = axes[0]
    for regime, keep, marker in (
        ("design counts (≤10)", _design, "o"),
        ("larger counts (>10)", _beyond, "^"),
    ):
        pts = []
        for v in xs:
            if v in believed:
                rate, n = _rate(believed[v]["by_count"], keep)
                if rate is not None:
                    pts.append((v, rate, n))
        if pts:
            ax.scatter(
                [p[0] for p in pts],
                [100 * p[1] for p in pts],
                s=[min(220, 18 + 3 * p[2]) for p in pts],
                marker=marker,
                facecolor="none" if marker == "^" else COLORS["believed"],
                edgecolor=COLORS["believed"],
                alpha=0.8,
                zorder=3,
                label=f"agent's own tests, {regime} (size = episodes)",
            )
    unknown = [
        (v, *_rate(believed[v]["by_count"], lambda c: c in ("None", "null")))
        for v in xs
        if v in believed
    ]
    unknown = [p for p in unknown if p[1] is not None]
    if unknown:
        ax.scatter(
            [p[0] for p in unknown],
            [100 * p[1] for p in unknown],
            s=[min(220, 18 + 3 * p[2]) for p in unknown],
            marker="s",
            facecolor="none",
            edgecolor=COLORS["believed"],
            alpha=0.6,
            zorder=3,
            label="agent's own tests, count not recorded",
        )
    runs_each = max((len(r) for r in measured.values()), default=0)
    episodes_each = max(
        (len(r[0]["results"]) for r in measured.values() if r), default=0
    )
    for regime, keep, style, shift in (
        ("design counts (≤10)", _design, "-", -0.07),
        ("larger counts (>10)", _beyond, "--", 0.07),
    ):
        # (checkpoint, mean, lowest run, highest run), in percent
        bands: list[tuple[int, float, float, float]] = []
        for v in xs:
            rates = _run_rates(measured.get(v, []), keep)
            if rates:
                bands.append(
                    (
                        v,
                        100 * sum(rates) / len(rates),
                        100 * min(rates),
                        100 * max(rates),
                    )
                )
        if not bands:
            continue
        ax.plot(
            [p[0] for p in bands],
            [p[1] for p in bands],
            style,
            color=COLORS["measured"],
            marker="o",
            markersize=4,
            linewidth=1.8,
            zorder=2,
            label=f"re-run on unseen evaluation scenes, {regime}"
            + (f": mean of {runs_each} runs, bar = range" if runs_each > 1 else ""),
        )
        spread = [p for p in bands if p[3] > p[2]]
        if spread:
            ax.vlines(
                [p[0] + shift for p in spread],
                [p[2] for p in spread],
                [p[3] for p in spread],
                color=COLORS["measured"],
                linewidth=4,
                alpha=0.3,
                zorder=1,
            )
    check = _official_check(args.out, history, measured)
    if check:
        for regime, keep, fill, shift in (
            ("design counts", _design, "black", -0.2),
            ("larger counts", _beyond, "white", 0.2),
        ):
            chosen = [e for e in check["official"] if keep(str(e["count"]))]
            if chosen:
                ax.scatter(
                    [check["index"] + shift],
                    [100 * sum(e["solved"] for e in chosen) / len(chosen)],
                    marker="*",
                    s=170,
                    facecolor=fill,
                    edgecolor="black",
                    zorder=4,
                    label=f"official evaluation of the final code, {regime}",
                )
    ax.set_ylim(-5, 105)
    ax.set_ylabel("Episodes solved (%)")
    ax.set_title(
        f"{label}: what the agent's own tests said vs a fixed re-run, per checkpoint",
        loc="left",
        fontweight="bold",
    )
    ax.grid(alpha=0.3)
    top_handles = ax.get_legend_handles_labels()
    # Which obstacle counts the agent tested at each checkpoint.
    counts = sorted(
        {
            int(c)
            for v in believed.values()
            for c in v["by_count"]
            if c not in ("None", "null")
        }
    )
    ax = axes[1]
    for v in xs:
        for c, (s, n) in (believed.get(v, {}).get("by_count") or {}).items():
            if c in ("None", "null"):
                continue
            ax.scatter(
                [v],
                [counts.index(int(c))],
                s=min(200, 12 + 2 * n),
                color=COLORS["believed"],
                alpha=0.25 + 0.75 * (s / n if n else 0),
                edgecolor="none",
            )
    ax.set_yticks(range(len(counts)), [str(c) for c in counts])
    ax.set_ylabel("Obstacle counts\nthe agent tested")
    ax.grid(alpha=0.3)
    # Kinds of test per checkpoint.
    ax = axes[2]
    bottom = [0] * len(xs)
    for kind in KINDS:
        heights = [believed.get(v, {}).get("kinds", {}).get(kind, 0) for v in xs]
        ax.bar(
            xs, heights, bottom=bottom, color=KIND_COLORS[kind], label=kind, width=0.8
        )
        bottom = [b + h for b, h in zip(bottom, heights)]
    ax.set_ylabel("Tests run at this\ncheckpoint (rough labels)")
    ax.set_xlabel("Checkpoint (commit that changed the policy's code, in order)")
    ax.legend(loc="upper left", fontsize=8, ncol=5, frameon=False)
    ax.grid(alpha=0.3, axis="y")
    fig.subplots_adjust(hspace=0.22, bottom=0.17, top=0.95)
    fig.legend(
        *top_handles,
        loc="lower left",
        bbox_to_anchor=(0.01, 0.045),
        ncol=2,
        fontsize=8.5,
        frameon=False,
    )
    fig.text(
        0.01,
        0.005,
        "Believed: episodes the agent ran itself (transcripts and committed result "
        "files), each scene counted once per checkpoint. Measured: the same checkpoint "
        f"on the first {episodes_each} instances of the run's own evaluation suite "
        "(seeds never seen during synthesis), with the evaluation timeout"
        + (
            f", run {runs_each} times (line = mean, bar = lowest to highest run)"
            if runs_each > 1
            else ", run once"
        )
        + ". "
        + (
            "Stars: the official evaluation of the final code on the same scenes "
            "(a check that re-runs on this machine match it). "
            if check
            else ""
        )
        + "Middle panel: dot size = episodes, darker = more solved. Bottom panel: "
        "kinds of test from automatic rules, not yet validated.",
        fontsize=8,
        wrap=True,
    )
    path = args.out / "believed_vs_measured.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    rows = [
        "| Checkpoint | Commit | Agent's tests: solved / episodes (design; larger) | "
        "Re-run: mean solved / episodes, (lowest–highest run) (design; larger) | "
        "Flaky scenes | Timeouts per run | Counts tested | "
        "Tests by kind (rough labels, not validated) |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    flaky_rows = []
    for v in history:
        b = believed.get(v["index"], {})
        cells = b.get("by_count", {})
        d = [sum(cells[c][i] for c in cells if _design(c)) for i in (0, 1)]
        g = [sum(cells[c][i] for c in cells if _beyond(c)) for i in (0, 1)]
        runs = measured.get(v["index"], [])
        tested = ", ".join(
            sorted((c for c in cells if c not in ("None", "null")), key=int)
        )
        kinds = ", ".join(
            f"{k} {n}"
            for k, n in sorted(b.get("kinds", {}).items(), key=lambda i: -i[1])
        )
        flaky = _flaky(runs) if len(runs) > 1 else []
        timeouts = [
            sum(bool(r.get("timed_out")) for r in run["results"]) for run in runs
        ]
        helpers = [f for f in v.get("files", []) if f != "approach.py"]
        changed = (
            f" [{', '.join(helpers)}]"
            if helpers and "approach.py" not in v.get("files", [])
            else ""
        )
        rows.append(
            f"| v{v['index']} | {v['subject'][:50]}{changed} | "
            f"{d[0]}/{d[1]}; {g[0]}/{g[1]} | "
            + (
                f"{_runs_text(runs, _design)}; {_runs_text(runs, _beyond)}"
                if runs
                else "—"
            )
            + " | "
            + (str(len(flaky)) if len(runs) > 1 else "—")
            + " | "
            + (_spread_text(timeouts) if runs else "—")
            + f" | {tested or '—'} | {kinds or '—'} |"
        )
        for i, results in flaky:
            outcomes = Counter(_outcome(r) for r in results)
            flaky_rows.append(
                f"| v{v['index']} | {i + 1} | {results[0]['count']} | "
                + ", ".join(f"{n} {k}" for k, n in outcomes.most_common())
                + " | "
                + ", ".join(f"{r.get('seconds', '?')}" for r in results)
                + " |"
            )
    runs_each = max((len(r) for r in measured.values()), default=0)
    flaky_text = (
        (
            "Suite episodes (numbered from 1) that a checkpoint solved in some re-runs "
            "and not in others.\n\n"
            "| Checkpoint | Episode | Obstacles | Outcomes | Seconds per run |\n"
            "| --- | --- | --- | --- | --- |\n" + "\n".join(flaky_rows)
            if flaky_rows
            else "Every checkpoint gave the same outcome on every episode in every run."
        )
        if runs_each > 1
        else "Each checkpoint was re-run once (use `replay --repeats 3` to find them)."
    )
    seen_rows = _seen_table(args.out, history)
    suite_path = args.out / "suite.json"
    gaps = gap_breakdown(
        history,
        believed,
        measured,
        json.loads(suite_path.read_text()) if suite_path.exists() else [],
    )
    gap_run = gap_summary(gaps, history)
    (args.out / "gap_breakdown.json").write_text(
        json.dumps({"run": gap_run, "checkpoints": gaps}, indent=1)
    )
    gap_path = plot_gap(plt, args.out, gaps, gap_run, label)
    (args.out / "summary.md").write_text(
        f"# {label}: the agent's own tests vs a fixed re-run\n\n"
        "A checkpoint is a commit that changed approach.py or a file it imports; "
        "[file] marks one that changed only such a file. "
        "Results are counted for the checkpoint they **tested** (the code loaded "
        "when the test was launched). Re-runs: each checkpoint on the same "
        "evaluation episodes, as many times as listed; the mean is over runs.\n\n"
        + "\n".join(rows)
        + "\n\n## Where the gap comes from\n\n"
        + _gap_text(gaps, gap_run)
        + "\n\n## Check against the official evaluation\n\n"
        + _official_text(check)
        + "\n\n## Flaky scenes\n\n"
        + flaky_text
        + "\n\n## What the agent had seen while each checkpoint was current\n\n"
        "Results whose output first reached the agent (main agent or a subagent) "
        "while this checkpoint was the latest commit: what it knew before making "
        "the next change.\n\n" + "\n".join(seen_rows) + "\n"
    )
    print(path)
    seen_path = plot_seen(plt, args.out, history, label)
    if seen_path:
        print(seen_path)
    if gap_path:
        print(gap_path)
    print(args.out / "summary.md")
    if check and check["runs"]:
        n = len(check["official"])
        print(
            f"official check, v{check['index']}: official "
            f"{sum(e['solved'] for e in check['official'])}/{n}; re-runs solved "
            + ", ".join(f"{r['solved']}/{n}" for r in check["runs"])
            + "; same outcome as official "
            + ", ".join(f"{r['same_outcome']}/{n}" for r in check["runs"])
        )


AGES = (
    (0, "tested on that same checkpoint", "#2a78d6"),
    (1, "1 checkpoint older", "#7fb0ec"),
    (2, "2 checkpoints older", "#f2a07b"),
    (3, "3 or more checkpoints older", "#c4501f"),
)


def plot_seen(plt, out: Path, history: list[dict], label: str) -> Path | None:
    """What the agent learned while each checkpoint was current, and how old it was."""
    path = out / "episodes.json"
    if not path.exists():
        return None
    episodes = json.loads(path.read_text())
    xs = [v["index"] for v in history]
    fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
    for ax, keep, ylabel in (
        (axes[0], lambda e: True, "Results first seen\n(all)"),
        (axes[1], lambda e: not e["solved"], "Results first seen\n(failures only)"),
    ):
        bottom = [0] * len(xs)
        for age, name, color in AGES:
            heights = [
                sum(
                    1
                    for e in episodes
                    if e["seen_at"] == v
                    and keep(e)
                    and min(v - e["tested_at"], 3) == age
                )
                for v in xs
            ]
            ax.bar(xs, heights, bottom=bottom, color=color, width=0.8, label=name)
            bottom = [b + h for b, h in zip(bottom, heights)]
        ax.set_ylabel(ylabel)
        ax.grid(alpha=0.3, axis="y")
        ax.yaxis.get_major_locator().set_params(integer=True)
        ax.set_ylim(0, max(*bottom, 1) * 1.45)
    never = [e for e in episodes if e["seen_at"] is None]
    axes[0].set_title(
        f"{label}: test results the agent learned while each checkpoint was current",
        loc="left",
        fontweight="bold",
    )
    axes[0].legend(
        title="Age of the tested code",
        fontsize=8.5,
        frameon=False,
        ncol=2,
        loc="upper center",
    )
    axes[1].set_xlabel("Checkpoint current when the result was first seen")
    fig.text(
        0.01,
        0.005,
        f"A result is seen when its output first reaches the main agent or a "
        f"subagent. Never shown line by line: {len(never)} of {len(episodes)} "
        f"results ({sum(not e['solved'] for e in never)} of them failures).",
        fontsize=8.5,
    )
    fig.subplots_adjust(hspace=0.15, bottom=0.11, top=0.94)
    target = out / "seen_timeline.png"
    fig.savefig(target, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return target


# -------------------------------------------------------------------------- main


def main() -> None:
    """Command-line entry."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    commands = parser.add_subparsers(dest="command", required=True)
    extract_parser = commands.add_parser("extract", help="tests.json and believed.json")
    extract_parser.add_argument("--run", type=Path, required=True)
    extract_parser.add_argument("--out", type=Path, required=True)
    replay_parser = commands.add_parser("replay", help="re-run every checkpoint")
    replay_parser.add_argument("--run", type=Path, required=True)
    replay_parser.add_argument("--out", type=Path, required=True)
    replay_parser.add_argument(
        "--episodes",
        type=int,
        default=100,
        help="first N instances of the run's evaluation suite (100 = all of it)",
    )
    replay_parser.add_argument(
        "--repeats",
        type=int,
        default=1,
        help="re-runs of every checkpoint (more scenes beat more repeats: use 100 x 1)",
    )
    replay_parser.add_argument("--timeout", type=float, default=60.0)
    replay_parser.add_argument(
        "--workers",
        type=int,
        default=3,
        help="re-runs at once; more than the fast cores makes timing noisier",
    )
    replay_parser.add_argument("--force", action="store_true")
    replay_parser.add_argument(
        "--versions", type=lambda t: {int(x) for x in t.split(",")}
    )
    one_parser = commands.add_parser("replay-one")
    one_parser.add_argument("--run", type=Path, required=True)
    one_parser.add_argument("--tree", type=Path, required=True)
    one_parser.add_argument("--timeout", type=float, required=True)
    one_parser.add_argument("--episodes-json", required=True)
    one_parser.add_argument("--result", help="also write the results here")
    plot_parser = commands.add_parser("plot", help="figures and summary.md")
    plot_parser.add_argument("--out", type=Path, required=True)
    plot_parser.add_argument("--label")
    args = parser.parse_args()
    {"extract": extract, "replay": replay, "replay-one": replay_one, "plot": plot}[
        args.command
    ](args)


if __name__ == "__main__":
    main()
