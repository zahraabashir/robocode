import numpy as np
from env_client import make_env
from approach import *
env = make_env(); obs, info = env.reset(seed=10)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
i,j = to_cell(0.30,-0.45)
np.set_printoptions(linewidth=200)
print(ap.V_send['rover0'][i-2:i+5, j-5:j+3].T[::-1])
print(ap.V_home['rover0'][i-2:i+5, j-5:j+3].T[::-1])
print(ap.send_reg['rover0'][i-2:i+5, j-5:j+3].T[::-1].astype(int))
