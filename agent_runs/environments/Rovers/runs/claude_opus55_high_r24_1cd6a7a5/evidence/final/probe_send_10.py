exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
X=0.5; base=L+d*((X-L[0])/d[0])
for th in [0.0, math.pi/2]:
    def setup(): goto(1,-1.0,0.3); turn_to(0,th)
    for sgn in [1,-1]:
        pts=[tuple(base+n*s*sgn) for s in np.arange(0.0,0.3,0.003)]
        r=scan(P,pts,setup); print(th,sgn,r,'theta',round(pos(0)[2],2))
