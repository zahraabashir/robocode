import numpy as np

def _rpy(r, p, y):
    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
                     [-sp, cp*sr, cp*cr]])

def _T(xyz, rpy):
    T = np.eye(4); T[:3, :3] = _rpy(*rpy); T[:3, 3] = xyz; return T

PI = np.pi
H = PI / 2
JOINTS = [
    _T((0, 0, 0.15643), (PI, 0, 0)),
    _T((0, 0.005375, -0.12838), (H, 0, 0)),
    _T((0, -0.21038, -0.006375), (-H, 0, 0)),
    _T((0, 0.006375, -0.21038), (H, 0, 0)),
    _T((0, -0.20843, -0.006375), (-H, 0, 0)),
    _T((0, 0.00017505, -0.10593), (H, 0, 0)),
    _T((0, -0.10593, -0.00017505), (-H, 0, 0)),
]
EE = _T((0, 0, -0.061525), (PI, 0, 0))
MOUNT = (0.12, 0.0, -0.0052)
TOOL = 0.12
HOME = np.array([0.0, -0.35, -np.pi, -2.5, 0.0, -0.87, np.pi / 2])

def _rz(q):
    c, s = np.cos(q), np.sin(q)
    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T

def mount_base(base):
    bx, by, br = base
    c, s = np.cos(br), np.sin(br)
    return (bx + c * MOUNT[0] - s * MOUNT[1], by + s * MOUNT[0] + c * MOUNT[1], br)

def _chain(q, base):
    """Returns tool transform and list of (axis, origin) of joints in world."""
    bx, by, br = mount_base(base)
    T = _rz(br); T[0, 3] = bx; T[1, 3] = by; T[2, 3] = MOUNT[2]
    axes = []
    for Tj, qj in zip(JOINTS, q):
        T = T @ Tj
        axes.append((T[:3, 2].copy(), T[:3, 3].copy()))
        T = T @ _rz(qj)
    T = T @ EE
    Tt = np.eye(4); Tt[2, 3] = TOOL
    return T @ Tt, axes

def tool_fk(q, base):
    return _chain(q, base)[0]

def _rot_err(Rc, Rd):
    Re = Rd @ Rc.T
    v = 0.5 * np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
    return v

def tool_ik(q0, p, R, base, iters=60, tol=1e-5, q_nom=None, k_null=0.3):
    q = np.array(q0, dtype=float)
    if q_nom is None:
        q_nom = HOME
    for it in range(iters):
        T, axes = _chain(q, base)
        e = np.concatenate([p - T[:3, 3], _rot_err(T[:3, :3], R)])
        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
            return q, True
        J = np.zeros((6, 7))
        pt = T[:3, 3]
        for j, (z, o) in enumerate(axes):
            J[:3, j] = np.cross(z, pt - o)
            J[3:, j] = z
        JJt = J @ J.T + 1e-6 * np.eye(6)
        Jp = J.T @ np.linalg.inv(JJt)
        dq = Jp @ e
        dn = (q_nom - q + np.pi) % (2 * np.pi) - np.pi
        dq += (np.eye(7) - Jp @ J) @ (k_null * dn)
        n = np.max(np.abs(dq))
        if n > 0.3:
            dq *= 0.3 / n
        q = q + dq
    T, _ = _chain(q, base)
    ok = np.linalg.norm(p - T[:3, 3]) < 1e-3
    return q, ok

def down_R(yaw):
    c, s = np.cos(yaw), np.sin(yaw)
    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
    return np.stack([x, y, z], axis=1)


def wb_fk(x):
    """x = [bx, by, br, q1..q7] -> tool transform."""
    return _chain(x[3:], x[:3])[0]


def wb_ik(x0, p, R, iters=40, tol=1e-5, q_nom=None, k_null=0.3, w_by=1.0, w_br=1.0):
    """Whole-body IK over base y, base rot and the 7 arm joints (base x fixed)."""
    x = np.array(x0, dtype=float)
    if q_nom is None:
        q_nom = HOME
    W = np.array([w_by, w_br] + [1.0] * 7)
    for it in range(iters):
        T, axes = _chain(x[3:], x[:3])
        pt = T[:3, 3]
        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
            return x, True
        J = np.zeros((6, 9))
        J[1, 0] = 1.0
        ez = np.array([0.0, 0.0, 1.0])
        J[:3, 1] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
        J[3:, 1] = ez
        for j, (z, o) in enumerate(axes):
            J[:3, 2 + j] = np.cross(z, pt - o)
            J[3:, 2 + j] = z
        JW = J * W
        Jp = JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6))
        Jp = W[:, None] * Jp
        dv = Jp @ e
        dn = np.zeros(9)
        dn[2:] = k_null * ((q_nom - x[3:] + np.pi) % (2 * np.pi) - np.pi)
        dv += dn - Jp @ (J @ dn)
        n = np.max(np.abs(dv))
        if n > 0.3:
            dv *= 0.3 / n
        x[1:] += dv
    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
    return x, ok


Q_NOM = np.array([0.0, 0.3, -np.pi, -2.15, 0.0, -0.69, 0.0])
K_NOM = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0])


def wb_ik2(x0, p, R, iters=40, tol=1e-5, k_null=0.3, bx_max=-0.12, w_base=1.0):
    """Whole-body IK over base x (<= bx_max), y, rot and the 7 arm joints.
    Null space pulls the arm to an extended nominal posture Q_NOM."""
    x = np.array(x0, dtype=float)
    ez = np.array([0.0, 0.0, 1.0])
    for it in range(iters):
        T, axes = _chain(x[3:], x[:3])
        pt = T[:3, 3]
        e = np.concatenate([p - pt, _rot_err(T[:3, :3], R)])
        if np.linalg.norm(e[:3]) < tol and np.linalg.norm(e[3:]) < 1e-4:
            return x, True
        J = np.zeros((6, 10))
        J[0, 0] = 1.0
        J[1, 1] = 1.0
        J[:3, 2] = np.cross(ez, pt - np.array([x[0], x[1], 0.0]))
        J[3:, 2] = ez
        for j, (z, o) in enumerate(axes):
            J[:3, 3 + j] = np.cross(z, pt - o)
            J[3:, 3 + j] = z
        dn = np.zeros(10)
        dn[3:] = k_null * K_NOM * ((Q_NOM - x[3:] + np.pi) % (2 * np.pi) - np.pi)
        W = np.array([w_base, w_base, w_base] + [1.0] * 7)
        for _ in range(2):
            JW = J * W
            Jp = W[:, None] * (JW.T @ np.linalg.inv(JW @ J.T + 1e-6 * np.eye(6)))
            dv = Jp @ e + dn - Jp @ (J @ dn)
            n = np.max(np.abs(dv))
            if n > 0.3:
                dv *= 0.3 / n
            if x[0] + dv[0] > bx_max + 1e-9 and W[0] > 0:
                W[0] = 0.0
                x[0] = min(x[0], bx_max)
                continue
            break
        x += dv
        x[0] = min(x[0], bx_max) if x0[0] <= bx_max + 1e-9 else x[0]
    ok = np.linalg.norm(p - wb_fk(x)[:3, 3]) < 1e-3
    return x, ok
