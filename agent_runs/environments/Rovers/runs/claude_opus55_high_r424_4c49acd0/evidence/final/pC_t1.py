from pC_lib import *
reset(11)
print(SM(3))
goto(0,1.0,-0.917)
for d in [0.35,0.3,0.28,0.26,0.255,0.25,0.245,0.24,0.2,0.15]:
    goto(0,0.677+d,-0.917)
    step(s0='sample'); print(d,R(0),SM(3))
    if R(0)[3]: break
