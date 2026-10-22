from pD_lib import *
S=(0.4,-0.6,np.pi)
for t in [0.4,0.45,0.5,0.55]:
    for th in [0,2.36]:
        p=pos_on_line(S,t,0.0,th); print(t,th,np.round(p,3),trial((S,p)),flush=True)
