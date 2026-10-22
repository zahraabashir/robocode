import itertools
import numpy as np
from env_client import make_env


def v(s, n, f): return float(s.get(s.get_object_from_name(n), f))


patterns = [
    (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0), (1, 0, 1), (-1, 0, -1),
    (1, 1, 1), (-1, -1, -1), (1, -1, 1), (-1, 1, -1),
]
for pat in patterns:
    env = make_env(); s, _ = env.reset(seed=0)
    ty = v(s, "target_block", "pose_y")
    base = (v(s,"target_block","pose_x"), ty, v(s,"target_block","pose_z"))
    # align laterally
    a=np.zeros(11,np.float32); a[1]=np.clip(ty-v(s,"robot","pos_base_y"),-.2,.2)
    s,*_=env.step(a)
    found = None; maxmove=0
    for t in range(120):
        a=np.zeros(11,np.float32)
        # Oscillate every 20 steps to scan rather than pin at limit.
        sg = 1 if (t//20)%2==0 else -1
        a[4]=.12*pat[0]*sg; a[6]=.12*pat[1]*sg; a[8]=.12*pat[2]*sg; a[10]=-1
        s,r,te,tr,info=env.step(a)
        xyz=(v(s,"target_block","pose_x"),v(s,"target_block","pose_y"),v(s,"target_block","pose_z"))
        maxmove=max(maxmove, sum((xyz[i]-base[i])**2 for i in range(3))**.5)
        if v(s,"robot","grasp_active") or v(s,"target_block","grasp_active"):
            found=(t,xyz,[v(s,"robot",f"joint_{i}") for i in range(1,8)],
                   [v(s,"robot",f"grasp_tf_{c}") for c in "xyz"])
            break
    print("PAT",pat,"found",found,"maxmove",round(maxmove,5),"final joints",[round(v(s,"robot",f"joint_{i}"),3) for i in range(1,8)])
    env.close()
