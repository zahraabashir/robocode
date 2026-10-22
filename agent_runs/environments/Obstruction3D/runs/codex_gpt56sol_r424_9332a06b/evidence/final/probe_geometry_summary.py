from collections import Counter
from env_client import make_env


def xyzhe(state, name):
    o = state.get_object_from_name(name)
    fs = ["pose_x", "pose_y", "pose_z", "half_extent_x", "half_extent_y", "half_extent_z"]
    return [float(state.get(o, f)) for f in fs]


def rng_update(ranges, key, vals):
    if key not in ranges:
        ranges[key] = [[x, x] for x in vals]
    for r, x in zip(ranges[key], vals):
        r[0] = min(r[0], x)
        r[1] = max(r[1], x)


env = make_env()
counts = Counter()
ranges = {}
on_region = 0
off_region = 0
overlaps = []
for seed in range(100):
    state, info = env.reset(seed=seed)
    names = state.get_object_names()
    obs = sorted(n for n in names if n.startswith("obstruction"))
    counts[len(obs)] += 1
    reg = xyzhe(state, "target_region")
    block = xyzhe(state, "target_block")
    rng_update(ranges, "region", reg)
    rng_update(ranges, "block", block)
    for name in obs:
        v = xyzhe(state, name)
        rng_update(ranges, "obstruction", v)
        dx, dy = abs(v[0]-reg[0]), abs(v[1]-reg[1])
        hit = dx < v[3]+reg[3] and dy < v[4]+reg[4]
        if hit: on_region += 1
        else: off_region += 1
        overlaps.append((dx, dy, dx-(v[3]+reg[3]), dy-(v[4]+reg[4])))
print("counts", counts)
print("ranges [x,y,z,hx,hy,hz]", ranges)
print("obstruction overlaps/off", on_region, off_region)
print("separation delta extrema", [[min(v[i] for v in overlaps), max(v[i] for v in overlaps)] for i in range(4)])

for count in [0, 1, 2, 3, 5, 10]:
    try:
        state, info = env.reset(seed=123, options={"object_count": count})
        actual = sum(n.startswith("obstruction") for n in state.get_object_names())
        print("forced", count, "actual", actual, "info", info)
    except Exception as e:
        print("forced", count, "ERR", repr(e))
env.close()
