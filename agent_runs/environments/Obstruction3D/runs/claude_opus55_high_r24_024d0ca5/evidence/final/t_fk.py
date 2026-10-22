import numpy as np
from kin import fk
q=[0,-0.35,-np.pi,-2.5,0,-0.87,np.pi/2]
T=fk(q,(-0.12,0,0)); np.set_printoptions(precision=3,suppress=True); print(T)
