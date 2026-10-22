"""Small black-box probes for DynPushT2D.  Not used by the submitted policy."""
import argparse
import math
import numpy as np

from env_client import make_env


def brief(seed):
    env = make_env()
    obs, _ = env.reset(seed=seed)
    print(seed, "max", env.max_steps,
          "block", np.round(obs[[0, 1, 2]], 5),
          "robot", np.round(obs[[16, 17]], 5),
          "goal", np.round(obs[[29, 30, 31]], 5),
          "dims", np.round(obs[[12, 13, 14, 15, 28]], 5))
    env.close()


def go(env, obs, target, speed=0.05, max_steps=100):
    """Move toward a point and return state plus trajectory samples."""
    out = []
    for _ in range(max_steps):
        delta = np.asarray(target, float) - obs[16:18]
        if np.linalg.norm(delta) < 1e-4:
            break
        norm = np.linalg.norm(delta)
        act = delta if norm <= speed else delta * (speed / norm)
        before = obs.copy()
        obs, _, term, trunc, _ = env.step(act)
        out.append((before, act.copy(), obs.copy()))
        if term or trunc:
            break
    return obs, out


def free_motion(seed, action, n=30):
    env = make_env()
    obs, _ = env.reset(seed=seed)
    initial = obs.copy()
    print("initial block/robot", initial[:3], initial[16:18])
    for i in range(n):
        prev = obs.copy()
        obs, _, term, trunc, _ = env.step(np.asarray(action, float))
        if i < 5 or i == n - 1:
            print(i + 1, "r", np.round(obs[16:22], 5), "b", np.round(obs[:6], 5),
                  "dr", np.round(obs[16:18] - prev[16:18], 5))
        if term or trunc:
            break
    env.close()


def ray(seed, angle, start_dist=0.45, end_dist=-0.05, speed=0.005):
    """Approach block center along world-space radial ray; report first response."""
    env = make_env()
    obs, _ = env.reset(seed=seed)
    c0 = obs[:2].copy()
    theta = obs[2]
    d = np.array([math.cos(angle), math.sin(angle)])
    start = c0 + d * start_dist
    # First place robot.  Record contamination from accidental collisions.
    obs, placement = go(env, obs, start, speed=0.025, max_steps=100)
    contaminated = np.linalg.norm(obs[:2] - c0) > 1e-5 or abs(obs[2] - theta) > 1e-5
    first = None
    samples = []
    target = c0 + d * end_dist
    for k in range(160):
        prev = obs.copy()
        delta = target - obs[16:18]
        norm = np.linalg.norm(delta)
        act = delta if norm <= speed else delta * (speed / norm)
        obs, _, term, trunc, _ = env.step(act)
        change = np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2])
        if change > 1e-7 and first is None:
            first = (k, prev.copy(), obs.copy())
        if first is not None and len(samples) < 4:
            samples.append(obs.copy())
        if np.linalg.norm(obs[16:18] - target) < 1e-4 or term or trunc:
            break
    label = f"seed={seed} worldang={angle:.3f} localang={(angle-theta):.3f} contam={contaminated}"
    if first is None:
        print(label, "NO CONTACT", "final r", np.round(obs[16:18], 4))
    else:
        k, before, after = first
        rel = before[16:18] - before[:2]
        local = np.array([[math.cos(-before[2]), -math.sin(-before[2])],
                          [math.sin(-before[2]), math.cos(-before[2])]]) @ rel
        print(label, "contactstep", k,
              "world_rel", np.round(rel, 5), "local_rel", np.round(local, 5),
              "center_dist", round(float(np.linalg.norm(rel)), 5),
              "block_delta", np.round(after[:3] - before[:3], 6))
        if samples:
            print("  after", [(np.round(x[:3], 4).tolist(), np.round(x[16:18], 4).tolist()) for x in samples])
    env.close()


def natural(seed, speed=0.005):
    """Approach directly from the reset robot location (no placement artifacts)."""
    env = make_env()
    obs, _ = env.reset(seed=seed)
    initial = obs.copy()
    first = None
    for k in range(1000):
        prev = obs.copy()
        delta = obs[:2] - obs[16:18]
        norm = np.linalg.norm(delta)
        act = delta if norm <= speed else delta * (speed / norm)
        obs, _, term, trunc, _ = env.step(act)
        change = np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2])
        if change > 1e-7:
            first = (k, prev.copy(), obs.copy())
            break
        if term or trunc:
            break
    if first is None:
        print(seed, "NO CONTACT")
    else:
        k, before, after = first
        rel = before[16:18] - before[:2]
        ct, st = math.cos(-before[2]), math.sin(-before[2])
        local = np.array([[ct, -st], [st, ct]]) @ rel
        a = math.atan2(local[1], local[0])
        print(seed, "theta", round(float(initial[2]), 4), "local_ray", round(a, 4),
              "contact_local", np.round(local, 5), "dist", round(float(np.linalg.norm(local)), 5),
              "dblock", np.round(after[:3] - before[:3], 7))
    env.close()


def push_response(seed, approach_speed=0.015, push_speed=0.01, pushes=20):
    """Approach along the reset-to-center line, then maintain that push direction."""
    env = make_env()
    obs, _ = env.reset(seed=seed)
    initial = obs.copy()
    direction = initial[:2] - initial[16:18]
    direction /= np.linalg.norm(direction)
    contact = None
    for k in range(400):
        prev = obs.copy()
        obs, _, term, trunc, _ = env.step(direction * approach_speed)
        if np.linalg.norm(obs[:2] - prev[:2]) + abs(obs[2] - prev[2]) > 1e-7:
            contact = prev.copy()
            break
        if term or trunc:
            break
    if contact is None:
        print("push", seed, "NO CONTACT")
        env.close()
        return
    at_contact = obs.copy()
    for _ in range(pushes):
        obs, _, term, trunc, _ = env.step(direction * push_speed)
        if term or trunc:
            break
    rel = contact[16:18] - contact[:2]
    ct, st = math.cos(-contact[2]), math.sin(-contact[2])
    local = np.array([[ct, -st], [st, ct]]) @ rel
    db = obs[:3] - at_contact[:3]
    print("push", seed, "local_contact", np.round(local, 4),
          "20step block", np.round(db, 5), "robot", np.round(obs[16:18] - at_contact[16:18], 5),
          "per_action_xy", round(float(np.linalg.norm(db[:2])) / pushes, 5),
          "rot_per_action", round(float(db[2]) / pushes, 5))
    env.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["brief", "free", "rays", "natural", "push"])
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    if args.mode == "brief":
        for s in range(12):
            brief(s)
    elif args.mode == "free":
        free_motion(args.seed, [0.05, 0.0])
    elif args.mode == "rays":
        env = make_env(); o, _ = env.reset(seed=args.seed); th = float(o[2]); env.close()
        for local_angle in np.linspace(0, 2 * math.pi, 12, endpoint=False):
            ray(args.seed, th + local_angle)
    elif args.mode == "natural":
        for s in range(40):
            natural(s)
    else:
        for s in range(12):
            push_response(s)
