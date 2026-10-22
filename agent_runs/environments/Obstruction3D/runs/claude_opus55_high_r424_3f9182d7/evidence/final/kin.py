import numpy as np
PI = np.pi

def _rpy(r, p, y):
    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],
                     [sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],
                     [-sp, cp*sr, cp*cr]])

def _T(xyz, R):
    M = np.eye(4); M[:3, :3] = R; M[:3, 3] = xyz; return M

def _rz(q):
    c, s = np.cos(q), np.sin(q)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])

_J = [((0, 0, 0.15643), (PI, 0, 0)), ((0, 0.005375, -0.12838), (PI/2, 0, 0)),
      ((0, -0.21038, -0.006375), (-PI/2, 0, 0)), ((0, 0.006375, -0.21038), (PI/2, 0, 0)),
      ((0, -0.20843, -0.006375), (-PI/2, 0, 0)), ((0, 0.00017505, -0.10593), (PI/2, 0, 0)),
      ((0, -0.10593, -0.00017505), (-PI/2, 0, 0))]
_JT = [_T(xyz, _rpy(*r)) for xyz, r in _J]
_EE = _T((0, 0, -0.061525), _rpy(PI, 0, 0))

BASE_Z = 0.0
TOOL = 0.0
# Calibrated from grasped-block poses (fit rms 5e-7 m): the arm's base link sits at
# this offset from (pos_base_x, pos_base_y, 0), expressed in the mobile-base frame.
ARM_OFFSET = (0.1199, 0.0, -0.0052)
# grasp_tf_* is the block pose relative to the frame end_effector_link @ Tz(GRASP_Z).
GRASP_Z = 0.12

def fk(base, q, tool=None):
    if tool is None:
        tool = TOOL
    bx, by, br = base
    M = _T((bx, by, BASE_Z), _rz(br)) @ _T(ARM_OFFSET, np.eye(3))
    for Jt, qi in zip(_JT, q):
        M = M @ Jt @ _T((0, 0, 0), _rz(qi))
    M = M @ _EE
    if tool:
        M = M @ _T((0, 0, tool), np.eye(3))
    return M

def _err(M, pos, R):
    ep = pos - M[:3, 3]
    Re = R @ M[:3, :3].T
    # rotation error as proper axis-angle (log map); the old skew-only version
    # was blind to 180-degree flips and let IK converge to flipped wrists.
    v = 0.5 * np.array([Re[2, 1]-Re[1, 2], Re[0, 2]-Re[2, 0], Re[1, 0]-Re[0, 1]])
    c = np.clip((np.trace(Re) - 1) / 2, -1.0, 1.0); sn = np.linalg.norm(v)
    ang = np.arctan2(sn, c)
    if sn > 1e-9:
        eo = v / sn * ang
    elif c > 0:
        eo = v
    else:  # ~180 deg: axis from the symmetric part
        B = (Re + np.eye(3)) / 2
        ax = B[:, np.argmax(np.diag(B))]; eo = ax / np.linalg.norm(ax) * np.pi
    return np.concatenate([ep, eo])

def ik(base, q0, pos, R, iters=200, tol=1e-4, rot_w=0.3, tool=None):
    q = np.array(q0, dtype=float)
    W = np.array([1, 1, 1, rot_w, rot_w, rot_w])
    for _ in range(iters):
        M = fk(base, q, tool)
        e = _err(M, pos, R) * W
        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < tol*3:
            return q, True
        Jm = np.zeros((6, 7))
        h = 1e-6
        for i in range(7):
            dq = q.copy(); dq[i] += h
            Jm[:, i] = (_err(M, pos, R) - _err(fk(base, dq, tool), pos, R)) * W / h
        lam = 1e-3
        d = Jm.T @ np.linalg.solve(Jm @ Jm.T + lam*np.eye(6), e)
        n = np.max(np.abs(d))
        if n > 0.3:
            d *= 0.3 / n
        q = q + d
    M = fk(base, q, tool)
    e = _err(M, pos, R)
    return q, bool(np.linalg.norm(e[:3]) < 1e-3 and np.linalg.norm(e[3:]) < 1e-2)

def down_R(yaw):
    # gripper z axis pointing down, x axis direction by yaw
    c, s = np.cos(yaw), np.sin(yaw)
    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
    return np.stack([x, y, z], axis=1)
