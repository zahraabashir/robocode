from probe_send_lib import *
reset(21)
goto(0,0.62,-0.82); step(0,op='sample')
goto(0,1.0,-1.75); step(0,op='send'); print('r1 home', dump('sample')['sample3'][-1])
goto(1,-1.0,-1.0); print(pos(1)[:2]); goto(0,1.0,-1.75); step(0,op='send'); print('r1 moved', dump('sample')['sample3'][-1])
