from pm_util import *
e=E(); seed=12
mv,obs,act=run_push(e,seed,[-0.45,0.25],[0,-1],0.02,60)
th=obs[:,2]; print(np.round(th[::4],4)); print("min/max",th.min(),th.max(), "block pos end",obs[-1][0:2])
