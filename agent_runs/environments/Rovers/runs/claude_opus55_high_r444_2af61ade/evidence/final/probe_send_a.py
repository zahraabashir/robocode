from probe_send_lib import *
e=E(0)
print(e.pose(1)); e.act(1,(0.1,0,0)); print('dx+0.1 at th0',e.pose(1))
e.act(1,(0,0,0.4)); e.act(1,(0.1,0,0)); print('dx+0.1 at th0.4',e.pose(1))
print(e.last)
