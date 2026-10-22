"""Independent black-box rotation probes for DynPushT2D (not policy code)."""
import math
import numpy as np

from env_client import make_env


def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi


def summarize(seed):
    env = make_env()
    s, _ = env.reset(seed=seed)
    print("RESET", seed,
          "block", np.round(s[[0, 1, 2]], 4),
          "robot", np.round(s[[16, 17]], 4),
          "goal", np.round(s[[29, 30, 31]], 4),
          "dims", np.round(s[[12, 13, 14, 28]], 4),
          "err", round(wrap(float(s[31] - s[2])), 4))
    env.close()


def move_to(env, s, target, nmax=200):
    for _ in range(nmax):
        d = np.asarray(target) - s[[16, 17]]
        if np.linalg.norm(d) < 0.012:
            break
        a = np.clip(d, -0.049, 0.049).astype(np.float32)
        s, _, done, trunc, _ = env.step(a)
        if done or trunc:
            break
    return s


def horizontal_scan(seed, yoff):
    env = make_env(); s, _ = env.reset(seed=seed)
    p0 = s[:3].copy(); bx, by = s[:2]
    # Route underneath/above the object before approaching from the left.
    safe_y = by + yoff
    s = move_to(env, s, [bx - 1.2, s[17]])
    s = move_to(env, s, [bx - 1.2, safe_y])
    first = None
    for k in range(38):
        s, _, done, trunc, _ = env.step(np.array([0.049, 0.0], dtype=np.float32))
        delta = np.linalg.norm(s[:2] - p0[:2])
        if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
            first = (k, float(s[16]), float(s[17]))
        if done or trunc: break
    print("HSCAN", yoff, "first", first, "dxy", np.round(s[:2]-p0[:2],4),
          "dth", round(wrap(float(s[2]-p0[2])),4), "robot", np.round(s[[16,17]],3))
    env.close()


def vertical_scan(seed, xoff):
    env = make_env(); s, _ = env.reset(seed=seed)
    p0 = s[:3].copy(); bx, by = s[:2]
    s = move_to(env, s, [s[16], by - 1.2])
    s = move_to(env, s, [bx + xoff, by - 1.2])
    first = None
    for k in range(38):
        s, _, done, trunc, _ = env.step(np.array([0.0, 0.049], dtype=np.float32))
        delta = np.linalg.norm(s[:2] - p0[:2])
        if first is None and (delta > 1e-4 or abs(wrap(float(s[2]-p0[2]))) > 1e-4):
            first = (k, float(s[16]), float(s[17]))
        if done or trunc: break
    print("VSCAN", xoff, "first", first, "dxy", np.round(s[:2]-p0[:2],4),
          "dth", round(wrap(float(s[2]-p0[2])),4), "robot", np.round(s[[16,17]],3))
    env.close()


def short_vertical(seed, xoff, direction, pushes):
    env = make_env(); s, _ = env.reset(seed=seed)
    bx, by = s[:2]
    start_y = by - 1.2 if direction > 0 else by + 1.2
    # Seed 11 starts well below the block; route around its left or right edge.
    route_x = bx - 1.0 if xoff < 0 else bx + 1.0
    s = move_to(env, s, [route_x, s[17]])
    s = move_to(env, s, [route_x, start_y])
    s = move_to(env, s, [bx + xoff, start_y])
    prep = s[:3].copy()
    contact = None
    after = 0
    for k in range(45):
        old = s[:3].copy()
        a = np.array([0.0, direction * 0.049], dtype=np.float32)
        s, _, done, trunc, _ = env.step(a)
        moved = np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5
        if contact is None and moved:
            contact = k
        if contact is not None:
            after += 1
            if after >= pushes: break
        if done or trunc: break
    print("SHORTV", "xoff", xoff, "dir", direction, "n", pushes,
          "prep", np.round(prep-[bx,by,s[2]*0 + prep[2]], 4),
          "contact", contact, "delta", np.round(s[:2]-prep[:2],4),
          "dth", round(wrap(float(s[2]-prep[2])),4),
          "vel", np.round(s[[3,4,5]],4))
    env.close()


def rot(theta, local):
    c, q = math.cos(theta), math.sin(theta)
    return np.array([c*local[0] - q*local[1], q*local[0] + c*local[1]])


def general_frame_trial(seed, xoff, pushes=4):
    env = make_env(); s, _ = env.reset(seed=seed)
    initial = s[:3].copy(); center = s[:2].copy(); theta = float(s[2])
    side = 1 if xoff > 0 else -1
    # Travel to the outer/below corner, then inward along local x, avoiding the T.
    s = move_to(env, s, center + rot(theta, [side*1.0, -1.15]))
    s = move_to(env, s, center + rot(theta, [xoff, -1.15]))
    prep = s[:3].copy()
    contact = None; moved_steps = 0
    for k in range(40):
        old = s[:3].copy()
        a = rot(theta, [0.0, 0.049]).astype(np.float32)
        s, _, done, trunc, _ = env.step(a)
        moved = np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5
        if contact is None and moved: contact = k
        if contact is not None:
            moved_steps += 1
            if moved_steps >= pushes: break
        if done or trunc: break
    world_dp = s[:2] - prep[:2]
    local_dp = rot(-theta, world_dp)
    print("FRAME", seed, "theta", round(theta,3), "xoff", xoff,
          "setup", np.round(prep[:2]-initial[:2],3), round(wrap(float(prep[2]-initial[2])),3),
          "contact", contact, "local_dp", np.round(local_dp,3),
          "dth", round(wrap(float(s[2]-prep[2])),3))
    env.close()


def push_until_moved(env, s, action, count=4):
    got = 0
    for _ in range(45):
        old = s[:3].copy()
        s, _, done, trunc, _ = env.step(np.asarray(action, dtype=np.float32))
        if np.linalg.norm(s[:2]-old[:2]) > 2e-5 or abs(wrap(float(s[2]-old[2]))) > 2e-5:
            got += 1
            if got >= count: break
        if done or trunc: break
    return s


def paired_torque(seed=11, sign=1):
    env = make_env(); s, _ = env.reset(seed=seed); initial = s[:3].copy()
    # For positive torque: right underside upward, then left topside downward.
    first_x = 0.5 * sign
    outer_x = 1.0 * sign
    second_x = -first_x
    b, th = s[:2].copy(), float(s[2])
    s = move_to(env, s, [b[0]+outer_x, s[17]])
    s = move_to(env, s, b + rot(th, [outer_x, -1.2]))
    s = move_to(env, s, b + rot(th, [first_x, -1.2]))
    s = push_until_moved(env, s, rot(th, [0, 0.049]), 4)
    middle = s[:3].copy()
    # Retreat and go around the outside to left topside; push down for same torque.
    b, th = s[:2].copy(), float(s[2])
    s = move_to(env, s, s[[16,17]] + rot(th, [0, -0.55]))
    s = move_to(env, s, b + rot(th, [outer_x, -1.2]))
    s = move_to(env, s, b + rot(th, [outer_x, 1.2]))
    s = move_to(env, s, b + rot(th, [second_x, 1.2]))
    s = push_until_moved(env, s, rot(th, [0, -0.049]), 4)
    final = s[:3].copy()
    print("PAIR", sign, "first", np.round(middle[:2]-initial[:2],3),
          round(wrap(float(middle[2]-initial[2])),3),
          "net", np.round(final[:2]-initial[:2],3),
          round(wrap(float(final[2]-initial[2])),3))
    env.close()


def main():
    paired_torque(sign=1)
    paired_torque(sign=-1)


if __name__ == "__main__":
    main()
