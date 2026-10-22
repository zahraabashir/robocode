import numpy as np
from probe_vis_geo import cam
from probe_vis_fit2 import s as s0
boxes=[(2.0,2.0,0.05,.25,.25,.05),(-2,2,.05,.25,.25,.05),(-0.215,-0.556,.201,.05,.05,.2),(0.735,0.444,.201,.05,.05,.2),(0.5,2,.05,.25,.25,.05),(-0.5,2,.05,.25,.25,.05),
(2.118,-0.961,.201,.05,.05,.2),(-1.717,0.906,.201,.05,.05,.2),(1.64,0.734,.201,.05,.05,.2),(1.786,-0.54,.201,.05,.05,.2),(-0.907,1.268,.201,.05,.05,.2),(-2.156,-1.004,.201,.05,.05,.2)]
O={'o0':(0.44,1.845,0.201),'o1':(-2.176,1.837,0.201),'o2':(-0.4922,1.8822,0.201)}
def hit(a,b,bx,eps=0.0):
    a=np.array(a);b=np.array(b);c=np.array(bx[:3]);h=np.array(bx[3:])+eps
    d=b-a; t0,t1=0.0,1.0
    for i in range(3):
        if abs(d[i])<1e-12:
            if abs(a[i]-c[i])>h[i]: return False
            continue
        ta=(c[i]-h[i]-a[i])/d[i]; tb=(c[i]+h[i]-a[i])/d[i]
        if ta>tb: ta,tb=tb,ta
        t0=max(t0,ta); t1=min(t1,tb)
        if t0>t1: return False
    return True
D=[]
for kv in s0.split():
    t,v=map(int,kv.split(':')); D.append(((0.81,0.083),t,'o0',v))
v1={-180:0,-165:0,-150:0,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:1,-15:1,0:1,15:1,30:1,45:1,60:1,75:1,90:0,105:0,120:0,135:0,150:0,165:1}
v2={-180:1,-165:1,-150:1,-135:1,-120:1,-105:1,-90:1,-75:1,-60:1,-45:1,-30:0,-15:0,0:1,15:0,30:0,45:0,60:0,75:0,90:0,105:1,120:0,135:0,150:0,165:1}
for t in v1: D.append(((-1.5267,0.3485),t,'o1',v1[t])); D.append(((-1.5267,0.3485),t,'o2',v2[t]))
D+= [((0.8138,0.0714),180,'o0',1),((0.8137,0.0719),180,'o0',0),((-1.5,0.25),0,'o2',0),((-1.57,0.31),0,'o2',1)]
def score(hc,zt=0.201,eps=0.0,ox=-0.087,oy=-0.0125,verbose=False):
    err=0
    for b,t,o,v in D:
        c=cam(b,np.deg2rad(t),ox,oy); a=(c[0],c[1],hc); ob=O[o]; tgt=(ob[0],ob[1],zt)
        vis= not any(hit(a,tgt,bx,eps) for bx in boxes)
        if vis!=bool(v):
            err+=1
            if verbose: print('miss',b,t,o,v)
    return err
if __name__=='__main__':
    res=[]
    for hc in np.arange(0.05,1.0,0.01):
      for zt in [0.15,0.201,0.25,0.3]:
        res.append((score(hc,zt),round(hc,3),zt))
    res.sort(); print(len(D),res[:10])
