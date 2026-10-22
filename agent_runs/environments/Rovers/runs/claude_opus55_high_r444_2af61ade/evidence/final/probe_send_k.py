from probe_send_lib import *
e=E(1)
# at_home tolerance
for dx in [0.01,0.05,0.1,0.15,0.2,0.25,0.3]:
    e.goto(1,-1.0+dx,-1.75); print('dx',dx,'at_home',e.g('rover1','at_home'))
e.goto(1,-1.0,-1.75)
for dy in [0.05,0.1,0.15,0.2,0.3]:
    e.goto(1,-1.0,-1.75+dy); print('dy',dy,'at_home',e.g('rover1','at_home'))
e.goto(1,-1.0,-1.75)
for th in [0.1,0.3,0.6,1.0,1.57,3.14]:
    e.turn(1,th); print('th',th,'at_home',e.g('rover1','at_home'))
e.turn(1,0.0); print('back',e.pose(1),e.g('rover1','at_home'))
