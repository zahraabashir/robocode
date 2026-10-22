exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
import sys
P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
X=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
base=L+d*((X-L[0])/d[0])
S_=np.round(np.arange(-0.16,0.161,0.02),3)
for k in range(8):
    th=-math.pi+k*math.pi/4
    rem=list(S_); row={}
    while rem:
        reset(21); goto(0,0.62,-0.82); step(0,op='sample'); goto(1,-1.0,0.3); turn_to(0,th)
        while rem:
            s=rem.pop(0); goto(0,*(base+n*s),tol=0.001); step(0,op='send')
            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
            if ok: break
    print(f'{th:6.2f}', ''.join(row[s] for s in S_))
print('s:',S_[0],'..',S_[-1])
