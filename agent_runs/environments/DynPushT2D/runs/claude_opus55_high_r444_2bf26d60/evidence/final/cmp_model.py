import numpy as np
from push_model import predict_step, geom_from_obs
from model_v import VModel
rng=np.random.default_rng(0)
g=dict(w=0.13,Lh=1.1,Lv=1.1); m=VModel(0.13,1.1,1.1)
P=[];Q=[]
for i in range(500):
    pose=np.array([2.5,2.5,rng.uniform(-3,3)]); rob=pose[:2]+rng.uniform(-0.8,0.8,2); a=rng.uniform(-0.049,0.049,2)
    p1,r1=predict_step(pose,rob,a,g); P.append(p1)
    Q.append((pose,rob,a))
p2,r2=m.step(np.array([q[0] for q in Q]),np.array([q[1] for q in Q]),np.array([q[2] for q in Q]))
print(np.abs(np.array(P)-p2).max(0))
