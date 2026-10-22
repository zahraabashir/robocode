from probe_samp_util import *
for s in [0,1,2,3]:
    D=Driver(s); print('seed',s, D.info); dump(D.obs)
