from pm_util import *
e=E()
for s in range(200):
    o=e.reset(s)
    d=np.linalg.norm(o[0:2]-2.5)
    if d<0.4: print(s,o[0:3],o[12:15],o[16:18])
