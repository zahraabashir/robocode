exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L)
X=0.5; base=L+d*((X-L[0])/d[0])
for th in [math.pi, -math.pi/2, math.pi*0.75, 0.0, math.pi/4]:
    reset(21); goto(0,0.62,-0.82); step(0,op='sample'); goto(1,-1.0,0.3)
    goto(0,*base,tol=0.001); turn_to(0,th); step(0,op='send')
    print(round(th,2), 'r0',np.round(pos(0),3),'r1',np.round(pos(1)[:2],3),'recv',dump('sample')['sample3'][-1])
