"""Targeted probes for hidden wall, collision radius, home and camera semantics."""
from env_client import make_env
import numpy as np


def rover_data(s, e, idx=0):
    t = e.observation_space.get_type("rover")
    o = sorted(s.get_objects(t), key=lambda q: q.name)[idx]
    return o, tuple(float(s.get(o, f)) for f in ("x", "y", "theta", "store_full", "calibrated", "at_home"))


def act(e, a0=(0, 0, 0, 0), a1=(0, 0, 0, 0)):
    a = np.asarray(a0 + a1, dtype=np.float32)
    return e.step(a)[0]


def move_axis(e, s, idx, axis, target, maxn=100):
    for _ in range(maxn):
        _, d = rover_data(s, e, idx)
        cur = d[axis]
        delta = max(-0.2, min(0.2, target-cur))
        if abs(delta) < 1e-5:
            break
        aa = [0., 0., 0., 0.]
        aa[axis] = delta
        s2 = act(e, tuple(aa), (0,0,0,0)) if idx == 0 else act(e, (0,0,0,0), tuple(aa))
        _, d2 = rover_data(s2, e, idx)
        s = s2
        if abs(d2[axis]-cur) < 1e-6:
            break
    return s


def wall_probe(seed, y):
    e = make_env(); s,_=e.reset(seed=seed)
    s=move_axis(e,s,0,1,y)
    s=move_axis(e,s,0,0,-1.0)
    print("WALL",seed,y,rover_data(s,e,0)[1])
    e.close()


def main():
    for y in (-2.3,-1.75,-1.0,0.0,1.0,1.5,1.8,2.3):
        wall_probe(20,y)

    # Boundary: choose mostly clear bottom/right edges.
    e=make_env(); s,_=e.reset(seed=30)
    s=move_axis(e,s,0,0,3.0); print("BOUND X",rover_data(s,e,0)[1])
    e.close()

    # Home status along x and y offsets.
    for dx,dy in ((.05,0),(.1,0),(.15,0),(.2,0),(0,.05),(0,.1),(0,.15),(0,.2)):
        e=make_env(); s,_=e.reset(seed=31)
        s=act(e,(dx,dy,0,0)); print("HOME",dx,dy,rover_data(s,e,0)[1]); e.close()

    # Camera at a clear standoff below seed 0's right-center mound/objective.
    # Route on right half, theta remains pi and objective lies roughly north.
    for heading_delta in (0.0, -1.57, 1.57, 3.14):
        e=make_env(); s,_=e.reset(seed=0)
        s=move_axis(e,s,0,0,1.0); s=move_axis(e,s,0,1,1.15)
        # Apply requested heading change in <=.4 increments.
        remain=heading_delta
        while abs(remain)>1e-4:
            q=max(-.4,min(.4,remain)); s=act(e,(0,0,q,0)); remain-=q
        s=act(e,(0,0,0,-.5))
        print("CAL",heading_delta,rover_data(s,e,0)[1])
        e.close()


if __name__ == "__main__":
    main()
