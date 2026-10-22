from env_client import make_env
import numpy as np
env = make_env()
def rob(obs):
    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
tests = [("x+.1",A(i0=.1)),("x-.1",A(i0=-.1)),("y+.1",A(i1=.1)),("y-.1",A(i1=-.1)),("rot+.1",A(i2=.1)),("rot-.1",A(i2=-.1)),
         ("x+.01",A(i0=.01)),("x-.05",A(i0=-.05)),("y+.05",A(i1=.05)),("rot.05",A(i2=.05)),("x-.1y.1rot.1",A(i0=-.1,i1=.1,i2=.1)),
         ("x+.5 clip?",A(i0=.5)),("x-.5",A(i0=-.5))]
for name,a in tests:
    obs,_ = env.reset(seed=1)
    s0 = rob(obs)
    obs,*_ = env.step(a); s1 = rob(obs)
    obs,*_ = env.step(a); s2 = rob(obs)
    print(name, "d1", np.round(s1-s0,5)[:3], "d2", np.round(s2-s1,5)[:3], "other", np.abs(s2-s0)[3:].max().round(5))
env.close()
