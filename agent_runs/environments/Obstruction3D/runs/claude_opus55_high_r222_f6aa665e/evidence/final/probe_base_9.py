from env_client import make_env
import numpy as np
env = make_env()
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
R=None
events=[]
for seed in [1,2]:
  for bx in [-0.07,-0.2,-0.35]:
    for by in [-0.3,0.0,0.3]:
      for j2 in [0.3,0.5,0.7]:
        obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
        steps=[A(i0=bx+0.12)] if abs(bx+0.12)>1e-9 else []
        for a in steps+[A(i1=by)]: obs,*_=env.step(a)
        n=int(round((j2+0.35)/0.1))
        for _ in range(n): obs,*_=env.step(A(i4=.1))
        o0=objs(obs); jj=obs.get(R,"joint_2")
        rej=0
        for d in [0.1]*32+[-0.1]*64:
            j=obs.get(R,"joint_1"); obs,*_=env.step(A(i3=d))
            if abs(obs.get(R,"joint_1")-j)<1e-6: rej+=1
        o=objs(obs); mv={k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6}
        if rej or mv: events.append((seed,bx,by,round(jj,2),rej,mv))
for e in events: print(e)
print(len(events))
env.close()
