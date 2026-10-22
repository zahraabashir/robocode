from collections import Counter
from env_client import make_env

counts = Counter()
ranges = {}
assignments = Counter()
for seed in range(40):
    env = make_env()
    s, info = env.reset(seed=seed)
    counts[info["object_count"]] += 1
    ots = {str(t): t for t in env.observation_space.types}
    # Some implementations stringify types as their bare names.
    for typ in env.observation_space.types:
        name = getattr(typ, "name", str(typ))
        for o in s.get_objects(typ):
            for feat in env.observation_space.type_features[typ]:
                v = float(s.get(o, feat))
                key = (name, feat)
                if key not in ranges:
                    ranges[key] = [v, v]
                else:
                    ranges[key][0] = min(ranges[key][0], v)
                    ranges[key][1] = max(ranges[key][1], v)
            if name == "objective":
                x, y = float(s.get(o, "x")), float(s.get(o, "y"))
                center = min(((2,2),(-2,2),(.5,2),(-.5,2)), key=lambda p:(x-p[0])**2+(y-p[1])**2)
                assignments[center] += 1
    env.close()
print("counts", counts)
print("objective mound assignments", assignments)
for k in sorted(ranges):
    if k[1] in ("x", "y", "z", "half_x", "half_y", "half_z", "theta"):
        print(k, tuple(round(v,4) for v in ranges[k]))
