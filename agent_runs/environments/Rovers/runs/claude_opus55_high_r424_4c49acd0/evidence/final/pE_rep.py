from pE_lib import *
import json
r=json.load(open('pE_data.json'))
def cr(a,b): return a[0]*b[1]-a[1]*b[0]
n=0
for x in r:
    if min(segd(p,x['sp'],x['obj']) for p in x['P'])>0.07: continue
    res=[]
    for rep in range(3):
        s=Sim(x['seed']); drive(s,x['i'],x['x'],x['y']); act1(s,x['i'],'cal'); res.append(s.r(x['i'])['calibrated'])
    print(x['seed'],x['i'],round(x['x'],2),round(x['y'],2),'orig',x['cal'],'rep',res,flush=True); n+=1
    if n>14: break
