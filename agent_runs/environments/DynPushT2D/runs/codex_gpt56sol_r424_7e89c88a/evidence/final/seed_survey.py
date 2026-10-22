"""Numerical seed survey for the current approach (kept separate from evaluation)."""

import argparse
import math

import numpy as np

from approach import GeneratedApproach
from env_client import make_env


def angle_error(a, b):
    return abs((a - b + math.pi) % (2 * math.pi) - math.pi)


def run_seed(seed, cap=None):
    env = make_env()
    obs, info = env.reset(seed=seed)
    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
    policy.reset(obs, info)
    initial = obs.copy()
    max_steps = min(env.max_steps, cap) if cap else env.max_steps
    min_pos = float("inf")
    min_ang = float("inf")
    min_joint = float("inf")
    max_displacement = 0.0
    max_rotation = 0.0
    first_motion = None
    block0 = initial[:2].copy()
    theta0 = float(initial[2])
    terminated = truncated = False
    for step in range(1, max_steps + 1):
        action = policy.get_action(obs)
        obs, reward, terminated, truncated, info = env.step(action)
        pe = float(np.linalg.norm(obs[:2] - obs[29:31]))
        ae = angle_error(float(obs[2]), float(obs[31]))
        min_pos = min(min_pos, pe)
        min_ang = min(min_ang, ae)
        # Unitless score where <1 in all termination dimensions approximately succeeds.
        joint = max(abs(float(obs[0] - obs[29])) / 0.03,
                    abs(float(obs[1] - obs[30])) / 0.03,
                    ae / math.radians(8))
        min_joint = min(min_joint, joint)
        displacement = float(np.linalg.norm(obs[:2] - block0))
        rotation = angle_error(float(obs[2]), theta0)
        max_displacement = max(max_displacement, displacement)
        max_rotation = max(max_rotation, rotation)
        if first_motion is None and (displacement > 0.002 or rotation > math.radians(1)):
            first_motion = step
        if terminated or truncated:
            break
    env.close()
    return {
        "seed": seed,
        "ok": bool(terminated),
        "steps": step,
        "init_b": initial[:3],
        "init_r": initial[16:18],
        "goal": initial[29:32],
        "final_b": obs[:3],
        "final_r": obs[16:18],
        "pos": float(np.linalg.norm(obs[:2] - obs[29:31])),
        "ang_deg": math.degrees(angle_error(float(obs[2]), float(obs[31]))),
        "min_pos": min_pos,
        "min_ang_deg": math.degrees(min_ang),
        "min_joint": min_joint,
        "max_disp": max_displacement,
        "max_rot_deg": math.degrees(max_rotation),
        "first_motion": first_motion,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="0-11")
    parser.add_argument("--cap", type=int)
    args = parser.parse_args()
    if "-" in args.seeds:
        lo, hi = map(int, args.seeds.split("-"))
        seeds = range(lo, hi + 1)
    else:
        seeds = [int(x) for x in args.seeds.split(",")]
    rows = [run_seed(seed, args.cap) for seed in seeds]
    for r in rows:
        print(
            f"seed={r['seed']:3d} ok={int(r['ok'])} n={r['steps']:4d} "
            f"initB=({r['init_b'][0]:.3f},{r['init_b'][1]:.3f},{math.degrees(r['init_b'][2]):6.1f}) "
            f"R=({r['init_r'][0]:.3f},{r['init_r'][1]:.3f}) "
            f"G=({r['goal'][0]:.3f},{r['goal'][1]:.3f},{math.degrees(r['goal'][2]):6.1f}) "
            f"finalerr=({r['pos']:.3f},{r['ang_deg']:5.1f}deg) "
            f"min=({r['min_pos']:.3f},{r['min_ang_deg']:5.1f}deg,J={r['min_joint']:.2f}) "
            f"motion@={r['first_motion']} disp={r['max_disp']:.3f} rot={r['max_rot_deg']:.1f}"
        )
    successes = [r for r in rows if r["ok"]]
    print(f"SUMMARY success={len(successes)}/{len(rows)} mean_steps_success=" +
          (f"{np.mean([r['steps'] for r in successes]):.1f}" if successes else "NA"))


if __name__ == "__main__":
    main()
