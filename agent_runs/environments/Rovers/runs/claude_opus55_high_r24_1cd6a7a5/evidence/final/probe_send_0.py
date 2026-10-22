from probe_ops_lib import *
reset(21)
for t in ['sample','lander','obstacle','rover','objective']: print(t, dump(t))
