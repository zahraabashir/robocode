import sys, json
from multiprocessing import Pool
from pD_lib import *
def f(j):
    S,t,off,th=j
    try: return j[1:],trial((S,pos_on_line(S,t,off,th)))
    except Exception as e: return j[1:],'E'
if __name__=='__main__':
    S=(0.4,-0.6,np.pi); th=float(sys.argv[1])
    ts=np.round(np.arange(0.30,0.75,0.02),3); offs=np.round(np.arange(-0.25,0.251,0.025),3)
    jobs=[(S,float(t),float(o),th) for t in ts for o in offs]
    with Pool(24) as p: res=p.map(f,jobs)
    d={(r[0][0],r[0][1]):r[1] for r in res}
    print('th',th,' offs:',' '.join('%+.2f'%o for o in offs))
    for t in ts:
        print('t=%.2f '%t+''.join({True:'.',False:'#',None:'?','E':'E'}[d[(float(t),float(o))]] for o in offs))
