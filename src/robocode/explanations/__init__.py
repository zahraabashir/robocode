"""Personalized explanations of generated robot policies.

A research prototype for the question: can an LLM learn, through repeated
interaction, to explain complex programmatic policies in the way a particular
user prefers, while still making the user understand them?

Components (one module each, so any can be swapped independently):

- :mod:`.policy_provider` -- frozen ``approach.py`` policies from the agent_runs
  archive, plus a rollout engine built on :mod:`robocode.utils.episode`.
- :mod:`.understanding` -- an offline bank of A/B rollout tests (target vs.
  distractor policy from the same initial state) and their scoring.
- :mod:`.explanation_generator` -- LLM explanation of one policy, optionally
  conditioned on a user profile.
- :mod:`.feedback` -- preference rating and free-text feedback.
- :mod:`.user_model` -- the persistent per-user, per-condition profile and the
  LLM that updates it. The condition decides which signals the updater sees.
- :mod:`.runner` -- step-wise study sessions and a simulated-participant loop.
- :mod:`.logger` -- JSONL interaction logs for analysis.
- :mod:`.web_app` -- minimal participant interface.
- :mod:`.mock_llm` / :mod:`.simulated_user` -- offline stand-ins for testing the
  learning loop without API calls or human participants.
"""
