from pF_lib import *
s=Sim(28); px,py=0.978,-0.969; i=0
print('free rot', step(s,i,0,0,0.1).round(4), step(s,i,0,0,-0.1).round(4))
d,p=approach(s,i,px,py,0,-1); print('contact',d)
for dth in (0.01,-0.01,0.05,-0.05):
    print('rot',dth,step(s,i,0,0,dth).round(4))
for back in (0.01,0.02,0.04,0.08):
    go(s,i,px,py-d-back)
    r=[step(s,i,0,0,dth)[2] for dth in (0.1,)]
    print('back',back,'rot+0.1 ->',round(r[0],4)); go(s,i,px,py-d-back,np.pi)
