"""Reproduce the single-run feasibility audit; never write to the source archive.

Stdlib extraction plus explicitly MANUAL action labels, not an automatic intent
classifier. Optional --replay uses installed KinDER and saved policy source only;
it never runs the archived test harness, shell commands, or remote env_client.
Run from anywhere with Python 3.11+. --replay needs the project's .venv Python.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "agent_runs/environments/Obstruction2D/runs/codex_gpt56sol_r424_2c85c614"
OUTPUT = RUN / "evidence/test_decisions.json"

# Reviewed against commands, outputs, messages, and code changes. Each row:
# feedback event | next substantive action event | action label | evidence note.
# V means further policy sampling/regression, NOT necessarily unseen seeds.
# K means checking a selected previously failing case without added diagnostics.
MANUAL = """
79|81|D|Manual grasp probe on the same seed; later probes precede testing other seeds without a policy edit.
88|90|D|Trace seed 1's controller phases before changing safe travel height.
94|99|V|Expand seeds 1–3 to 0–11 although seeds 2 and 3 still fail; skip process/budget poll E0097.
99|102|D|Trace failing seed 2; E0100 was requested before this result and is not a response.
106|108|D|Inspect seed 1's task list and poses before excluding the static surface.
112|114|D|Trace seed 1 before changing vacuum during transit.
118|120|D|Trace seed 1 before lowering the parking height.
124|126|D|Inspect seed 1's final placement before lateral parking.
130|132|V|Seed 1 passes after an edit; sample seeds 0–9.
132|134|D|Attempted diagnostic command exits 143; actual seed-0 diagnosis follows at E0136.
144|146|D|Trace seed 1 before correcting a moving parking goal.
150|152|D|Inspect seed 1, then find/test simpler zero-obstruction scenes before editing.
163|165|D|Inspect failing zero-obstruction seed 14, then controlled grasp/placement probes.
177|179|R|Immediate policy edit biases the final placement; no new intervening diagnostic tool.
181|183|V|Seed 1 passes after an edit; sample four other zero/one-obstruction cases.
183|185|D|Inspect geometry of the sampled cases, then controller and fine-step grasp probes.
193|195|D|Inspect phases/poses for failing seeds 0, 2, and 3.
201|203|D|Inspect phases/poses for failing seeds 0, 2, and 4.
207|209|D|Inspect failing scenes before changing parking separation.
213|215|D|Trace failures and compare additional cases; diagnostic rather than a plain coverage sweep.
221|223|V|Extend testing despite seeds 2 and 4 still failing; includes known failures and easier cases.
223|225|D|Inspect the multi-obstruction failures before edge-grasp changes.
229|231|D|Inspect remaining failed scenes before geometry-scored parking.
236|238|D|Inspect failed seeds 2, 3, and 5 before reserving a temporary-target slot.
242|244|D|Trace the remaining seed-3 failure.
248|250|D|Trace new seed-5 failure after fixing seed 3.
254|256|D|Inspect seed 5's lift/ceiling state before capping verification height.
260|263|V|Only seed 5 is rerun after the edit, then seeds 11–30; no fresh 0–10 regression on this revision.
263|265|D|Inspect failing seeds 18 and 22.
271|273|D|Inspect seeds 18 and 22 again after both still fail.
277|279|D|Seed 22 passes but 18 fails; inspect 18 rather than broaden.
283|285|D|Inspect still-failing seed 18.
289|291|R|Immediate carry-height edit after local failure plus regression failures.
293|295|R|Restore low parking behavior after the local case and regression remain poor.
297|299|R|Return to globally clear parking after an incomplete recovery of regression performance.
301|303|D|Inspect remaining seed-10 failure.
307|311|V|Seed 10 passes but 18 fails; nevertheless sample seeds 31–60. Motive unstated.
311|313|D|Inspect previously and newly failing seeds together.
317|319|R|Restore the previous clearance margin, then end the first segment; resumed work is a separate prompted segment.
342|344|D|Regression 0–10 passes but seed 18 still fails; inspect seed 18.
348|351|K|Seed 18 and regression pass; explicitly check other known failures 39, 45, and 53 (E0349).
351|353|D|Inspect seeds 39 and 45, which still fail.
358|360|D|Targeted repairs 39/45 pass but regression seed 3 fails; investigate seed 3.
366|370|V|Targeted cases plus regression pass; sample seeds 11–40, many already tested earlier.
370|373|D|Inspect failing seeds 15 and 26.
378|380|V|Targeted cases and regression pass; repeat seeds 11–35 on the new revision.
380|382|D|Investigate recurrent seed-18 failure.
387|389|V|Targeted cases and regression pass; sample seeds 35–60.
389|391|D|Inspect seed 59 before changing parking order.
396|401|V|Targeted cases and regression pass; sample seeds 61–90 after a budget check.
401|404|T|Inspect reset/count capabilities, edit the tester, then test count 3; no visible targeted repair or acknowledgment of seed 85.
411|413|D|Inspect failed count-3 seeds 1 and 3.
417|419|D|Targeted seeds 1/3 pass but count-3 regression seed 4 fails; inspect seed 4.
423|426|V|Targeted count-3 seed 4 plus baseline pass; attempt counts 4 and 5. Count 5 fails to initialize.
426|428|D|Mixed feedback: four count-4 policy failures plus count-5 initialization error; inspect count-4 seed 0.
437|439|R|Immediate policy edit after count-4 failures and a baseline regression failure.
441|443|D|Inspect remaining count-4 seed 1 after other targeted cases pass.
447|449|V|Count-4 repair and regression pass; attempt count 5, which fails during initialization.
451|453|D|Inspect seed 93 after an ordinary sweep.
458|460|D|Seed 93 is fixed but count-4 regression breaks; inspect count-4 seeds 0 and 1.
464|469|V|Seed 93 and regressions pass; sample new count-3/count-4 seeds 5–14.
469|471|D|Inspect count-4 seeds 5 and 6, two of three failures.
475|477|D|Baseline passes but targeted count-4 seed 5 still fails; inspect seed 5.
481|483|D|Targeted seed 5 still fails; inspect phases, then detailed lift variables.
489|491|K|Seed 5 and count-4 regression pass; check other known failure seed 6.
491|493|V|Known failure seed 6 passes; rerun count-4 seeds 5–14.
493|495|D|Inspect remaining count-4 seed 7.
500|502|V|Seed 7, seed 93, and baseline pass; sample count-4 seeds 15–24.
502|504|V|Count-4 sweep passes; attempt count 5 again on a different seed (initialization error).
509|511|V|An ordinary block passes; continue with seeds 36–60.
511|513|D|Inspect recurrent ordinary seed-53 failure.
518|523|V|Targeted seed 53 and regressions pass; test the count 0–4 matrix after integrity checks.
523|526|S|All 15 matrix episodes pass; write confidence marker and finish after integrity checks.
"""
LABELS = {
    "D": "Inspect/probe a failure",
    "R": "Edit/restore policy immediately",
    "V": "Further policy sampling/regression",
    "K": "Check other selected known failures",
    "T": "Investigate testing capability",
    "S": "Declare confidence / finish",
}
SUMMARY = re.compile(r"^success (\d+) / (\d+)", re.M)
EPISODE = re.compile(r"^(\d+) \((True|False), (\d+), (\d+), ([^\n)]+)\)", re.M)
CALL = re.compile(r"(?:python3?|python3\.\d+)(?: -u)? test_approach\.py([^;&|'\"\n]*)")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract():
    events = json.loads((RUN / "evidence/events.json").read_text())
    by_id = {e["id"]: e for e in events}
    commits = json.loads((RUN / "evidence/commits.json").read_text())
    annotations = {}
    for line in MANUAL.strip().splitlines():
        a, b, label, note = line.split("|", 3)
        annotations[f"E{int(a):04}"] = dict(next_event=f"E{int(b):04}", label=label, note=note)
    rows, exceptions = [], []
    seen_cases = set()
    for e in events:
        item = e["item"]
        if item.get("type") != "command_execution":
            continue
        command = item.get("command", "")
        calls = CALL.findall(command)
        if not calls:
            continue  # excludes process polls / textual mentions of the tester
        out = item.get("aggregated_output", "")
        summaries = list(SUMMARY.finditer(out))
        invocations = []
        for arguments in calls:
            opts = dict(re.findall(r"--(start|n|count)\s+(\d+)", arguments))
            invocations.append(dict(start=int(opts.get("start", 0)), n=int(opts.get("n", 10)),
                                    count=int(opts["count"]) if "count" in opts else None))
        if not summaries:
            exceptions.append(dict(event=e["id"], invocations=invocations,
                exit_code=item.get("exit_code"), status=("initialization_error" if "Failed to sample initial state" in out
                else "interrupted" if item.get("exit_code") == 143 else "incomplete_or_pipe_error")))
            continue
        assert e["id"] in annotations, f"Missing manual label: {e['id']}"
        assert len(summaries) <= len(invocations)
        episodes, batches, offset = [], [], 0
        for index, s in enumerate(summaries):
            run = invocations[index]
            eps = [dict(seed=int(m[0]), success=m[1] == "True", steps=int(m[2]),
                        observed_count=int(m[3]), requested_count=run["count"])
                   for m in EPISODE.findall(out[offset:s.start()])]
            solved, total = map(int, s.groups())
            assert len(eps) == total == run["n"], (e["id"], len(eps), total, run)
            assert sum(x["success"] for x in eps) == solved, e["id"]
            assert [x["seed"] for x in eps] == list(range(run["start"], run["start"] + total))
            for x in eps:
                key = (x["requested_count"], x["seed"])
                x["previously_in_completed_test_batch"] = key in seen_cases
                seen_cases.add(key)
            batches.append(dict(**run, solved=solved, total=total))
            episodes.extend(eps)
            offset = s.end()
        a = annotations[e["id"]]
        nxt = by_id[a["next_event"]]
        assert (nxt.get("start_line") or nxt["source_line"]) > e["source_line"], (e["id"], a)
        eligible_commits = [c for c in commits if c.get("version") and any(
            int(v["event"][1:]) <= e["source_line"] for v in c["events"])]
        c = eligible_commits[-1]
        complete = len(summaries) == len(invocations) and item.get("exit_code") == 0
        row = dict(event=e["id"], source_line=e["source_line"], request_line=e["start_line"],
            segment=1 if e["source_line"] < 329 else 2,
            complete_clean_command=complete, exit_code=item.get("exit_code"),
            policy_commit=c["commit"], policy_version=c["version"], policy_commit_id=c["id"],
            batches=batches, episodes=episodes, solved=sum(x["solved"] for x in batches),
            total=sum(x["total"] for x in batches),
            result="any_failure" if any(not x["success"] for x in episodes) else "all_pass",
            uncompleted_invocations=invocations[len(summaries):], **a)
        rows.append(row)
    assert {x["event"] for x in rows} == set(annotations)
    tables = {}
    subsets = {"clean_commands": [r for r in rows if r["complete_clean_command"]],
               "including_partial_E0426": rows}
    for seg in (1, 2):
        subsets[f"segment_{seg}"] = [r for r in rows if r["complete_clean_command"] and r["segment"] == seg]
    for name, subset in subsets.items():
        tables[name] = {outcome: dict(Counter(r["label"] for r in subset if r["result"] == outcome))
                        for outcome in ("any_failure", "all_pass")}
    manifest = json.loads((RUN / "evidence/manifest.json").read_text())
    source_root = Path(manifest["source_run"])
    thread_id = events[0]["item"]["thread_id"]
    resume_evidence = []
    for path in (source_root / "sandbox/.agent_sessions").rglob(f"rollout-*{thread_id}.jsonl"):
        for line_no, line in enumerate(path.read_text().splitlines(), 1):
            record = json.loads(line).get("payload", {})
            if record.get("role") != "user":
                continue
            text = "\n".join(c.get("text", "") for c in record.get("content", []) if isinstance(c, dict))
            if "Remaining shared budget:" in text:
                resume_evidence.append(dict(source=str(path.relative_to(source_root)), line=line_no,
                    file_sha256=sha(path), excerpt=text[text.index("Remaining shared budget:"):]))
    return dict(schema_version=1, date="2026-10-11", run=RUN.name,
        labeling="Manual, single analyst; not blinded, not independent ACT*ONOMY labels.",
        unit="One returned command batch. Subtests in the same command are not separate agent decisions.",
        source_hashes={name: sha(RUN / "evidence" / name) for name in ("events.json", "stream.jsonl", "commits.json")},
        labels=LABELS, tables=tables, rows=rows, excluded_no_summary=exceptions,
        historical_resume_prompt_evidence=resume_evidence)


def plot(data):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    colors = {"D": "#356d9b", "R": "#bc7540", "V": "#51958b", "K": "#8b77aa", "T": "#c9a146", "S": "#7b8490"}
    fig, ax = plt.subplots(figsize=(11, 5.2))
    table = data["tables"]["clean_commands"]
    for y, outcome in enumerate(("any_failure", "all_pass")):
        n = sum(table[outcome].values())
        left = 0
        for label, color in colors.items():
            count = table[outcome].get(label, 0)
            if not count:
                continue
            width = count / n * 100
            ax.barh(y, width, left=left, height=.52, color=color, edgecolor="white", linewidth=1.5)
            ax.text(left + width / 2, y, str(count), ha="center", va="center", color="white", weight="bold", fontsize=12)
            left += width
    ax.set(yticks=[0, 1], yticklabels=["At least one failure\n54 batches", "All reported cases pass\n18 batches"],
           xlim=(0, 100), ylim=(1.7, -.65), xlabel="Share of returned test batches (%)")
    ax.set_title("What did the agent do after testing?", loc="left", fontsize=19, pad=24, weight="bold")
    ax.tick_params(axis="both", length=0, labelsize=11)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.legend(handles=[Patch(facecolor=colors[k], label=LABELS[k]) for k in colors],
              loc="upper left", bbox_to_anchor=(-.24, -.25), ncol=2, frameon=False, fontsize=10)
    fig.text(.045, .92, "Obstruction2D · GPT-5.6-sol · development replicate 424", fontsize=11, color="#535b63")
    fig.text(.045, .025, "Numbers inside bars are counts. One dependent development trajectory; manual labels.\n"
             "72 complete command batches; partial/error batches excluded. These are not independent trials.",
             fontsize=9, color="#535b63")
    fig.subplots_adjust(left=.25, right=.97, top=.79, bottom=.40)
    output = RUN / "evidence/figures/04_next_action_after_test.png"
    fig.savefig(output, dpi=200, facecolor="white")
    plt.close(fig)


def replay():
    # Import installed local environment, never the archived remote client.
    from robocode.environments.variable_object_count_env import VariableObjectCountEnv
    import numpy as np

    class ClientObservationView:
        """Match the saved client's float32 feature decoding and float getter.

        See evidence/final/env_client.py lines 140–151 and 200. Keep physics
        state untouched; quantize ONLY what the policy observes.
        """
        def __init__(self, state):
            self.state = state

        def get(self, obj, feature):
            return float(np.float32(self.state.get(obj, feature)))

        def get_objects(self, typ):
            return sorted(self.state.get_objects(typ), key=lambda obj: obj.name)

        def __getattr__(self, name):
            return getattr(self.state, name)
    commits = {c["id"]: c for c in json.loads((RUN / "evidence/commits.json").read_text())}
    # Prospectively selected contrasting checkpoints: early failure/pass, known
    # failures despite passing regression, and the seed-85 coverage-switch case.
    cases = [
        ("C009", 1, None, False, 1000, "E0124"),
        ("C010", 1, None, True, 125, "E0130"),
        ("C037", 18, None, False, 1000, "E0342"),
        ("C038", 18, None, True, 436, "E0348"),
        ("C038", 39, None, False, 1000, "E0351"),
        ("C043", 85, None, False, 1000, "E0401"),
        ("C043", 0, 3, True, 357, "E0411"),
        ("C043", 1, 3, False, 1000, "E0411"),
    ]
    records = []
    for cid, seed, count, expected, expected_steps, evidence in cases:
        path = RUN / commits[cid]["version"]
        source = path.read_text()
        tree = ast.parse(source)
        # Do not evaluate arbitrary archived scripts or module-level expressions.
        assert all(isinstance(n, (ast.Import, ast.ClassDef)) or
                   isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)
                   for n in tree.body), path
        assert all(a.name in ("math", "numpy") for n in tree.body if isinstance(n, ast.Import) for a in n.names)
        namespace = {}
        exec(compile(tree, str(path), "exec"), namespace)
        env = VariableObjectCountEnv(
            constant_object_env_path="kinder.envs.kinematic2d.obstruction2d:Obstruction2DEnv",
            count_kwarg="num_obstructions", count_object_prefix="obstruction",
            design_counts=[0, 1, 2], eval_counts=[0, 1, 2, 3, 4], bilevel_env_name="obstruction2d")
        try:
            state, info = env.reset(seed=seed, options=None if count is None else {"object_count": count})
            initial_count = info["object_count"]
            policy = namespace["GeneratedApproach"](env.action_space, env.observation_space, {})
            policy.reset(ClientObservationView(state), info)
            terminated = truncated = False
            steps = 0
            # Reproduce the archived development harness's cap, not today's
            # wrapper max_steps_for_count nor the separate final evaluation.
            while not (terminated or truncated) and steps < 1000:
                state, _, terminated, truncated, _ = env.step(policy.get_action(ClientObservationView(state)))
                steps += 1
            records.append(dict(commit_id=cid, policy_sha256=sha(path), seed=seed, requested_count=count,
                observed_count=initial_count, success=bool(terminated), steps=steps,
                truncated=bool(truncated), historical_success=expected, historical_steps=expected_steps,
                source_event=evidence, outcome_matches=bool(terminated) == expected,
                step_count_matches=steps == expected_steps))
        finally:
            env.close()
    return dict(date="2026-10-11", python=sys.version, cap=1000,
                observation_adapter="float(np.float32(feature)); get_objects sorted by name, matching the saved black-box client",
                scope="Local policy replay smoke test; not new coding-agent continuations or full historical environment equivalence.",
                packages={p: importlib.metadata.version(p) for p in ("kindergarden", "numpy", "gymnasium")},
                environment_source_sha256=sha(ROOT / "src/robocode/environments/variable_object_count_env.py"), cases=records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    data = extract()
    if args.replay:
        previous = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {}
        data["replay"] = replay()
        if "replay_initial_native_observations" in previous:
            data["replay_initial_native_observations"] = previous["replay_initial_native_observations"]
        elif previous.get("replay") and not previous["replay"].get("observation_adapter"):
            data["replay_initial_native_observations"] = previous["replay"]
    elif OUTPUT.exists():
        previous = json.loads(OUTPUT.read_text())
        if "replay" in previous:
            data["replay"] = previous["replay"]
        if "replay_initial_native_observations" in previous:
            data["replay_initial_native_observations"] = previous["replay_initial_native_observations"]
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n")
    # if args.plot:
    plot(data)
    print(json.dumps({"rows": len(data["rows"]), "tables": data["tables"],
                      "excluded": data["excluded_no_summary"], "replay": data.get("replay")}, indent=2))


if __name__ == "__main__":
    main()
