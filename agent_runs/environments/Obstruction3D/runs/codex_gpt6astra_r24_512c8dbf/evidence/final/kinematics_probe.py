import numpy as np
from scipy.spatial.transform import Rotation as R
q=[0,-.35,-np.pi,-2.5,0,-.87,np.pi/2]
origins=[([0,0,.15643],np.pi),([0,.005375,-.12838],np.pi/2),([0,-.21038,-.006375],-np.pi/2),([0,.006375,-.21038],np.pi/2),([0,-.20843,-.006375],-np.pi/2),([0,0,-.10593],np.pi/2),([0,-.10593,0],-np.pi/2)]
t=np.array([-.12,0,0.]);r=np.eye(3)
for (p,a),j in zip(origins,q):
 t+=r@p;r=r@R.from_euler('x',a).as_matrix()@R.from_euler('z',j).as_matrix()
 print(t)
print('orientation',r)
for d in [.06,.12,.18]: print('ee',d,t+r@[0,0,-d])
