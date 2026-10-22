"""A deterministic stand-in LLM for both explainer and profile-updater prompts.

``MockLLMClient`` implements :class:`robocode.utils.llm.LLMClient`. It
recognizes the two prompt types by their tags (``<policy_code>`` for
explanations, ``<round_observation>`` for profile updates) and answers with
simple, rule-based outputs:

- Explanations are assembled from the policy's own docstrings, method names,
  comments and constants. Length, format (bullets vs. prose) and focus follow
  phrases found in the ``<user_profile>`` block (e.g. "about 150 words",
  "bullet", "algorithm").
- Profile updates turn recognizable feedback phrases (from
  :mod:`robocode.explanations.simulated_user`) and test outcomes into
  profile claims. Each claim records its supporting rounds, and its confidence
  grows with the evidence.

This lets tests and demos exercise the full learning loop offline. It is
not a model of what a real LLM would write.
"""

from __future__ import annotations

import ast
import json
import re
from typing import Any

from robocode.utils.llm import LLMResponse

DEFAULT_WORDS = 320


class MockLLMClient:
    """Rule-based completions; records every prompt it receives."""

    def __init__(self, *_: Any, **__: Any) -> None:
        self.prompts: list[str] = []

    def complete(self, messages: list[dict[str, str]]) -> LLMResponse:
        """Return the model's reply to a message list."""
        prompt = messages[-1]["content"]
        self.prompts.append(prompt)
        if "<round_observation>" in prompt:
            return LLMResponse(text=_mock_update(prompt), cost_usd=0.0)
        if "<policy_code>" in prompt:
            return LLMResponse(text=_mock_explanation(prompt), cost_usd=0.0)
        return LLMResponse(text="(mock) unrecognized prompt", cost_usd=0.0)


def _between(text: str, tag: str) -> str | None:
    match = re.search(rf"<{tag}>\n?(.*?)\n?</{tag}>", text, re.DOTALL)
    return match.group(1) if match else None


# --------------------------------------------------------------- explanations


def _profile_directives(profile: dict[str, Any] | None) -> dict[str, Any]:
    """Read length/format/focus wishes out of a profile's free text."""
    out: dict[str, Any] = {
        "words": DEFAULT_WORDS,
        "bullets": None,
        "focus": None,
        "constants": True,
    }
    if not profile:
        return out
    parts = [profile.get("guidance", "")]
    for key in ("preferences", "struggles"):
        parts += [i["claim"] for i in profile.get(key, []) if isinstance(i, dict)]
    text = " ".join(parts).lower()
    number = re.search(r"(?:about|around|under|at most|~)\s*(\d{2,4})\s*words", text)
    if number:
        out["words"] = int(number.group(1))
    elif re.search(r"shorter|too long|concise", text):
        out["words"] = int(DEFAULT_WORDS * 0.6)
    elif re.search(r"more detail|too brief|longer", text):
        out["words"] = int(DEFAULT_WORDS * 1.6)
    if "bullet point" in text or "prefers bullet" in text:
        out["bullets"] = True
    elif "prose" in text:
        out["bullets"] = False
    if re.search(r"algorithm|planning|search", text):
        out["focus"] = "algorithm"
    elif re.search(r"threshold|number|worked example", text):
        out["focus"] = "details"
    elif re.search(r"decision rules|distinguish", text):
        out["focus"] = "decisions"
    if re.search(r"(skip|avoid|not want)[^.]*constant", text):
        out["constants"] = False
    return out


def _code_facts(code: str) -> dict[str, Any]:
    facts: dict[str, Any] = {"doc": "", "methods": [], "comments": [], "constants": []}
    try:
        tree = ast.parse(code)
    except SyntaxError:
        tree = None
    if tree is not None:
        facts["doc"] = (ast.get_docstring(tree) or "").replace("\n", " ")
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("__"):
                doc = (ast.get_docstring(node) or "").split("\n")[0]
                facts["methods"].append((node.name, doc))
            if (
                isinstance(node, ast.Assign)
                and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id.isupper()
                and isinstance(node.value, ast.Constant)
            ):
                facts["constants"].append((node.targets[0].id, node.value.value))
    facts["comments"] = [
        c.strip()
        for c in re.findall(r"#\s*(.{12,90})$", code, re.MULTILINE)
        if not set(c.strip()) <= set("-=# ")
    ]
    lowered = code.lower()
    if "heapq" in lowered or "a*" in lowered or "astar" in lowered:
        facts["algorithm"] = "a best-first (priority-queue) search over candidate plans"
    elif "deque" in lowered or "bfs" in lowered:
        facts["algorithm"] = "a breadth-first search over discrete moves"
    elif "itertools.permutations" in lowered or "permutations(" in lowered:
        facts["algorithm"] = "an enumeration of task orderings, keeping the cheapest"
    elif "_plan" in lowered:
        facts["algorithm"] = (
            "a hand-written planner that builds a staged sequence of waypoints"
        )
    else:
        facts["algorithm"] = (
            "a reactive controller that picks the next motion from the current state"
        )
    return facts


def _mock_explanation(prompt: str) -> str:
    code = _between(prompt, "policy_code") or ""
    profile_text = _between(prompt, "user_profile")
    profile = json.loads(profile_text) if profile_text else None
    d = _profile_directives(profile)
    f = _code_facts(code)

    algorithm = [
        f"The core of the policy is {f['algorithm']}.",
        "At every step it checks its current plan; if the plan is exhausted or no "
        "longer "
        "valid it replans from the observed state, otherwise it executes the next "
        "action.",
        "When several options exist it chooses the one its planning cost prefers first, "
        "then falls back to alternatives if that search fails.",
    ]
    overview = [
        f"Overview: {f['doc']}" if f["doc"] else "The program defines one policy class."
    ]
    decisions = [
        (
            f"`{name}`: {doc}."
            if doc
            else f"It uses `{name}` as one step of its decision process."
        )
        for name, doc in f["methods"]
    ]
    notes = [f"A code comment notes: {c}" for c in f["comments"]]
    details: list[str] = []
    if d["constants"]:
        details = [
            f"It sets {name} = {value}, a threshold that tunes when it acts."
            for name, value in f["constants"]
        ]
    details.append(
        "For example, if an object blocks the goal, it first plans to clear it, then "
        "returns to the goal."
    )

    if d["focus"] == "algorithm":
        sentences = algorithm + overview + decisions + notes + details
    elif d["focus"] == "details":
        sentences = overview + details + decisions + algorithm + notes
    elif d["focus"] == "decisions":
        sentences = (
            algorithm[1:] + decisions + algorithm[:1] + overview + notes + details
        )
    else:
        sentences = overview + algorithm + decisions + details + notes

    chosen: list[str] = []
    total = 4  # the "How this policy works" heading
    for s in sentences:  # stay within the word target (but say something)
        if chosen and total + len(s.split()) > d["words"]:
            continue
        chosen.append(s)
        total += len(s.split())
    if d["bullets"]:
        return "## How this policy works\n\n" + "\n".join(f"- {s}" for s in chosen)
    head, body = chosen[:3], chosen[3:]
    paragraphs = [" ".join(head)] + [
        " ".join(body[i : i + 4]) for i in range(0, len(body), 4)
    ]
    return "## How this policy works\n\n" + "\n\n".join(p for p in paragraphs if p)


# ------------------------------------------------------------ profile updates


def _confidence(evidence: list[int]) -> str:
    return "low" if len(evidence) < 2 else "medium" if len(evidence) < 3 else "high"


def _upsert(
    items: list[dict[str, Any]],
    item_id: str,
    claim: str,
    rnd: int,
    keep_evidence: bool = True,
) -> None:
    for item in items:
        if item.get("id") == item_id:
            evidence = (item.get("evidence", []) if keep_evidence else []) + [rnd]
            item.update(
                claim=claim, evidence=evidence, confidence=_confidence(evidence)
            )
            return
    items.append(
        {"id": item_id, "claim": claim, "evidence": [rnd], "confidence": "low"}
    )


def _mock_update(prompt: str) -> str:
    profile = json.loads(_between(prompt, "previous_profile") or "{}")
    obs = json.loads(_between(prompt, "round_observation") or "{}")
    rnd = obs.get("round", 0)
    words = obs.get("explanation_words", DEFAULT_WORDS)
    prefs = profile.get("preferences", [])
    understood = profile.get("understood", [])
    struggles = profile.get("struggles", [])
    questions = list(profile.get("open_questions", []))

    pref = obs.get("preference")
    if pref is not None:
        text = pref.get("text", "").lower()
        number = re.search(r"(\d{2,4}) words", text)
        old_length = next((i["claim"] for i in prefs if i.get("id") == "length"), "")
        if "too long" in text:
            target = int(number.group(1)) if number else int(words * 0.6)
            _upsert(
                prefs,
                "length",
                f"Prefers shorter explanations, about {target} words.",
                rnd,
                keep_evidence="shorter" in old_length,
            )
        elif "too brief" in text or "more detail" in text:
            target = int(words * 1.6)
            _upsert(
                prefs,
                "length",
                f"Prefers more detailed explanations, about {target} words.",
                rnd,
                keep_evidence="detailed" in old_length,
            )
        if "bullet points" in text:
            _upsert(prefs, "format", "Prefers bullet points over paragraphs.", rnd)
        elif "prose" in text:
            _upsert(prefs, "format", "Prefers prose over bullet lists.", rnd)
        focus = re.search(r"focusing on (.+?)\.?$", text)
        if focus:
            _upsert(
                prefs, "focus", f"Wants explanations to focus on {focus.group(1)}.", rnd
            )
        if "constants" in text:
            _upsert(
                prefs,
                "avoid-constants",
                "Does not want low-level implementation constants.",
                rnd,
            )
        if "keep this style" in text:
            _upsert(
                prefs,
                "style-ok",
                f"Satisfied with an explanation of about {words} words.",
                rnd,
            )
        if pref.get("rating", 3) <= 2 and not text:
            questions.append(
                f"Round {rnd}: low rating without a comment; unclear what to change."
            )

    und = obs.get("understanding")
    if und is not None:
        if und.get("correct"):
            _upsert(
                understood,
                f"{obs.get('env_name', 'task')}-behaviour".lower(),
                f"Recognized the explained policy's behaviour in {obs.get('env_name')}.",
                rnd,
            )
        else:
            _upsert(
                struggles,
                "distinguishing-decisions",
                "Missed what distinguishes the explained policy from alternatives "
                f"({und.get('difficulty')} test).",
                rnd,
            )

    guidance_parts = [i["claim"] for i in prefs if i.get("id") != "style-ok"]
    if any(i.get("id") == "distinguishing-decisions" for i in struggles):
        guidance_parts.append(
            "Emphasize the concrete decision rules that set this policy apart."
        )
    new = {
        "summary": f"Updated after round {rnd} from {len(prefs)} preference and "
        f"{len(understood) + len(struggles)} understanding observations.",
        "preferences": prefs,
        "understood": understood,
        "struggles": struggles,
        "open_questions": questions[-4:],
        "guidance": " ".join(guidance_parts),
    }
    return "```json\n" + json.dumps(new, indent=2) + "\n```"
