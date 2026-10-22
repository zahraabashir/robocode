from env_client import make_env
import numpy as np, math
env = make_env()
SP = env.observation_space
SEL={'sample':-5/6,'calibrate':-0.5,'image':-1/6,'noop':1/6,'send':0.5,'drop':5/6}
FEAT={}
for t in ['rover','lander','objective','sample','obstacle']:
    pass
def objs(obs,t): return sorted(obs.get_objects(SP.get_type(t)),key=lambda o:o.name)
def feats(obs,o,fs): return [round(float(obs.get(o,f)),3) for f in fs]
TF={'rover':['x','y','theta','store_full','calibrated','at_home'],'lander':['x','y','z'],
 'objective':['x','y','z','have_image_rover0','have_image_rover1','received_image'],
 'sample':['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis'],
 'obstacle':['x','y','z','half_x','half_y','half_z']}
def dump(obs,types=TF):
    for t in types:
        for o in objs(obs,t): print(t,o.name,feats(obs,o,TF[t]))
class R:
    def __init__(s,seed):
        s.obs,_=env.reset(seed=seed)
    def rv(s,i):
        o=[r for r in objs(s.obs,'rover') if r.name=='rover%d'%i][0]
        return {f:float(s.obs.get(o,f)) for f in TF['rover']}
    def step(s,a0=(0,0,0),s0='noop',a1=(0,0,0),s1='noop'):
        a=np.array([a0[0],a0[1],a0[2],SEL[s0],a1[0],a1[1],a1[2],SEL[s1]],dtype=np.float32)
        s.obs,r,te,tr,info=env.step(a); s.last=(r,te,tr,info); return s.obs
    def act(s,i,sel):
        if i==0: return s.step(s0=sel)
        return s.step(s1=sel)
    def move(s,i,d):
        if i==0: return s.step(a0=d)
        return s.step(a1=d)
    def goto(s,i,x,y,tol=1e-3,maxit=200):
        for _ in range(maxit):
            r=s.rv(i); dx,dy=x-r['x'],y-r['y']; d=math.hypot(dx,dy)
            if d<tol: return True
            k=min(1,0.19/d); s.move(i,(dx*k,dy*k,0))
            r2=s.rv(i)
            if abs(r2['x']-r['x'])+abs(r2['y']-r['y'])<1e-9: return False
        return False
    def turn(s,i,th):
        for _ in range(50):
            r=s.rv(i); d=(th-r['theta']+math.pi)%(2*math.pi)-math.pi
            if abs(d)<1e-4: return
            s.move(i,(0,0,max(-0.39,min(0.39,d))))
    def objst(s):
        return {o.name:feats(s.obs,o,TF['objective'][3:]) for o in objs(s.obs,'objective')}
def path(r,i,wps):
    for (x,y) in wps:
        if not r.goto(i,x,y):
            print('blocked at',r.rv(i),'going',(x,y)); return False
    return True
