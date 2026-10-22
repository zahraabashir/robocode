"""Empirical end-effector kinematics calibrated from object grasp transforms."""
import numpy as np
from scipy.spatial.transform import Rotation as R
_ORIGINS=[([0,0,.15643],[np.pi,0,0]),([0,.005375,-.12838],[np.pi/2,0,0]),([0,-.21038,-.006375],[-np.pi/2,0,0]),([0,.006375,-.21038],[np.pi/2,0,0]),([0,-.20843,-.006375],[-np.pi/2,0,0]),([0,0,-.10593],[np.pi/2,0,0]),([0,-.10593,0],[-np.pi/2,0,0])]
_CORRECTIONS=np.array([[.119900586,-.000000907388036,-.00260022157],[-.00000199051248,.000000914355447,.00260022157],[.00000144000406,-.000000333673386,-.000000914355447],[-.00000101922,.000000233451646,-.000000333673386],[.00000259857607,-.000000906154370,-.000000233451646],[-.00000298101870,.000176597705,-.000000906154370],[.00000162928733,-.0599982073,-.000176597705],[-.00000337081718,.00000238525014,.0599982073]])
_TRANSFORMS=[R.from_euler('xyz',r).as_matrix() for _,r in _ORIGINS]
_FLIP=R.from_euler('x',np.pi).as_matrix()
def fk(q):
    p=np.zeros(3); rot=np.eye(3)
    for i,(a,(v,_),rr) in enumerate(zip(q,_ORIGINS,_TRANSFORMS)):
        p+=rot@(np.array(v)+_CORRECTIONS[i]);c=np.cos(a);s=np.sin(a)
        rot=rot@rr@np.array([[c,-s,0],[s,c,0],[0,0,1]])
    p+=rot@np.array([0,0,-.061525]);rot=rot@_FLIP
    p+=rot@_CORRECTIONS[-1]
    return p,rot
