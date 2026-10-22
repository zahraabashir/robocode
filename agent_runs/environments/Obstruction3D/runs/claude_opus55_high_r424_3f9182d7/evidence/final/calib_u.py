from env_client import make_env
import numpy as np, kin
F=['joint_%d'%i for i in range(1,8)]
class R:
    def __init__(s): s.env=make_env()
    def reset(s,seed):
        s.obs,_=s.env.reset(seed=seed); s.r=s.obs.get_object_from_name('robot'); return s.obs
    def g(s,name,f): return s.obs.get(s.obs.get_object_from_name(name),f)
    def rob(s,f): return s.obs.get(s.r,f)
    def q(s): return np.array([s.rob(f) for f in F])
    def base(s): return (s.rob('pos_base_x'),s.rob('pos_base_y'),s.rob('pos_base_rot'))
    def blk(s,name='target_block'): return np.array([s.g(name,f) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
    def step(s,a):
        a=np.asarray(a,dtype=np.float32); s.obs,rew,term,trunc,info=s.env.step(a); return rew,term,info
    def stepq(s,dq,grip=0.0,db=(0,0,0)):
        a=np.zeros(11,np.float32); a[:3]=db; a[3:10]=dq; a[10]=grip
        v0=s.env and np.concatenate([s.q(),s.base()]); s.step(a)
        return not np.allclose(v0,np.concatenate([s.q(),s.base()]))
    def goq(s,qt,grip=0.0):
        q=s.q()
        while np.max(np.abs(qt-q))>1e-6:
            if not s.stepq(np.clip(qt-q,-0.19,0.19),grip): return False
            q=s.q()
        return True
    def go(s,p,yaw=0.0,grip=0.0,R=None,tool=None):
        qt,ok=kin.ik(s.base(),s.q(),np.array(p,float),kin.down_R(yaw) if R is None else R,tool=tool)
        if not ok: return None
        return s.goq(qt,grip)
    def ee(s,tool=None): return kin.fk(s.base(),s.q(),tool)
