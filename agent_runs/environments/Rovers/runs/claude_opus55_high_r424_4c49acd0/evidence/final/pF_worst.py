from pF_model import *
base=[0.1583,0.1705,0.1868,0.14,0.1768]
dirs=[(np.cos(a),np.sin(a)) for a in np.arange(8)*np.pi/4]
names=['+x','+x+y','+y','-x+y','-x','-x-y','-y','+x-y']
yaws=np.radians(np.arange(0,90,7.5))
for thr in [0,0.4,0.785,1.57]:
    row=[max(contact(base+[y],np.pi+thr,*d) for y in yaws) for d in dirs]
    mn=[min(contact(base+[y],np.pi+thr,*d) for y in yaws) for d in dirs]
    print(thr,' '.join('%s:%.3f-%.3f'%(n,a,b) for n,a,b in zip(names,mn,row)))
