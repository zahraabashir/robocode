import numpy as np
L=np.array([-1.9,-2.0]); P=np.array([-0.135,-0.64]); d=(P-L)/np.linalg.norm(P-L); perp=np.array([-d[1],d[0]])
def segd(a,b,p):
    ab=b-a; t=np.clip(np.dot(p-a,ab)/np.dot(ab,ab),0,1); return np.linalg.norm(a+t*ab-p)
pil={'p6':np.array([-0.135,-0.64]),'p9':np.array([0.654,-0.199])}
for sv in np.arange(-0.2,0.2,0.02):
    q=L+3.5*d+sv*perp; e=q+np.array([0.087,0.012])  # theta=pi offset
    print(round(sv,2), {k:(round(segd(q,L,v),3),round(segd(e,L,v),3)) for k,v in pil.items()})
