import numpy as np, json, glob
def box(x0,x1,y0,y1): return np.array([[x0,y0],[x1,y0],[x1,y1],[x0,y1]])
def circ(r,n=72): a=np.arange(n)*2*np.pi/n; return np.c_[r*np.cos(a),r*np.sin(a)]/np.cos(np.pi/n)*1.0
def sat(A,B):
    for P in (A,B):
        for k in range(len(P)):
            e=P[(k+1)%len(P)]-P[k]; n=np.array([-e[1],e[0]])
            a=A@n; b=B@n
            if a.max()<=b.min() or b.max()<=a.min(): return False
    return True
def make(prm):
    f,s,r,rw,rc,pyaw=prm
    parts=[box(-f,f,-s,s),box(-r,0,-rw,rw),circ(rc)]
    a=np.arange(4)*np.pi/2+pyaw+np.pi/4; pil=0.05*np.sqrt(2)*np.c_[np.cos(a),np.sin(a)]
    return parts,pil
def coll(parts,pil,cx,cy,th):
    R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    return any(sat(p@R.T+[cx,cy],pil) for p in parts)
def contact(prm,th,ux,uy,e=0.0):
    parts,pil=make(prm); vx,vy=-uy,ux
    lo,hi=-0.05,0.6
    # find first contact moving from hi down: scan then bisect
    ts=np.arange(0.6,-0.05,-0.005); prev=0.6
    for t in ts:
        if coll(parts,pil,t*ux+e*vx,t*uy+e*vy,th): lo,hi=t,prev; break
        prev=t
    else: return None
    for _ in range(20):
        m=(lo+hi)/2
        if coll(parts,pil,m*ux+e*vx,m*uy+e*vy,th): lo=m
        else: hi=m
    return hi
if __name__=='__main__':
    import sys
    prm=[0.1583,0.1705,0.1868,0.14,0.1768,np.pi/4]
    dirs=[(np.cos(a),np.sin(a)) for a in np.arange(8)*np.pi/4]
    errs=[]
    for fn in sorted(glob.glob('pF_out_[AB].json')):
        for thr,v in json.load(open(fn)).items():
            pr=[contact(prm,v['theta'],*dirs[k]) for k in v['order']]
            print('thr',thr,' '.join('%.4f/%.4f'%(m,p) for m,p in zip(v['d'],pr)))
            errs+=[m-p for m,p in zip(v['d'],pr)]
    for fn in sorted(glob.glob('pF_prof_*.json')):
        v=json.load(open(fn)); th=np.pi+v['thr']; u=(np.cos(v['ang']),np.sin(v['ang']))
        pr=[contact(prm,th,*u,e) for e in v['offs']]
        ee=[(m-p) for m,p in zip(v['res'],pr) if m is not None and p is not None]
        miss=sum((m is None)!=(p is None) for m,p in zip(v['res'],pr))
        print(fn,'maxerr %.4f meanabs %.4f hitmismatch %d'%(np.max(np.abs(ee)),np.mean(np.abs(ee)),miss)); errs+=ee
    errs=np.array(errs); print('ALL n',len(errs),'mean',errs.mean().round(4),'maxabs',np.abs(errs).max().round(4),'rms',np.sqrt((errs**2).mean()).round(4))
