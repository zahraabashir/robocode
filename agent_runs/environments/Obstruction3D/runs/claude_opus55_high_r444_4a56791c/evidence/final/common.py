import numpy as np, kin
JN = [f'joint_{i}' for i in range(1,8)]
def robot(obs): return obs.get_object_from_name('robot')
def getq(obs):
    R = robot(obs); return np.array([obs.get(R,f) for f in JN])
def getbase(obs):
    R = robot(obs); return np.array([obs.get(R,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']])
def objd(obs, n):
    o = obs.get_object_from_name(n)
    return {f: obs.get(o,f) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','grasp_active','pose_qx','pose_qy','pose_qz','pose_qw']}
def move_to(env, obs, qt, grip=0.0, maxd=0.2):
    """step joints toward qt; returns obs, blocked flag"""
    while True:
        q = getq(obs)
        d = np.array(qt) - q
        d = (d + np.pi) % (2*np.pi) - np.pi
        if np.max(np.abs(d)) < 1e-6: return obs, False
        s = max(1.0, np.max(np.abs(d))/maxd)
        a = np.zeros(11, dtype=np.float32); a[3:10] = d/s; a[10]=grip
        obs, r, t, tr, info = env.step(a)
        if np.max(np.abs(getq(obs)-q)) < 1e-7: return obs, True
        if t: return obs, False
