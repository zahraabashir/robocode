import sys, numpy as np
from multiprocessing import Pool
from env_client import make_env
import approach
def run(seed):
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    rows=[]
    for t in range(400):
        a=ap.get_action(obs); obs,r,term,trunc,_=env.step(a)
        rows.append(np.concatenate([obs,[float(term)]]))
        if term: break
    env.close(); return np.array(rows)
with Pool(10) as p: res=p.map(run, range(300,340))
np.save("term_data.npy", np.concatenate(res))
