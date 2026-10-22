exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
def away(): goto(1,-1.0,0.3)
for X in [0.4,0.6]:
    base=L+d*((X-L[0])/d[0])
    for sgn in [1,-1]:
        pts=[tuple(base+n*s*sgn) for s in np.arange(0.0,0.4,0.004)]
        print(X,sgn,'start',np.round(pts[0],3),scan(P,pts,away), np.round(pos(0)[:2],3))
# also pillar obstacle9 (-1.24,-0.79) and obstacle11 (-1.49,-1.03)
for P in [np.array([-1.24,-0.79]),np.array([-1.49,-1.03])]:
    d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
    base=L+d*((0.5-L[0])/d[0])
    pts=[tuple(base+n*s) for s in np.arange(0.0,0.4,0.004)]
    print(P,'start',np.round(pts[0],3),scan(P,pts,away), np.round(pos(0)[:2],3))
