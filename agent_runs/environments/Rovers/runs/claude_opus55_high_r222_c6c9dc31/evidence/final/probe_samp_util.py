from env_client import make_env
import numpy as np, math
env = make_env()
SP = env.observation_space
SEL={'sample':-5/6,'calibrate':-0.5,'image':-1/6,'noop':1/6,'send':0.5,'drop':5/6}
def objs(obs,t): return obs.get_objects(SP.get_type(t))
def feats(obs,t):
    out={}
    for o in objs(obs,t):
        out[o.name]={f:round(float(obs.get(o,f)),4) for f in SP.get_type(t).feature_names} if hasattr(SP.get_type(t),'feature_names') else None
    return out
def dump(obs):
    for t in ['rover','lander','objective','sample','obstacle']:
        try:
            for o in objs(obs,t):
                print(t,o.name,{f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]})
        except Exception as e: print(t,'err',e)
def rov(obs,i):
    r={o.name:o for o in objs(obs,'rover')}['rover%d'%i]
    return {f:float(obs.get(r,f)) for f in obs.type_features[r.type]}
class Driver:
    def __init__(self,seed):
        self.obs,self.info=env.reset(seed=seed); self.R=0; self.steps=0; self.term=False
    def step(self,a0=(0,0,0),s0='noop',a1=(0,0,0),s1='noop'):
        a=np.array([*a0,SEL[s0],*a1,SEL[s1]],dtype=np.float32)
        self.obs,r,te,tr,info=env.step(a); self.R+=r; self.steps+=1; self.term=te
        self.last=(r,te,tr,info); return self.obs,r,te,tr,info
    def goto(self,i,tx,ty,tol=1e-3,maxn=200):
        for _ in range(maxn):
            p=rov(self.obs,i); dx,dy=tx-p['x'],ty-p['y']; d=math.hypot(dx,dy)
            if d<tol: return True
            s=min(1,0.2/max(abs(dx),abs(dy),1e-9)); mv=(dx*s,dy*s,0)
            self.step(mv if i==0 else (0,0,0),'noop',mv if i==1 else (0,0,0),'noop')
            q=rov(self.obs,i)
            if abs(q['x']-p['x'])+abs(q['y']-p['y'])<1e-6: return False
        return False
    def turn(self,i,th):
        for _ in range(50):
            p=rov(self.obs,i); d=(th-p['theta']+math.pi)%(2*math.pi)-math.pi
            if abs(d)<1e-4: return True
            d=max(-0.4,min(0.4,d)); mv=(0,0,d)
            self.step(mv if i==0 else (0,0,0),'noop',mv if i==1 else (0,0,0),'noop')
        return False
    def act(self,i,sel):
        return self.step((0,0,0),sel if i==0 else 'noop',(0,0,0),sel if i==1 else 'noop')

def goto_fine(D,i,tx,ty,maxn=300):
    """straight line; on block, halve step until 0.005; returns (reached, pos)"""
    for _ in range(maxn):
        p=rov(D.obs,i); dx,dy=tx-p['x'],ty-p['y']; d=math.hypot(dx,dy)
        if d<1e-3: return True,(p['x'],p['y'])
        step=0.2
        while True:
            s=min(1,step/max(abs(dx),abs(dy),1e-9)); mv=(dx*s,dy*s,0)
            D.step(mv if i==0 else (0,0,0),'noop',mv if i==1 else (0,0,0),'noop')
            q=rov(D.obs,i)
            if abs(q['x']-p['x'])+abs(q['y']-p['y'])>1e-7: break
            step/=2
            if step<0.004: return False,(q['x'],q['y'])
    return False,(q['x'],q['y'])
