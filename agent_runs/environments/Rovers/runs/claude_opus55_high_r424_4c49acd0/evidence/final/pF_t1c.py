from pF_lib import *
s=Sim(28); px,py=0.9779,-0.9694; i=0
d,p=approach(s,i,px,py,0,-1); print('contact',round(d,5))
print('rot +0.05 alone ok? then undo'); print(step(s,i,0,0,0.05).round(4)); print(step(s,i,0,0,-0.05).round(4))
print('blocked translate (0,+0.02) + rot 0.05 ->',step(s,i,0,0.02,0.05).round(4))
print('free translate (0,-0.02) + rot 0.05 ->',step(s,i,0,-0.02,0.05).round(4))
