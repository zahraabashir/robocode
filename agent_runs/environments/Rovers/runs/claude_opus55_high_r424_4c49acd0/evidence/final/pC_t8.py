from pC_lib import *
import numpy as np
def img():
    goto(1,-1.5,-1.0); goto(1,-2.0,1.0,np.pi/2); step(s1='calibrate'); step(s1='image'); step(s1='send')
def rock():
    sx,sy=g('sample0','x'),g('sample0','y'); goto(1,sx,sy); step(s1='sample'); step(s1='send'); step(s1='drop')
def soil():
    goto(1,-1.0,-1.0)
    sx,sy=g('sample3','x'),g('sample3','y'); goto(0,1.0,sy); goto(0,sx,sy); step(s0='sample'); step(s0='send'); step(s0='drop'); goto(0,1.0,-0.9); goto(0,1.0,-1.75,np.pi)
def home1():
    goto(1,-1.5,-1.0); goto(1,-1.0,-1.75,0.0); step()
for name,seq in [('img only',[img]),('img+rock',[img,rock]),('img+soil',[img,soil])]:
    reset(11)
    for f in seq: f()
    home1(); print(name,S.te,S.n,R(0),R(1))
reset(11); img(); rock(); soil(); goto(1,-1.5,-1.0); goto(1,-1.0,-1.70,0.0); step(); print('home off by .05',S.te,R(1))
goto(1,-1.0,-1.75,0.5); step(); print('theta .5',S.te,R(1))
goto(1,-1.0,-1.75,0.0); step(); print('exact',S.te,R(1))
