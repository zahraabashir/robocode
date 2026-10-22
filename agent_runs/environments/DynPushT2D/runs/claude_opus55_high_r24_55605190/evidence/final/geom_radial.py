from geom_lib import *
import sys
P=Prober(); seed=int(sys.argv[1])
o=P.reset(seed); print('seed',seed,'w,Lh,Lv',o[12:15],'r',o[28])
for k in range(24):
    a=2*np.pi*k/24; u=np.array([np.cos(a),np.sin(a)])
    res,msg=P.probe(seed,1.5*u,-u)
    if res is None: print(k,msg); continue
    print('ang %5.1f contact robot body pos prev %s now %s'%(np.degrees(a),np.round(res[0],4),np.round(res[1],4)))
