from env_client import make_env
import numpy as np
env = make_env()
obs,_ = env.reset(seed=0)
o=obs.copy(); o[0]=2.5;o[1]=2.5;o[2]=0.0; o[16]=2.5;o[17]=2.5; o[29]=1;o[30]=1;o[31]=0.5
print(o.tolist())
