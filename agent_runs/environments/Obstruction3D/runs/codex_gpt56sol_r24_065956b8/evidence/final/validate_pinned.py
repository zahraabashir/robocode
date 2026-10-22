"""Run one pinned obstruction-count case; intended for parallel shell use."""
import argparse
from env_client import make_env
from approach import GeneratedApproach

p = argparse.ArgumentParser()
p.add_argument("seed", type=int)
p.add_argument("count", type=int)
p.add_argument("--limit", type=int, default=800)
a = p.parse_args()

env = make_env()
state, info = env.reset(seed=a.seed, options={"object_count": a.count})
policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
policy.reset(state, info)
last_phase = getattr(policy, "phase", None)
changes = []
for step in range(a.limit):
    state, reward, terminated, truncated, info = env.step(policy.get_action(state))
    phase = getattr(policy, "phase", None)
    if phase != last_phase:
        changes.append((step + 1, last_phase, phase, getattr(policy, "object", None)))
        last_phase = phase
    if terminated or truncated:
        break
held = None
for name in state.get_object_names():
    if name == "robot":
        continue
    try:
        if float(state.get(state.get_object_from_name(name), "grasp_active")) > .5:
            held = name
    except Exception:
        pass
def pos(name):
    o = state.get_object_from_name(name)
    return tuple(round(float(state.get(o, "pose_" + c)), 4) for c in "xyz")
print({"seed": a.seed, "count": a.count, "steps": step + 1,
       "terminated": terminated, "truncated": truncated,
       "phase": getattr(policy, "phase", None), "phase_steps": getattr(policy, "phase_steps", None),
       "object": getattr(policy, "object", None), "held": held,
       "target": pos("target_block"), "region": pos("target_region"),
       "transitions": changes[-15:]})
env.close()
