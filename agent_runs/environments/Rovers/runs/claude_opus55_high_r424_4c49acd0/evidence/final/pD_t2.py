import sys
from multiprocessing import Pool
from pD_lib import *
def bis(job):
    S,t,side,th=job
    lo,hi=0.0,0.5  # lo blocked, hi free
    if trial((S,pos_on_line(S,t,side*hi,th))) is not True: return job,'hi not free'
    for _ in range(8):
        m=(lo+hi)/2; r=trial((S,pos_on_line(S,t,side*m,th)))
        if r is None: return job,('placefail',m)
        if r: hi=m
        else: lo=m
    return job,(round(lo,4),round(hi,4))
if __name__=='__main__':
    S=(0.4,-0.6,np.pi)
    jobs=[(S,t,sd,th) for t in [0.35,0.5,0.65,0.72] for sd in [1,-1] for th in [0.0,np.pi/4]]
    with Pool(8) as p:
        for j,r in p.imap(bis,jobs): print('t=%.2f side=%+d th=%.2f'%j[1:],r,flush=True)
