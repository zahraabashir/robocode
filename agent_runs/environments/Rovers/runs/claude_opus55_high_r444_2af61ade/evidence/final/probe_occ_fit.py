import numpy as np, math, re, sys, ast
recs=[]
for line in open(sys.argv[1]):
    if not line.startswith('((('): continue
    j,r=ast.literal_eval(line.strip())
    if r.get('i') in (None,0): continue
    P0,Q,h,d=j; b=((r['p1'][0]+r['prev'][0])/2,(r['p1'][1]+r['prev'][1])/2)
    recs.append((r['p0'],b,h,d))
def segd(p,a,b):
    a,b,p=map(np.array,(a,b,p)); t=np.clip(np.dot(p-a,b-a)/np.dot(b-a,b-a),0,1); 
    v=p-(a+t*(b-a)); return np.linalg.norm(v), np.sign(np.cross(b-a,p-a))
def cam(p0):
    x,y,th=p0; c,s=math.cos(th),math.sin(th); return (x+c*-0.087-s*-0.0125, y+s*-0.087+c*-0.0125)
L=(-1.9,-2.0)
for name,src in [('centre',lambda p:p[:2]),('cam',cam)]:
    print(name)
    for p0,b,h,d in recs:
        dist,sg=segd(b,src(p0),L); print('  ',p0[:2],b,h,d,round(dist*sg,4))
