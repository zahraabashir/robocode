import numpy as np
from scipy.spatial.transform import Rotation as R
origins=[([0,0,.15643],[np.pi,0,0]),([0,.005375,-.12838],[np.pi/2,0,0]),([0,-.21038,-.006375],[-np.pi/2,0,0]),([0,.006375,-.21038],[np.pi/2,0,0]),([0,-.20843,-.006375],[-np.pi/2,0,0]),([0,0,-.10593],[np.pi/2,0,0]),([0,-.10593,0],[-np.pi/2,0,0])]
def fk(q):
 p=np.zeros(3); rot=np.eye(3)
 for a,(v,r) in zip(q,origins):
  p+=rot@v;rot=rot@R.from_euler('xyz',r).as_matrix()@R.from_euler('z',a).as_matrix()
 p+=rot@[0,0,-.061525]; rot=rot@R.from_euler('x',np.pi).as_matrix()
 return p,rot
if __name__=='__main__':
 q=[0,-.35,-np.pi,-2.5,0,-.87,np.pi/2]
 p,r=fk(q);print(p,r, 'fingers',p+r@[0,0,.12])
