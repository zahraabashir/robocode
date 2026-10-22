from probe_ops_lib import *
def run(two_soil, two_rock=True):
    reset(1)
    goto(1,-1.27,-1.37); step(1,op='sample'); step(1,op='send'); step(1,op='drop')
    goto(1,-1.7,-1.2); goto(1,-1.7,0.17)
    if two_soil:
        goto(1,-1.92,0.17); step(1,op='sample'); step(1,op='send'); step(1,op='drop')
    goto(1,-1.92,0.17); step(1,op='calibrate'); step(1,op='image'); step(1,op='send')
    goto(1,-1.7,-1.2); goto(1,-1.0,-1.2); goto(1,-1.0,-1.75,tol=0.001)
    goto(0,0.77,-1.35); step(0,op='sample'); step(0,op='send'); step(0,op='drop')
    if two_rock:
        goto(0,1.0,-0.5); goto(0,2.0,0.5); goto(0,2.3,1.17); step(0,op='sample')
    else: goto(0,1.0,-0.5); goto(0,2.0,0.5); goto(0,2.3,1.17)
    step(0,op='calibrate'); step(0,op='image')
    goto(0,2.0,0.5); goto(0,1.0,-0.5); step(0,op='send'); step(0,op='drop')
    goto(0,1.0,-1.75,tol=0.001); r,term,tr=step(0)
    print('two_soil',two_soil,'two_rock',two_rock,'term',term,'n',S.n)
    print(' ',dump('objective')); print(' ',dump('sample')); print(' ',dump('rover'))
run(True); run(False); run(True,False)
