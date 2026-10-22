from pE_lib import *
import sys
def approach(seed,i,px,py,side):
    s=Sim(seed)
    # start below pillar at y=py-0.6
    if side=='below': start=(px,py-0.6); d=(0,0.01)
    else: start=(px+(0.6 if i==0 else -0.6) ,py); d=((-0.01 if i==0 else 0.01),0)
    if not drive(s,i,*start): return 'noreach'
    for k in range(80):
        p=s.r(i); a=(d[0],d[1],0,'noop')
        if i==0: s.act(a0=a)
        else: s.act(a1=a)
        if s.r(i)==p: break
    c=s.r(i); return (round(c['x']-px,3),round(c['y']-py,3))
for seed,i,px,py in eval(sys.argv[1]):
    print(seed,i,(px,py),approach(seed,i,px,py,'below'),approach(seed,i,px,py,'side'))
