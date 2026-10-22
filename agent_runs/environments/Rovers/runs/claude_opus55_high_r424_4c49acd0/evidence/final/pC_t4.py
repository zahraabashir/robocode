from pC_lib import *
def d(i): return round(((g(f'rover{i}','x')+1.9)**2+(g(f'rover{i}','y')+2)**2)**.5,3)
reset(11)
sx,sy=g('sample0','x'),g('sample0','y')
goto(1,-1.5,-1.0); goto(1,sx,sy-0.2); step(s1='sample')
for p in [(-1.5,1.4),(-1.0,1.5),(-0.4,1.4),(-0.4,0.5)]:
    ok=goto(1,*p); step(s1='send'); print('r1',p,ok,d(1),SM(0)[6])
    if SM(0)[6]: break
# rover0
s3=(g('sample3','x'),g('sample3','y'))
goto(0,1.0,s3[1]); goto(0,s3[0]+0.2,s3[1]); step(s0='sample'); print(R(0),SM(3))
for p in [(0.877,-0.917),(0.5,-1.5),(0.35,-1.9),(0.35,-1.2),(0.35,0.0),(0.35,1.0)]:
    ok=goto(0,*p); step(s0='send'); print('r0',p,ok,R(0)[:2],d(0),SM(3)[6])
    if SM(3)[6]: break
