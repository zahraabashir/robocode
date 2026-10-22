import time
from env_client import make_env
t=time.time(); env=make_env(); o,i=env.reset(seed=0); print("ok", time.time()-t); env.close()
