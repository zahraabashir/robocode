from pF_model import *
import sys
dirs=[(np.cos(a),np.sin(a)) for a in np.arange(8)*np.pi/4]
base=[0.1583,0.1705,0.1868,0.14,0.1768]
for tag in sys.argv[1:]:
    D=json.load(open('pF_out_%s.json'%tag))
    for yaw in np.pi/4+np.radians(np.arange(-45,45,3)):
        e=[]
        for thr,v in D.items():
            pr=[contact(base+[yaw],v['theta'],*dirs[k]) for k in v['order']]
            e+=[m-p for m,p in zip(v['d'],pr)]
        e=np.array(e); print(tag,'yaw_deg %.0f'%np.degrees(yaw),'rms %.4f max %.4f mean %.4f'%(np.sqrt((e**2).mean()),np.abs(e).max(),e.mean()))
