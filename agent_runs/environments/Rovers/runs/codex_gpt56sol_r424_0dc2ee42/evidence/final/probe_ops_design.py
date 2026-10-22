import numpy as np
from env_client import make_env


SAMPLE = -5 / 6
SEND = 1 / 2


env = make_env()
obs, _ = env.reset(seed=1)
st = next(t for t in env.observation_space.types if t.name == "sample")
rv = next(t for t in env.observation_space.types if t.name == "rover")
r0 = sorted(obs.get_objects(rv), key=lambda o: o.name)[0]
s3 = sorted(obs.get_objects(st), key=lambda o: o.name)[3]


def status(label):
    print(label, "rover", [float(obs.get(r0, f)) for f in ("x", "y", "store_full")],
          "sample", [float(obs.get(s3, f)) for f in ("analyzed_rover0", "received_analysis")])


status("start")
for k in range(2):
    a = np.zeros(8, np.float32)
    a[:2] = (-.2, .2)
    if k == 1:
        a[3] = SAMPLE
    obs, *_ = env.step(a)
    status("move/sample")
for pos_label, delta in (("send-here", (0, 0)), ("south", (0, -.2)), ("south", (0, -.2)),
                         ("west", (-.2, 0)), ("west", (-.2, 0))):
    a = np.zeros(8, np.float32)
    a[:2] = delta
    a[3] = SEND
    obs, *_ = env.step(a)
    status(pos_label)
for k in range(3):
    a = np.zeros(8, np.float32)
    a[1] = -.2
    a[3] = SEND
    obs, *_ = env.step(a)
    status("gap-send")
env.close()
