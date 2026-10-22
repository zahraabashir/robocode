from dyn_lib import *
import sys
# probe surface: approach along body-frame direction, detect first block motion
def probe(seed, start_b, dir_b, step=0.002):
    e=E(seed); e.goto_safe(start_b); o0=e.obs.copy()
    d=np.asarray(dir_b,float); d/=np.linalg.norm(d)
    dw=R(o0[2])@d
    for i in range(1500):
        p_before=e.obs[16:18].copy()
        o=e.step(dw*step)
        if np.linalg.norm(o[0:3]-o0[0:3])>1e-9:
            return to_body(o0,p_before), o[0:3]-o0[0:3]
    return None,None
for s in [0,1]:
  for x in [0.0,0.3,0.5,-0.5]:
    pb,dp=probe(s,[x,1.0],[0,-1]); print('seed',s,'bar top x',x,'contact robot body',pb,dp)
  for x in [0.0]:
    pb,dp=probe(s,[x,-1.8],[0,1]); print('seed',s,'stem end',x,pb,dp)
    pb,dp=probe(s,[x,-0.3],[0,1]) if False else (None,None)
  for y in [-0.3,-0.6]:
    pb,dp=probe(s,[1.0,y],[-1,0]); print('seed',s,'stem side y',y,pb,dp)
  pb,dp=probe(s,[1.2,0.0],[-1,0]); print('seed',s,'bar end +x',pb,dp)
  pb,dp=probe(s,[0.4,-0.6],[0,1]); print('seed',s,'bar bottom x=.4',pb,dp)
  print('dims',E(s).obs[12:15])
