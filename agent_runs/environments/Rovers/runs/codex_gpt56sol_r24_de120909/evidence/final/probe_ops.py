from env_client import make_env
import numpy as np


def snap(state):
    out = {}
    for name in state.get_object_names():
        obj = state.get_object_from_name(name)
        feats = {}
        # Public type metadata is awkward to recover from obj, so query known fields.
        for f in ("x", "y", "z", "theta", "store_full", "calibrated", "at_home",
                  "is_soil", "analyzed_rover0", "analyzed_rover1", "received_analysis",
                  "have_image_rover0", "have_image_rover1", "received_image",
                  "half_x", "half_y", "half_z"):
            try:
                feats[f] = float(state.get(obj, f))
            except Exception:
                pass
        out[name] = feats
    return out


def main():
    env = make_env()
    s, info = env.reset(seed=0)
    print("max_steps", env.max_steps, "action", env.action_space.shape,
          env.action_space.low.tolist(), env.action_space.high.tolist(), env.action_space.dtype)
    print("types", env.observation_space.types)
    print("features", env.observation_space.type_features)
    print("names", s.get_object_names())
    for k, v in snap(s).items():
        print(k, v)
    print("info", info)
    env.close()


def rover_values(s, i=0):
    r = s.get_object_from_name("rover%d" % i)
    return tuple(float(s.get(r, f)) for f in
                 ("x", "y", "theta", "store_full", "calibrated", "at_home"))


def move_to(env, s, xy, rover=0, selector=0.0):
    for _ in range(100):
        vals = rover_values(s, rover)
        dx = max(-0.2, min(0.2, xy[0] - vals[0]))
        dy = max(-0.2, min(0.2, xy[1] - vals[1]))
        if abs(dx) < 1e-5 and abs(dy) < 1e-5:
            return s
        a = np.zeros(8, dtype=np.float32)
        off = rover * 4
        a[off:off + 4] = (dx, dy, 0.0, selector)
        s, _, term, trunc, _ = env.step(a)
        if term or trunc:
            return s
    return s


def sample_trial(selector, pre_offset=0.20, motion=0.0, rover=1, side=-1):
    env = make_env()
    s, _ = env.reset(seed=0)
    sample = s.get_object_from_name("sample4")
    sx, sy = float(s.get(sample, "x")), float(s.get(sample, "y"))
    # Approach from east through clear southern region.
    s = move_to(env, s, (sx + side * pre_offset, sy), rover=rover)
    before = rover_values(s, rover)
    a = np.zeros(8, np.float32)
    off = rover * 4
    a[off:off + 4] = (-side * motion, 0, 0, selector)
    s, rew, term, trunc, _ = env.step(a)
    after = rover_values(s, rover)
    analyzed = float(s.get(sample, "analyzed_rover%d" % rover))
    env.close()
    return before, after, analyzed, rew, term, trunc


def trials():
    print("SAMPLE SELECTORS")
    for sel in (-1.0, -0.999, -2/3 - 1e-4, -2/3, -2/3 + 1e-4,
                -0.5, -1/3, 0.0, 1/3, 2/3, 1.0):
        print(sel, sample_trial(sel))
    print("SAMPLE DISTANCE / MOTION ORDER")
    for off, motion in ((0.249, 0), (0.251, 0), (0.26, .02), (.24, -.02)):
        print(off, motion, sample_trial(-5/6, off, motion))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        trials()
    else:
        main()
