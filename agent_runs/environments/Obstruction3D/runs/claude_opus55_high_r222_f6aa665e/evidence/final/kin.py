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

def fk_all(q, base=(0, 0, 0), base_z=0.0, tool=0.0):
    T = np.eye(4)
    T[:3, :3] = rpy_mat(0, 0, base[2]); T[:3, 3] = [base[0], base[1], base_z]
    frames = [T.copy()]
    for i in range(7):
        T = T @ JOINTS[i] @ rotz(q[i])
        frames.append(T.copy())
    T = T @ EE
    frames.append(T.copy())
    Tt = T.copy(); Tt[:3, 3] = T[:3, 3] + T[:3, 2] * tool
    frames.append(Tt)
    return frames

def ee_pose(q, base, base_z=0.0, tool=0.0):
    return fk_all(q, base, base_z, tool)[-1]

def pose_err(T, pos, R):
    ep = pos - T[:3, 3]
    Re = R @ T[:3, :3].T
    # axis-angle of Re
    ang = np.array([Re[2, 1] - Re[1, 2], Re[0, 2] - Re[2, 0], Re[1, 0] - Re[0, 1]]) * 0.5
    return np.concatenate([ep, ang])

def down_R(yaw):
    # z axis pointing down, x axis along yaw
    c, s = np.cos(yaw), np.sin(yaw)
    x = np.array([c, s, 0.0]); z = np.array([0, 0, -1.0]); y = np.cross(z, x)
    return np.stack([x, y, z], axis=1)

def ik(q0, pos, R, base, base_z=0.0, tool=0.0, iters=200, wrot=0.3, tol=1e-4):
    q = np.array(q0, dtype=float)
    W = np.array([1, 1, 1, wrot, wrot, wrot])
    for it in range(iters):
        T = ee_pose(q, base, base_z, tool)
        e = pose_err(T, pos, R) * W
        if np.linalg.norm(e) < tol:
            break
        J = np.zeros((6, 7)); h = 1e-6
        for i in range(7):
            dq = q.copy(); dq[i] += h
            J[:, i] = (pose_err(ee_pose(dq, base, base_z, tool), pos, R) * W - e) / -h
        lam = 1e-3
        step = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
        n = np.linalg.norm(step)
        if n > 0.3: step *= 0.3 / n
        q += step
    return q, np.linalg.norm(e)

from scipy.spatial.transform import Rotation as _Rot
def pose_err(T, pos, R):
    ep = pos - T[:3, 3]
    ang = _Rot.from_matrix(R @ T[:3, :3].T).as_rotvec()
    return np.concatenate([ep, ang])
