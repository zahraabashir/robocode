from probe_vis_util import *
import sys
side=float(sys.argv[1])
r=R(0)
path(r,0,[(1.2,0.0),(1.2,1.6)])
r.act(0,'calibrate'); r.act(0,'image')
path(r,0,[(1.2,0.0),(0.5,-1.0)])
rv=r.rv(0); th=rv['theta']
cam=np.array([rv['x'],rv['y']])+0.0875*np.array([math.cos(th+math.radians(188)),math.sin(th+math.radians(188))])
L=np.array([-1.9,-2.0]); u=(L-cam)/np.linalg.norm(L-cam); w=np.array([-u[1],u[0]])
base=cam+u*1.5
print(path(r,1,[(-1.0,-1.3),tuple(base)]), r.rv(1))
for s in np.arange(0,0.5,0.01):
    p=base+side*s*w; r.goto(1,*p,tol=1e-6)
    r.act(0,'send')
    if r.objst()['objective0'][2]: print('side',side,'clear at lateral offset s=%.3f'%s, r.rv(1)); break
