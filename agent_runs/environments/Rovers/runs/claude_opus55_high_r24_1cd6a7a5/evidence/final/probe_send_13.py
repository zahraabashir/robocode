exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
R1=np.array([-1.0,-1.75]); d=(R1-L)/np.linalg.norm(R1-L); n=np.array([-d[1],d[0]])
X=1.0; base=L+d*((X-L[0])/d[0])
S_=np.round(np.arange(-0.3,0.301,0.03),3)
for k in range(8):
    th=-math.pi+k*math.pi/4
    rem=list(S_); row={}
    while rem:
        reset(21); goto(0,0.62,-0.82); step(0,op='sample'); turn_to(0,th)
        while rem:
            s=rem.pop(0); goto(0,*(base+n*s),tol=0.001); step(0,op='send')
            ok=dump('sample')['sample3'][-1]>0; row[s]='o' if ok else 'X'
            if ok: break
    print(f'{th:6.2f}', ''.join(row[s] for s in S_))
print('s:',S_[0],'..',S_[-1], 'base',base)
