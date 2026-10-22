import sys, json, numpy as np
from multiprocessing import Pool
import test_approach as T
import approach
params = json.loads(sys.argv[1]); a,b = int(sys.argv[2]), int(sys.argv[3])
def run(seed):
    for k,v in params.items(): setattr(approach.GeneratedApproach, k, v)
    return T.run(seed)
with Pool(10) as p: res = p.map(run, range(a,b))
print(params, "succ", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]), "maxt %.1f"%max(r[3] for r in res))
for r in res:
    if not r[1] or r[3]>20 or r[2]>250: print("  bad", r[0], r[2], "%.1f"%r[3], np.round(r[4],3))
