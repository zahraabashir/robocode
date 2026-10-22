from env_client import make_env
import numpy as np
env = make_env()
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
obs,_=env.reset(seed=1)
for _ in range(5): obs,*_=env.step(A(i4=.2))
for _ in range(6): obs,*_=env.step(A(i4=.01))
st=env.get_state(); print(type(st))
R=st.get_object_from_name("robot"); print("j2",st.get(R,"joint_2"))
res=[]
for ob in ["obstruction0","target_block"]:
  for x in np.arange(0.0,0.8,0.1):
    for y in np.arange(-0.6,0.61,0.2):
        s=st.copy(); O=s.get_object_from_name(ob)
        s.set(O,"pose_x",x); s.set(O,"pose_y",y)
        # move other objects far away
        for n in s.get_object_names():
            if n not in ("robot",ob,"target_region"):
                o2=s.get_object_from_name(n); s.set(o2,"pose_y",5.0)
        env.set_state(s)
        o=env.get_state(); p0=np.array([o.get(O,"pose_x"),o.get(O,"pose_y"),o.get(O,"pose_z")])
        rej=0
        for k in range(126):
            o=env.get_state(); jr=o.get(R,"joint_1")
            obs,*_=env.step(A(i3=.05))
            if abs(obs.get(R,"joint_1")-jr)<1e-6: rej+=1; break
        p1=np.array([obs.get(O,"pose_x"),obs.get(O,"pose_y"),obs.get(O,"pose_z")])
        mv=np.abs(p1-p0).max()
        if rej or mv>1e-6: res.append((ob,round(x,2),round(y,2),rej,round(mv,4),round(obs.get(R,"joint_1"),2)))
for r in res: print(r)
print("n events",len(res))
env.close()
