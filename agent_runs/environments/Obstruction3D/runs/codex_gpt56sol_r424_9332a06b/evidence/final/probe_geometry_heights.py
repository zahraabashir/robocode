from collections import Counter
from env_client import make_env

env = make_env()
c = Counter()
samples = []
for seed in range(300):
    s, _ = env.reset(seed=seed)
    for n in s.get_object_names():
        if not n.startswith("obstruction"):
            continue
        o = s.get_object_from_name(n)
        bottom = float(s.get(o, "pose_z") - s.get(o, "half_extent_z"))
        r = s.get_object_from_name("target_region")
        dx = abs(float(s.get(o,"pose_x") - s.get(r,"pose_x")))
        dy = abs(float(s.get(o,"pose_y") - s.get(r,"pose_y")))
        kind = round(bottom, 3)
        c[kind] += 1
        if len(samples) < 10 and kind == .075:
            samples.append((seed,n,bottom,dx,dy))
print(c)
print("table samples", samples)
env.close()
