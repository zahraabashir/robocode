"""Pure-numpy one-step model of the push-T block.

Geometry (block local frame, origin = block pose (x, y), theta CCW):
  bar : x in [-Lh/2, Lh/2], y in [-w, 0]         (origin = top-centre of the bar)
  stem: x in [-w/2, w/2],   y in [-w-Lv, -w]
Robot: disc of radius R=0.1, kinematic, moves exactly by the (clipped) action.

Model: per sub-step, the robot moves action/NSUB; for every rectangle of the T that the
robot disc penetrates, an inelastic point-contact impulse (with Coulomb friction) is
applied to the block so the contact point is pushed out of the robot:
    block COM displacement = P / m,  rotation = (r x P) / I   (m = 1, I = K2)
Block velocity is not carried between env steps (quasi-static).
"""
import numpy as np

R_ROBOT = 0.1
ACT_MAX = 0.05
WORLD_LO, WORLD_HI = 0.0, 5.0

# fitted parameters (see fit.py)
PARAMS = dict(cx=None, cy=None, k2=None, mu=0.99, nsub=4, r_eff=0.1015, beta=0.22)


def mass_props(geom):
    """Uniform-density COM (local) and I/m of the T about its COM."""
    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
    a1, a2 = Lh * w, Lv * w
    y1, y2 = -w / 2, -w - Lv / 2
    cy = (a1 * y1 + a2 * y2) / (a1 + a2)
    I = a1 * ((Lh ** 2 + w ** 2) / 12 + (y1 - cy) ** 2) + a2 * ((w ** 2 + Lv ** 2) / 12 + (y2 - cy) ** 2)
    return np.array([0.0, cy]), I / (a1 + a2)


def geom_from_obs(obs):
    """dict(w, Lh, Lv) from an env observation."""
    return dict(w=float(obs[12]), Lh=float(obs[13]), Lv=float(obs[14]))


def _rot(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]])


def t_rects_local(geom):
    """[(x0, x1, y0, y1), ...] for bar and stem in the block frame."""
    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
    return [(-Lh / 2, Lh / 2, -w, 0.0), (-w / 2, w / 2, -w - Lv, -w)]


def t_outline_local(geom):
    """8 vertices (CCW) of the T outline in the block frame."""
    w, Lh, Lv = geom['w'], geom['Lh'], geom['Lv']
    return np.array([(-Lh / 2, 0), (-Lh / 2, -w), (-w / 2, -w), (-w / 2, -w - Lv),
                     (w / 2, -w - Lv), (w / 2, -w), (Lh / 2, -w), (Lh / 2, 0)])


def t_polygon_world(pose, geom):
    """8x2 outline vertices (CCW) in world frame for block pose (x, y, theta)."""
    pose = np.asarray(pose, float)
    return t_outline_local(geom) @ _rot(pose[2]).T + pose[:2]


def t_rects_world(pose, geom):
    """Two 4x2 convex rectangles (bar, stem) in world frame."""
    pose = np.asarray(pose, float)
    Rm = _rot(pose[2])
    out = []
    for x0, x1, y0, y1 in t_rects_local(geom):
        P = np.array([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])
        out.append(P @ Rm.T + pose[:2])
    return out


def block_distance(pose, geom, p):
    """Distance from world point p to the T (0 if inside)."""
    pose = np.asarray(pose, float)
    pl = (np.asarray(p, float) - pose[:2]) @ _rot(pose[2])
    d = np.inf
    for x0, x1, y0, y1 in t_rects_local(geom):
        dx = max(x0 - pl[0], 0.0, pl[0] - x1)
        dy = max(y0 - pl[1], 0.0, pl[1] - y1)
        d = min(d, np.hypot(dx, dy))
    return d


def _rect_contact(pl, rect):
    """Nearest point q on rect to local point pl, outward normal n, distance d."""
    x0, x1, y0, y1 = rect
    q = np.array([min(max(pl[0], x0), x1), min(max(pl[1], y0), y1)])
    v = pl - q
    d = np.hypot(v[0], v[1])
    if d > 1e-9:
        return q, v / d, d
    # centre inside rectangle: push out through the nearest face
    cand = [(pl[0] - x0, np.array([-1.0, 0])), (x1 - pl[0], np.array([1.0, 0])),
            (pl[1] - y0, np.array([0, -1.0])), (y1 - pl[1], np.array([0, 1.0]))]
    dd, n = min(cand, key=lambda c: c[0])
    return pl + n * dd, n, -dd


def predict_step(block_pose, robot_xy, action, geom, params=None):
    """Predict (new_block_pose, new_robot_xy) after one env step.

    block_pose: (x, y, theta); robot_xy: (x, y); action: (dx, dy) (clipped to +-0.05).
    geom: dict(w, Lh, Lv) (see geom_from_obs).
    """
    p = PARAMS if params is None else params
    cg, k2g = mass_props(geom)
    cl = cg if p.get('cx') is None else np.array([p['cx'], p['cy']])
    k2 = k2g if p.get('k2') is None else p['k2']
    mu, nsub, reff0, beta = p['mu'], int(p['nsub']), p['r_eff'], p.get('beta', 0.0)
    pose = np.array(block_pose, float)
    rob = np.array(robot_xy, float)
    a = np.clip(np.asarray(action, float), -ACT_MAX, ACT_MAX)
    lo, hi = WORLD_LO + R_ROBOT, WORLD_HI - R_ROBOT
    rects = t_rects_local(geom)
    for _ in range(nsub):
        new = np.clip(rob + a / nsub, lo, hi)
        da = new - rob
        rob = new
        for rect in rects:
            Rm = _rot(pose[2])
            pl = (rob - pose[:2]) @ Rm
            q, n, d = _rect_contact(pl, rect)
            if d >= reff0:
                continue
            nw = Rm @ n                           # outward normal (towards robot), world
            # block overshoots: ends ~beta*(normal push speed) beyond touching
            delta = reff0 + beta * max(0.0, -np.dot(a, nw)) - d
            tw = np.array([-nw[1], nw[0]])
            com = pose[:2] + Rm @ cl
            r = pose[:2] + Rm @ q - com           # contact point rel. COM
            rp = np.array([-r[1], r[0]])
            K = np.eye(2) + np.outer(rp, rp) / k2  # contact-point compliance
            # desired contact-point displacement: -n*delta (into block), tangential follows robot
            want = -nw * delta + tw * np.dot(da, tw)
            P = np.linalg.solve(K, want)
            Pn, Pt = -np.dot(P, nw), np.dot(P, tw)
            if Pn <= 0:
                continue
            if abs(Pt) > mu * Pn:                 # sliding
                s = np.sign(Pt)
                dirv = -nw + mu * s * tw
                Pn = delta / np.dot(-nw, K @ dirv)
                P = Pn * dirv
            dth = (r[0] * P[1] - r[1] * P[0]) / k2
            com = com + P
            pose[2] += dth
            pose[:2] = com - _rot(pose[2]) @ cl
    return pose, rob


def near_wall(pose, geom, margin=0.02):
    """True if the T is within `margin` of the world walls (x,y in [0,5]); the model
    ignores block-wall contact, so predictions there are unreliable."""
    P = t_polygon_world(pose, geom)
    return bool(P.min() < WORLD_LO + margin or P.max() > WORLD_HI - margin)
