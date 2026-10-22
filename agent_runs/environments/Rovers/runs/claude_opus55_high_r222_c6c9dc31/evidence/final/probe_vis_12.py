from probe_vis_util import *
import sys
seed,i,on,pn=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4]; wps=eval(sys.argv[5]); extra=float(sys.argv[6])
r=R(seed)
g=lambda n:np.array([float(r.obs.get(r.obs.get_object_from_name(n),f)) for f in 'xy'])
O=g(on); P=g(pn)
v=P-O; n=np.linalg.norm(v); u=v/n; w=np.array([-u[1],u[0]])
print('n',n, path(r,i,wps))
a=math.atan2(-u[1],-u[0]); th=a-math.radians(188)
out=''
for s in np.arange(-0.30,0.301,0.01):
    q=O+u*(n+extra)+w*s
    if not r.goto(i,q[0],q[1],tol=1e-6): out+='X'; continue
    r.turn(i,th)
    rv=r.rv(i); cam=np.array([rv['x'],rv['y']])+0.0875*np.array([math.cos(rv['theta']+math.radians(188)),math.sin(rv['theta']+math.radians(188))])
    # lateral distance of pillar center from segment cam-O
    d=cam-O; t=np.dot(P-O,d)/np.dot(d,d); lat=np.cross(d/np.linalg.norm(d),P-O)
    r.act(i,'calibrate'); c=r.rv(i)['calibrated']
    if c: r.act(i,'image')
    print('s %.2f lat %.3f cal %d'%(s,lat,c))
