import numpy as np

def rpy_mat(r, p, y):
    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
    return np.array([[cy*cp, cy*sp*sr - sy*cr, cy*sp*cr + sy*sr],
                     [sy*cp, sy*sp*sr + cy*cr, sy*sp*cr - cy*sr],
                     [-sp, cp*sr, cp*cr]])

def tf(xyz, rpy):
    T = np.eye(4); T[:3, :3] = rpy_mat(*rpy); T[:3, 3] = xyz; return T

def rotz(q):
    c, s = np.cos(q), np.sin(q)
    T = np.eye(4); T[0, 0] = c; T[0, 1] = -s; T[1, 0] = s; T[1, 1] = c; return T

PI = np.pi
JOINTS = [
    tf([0, 0, 0.15643], [PI, 0, 0]),
    tf([0, 0.005375, -0.12838], [PI/2, 0, 0]),
    tf([0, -0.21038, -0.006375], [-PI/2, 0, 0]),
    tf([0, 0.006375, -0.21038], [PI/2, 0, 0]),
    tf([0, -0.20843, -0.006375], [-PI/2, 0, 0]),
    tf([0, 0.00017505, -0.10593], [PI/2, 0, 0]),
    tf([0, -0.10593, -0.00017505], [-PI/2, 0, 0]),
]
EE = tf([0, 0, -0.061525], [PI, 0, 0])
BASE_Z = -0.0052
TOOL = 0.12
MOUNT_X = 0.12

def fk(base, q, tool=None, base_z=None):
    tool = TOOL if tool is None else tool
    base_z = BASE_Z if base_z is None else base_z
    T = np.eye(4)
    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
    M = np.eye(4); M[0, 3] = MOUNT_X; T = T @ M
    for J, qi in zip(JOINTS, q):
        T = T @ J @ rotz(qi)
    T = T @ EE
    Tt = np.eye(4); Tt[2, 3] = tool
    return T @ Tt

_JR = [J[:3, :3].copy() for J in JOINTS]
_JP = [J[:3, 3].copy() for J in JOINTS]
_EER = EE[:3, :3].copy(); _EEP = EE[:3, 3].copy()

def fk_jac(base, q, tool=None, base_z=None):
    tool = TOOL if tool is None else tool
    base_z = BASE_Z if base_z is None else base_z
    c0, s0 = np.cos(base[2]), np.sin(base[2])
    R = np.array([[c0, -s0, 0.0], [s0, c0, 0.0], [0.0, 0.0, 1.0]])
    p = np.array([base[0] + MOUNT_X * c0, base[1] + MOUNT_X * s0, base_z])
    axes = np.empty((7, 3)); origins = np.empty((7, 3))
    cq = np.cos(q); sq = np.sin(q)
    for i in range(7):
        p = p + R @ _JP[i]
        R = R @ _JR[i]
        axes[i] = R[:, 2]; origins[i] = p
        c, s_ = cq[i], sq[i]
        x = R[:, 0] * c + R[:, 1] * s_
        y = -R[:, 0] * s_ + R[:, 1] * c
        R = np.column_stack((x, y, R[:, 2]))
    p = p + R @ _EEP
    R = R @ _EER
    p = p + R[:, 2] * tool
    T = np.eye(4); T[:3, :3] = R; T[:3, 3] = p
    Jm = np.empty((6, 7))
    Jm[:3] = np.cross(axes, p - origins).T
    Jm[3:] = axes.T
    return T, Jm

def rot_err(Rc, Rt):
    Re = Rt @ Rc.T
    # axis-angle vector
    ang = np.arccos(np.clip((np.trace(Re) - 1) / 2, -1, 1))
    if ang < 1e-9:
        return np.zeros(3)
    v = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]])
    s = np.sin(ang)
    if s < 1e-6:
        # near pi
        w = np.sqrt(np.maximum((np.diag(Re) + 1) / 2, 0))
        return w * ang
    return v / (2 * s) * ang

def topdown_R(yaw):
    c, s = np.cos(yaw), np.sin(yaw)
    Rz = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return Rz @ np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.0]])

def ik(base, q0, p, R, iters=200, tol=1e-4, wrot=0.5, tool=None, base_z=None, lim=None):
    q = np.array(q0, dtype=float)
    for it in range(iters):
        T, J = fk_jac(base, q, tool, base_z)
        J[3:] *= wrot
        e = np.concatenate([p - T[:3, 3], wrot * rot_err(T[:3, :3], R)])
        if np.linalg.norm(e) < tol:
            return q, True
        lam = 1e-3
        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
        n = np.linalg.norm(dq)
        if n > 0.3: dq *= 0.3 / n
        q += dq
        if lim is not None:
            q = np.clip(q, -lim, lim)
    return q, False
