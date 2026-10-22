from probe_send_lib import *
e=E(0)
p=plan(e,1,(-1.25,2.25)); print(p is None, p and len(p))
p=plan(e,1,(-1.25,1.0)); print(p is None, p and len(p))
