from probe_send_lib import *
e=E(3)
for i in range(1005):
    r=e.act(1,(0,0,0),0.0)
    if r[1] or r[2] or i>=997: print(e.t,r)
    if r[1] or r[2]: break
