from collections import Counter
from env_client import make_env


def box(s, n):
    o = s.get_object_from_name(n)
    return tuple(float(s.get(o, f)) for f in
                 ("pose_x", "pose_y", "half_extent_x", "half_extent_y"))


def signed_axis_gaps(a, b):
    return abs(a[0]-b[0])-a[2]-b[2], abs(a[1]-b[1])-a[3]-b[3]


env = make_env()
ncounts = Counter()
br = []
bo = []
rratios = []
for seed in range(300):
    s, info = env.reset(seed=1000+seed)
    reg, blk = box(s, "target_region"), box(s, "target_block")
    ncounts[info["object_count"]] += 1
    br.append(signed_axis_gaps(reg, blk))
    rratios.append((blk[2]/reg[2], blk[3]/reg[3]))
    for n in s.get_object_names():
        if n.startswith("obstruction"):
            bo.append(signed_axis_gaps(blk, box(s, n)))
print("counts", ncounts)
print("block/region axis gap minima", min(x[0] for x in br), min(x[1] for x in br))
print("block/region overlap both", sum(x < 0 and y < 0 for x, y in br))
print("block/obstruction axis gap minima", min(x[0] for x in bo), min(x[1] for x in bo))
print("block/obstruction overlap both", sum(x < 0 and y < 0 for x, y in bo))
print("extent ratios", min(x for x,y in rratios), max(x for x,y in rratios), min(y for x,y in rratios), max(y for x,y in rratios))
env.close()
