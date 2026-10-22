import sys
from env_client import make_env
from approach import GeneratedApproach

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
env = make_env(); s, info = env.reset(seed=seed)
a = GeneratedApproach(env.action_space, env.observation_space, {})
a.reset(s, info)
last = None
for k in range(250):
    act = a.get_action(s)
    s, r, term, trunc, info = env.step(act)
    rovers = sorted(a._objs(s, "rover"), key=a._name)
    snap = (tuple(a.phase), tuple((round(a._v(s, x, "x"), 2), round(a._v(s, x, "y"), 2)) for x in rovers))
    if k % 10 == 0 or tuple(a.phase) != (last[0] if last else None):
        print(k + 1, snap, [round(float(x), 2) for x in act], [a.stuck[i] for i in range(2)], a.targets)
    last = snap
    if term or trunc:
        print("END", k + 1, term, trunc); break
env.close()
