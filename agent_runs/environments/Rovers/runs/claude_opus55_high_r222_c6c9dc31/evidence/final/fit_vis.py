import json, glob, math
import numpy as np
from env_client import make_env
from approach import seg_point_dist, seg_hits_box
rows=[json.loads(l) for f in glob.glob('vis_data_*.jsonl') for l in open(f)]
env=make_env(); T=lambda n: env.observation_space.get_type(n)
obst={}
for s in set(r['seed'] for r in rows):
    obs,_=env.reset(seed=s)
    obst[s]=[(obs.get(o,'x'),obs.get(o,'y'),obs.get(o,'half_x'),obs.get(o,'half_y'),obs.get(o,'half_z')) for o in obs.get_objects(T('obstacle'))]
    rv={o.name:(obs.get(o,'x'),obs.get(o,'y')) for o in obs.get_objects(T('rover'))}
    obst[s+1000]=rv
CA=math.radians(188)
def cam(r):
    return r['x']+0.0875*math.cos(r['th']+CA), r['y']+0.0875*math.sin(r['th']+CA)
inr=[]
for r in rows:
    cx,cy=cam(r); d=math.hypot(cx-r['ox'],cy-r['oy'])
    r['d']=d; r['cx']=cx; r['cy']=cy
print('total',len(rows),'vis',sum(r['vis'] for r in rows))
print('range check: max d visible', max(r['d'] for r in rows if r['vis']>0.5), 'min d invisible among d<2', sorted(r['d'] for r in rows if r['vis']<0.5)[:3])
sub=[r for r in rows if r['d']<1.99]
print('in range',len(sub),'invisible',sum(1 for r in sub if r['vis']<0.5))
def model_eval(name, blockfn):
    fp=fn=0; ex=[]
    for r in sub:
        b=blockfn(r)
        if b and r['vis']>0.5: fn+=1; ex.append(('fn',r['seed'],r['r'],round(r['x'],2),round(r['y'],2)))
        if (not b) and r['vis']<0.5: fp+=1; ex.append(('fp',r['seed'],r['r'],round(r['x'],2),round(r['y'],2)))
    print(name,'wrongly-blocked',fn,'missed-block',fp, ex[:4])
for m in (-0.02,0,0.01,0.02,0.04):
    model_eval('cyl r=0.05+%.2f'%m, lambda r: any(seg_point_dist(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py)<hx+m for px,py,hx,hy,hz in obst[r['seed']] if hx<0.1))
    model_eval('box +%.2f'%m, lambda r: any(seg_hits_box(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py,hx+m,hy+m) for px,py,hx,hy,hz in obst[r['seed']] if hx<0.1))
print('---- 3D analysis')
res=[]
for r in sub:
    for px,py,hx,hy,hz in obst[r['seed']]:
        if hx>0.1: continue
        if seg_hits_box(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py,hx+0.005,hy+0.005):
            L=math.hypot(r['ox']-r['cx'],r['oy']-r['cy'])
            s=((px-r['cx'])*(r['ox']-r['cx'])+(py-r['cy'])*(r['oy']-r['cy']))/L**2
            perp=float(seg_point_dist(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py))
            res.append((round(s,3),round(L*s,3),round(L*(1-s),3),round(perp,3),int(r['vis'])))
res.sort()
for x in res: print(x)
