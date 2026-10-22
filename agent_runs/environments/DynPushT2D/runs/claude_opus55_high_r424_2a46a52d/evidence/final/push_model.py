"""Empirical per-step push model for the T-block env (pure numpy).

Geometry (block local frame, ref point = obs[0:2], theta = obs[2], world = R(theta) @ local + ref):
  bar  = [-L/2, L/2] x [-w, 0]           (ref = midpoint of the bar's TOP edge)
  stem = [-w/2, w/2] x [-(w+V), -w]      (w=obs[12], L=obs[13], V=obs[14])
  COM  = (0, yc), yc = (A1*(-w/2) + A2*(-w-V/2)) / (A1+A2), A1=L*w, A2=V*w  (uniform density)
  k2   = I/m of the union about COM.
Dynamics (robot radius r=obs[28], moves exactly by action a unless blocked by a wall):
  contact if dist(robot_new, T) < g* = r + C_GAP*a_n  (a_n = component of a into the surface)
  effective push u = a * clip((g* - dist)/a_n, 0, 1)   (partial on first-contact step)
  impulse at the surface point p with Coulomb friction MU (point sticks if inside cone):
     v_com = J, omega = cross(p-com, J)/k2, s.t. normal velocity of p equals u_n
  block rotates by omega about COM and COM translates by v_com.
"""
import numpy as np

C_GAP = 0.265
MU = 1.0  # robot-block Coulomb friction (fitted; 0.9/1.1 are worse)
N_SUB = 2  # sub-steps per env step (small accuracy gain)


def _R(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]])


def geometry(obs):
    w, L, V = obs[12], obs[13], obs[14]
    A1, A2 = L * w, V * w
    y1, y2 = -w / 2, -w - V / 2
    yc = (A1 * y1 + A2 * y2) / (A1 + A2)
    I = A1 * (L * L + w * w) / 12 + A1 * (y1 - yc) ** 2 + A2 * (V * V + w * w) / 12 + A2 * (y2 - yc) ** 2
    rects = [(-L / 2, L / 2, -w, 0.0), (-w / 2, w / 2, -w - V, -w)]
    return rects, np.array([0.0, yc]), I / (A1 + A2)


def _closest(q, rects):
    """closest point on union boundary to external point q, distance, outward normal"""
    best = None
    for x0, x1, y0, y1 in rects:
        p = np.array([min(max(q[0], x0), x1), min(max(q[1], y0), y1)])
        d = np.linalg.norm(q - p)
        if best is None or d < best[1]:
            best = (p, d)
    p, d = best
    if d < 1e-12:  # q inside: fall back
        return p, d, np.array([0.0, 1.0])
    return p, d, (q - p) / d


def predict(obs, action, mu=None, c_gap=None, n_sub=None):
    """obs: 45-vector, action: robot delta (2,). returns new block (x, y, theta) in world."""
    n_sub = N_SUB if n_sub is None else n_sub
    c_gap = C_GAP if c_gap is None else c_gap
    x = np.array(obs, float)
    a = np.asarray(action, float)
    for _ in range(n_sub):
        b = _predict1(x, a / n_sub, mu, c_gap * n_sub)
        x[0:3] = b
        x[16:18] = x[16:18] + a / n_sub
    return x[0:3].copy()


def _predict1(obs, action, mu=None, c_gap=None):
    mu = MU if mu is None else mu
    c_gap = C_GAP if c_gap is None else c_gap
    obs = np.asarray(obs, float)
    a = np.asarray(action, float)
    pos, th = obs[0:2], obs[2]
    r = obs[28]
    rects, com, k2 = geometry(obs)
    Rt = _R(th)
    rob1 = obs[16:18] + a
    q = Rt.T @ (rob1 - pos)
    al = Rt.T @ a
    p, d, n = _closest(q, rects)
    a_n = -al @ n  # into-surface component of robot step
    gstar = r + c_gap * max(a_n, 0.0)
    if d >= gstar or a_n <= 1e-12:
        return np.array([pos[0], pos[1], th])
    frac = min((gstar - d) / a_n, 1.0)
    u = al * frac
    rc = p - com
    K = np.eye(2) + np.array([[rc[1] ** 2, -rc[0] * rc[1]], [-rc[0] * rc[1], rc[0] ** 2]]) / k2
    nin = -n
    t = np.array([-nin[1], nin[0]])
    J = np.linalg.solve(K, u)
    jn, jt = J @ nin, J @ t
    if abs(jt) > mu * jn:  # sliding
        dirJ = nin + mu * np.sign(jt) * t
        j = (u @ nin) / (nin @ (K @ dirJ))
        J = j * dirJ
    om = (rc[0] * J[1] - rc[1] * J[0]) / k2
    # rigid update: rotate by om about COM, translate COM by J (local frame of old pose)
    com_w = pos + Rt @ com
    com_w_new = com_w + Rt @ J
    th_new = th + om
    pos_new = com_w_new - _R(th_new) @ com
    th_new = (th_new + np.pi) % (2 * np.pi) - np.pi
    return np.array([pos_new[0], pos_new[1], th_new])
