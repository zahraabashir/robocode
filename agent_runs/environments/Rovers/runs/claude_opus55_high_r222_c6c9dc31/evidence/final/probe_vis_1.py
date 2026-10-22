from probe_vis_util import *
for seed in [0,1]:
    r=R(seed); print('seed',seed); dump(r.obs)
    r.step(); print(r.last)
