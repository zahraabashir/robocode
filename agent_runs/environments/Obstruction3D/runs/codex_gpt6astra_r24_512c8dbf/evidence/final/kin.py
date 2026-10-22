import numpy as np
ORIGINS=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
MATS=[np.array([[1.,0.,0.],[0.,np.cos(a),-np.sin(a)],[0.,np.sin(a),np.cos(a)]]) for p,a in ORIGINS]
Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def fk(q,d=.18):
 t=np.zeros(3);r=np.eye(3)
 for (p,a),rx,j in zip(ORIGINS,MATS,q):
  c,s=np.cos(j),np.sin(j)
  rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
  t+=r@p;r=r@rx@rz
 return t-r[:,2]*d,r

def ik(x,z,d=.18):
    # Closed-form planar elbow solution with a vertically aligned wrist.
    l1,l2=.42076,.31436
    zz=z-(.28481-.10593-d)
    c=np.clip((x*x+zz*zz-l1*l1-l2*l2)/(2*l1*l2),-1.,1.)
    beta=np.arccos(c)
    shoulder=np.arctan2(x,zz)-np.arctan2(l2*np.sin(beta),l1+l2*c)
    q=Q0.copy()
    q[1]=shoulder;q[3]=-beta;q[5]=shoulder+beta-np.pi
    return q
