# Personalized explanations of generated policies (prototype)

Research question: can an LLM learn, over repeated interactions, to explain
complex generated robot policies the way a particular user prefers, while the
user still understands them? The prototype keeps two signals separate:

- **Understanding**: an A/B rollout test. Which of two videos shows the
  explained policy?
- **Preference**: a 1-5 satisfaction rating plus optional free text.

Code: [`src/robocode/explanations/`](../src/robocode/explanations/).
Scripts and configs: [`experiments/explanations/`](../experiments/explanations/).
Tests: [`tests/explanations/`](../tests/explanations/).

## Quick start

```bash
source .venv/bin/activate
CFG=experiments/explanations/conf/demo_mock.yaml

# 1. Build the A/B test bank (real KinDER rollouts, no LLM; ~5 min, 27 MB)
python experiments/explanations/build_test_bank.py --config $CFG

# 2a. Offline demo: mock LLM + simulated participants, all three conditions
python experiments/explanations/run_simulated_study.py --config $CFG
python experiments/explanations/analyze_study.py outputs/explanations/demo_mock

# 2b. Human session with a real LLM (Claude CLI auth; see pilot.yaml for API use)
python experiments/explanations/serve_study.py --config experiments/explanations/conf/pilot.yaml
# open http://127.0.0.1:8765
```

Any config key can be overridden as `key=value` (OmegaConf dotlist), e.g.
`num_rounds=6 study_seed=3 explainer_llm.model=claude-sonnet-5`.

## Components

| Component | Module | Notes |
|---|---|---|
| Policy Provider | `policy_provider.py` | Indexes `actonomoy/environments/<Env>/runs/<run>/evidence/` (frozen `final/approach.py`, `config.yaml`, `task.md`, `results.json`). `RolloutEngine` rebuilds each env from the run's saved Hydra config and loads policies with `robocode.utils.episode.load_generated_approach`. |
| Understanding Evaluator | `understanding.py` | Offline test bank of *pair tests* (two policies, one initial state, two GIFs via `episode.save_video`). `present()` makes a randomized A/B question; `ABPresentation.is_correct()` scores it. |
| Explanation Generator | `explanation_generator.py` | One prompt template for all conditions: task description + policy code, plus a `<user_profile>` block when a profile exists. |
| Feedback Collector | `feedback.py` | Validated rating and comment. Collected in every condition. |
| User Model / Memory | `user_model.py` | JSON profile per (condition, user); `LLMProfileUpdater`; `observation_for_update()` removes the signals a condition may not use before the updater sees anything. |
| Experiment Runner | `runner.py`, `study.py` | `StudySession` state machine (explanation → test → feedback); condition-independent schedules; resume after a restart. |
| Experiment Logger | `logger.py` | `rounds.jsonl` (one line per round), `events.jsonl`, `config.json` (+ git commit). |
| Participant UI | `web_app.py` | Standard-library HTTP server, no new dependencies. |
| Offline stand-ins | `mock_llm.py`, `simulated_user.py` | Deterministic mock LLM for both prompt types; personas with hidden preferences. |

## Design decisions worth knowing

**Tests are fixed before any explanation exists.** `build_test_bank.py` uses
only rollouts, so questions cannot leak from the explainer. The explainer
never sees the test, the distractor, or other policies.

**Non-trivial tests.** A pair test is kept only when both policies have the
*same outcome* on that state (both solve or both fail) and their state
trajectories differ by at least `min_divergence`. Divergence is scale-free and
length-agnostic: resample both trajectories to normalized time, scale each
feature by its pooled std, then take the mean RMS difference. For each policy
pair, `tests_per_pair` states are chosen spread across the divergence range.

**Difficulty is tracked and balanced.** Each test's divergence is ranked
within its environment (`divergence_percentile`) and binned
hard/medium/easy. The schedule assigns bins in shuffled blocks of one of each,
so mean difficulty does not drift over rounds. The analysis also reports
accuracy adjusted for difficulty.

**Held-out policies.** A policy never repeats within a user, so each round
explains a policy the profile has never seen. The last `num_eval_rounds` rounds
are flagged `is_eval_round` for a separate held-out comparison.

**Paired conditions.** The schedule (policies, tests, A/B order, difficulty)
depends only on `(study_seed, user_id)`. A simulated persona run in all three
conditions sees identical questions. Human participants get one condition
each, assigned by a hash of the user id unless the researcher picks one in
the UI.

**Conditions differ only in what adaptation may see.**

| Condition | Profile given to explainer | Updater sees |
|---|---|---|
| `no_learning` | never | (no updater) |
| `understanding_only` | from round 2 | explanation, test outcome, difficulty, behavioural test summary |
| `understanding_preference` | from round 2 | the above + rating + comment |

The behavioural test summary describes only the two rollouts (steps, solved,
which objects changed first), never the explanation or policy ids.

**Profiles are free-form but traceable.** There are no predefined
explanation categories. Every item is
`{"id", "claim", "evidence": [rounds], "confidence": low|medium|high}`, and
lists hold `preferences`, `understood`, `struggles` and `open_questions`,
plus a short `guidance` for the explainer and a `summary`. The updater prompt
says one round is weak evidence (confidence `low`), that confidence should
rise only when several rounds agree, and that understanding and preference
are different things. Unparseable updates keep the previous profile and log
the error. Every version is saved under
`memory/<condition>/<user>/versions/`, and each round logs
`profile_before` and `profile_after`.

**UI defaults.** The explanation is hidden during the test
(`ui.show_explanation_during_test: false`), and correctness is not revealed
before the rating (`ui.reveal_correctness: false`) so it cannot bias
satisfaction. Reading and answer times are logged.

**LLM configuration.** `explainer_llm` and `updater_llm` take the same keys
as `experiments/conf/approach/completion/*.yaml` (`cli`, `anthropic`,
`openai_compatible`), or `provider: mock`. API keys come from the
environment variable named by `api_key_env`. Logged model info strips
credential fields. Each session builds its own clients, so the CLI client's
conversation cache cannot carry anything across users.

## What a round record contains

`rounds.jsonl`, one JSON object per completed round: `study_id`, `user_id`,
`condition`, `round`, `is_eval_round`, `participant` (persona for simulated
users), `env_name`, `policy_id`, `policy_metadata` (agent model, seed,
solve rate, program length), `explanation` (text, word/char counts,
structure counts, whether a profile was used and which version, prompt hash,
latency, cost, model config), `test` (test id, question, target/distractor
ids, A/B → policy mapping and videos, seed, object count, difficulty,
divergence and percentile, rollout stats, correct label), `answer` (label,
correct, reading and answer times), `cumulative_accuracy`, `feedback`,
`profile_before`, `profile_after`, `profile_update` (performed, visible
signals, raw LLM response, error, latency, cost) and `completed_at`.

## Analysis

`analyze_study.py <study_dir>` writes `analysis/`:

- `rounds.csv`, `by_condition_round.csv`: the underlying tables.
- `trends.csv`: per-condition slopes per round, with a user-level bootstrap.
  Accuracy is regressed on round + difficulty percentile; rating and length
  on round.
- `trends.png`: accuracy, satisfaction and length by round.
- `report.md`: learning vs. held-out rounds, accuracy by difficulty, and for
  each adaptive user a round-by-round trace (guidance used → explanation
  length/format → correct → rating → comment), plus the final profile with
  evidence. This is how to inspect *what* was learned and how it shaped the
  next explanation. For simulated users the hidden persona is shown next to
  it.

## Demo results (mock LLM, 6 simulated users × 3 conditions × 9 rounds)

These results check the plumbing. They are not evidence about people or real LLMs.

- With `understanding_preference`, the `concise_algorithmic` persona's
  profile converged on "about 180 words, bullet points, focus on the planning
  algorithm". From round 3 on, its explanations averaged 176 words (baseline
  300) in bullets, and its mean rating was 5.0 (baseline 3.1). The
  `detail_oriented` persona moved the other way: 413 words (baseline 295),
  rating 4.6 (baseline 4.2). So adaptation is user-specific, not
  "always shorter".
- `quiet_rater` never comments and its ratings didn't change across
  conditions. Ratings alone gave the mock updater nothing actionable.
- `understanding_only` produced different explanation content from
  `no_learning`, but the toy simulator's accuracy does not respond to it, so
  their accuracies match. Whether understanding signals help needs real
  participants (or a better simulator).

## Known limitations and next steps

- **The real-LLM path has not been exercised end to end yet.** The prompts
  are built and logged, and the parser accepts fenced/unfenced JSON, but no
  real explainer/updater call was made while building the prototype (no
  credentials were available in that shell). Run a 2-round smoke test first:
  `run_simulated_study.py --config experiments/explanations/conf/pilot.yaml study_id=smoke num_rounds=2 num_eval_rounds=0`.
- Divergence over the full state vector is a generic proxy for "meaningfully
  different decisions". Task-specific signatures (e.g. obstruction removal
  order, push sequence, rover task order) would make better tests and
  difficulty labels. `Rollout.object_change_order` is a first step.
- Distractors are other policies from the same pool, so a participant may
  have seen an explanation of the distractor earlier. That isn't logged as a
  flag yet. It can be derived from `rounds.jsonl`.
- Policy `get_action` calls are not preempted. A hung policy would block the
  bank build, though the wall-time limit stops runaway episodes between steps.
- Obstruction3D is not in the default pool; its MuJoCo rollouts work (about 1 s
  per episode) but were left out to keep the bank build short. Add it to `envs`.
- To swap the learner (bandit/RL over explanation strategies), implement
  `user_model.ProfileUpdater` and keep the observation format; the runner,
  logs and analysis do not change. A cross-user baseline would read profiles
  from other users' `memory/` directories, which `UserMemoryStore` keeps
  separate by design.
