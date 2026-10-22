import sys
from multiprocessing import Pool
from pD_t2 import bis
from pD_lib import *
if __name__=='__main__':
    S=(0.4,-0.6,np.pi)
    jobs=[(S,t,sd,th) for t in [0.45,0.65] for sd in [1,-1] for th in np.arange(8)*np.pi/8]
    with Pool(16) as p:
        for j,r in p.imap(bis,jobs): print('t=%.2f side=%+d th=%.2f'%j[1:],r,flush=True)
