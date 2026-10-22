from pF_lib import *
s=Sim(28); px,py=0.978,-0.969; i=0
print('start',pose(s,i))
d,p=approach(s,i,px,py,0,-1); print('contact from below',d,p)
# translation into pillar + rotation
q=step(s,i,0,0.05,0.3); print('blocked move+rot ->',q)
# pure rotation near pillar
for k in range(8):
    q=step(s,i,0,0,0.4); print('pure rot ->',q.round(4))
