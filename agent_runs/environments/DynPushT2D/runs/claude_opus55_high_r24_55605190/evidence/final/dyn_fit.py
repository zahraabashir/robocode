from dyn_push import *
from scipy.optimize import least_squares
import pickle
cases=[ # start_b, dir_b, normal(outward) for contact point
 ([0.2,0.6],[0,-1],[0,1]),([0.4,0.6],[0,-1],[0,1]),([0.55,0.6],[0,-1],[0,1]),([-0.3,0.6],[0,-1],[0,1]),
 ([-0.8,-0.5],[1,0],[-1,0]),([-0.8,-0.8],[1,0],[-1,0]),([-0.8,-1.1],[1,0],[-1,0]),
 ([0.8,-0.4],[-1,0],[1,0]),([0.8,-0.9],[-1,0],[1,0]),
 ([0.4,-0.8],[0,1],[0,-1]),([0.25,-0.8],[0,1],[0,-1]),
 ([0.03,-1.8],[0,1],[0,-1]),([0.0,-1.8],[0,1],[0,-1]),
 ([1.0,-0.065],[-1,0],[1,0]),
]
data=[]
for sb,d,n in cases:
    out,e=push(0,sb,d,0.01,5)
    cb,tw=out[3]
    u=np.array(d,float)*0.01
    cp=cb-0.1*np.array(n)
    data.append((cp,u,tw)); print(sb,d,'contact',cp,'twist',tw)
pickle.dump(data,open('dyn_fitdata.pkl','wb'))
