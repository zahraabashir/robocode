import sys, math, json, numpy as np
from env_client import make_env
from approach import SEL
LX,LY=-1.9,-2.0
env=make_env()
T=env.observation_space
def objs(obs,t): return list(obs.get_objects(T.get_type(t)))
def pos(obs,o): return float(obs.get(o,'x')),float(obs.get(o,'y'))
def run(seed, rover, path, park=None, a_h=0.05, pre=()):
    """path: list of waypoints; after sampling, rover drives through waypoints issuing send each step."""
    obs,_=env.reset(seed=seed)
    R={o.name:o for o in objs(obs,'rover')}; S=objs(obs,'sample')
    me=R[rover]; oth=R['rover1' if rover=='rover0' else 'rover0']
    k=0 if rover=='rover0' else 4; ko=4-k
    side=1 if rover=='rover0' else -1
    mx,my=pos(obs,me)
    cand=[s for s in S if pos(obs,s)[0]*side>0.3 and (abs(pos(obs,s)[0]-LX)>0.85 or abs(pos(obs,s)[1]-LY)>0.7) and abs(pos(obs,s)[0])<2.3 and abs(pos(obs,s)[1])<2.3]
    tgt=min(cand,key=lambda s:math.hypot(pos(obs,s)[0]-mx,pos(obs,s)[1]-my))
    log=[]
    def step(dx,dy,sel,odx=0,ody=0):
        nonlocal obs
        a=np.zeros(8,np.float32); a[k:k+4]=[dx,dy,0,sel]; a[ko:ko+4]=[odx,ody,0,SEL['none']]
        obs,*_=env.step(a)
    def goto(tx,ty,sel=SEL['none'],tol=0.02,maxn=200,oth_t=None,h=0.2):
        out=[]
        for _ in range(maxn):
            x,y=pos(obs,me); dx,dy=np.clip(tx-x,-h,h),np.clip(ty-y,-h,h)
            odx=ody=0
            if oth_t:
                ox,oy=pos(obs,oth); odx,ody=np.clip(oth_t[0]-ox,-.2,.2),np.clip(oth_t[1]-oy,-.2,.2)
            if abs(dx)<tol and abs(dy)<tol and (not oth_t or (abs(odx)<tol and abs(ody)<tol)): break
            before=pos(obs,me)
            rec=sum(float(obs.get(s,'received_analysis')) for s in S)
            step(dx,dy,sel,odx,ody)
            if pos(obs,me)==before and sel!=SEL['send']:
                for ax,ay in [(dx,0),(0,dy),(0,0.2),(0,-0.2),(0.2,0),(-0.2,0)]:
                    if abs(ax)+abs(ay)<1e-6: continue
                    for _r in range(3):
                        b2=pos(obs,me); step(ax,ay,sel)
                        if pos(obs,me)==b2: break
                    if pos(obs,me)!=before: break
            if sel==SEL['send']:
                ok=sum(float(obs.get(s,'received_analysis')) for s in S)>rec
                # send happens at pre-move or post-move pos? record both
                out.append((before,pos(obs,me),ok))
                if ok: return out,True
            if pos(obs,me)==before and not oth_t: 
                return out,'stuck'
        return out,False
    sx,sy=pos(obs,tgt)
    # move toward sample, park other
    goto(sx-0.12*np.sign(sx),sy-0.12*np.sign(sy),oth_t=park)
    for ox_,oy_ in [(0,-0.12*np.sign(sy)),(-0.12*np.sign(sx),0),(0,0.12),(0,-0.12),(0.12,0),(-0.12,0)]:
        if math.hypot(pos(obs,me)[0]-sx,pos(obs,me)[1]-sy)<0.22: break
        goto(sx+ox_,sy+oy_)
    step(0,0,SEL['sample']); 
    assert float(obs.get(tgt,'analyzed_'+rover))==1, ('sample failed',tgt.name,pos(obs,tgt),pos(obs,me),pos(obs,oth),[float(obs.get(s,'analyzed_'+rover)) for s in S])
    step(0,0,SEL['drop'])
    res=[]
    for i_,(wx,wy) in enumerate(path):
        # move to first waypoint silently, then send along the rest
        if i_==0:
            for px,py in pre: goto(px,py)
            o,_=goto(wx,wy); res.append(('start',pos(obs,me))); continue
        o,f=goto(wx,wy,sel=SEL['send'],h=a_h,tol=0.005)
        res+=o
        if f is True or f=='stuck': break
    return res
if __name__=='__main__':
    a=json.loads(sys.argv[1])
    r=run(a['seed'],a['rover'],a['path'],a.get('park'),a.get('h',0.05),a.get('pre',[[-0.6,-1.0]] if a['rover']=='rover1' else [[1.0,-1.0]]))
    print(json.dumps({'args':a,'res':r}))
