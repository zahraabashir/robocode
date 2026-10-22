from probe_vis_lib import *
import probe_vis_lib as L, sys, json
L.RV='rover0'
seed=2; name='objective0'; pill=np.array([0.735,0.444])
r=float(sys.argv[1]); ths=eval(sys.argv[2]); ss=np.arange(-0.4,0.4001,0.01)
reset(seed); o=objpos(name)[:2]
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
p=o+r*u+ss[0]*n; goto([(1.0,-1.75),(p[0],-1.75),tuple(p)])
data=[]
for k,thd in enumerate(ths):
    turn(np.deg2rad(thd)); line=''
    seq=ss if k%2==0 else ss[::-1]
    for s in seq:
        p=o+r*u+s*n; q=goto([tuple(p)])
        if np.linalg.norm(q[:2]-p)>1e-4: line+='X'; continue
        c=cal(); line+=str(int(c))
        if c>0.5: step(op=-1/6)
        data.append((float(q[0]),float(q[1]),float(q[2]),int(c)))
    if k%2: line=line[::-1]
    print(f"{thd:5d} {line}",flush=True)
json.dump(data,open(f'probe_vis_data_row_{r}.json','w'))
