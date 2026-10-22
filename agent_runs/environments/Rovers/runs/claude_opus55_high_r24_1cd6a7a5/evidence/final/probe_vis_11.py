from probe_vis_lib import *
import probe_vis_lib as L, sys, json
L.RV='rover0'
seed=2; name='objective0'; pill=np.array([0.735,0.444])
thd=float(sys.argv[1]); rs=np.arange(float(sys.argv[2]),float(sys.argv[3])+1e-9,float(sys.argv[4])); ss=np.arange(-0.15,0.15+1e-9,0.01)
reset(seed); o=objpos(name)[:2]
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
goto([(1.0,-1.75),(0.9,-1.75)]); turn(np.deg2rad(thd))
rows=[]; data=[]
for i,r in enumerate(rs[::-1]):
    line=''
    for s in (ss if i%2==0 else ss[::-1]):
        p=o+r*u+s*n; q=goto([tuple(p)])
        if np.linalg.norm(q[:2]-p)>1e-4: ch='X'
        else:
            c=cal(); ch=str(int(c))
            if c>0.5: step(op=-1/6)
            data.append((float(q[0]),float(q[1]),float(q[2]),int(c)))
        line+=ch
    rows.append((r,line if i%2==0 else line[::-1]))
for r,l in rows: print(f"{r:.3f} {l}")
json.dump(data,open(f'probe_vis_data_r0_{int(thd)}.json','w'))
