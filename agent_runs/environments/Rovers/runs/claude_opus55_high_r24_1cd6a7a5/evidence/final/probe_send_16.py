exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
P=np.array([-1.81,-1.55]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
S_=np.round(np.arange(-0.3,0.301,0.03),3)
for Y in [-0.5,0.5]:
  t=(Y-L[1])/d[1]; base=L+d*t
  for th in [-math.pi/2, math.pi/2, 0.0]:
    rem=list(S_); row={}
    while rem:
        reset(0); goto(1,-1.39,0.15+0.1); step(1,op='sample'); assert dump('sample')['sample3'][5]==1
        turn_to(1,th)
        while rem:
            s=rem.pop(0); goto(1,*(base+n*s),tol=0.002); step(1,op='send')
            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
            if ok: break
    print(Y, f'{th:6.2f}', ''.join(row[s] for s in S_), np.round(base,2))
