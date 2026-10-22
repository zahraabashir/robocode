from pE_lib import *
for seed in (6,19,12,8):
    s=Sim(seed); o=s.obs
    print(seed,[ (n,[round(float(o.get(o.get_object_from_name(n),f)),3) for f in ['z','half_z']]) for n in sorted(o.get_object_names()) if str(n).startswith('obstacle') or str(n).startswith('objective')][:20])
