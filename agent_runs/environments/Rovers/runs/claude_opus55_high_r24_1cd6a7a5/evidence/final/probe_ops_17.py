from probe_ops_lib import *
import sys
def run(do_rock, do_drop):
    reset(14)
    for wp in [(-1.0,-1.2),(-1.5,-1.2),(-1.47,-0.65)]: goto(1,*wp)
    step(1,op='sample'); goto(1,-1.5,-1.2); step(1,op='send')
    if do_drop: step(1,op='drop')
    goto(1,-1.0,-1.75,tol=0.001)
    for wp in [(1.0,0.0),(1.3,1.2),(1.78,1.45)]: goto(0,*wp)
    if do_rock: step(0,op='sample')
    step(0,op='calibrate'); step(0,op='image')
    for wp in [(1.3,1.2),(1.0,0.0),(1.0,-0.5)]: goto(0,*wp)
    step(0,op='send'); step(0,op='drop')
    goto(0,1.0,-1.75,tol=0.001); r,term,tr=step(0); print('rock',do_rock,'drop',do_drop,'term',term,'store1',pos(1)[3])
    if not term and not do_drop:
        r,term,tr=step(1,op='drop'); print(' after r1 drop term',term)
run(False,True); run(True,False)
