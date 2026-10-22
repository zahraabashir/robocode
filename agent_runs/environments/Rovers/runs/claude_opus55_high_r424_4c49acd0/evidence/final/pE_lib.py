from pB_lib import *
import numpy as np
def objs(s):
    out=[]
    for k in range(10):
        try: o=s.obs.get_object_from_name('objective%d'%k)
        except Exception: break
        out.append([float(s.obs.get(o,f)) for f in ['x','y','have_image_rover0','have_image_rover1','received_image']])
    return out
def pillars(s):
    P=[]
    for n in s.obs.get_object_names():
        if str(n).startswith('obstacle'):
            o=s.obs.get_object_from_name(n)
            if abs(float(s.obs.get(o,'half_x'))-0.05)<1e-3: P.append((float(s.obs.get(o,'x')),float(s.obs.get(o,'y'))))
    return P
def sense(s,i):
    c=s.r(i); th=c['theta']; return (c['x']-0.087*np.cos(th)+0.012*np.sin(th), c['y']-0.087*np.sin(th)-0.012*np.cos(th))
def segd(p,a,b):
    p,a,b=map(np.array,(p,a,b)); d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p)
def info(s,i):
    sp=sense(s,i); P=pillars(s); res=[]
    for k,o in enumerate(objs(s)):
        d=np.hypot(o[0]-sp[0],o[1]-sp[1]); m=min([segd(p,sp,o[:2]) for p in P]+[9])
        res.append((k,round(d,3),round(m,3),o[2:]))
    return res
def drive(s,i,x,y):
    c=s.r(i)
    for pts in ([(c['x'],y),(x,y)],[(x,c['y']),(x,y)],[(c['x'],(c['y']+y)/2),((c['x']+x)/2,(c['y']+y)/2),(x,y)]):
        if gp(s,i,pts): return True
    return False
def act1(s,i,sel):
    a=(0,0,0,sel)
    if i==0: s.act(a0=a)
    else: s.act(a1=a)
def probe(s,i,x,y,verbose=True):
    ok=drive(s,i,x,y)
    c=s.r(i); before=objs(s); I=info(s,i)
    act1(s,i,'cal'); cal=s.r(i)['calibrated']
    act1(s,i,'img'); after=objs(s)
    got=[k for k in range(len(before)) if after[k][2+i]!=before[k][2+i]]
    if verbose: print('rover',i,'reached',ok,(c['x'],c['y']),'cal',cal,'imaged',got,'calafter',s.r(i)['calibrated'],'\n  (k,dist,minpillar,[h0,h1,rec])',I)
    return cal,got
