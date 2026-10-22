import sys, json
from multiprocessing import Pool
from pB_lib import *
from pD_lib import pos_on_line
IMG={2:(0.4,0.2),1:(1.0,0.3)}
def image(s,k,S):
    gp(s,0,[IMG[k]],th=np.pi); s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img'))
    assert objf(s,k,'have_image_rover0')==1 and objf(s,k,'received_image')==0
    assert gp(s,0,[(S[0],IMG[k][1]),(S[0],S[1])],th=S[2])
def scanside(s,k,S,t,side,th,offs):
    out=[]
    for o in offs:
        p=pos_on_line(S,t,side*o,th)
        ok=s.goto(1,p[0],p[1],th=p[2]); r=s.r(1)
        if not(ok and abs(r['x']-p[0])<2e-3 and abs(r['y']-p[1])<2e-3): out.append((o,None)); continue
        s.act(a0=(0,0,0,'send'))
        res=objf(s,k,'received_image')==1; out.append((o,res))
        if res: break
    return out
def job(j):
    S,t,th=j
    try:
        s=Sim(44); s.goto(1,-1.0,-0.3)
        offs=list(np.round(np.arange(0,0.301,0.01),3))
        image(s,2,S); a=scanside(s,2,S,t,+1,th,offs)
        s.goto(1,-1.0,-0.3)
        image(s,1,S); b=scanside(s,1,S,t,-1,th,offs)
        return j,a,b
    except Exception as e: return j,'ERR',repr(e)
def summ(a):
    if a=='ERR': return a
    fails=[o for o,r in a if r is None]; succ=[o for o,r in a if r]
    blocked=[o for o,r in a if r is False]
    return 'first_free=%s lastblocked=%s placefail=%s'%(succ[0] if succ else None, blocked[-1] if blocked else None, fails[:3])
if __name__=='__main__':
    S=tuple(json.loads(sys.argv[1])); ths=json.loads(sys.argv[2]); ts=json.loads(sys.argv[3])
    jobs=[(S,t,th) for th in ths for t in ts]
    with Pool(int(sys.argv[4]) if len(sys.argv)>4 else 8) as p:
        for j,a,b in p.imap(job,jobs):
            print('t=%.2f th=%.2f | +side %s | -side %s'%(j[1],j[2],summ(a),summ(b) if a!='ERR' else b),flush=True)
