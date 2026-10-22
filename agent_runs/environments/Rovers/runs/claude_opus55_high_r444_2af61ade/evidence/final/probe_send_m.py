from probe_send_lib import *
e=E(1)
for r in [0.2,0.21,0.22,0.23,0.24,0.25]:
    e.goto(1,-1.0+r,-1.75); a=e.g('rover1','at_home')
    e.goto(1,-1.0+r/np.sqrt(2),-1.75+r/np.sqrt(2)); b=e.g('rover1','at_home')
    print('r',r,'axis',a,'diag',b)
e.goto(1,-1.0,-1.75)
for th in [0.35,0.4,0.45,0.5,0.55,-0.5,-0.55]:
    e.turn(1,th); print('th',th,e.g('rover1','at_home'))
