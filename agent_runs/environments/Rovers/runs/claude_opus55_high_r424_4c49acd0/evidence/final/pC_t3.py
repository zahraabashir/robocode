from pC_lib import *
reset(11)
sx,sy=g('sample0','x'),g('sample0','y')
goto(1,-1.5,-1.0); goto(1,sx,sy-0.2); step(s1='sample'); print(R(1),SM(0))
# send attempts from current then moving toward lander
step(s1='send'); print('send far',R(1),SM(0))
for y in [-0.5,-1.0,-1.2,-1.4,-1.5,-1.6,-1.7,-1.8]:
    ok=goto(1,-1.9,y); step(s1='send'); r=SM(0); print(y,ok,R(1),r, 'dist',round(((g('rover1','x')+1.9)**2+(g('rover1','y')+2)**2)**.5,3))
    if r[6]: break
print('store after send',R(1))
