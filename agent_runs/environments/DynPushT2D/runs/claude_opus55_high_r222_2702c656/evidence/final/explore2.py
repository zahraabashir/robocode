from env_client import make_env
import numpy as np
np.set_printoptions(precision=2, suppress=True, linewidth=200)
env = make_env()
rows=[]
for s in range(40):
    obs,_ = env.reset(seed=s)
    rows.append([obs[0],obs[1],obs[2],obs[29],obs[30],obs[31],obs[16],obs[17],obs[12],obs[13],obs[14]])
rows=np.array(rows)
print(rows.min(0)); print(rows.max(0))
