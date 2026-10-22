from pm_util import *
e=E()
for s in range(6):
    o=e.reset(s); print(s,o[0:3],o[12:15],o[16:18],o[28],o[29:32],o[41:44])
o=e.reset(0); print(o)
