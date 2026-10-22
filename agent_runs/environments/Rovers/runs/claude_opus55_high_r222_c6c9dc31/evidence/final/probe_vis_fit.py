import numpy as np, math, sys
data=open(sys.argv[1]).read().strip(); beta=math.radians(float(sys.argv[2]))
rows=[(float(l.split()[0]),[int(c) for c in l.split()[1]]) for l in data.splitlines()]
D=np.array([d for d,b in rows]); B=np.array([b for d,b in rows],bool)
N=B.shape[1]; th=-math.pi+np.arange(N)*2*math.pi/N
rho=np.arange(0.0,0.25,0.0025)[:,None,None,None]; phi=np.radians(np.arange(150,211,1.0))[None,:,None,None]
cx=rho*np.cos(th[None,None,None,:]+phi); cy=rho*np.sin(th[None,None,None,:]+phi)
dist=np.hypot(D[None,None,:,None]*math.cos(beta)-cx,D[None,None,:,None]*math.sin(beta)-cy)
res=[]
for R in np.arange(1.95,2.05,0.0025):
    err=((dist<=R)!=B[None,None]).sum(axis=(2,3))
    i,j=np.unravel_index(err.argmin(),err.shape)
    res.append((int(err[i,j]),round(R,4),round(float(rho[i,0,0,0]),4),round(math.degrees(float(phi[0,j,0,0])),1)))
res.sort(); print(res[:8])
