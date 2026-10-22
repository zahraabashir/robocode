from probe_occ_lib import *
from probe_send_lib import diff
e,err=setup(44,(0.6,-0.35),math.pi,(-0.5,0.0),0.0)
print(err,e.feats('rover0'))
a=e.flags()
e.step((0,0,0,SEL['send']),(0,0,0,0))
print(diff(a,e.flags()), e.last[0], e.last[3])
