import numpy as np

WORLD_X = (0.0, 1.618)
WORLD_Y = (0.0, 1.0)
MAXD = 0.05
ARM_MAX = 0.2
EARLY = True


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.low = np.array(action_space.low, dtype=np.float32)
        self.high = np.array(action_space.high, dtype=np.float32)

    # ------------------------------------------------------------------ utils
    def _parse(self, state):
        robot = None
        rects = {}
        for name in state.get_object_names():
            obj = state.get_object_from_name(name)
            tname = obj.type.name
            if tname == 'crv_robot':
                robot = obj
                continue
            try:
                d = dict(x=float(state.get(obj, 'x')), y=float(state.get(obj, 'y')),
                         w=float(state.get(obj, 'width')), h=float(state.get(obj, 'height')),
                         theta=float(state.get(obj, 'theta')), type=tname, name=name)
            except Exception:
                continue
            # axis aligned bounding box (x,y is a corner, rotation about it)
            c, s = np.cos(d['theta']), np.sin(d['theta'])
            pts = np.array([[0, 0], [d['w'], 0], [d['w'], d['h']], [0, d['h']]])
            rot = pts @ np.array([[c, s], [-s, c]])
            d['x0'] = d['x'] + rot[:, 0].min()
            d['x1'] = d['x'] + rot[:, 0].max()
            d['y0'] = d['y'] + rot[:, 1].min()
            d['y1'] = d['y'] + rot[:, 1].max()
            rects[name] = d
        r = dict(x=float(state.get(robot, 'x')), y=float(state.get(robot, 'y')),
                 theta=float(state.get(robot, 'theta')),
                 R=float(state.get(robot, 'base_radius')),
                 aj=float(state.get(robot, 'arm_joint')),
                 al=float(state.get(robot, 'arm_length')),
                 vac=float(state.get(robot, 'vacuum')),
                 gh=float(state.get(robot, 'gripper_height')),
                 gw=float(state.get(robot, 'gripper_width')))
        return r, rects

    def _clear_y_at(self, x, rects, held=None, aj=None, exclude=()):
        """Min robot y at horizontal pos x so nothing collides (robot above objects)."""
        r = self.r
        if aj is None:
            aj = r['aj']
        R = r['R']
        need = -1.0
        for name, o in rects.items():
            if name in exclude or (held is not None and name == held['name']):
                continue
            x0, x1, y1 = o['x0'], o['x1'], o['y1']
            # base circle
            dx = max(x0 - x, 0.0, x - x1)
            if dx < R:
                need = max(need, y1 + np.sqrt(R * R - dx * dx))
            # arm + gripper
            g0, g1 = x - r['gh'] / 2, x + r['gh'] / 2
            if g1 > x0 and g0 < x1:
                need = max(need, y1 + aj + r['gw'])
            # held object
            if held is not None:
                hx0 = x + held['dx0']
                hx1 = x + held['dx1']
                if hx1 > x0 and hx0 < x1:
                    need = max(need, y1 - held['dy0'])
        return need

    def _clear_y_range(self, a, b, rects, held=None, aj=None, exclude=()):
        lo, hi = min(a, b), max(a, b)
        n = max(2, int(np.ceil((hi - lo) / 0.004)) + 1)
        xs = np.linspace(lo, hi, n)
        return max(self._clear_y_at(x, rects, held, aj, exclude) for x in xs)

    # ----------------------------------------------------------------- reset
    def reset(self, state, info):
        self.phase = 'plan'
        self.task = None
        self.held = None
        self.stuck = 0
        self.last_pos = None
        self.grasp_eps = 0.002
        self.fail_count = {}
        self.t = 0

    # -------------------------------------------------------------- planning
    def _held_info(self, o, r):
        return dict(name=o['name'], dx0=o['x0'] - r['x'], dx1=o['x1'] - r['x'],
                    dy0=o['y0'] - r['y'], dy1=o['y1'] - r['y'])

    def _grasp_xs(self, o, rects):
        """Candidate robot x's to grasp object o from above, best first (only collision-free ones if any)."""
        r = self.r
        top = o['y1']
        cands = np.linspace(o['x0'] + 0.008, o['x1'] - 0.008, 21)
        centre = (o['x0'] + o['x1']) / 2
        out = []
        for cx in cands:
            if cx < WORLD_X[0] + r['R'] + 1e-3 or cx > WORLD_X[1] - r['R'] - 1e-3:
                continue
            need = self._clear_y_at(cx, rects, None, ARM_MAX, exclude=(o['name'],))
            goal = top + ARM_MAX + r['gw'] + self.grasp_eps
            bad = max(0.0, need - goal)
            out.append((round(bad, 4), abs(cx - centre), float(cx)))
        out.sort()
        if not out:
            return [float(np.clip(centre, WORLD_X[0] + r['R'] + 1e-3, WORLD_X[1] - r['R'] - 1e-3))]
        good = [c[2] for c in out if c[0] == 0]
        return good if good else [out[0][2]]

    def _grasp_x(self, o, rects):
        return self._grasp_xs(o, rects)[0]

    def _place_candidates_target(self, blk, surf, rects):
        """Return (list of (n_blockers, cost, rx, ry, blockers), held, gx, gy)."""
        r = self.r
        gxs = self._grasp_xs(blk, rects)
        centre_g = (blk['x0'] + blk['x1']) / 2
        # a handful of grasp offsets: best one, then spread
        if len(gxs) > 5:
            idx = np.linspace(0, len(gxs) - 1, 5).astype(int)
            gxs = [gxs[0]] + [gxs[i] for i in idx]
        bw = blk['x1'] - blk['x0']
        m = 0.004
        lo = surf['x0'] + m
        hi = surf['x1'] - bw - m
        if hi < lo:
            lo = hi = (surf['x0'] + surf['x1']) / 2 - bw / 2
        xs = np.linspace(lo, hi, max(2, int((hi - lo) / 0.004) + 2))
        centre = (surf['x0'] + surf['x1']) / 2 - bw / 2
        best = None
        others = [(n, o) for n, o in rects.items()
                  if o['type'] != 'target_surface' and n != blk['name']]
        for gi, gx in enumerate(gxs):
            gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
            held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
                        dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
            bottom = surf['y1'] + 0.008
            ry = bottom - held['dy0']
            res = []
            for px in xs:
                rx = px - held['dx0']
                if rx < WORLD_X[0] + r['R'] + 1e-3 or rx > WORLD_X[1] - r['R'] - 1e-3:
                    continue
                blockers = []
                for name, o in others:
                    need = self._clear_y_at(rx, {name: o}, held, ARM_MAX)
                    if need > ry - 1e-4:
                        blockers.append(name)
                cost = abs(px - centre) * 0.1 + 0.001 * gi
                res.append((len(blockers), cost, rx, ry, blockers))
            if not res:
                continue
            res.sort(key=lambda t: (t[0], t[1]))
            if best is None or (res[0][0], res[0][1]) < (best[0][0][0], best[0][0][1]):
                best = (res, held, gx, gy)
        if best is None:
            gx = gxs[0]
            gy = blk['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
            held = dict(name=blk['name'], dx0=blk['x0'] - gx, dx1=blk['x1'] - gx,
                        dy0=blk['y0'] - gy, dy1=blk['y1'] - gy)
            return [], held, gx, gy
        return best

    def _drop_spot(self, o, rects, surf, blk):
        r = self.r
        gx = self._grasp_x(o, rects)
        held = dict(name=o['name'], dx0=o['x0'] - gx, dx1=o['x1'] - gx)
        gy = o['y1'] + ARM_MAX + r['gw'] + self.grasp_eps
        held['dy0'] = o['y0'] - gy
        held['dy1'] = o['y1'] - gy
        ry = gy + 0.003
        others = {k: v for k, v in rects.items() if k != o['name']}
        for margin in (0.12, 0.06, 0.02, 0.005):
            best = None
            for rx in np.arange(WORLD_X[0] + r['R'] + 0.002, WORLD_X[1] - r['R'] - 0.002, 0.005):
                x0, x1 = rx + held['dx0'], rx + held['dx1']
                if x0 < WORLD_X[0] or x1 > WORLD_X[1]:
                    continue
                # stay away from the surface
                if x1 > surf['x0'] - margin - 0.02 and x0 < surf['x1'] + margin + 0.02:
                    continue
                ok = True
                for k, v in others.items():
                    if x1 > v['x0'] - margin and x0 < v['x1'] + margin:
                        ok = False
                        break
                if not ok:
                    continue
                if self._clear_y_at(rx, others, held, ARM_MAX) > ry - 1e-4:
                    continue
                cost = abs(rx - gx) + abs(rx - self.r['x']) * 0.2
                if best is None or cost < best[0]:
                    best = (cost, rx)
            if best is not None:
                return best[1], ry, gx, gy
        return None

    def _plan(self, rects):
        surf = None
        blk = None
        for o in rects.values():
            if o['type'] == 'target_surface':
                surf = o
            elif o['type'] == 'target_block':
                blk = o
        cands, held, gx, gy = self._place_candidates_target(blk, surf, rects)
        if not cands or cands[0][0] == 0:
            if cands:
                _, _, rx, ry, _ = cands[0]
            else:
                rx = (surf['x0'] + surf['x1']) / 2 - (held['dx0'] + held['dx1']) / 2
                ry = surf['y1'] + 0.008 - held['dy0']
            return dict(obj=blk['name'], gx=gx, gy=gy, px=rx, py=ry, kind='target')
        blockers = cands[0][4]
        # remove the blocker closest to robot
        blockers = sorted(blockers, key=lambda n: abs((rects[n]['x0'] + rects[n]['x1']) / 2 - self.r['x']))
        name = blockers[0]
        o = rects[name]
        spot = self._drop_spot(o, rects, surf, blk)
        if spot is None:
            rx = WORLD_X[0] + 0.15 if (o['x0'] > 0.8) else WORLD_X[1] - 0.15
            gxx = self._grasp_x(o, rects)
            return dict(obj=name, gx=gxx, gy=o['y1'] + ARM_MAX + self.r['gw'] + self.grasp_eps,
                        px=rx, py=0.6, kind='obst')
        rx, ry, gxx, gyy = spot
        return dict(obj=name, gx=gxx, gy=gyy, px=rx, py=ry, kind='obst')

    # ---------------------------------------------------------------- motion
    def _move_toward(self, gx, gy, rects, held, margin=0.004):
        """One step toward (gx, gy) avoiding collisions, returns (dx, dy)."""
        r = self.r
        x, y = r['x'], r['y']
        dx = float(np.clip(gx - x, -MAXD, MAXD))
        nx = x + dx
        # the height needed over remaining horizontal sweep
        if abs(gx - x) > 1e-6:
            need_rest = self._clear_y_range(nx, gx, rects, held) + margin
            need_step = self._clear_y_range(x, nx, rects, held) + margin
            ty = max(gy, need_rest)
            dy = float(np.clip(ty - y, -MAXD, MAXD))
            if y + dy < need_step:
                dy = float(np.clip(need_step - y, -MAXD, MAXD))
            if y + dy < need_step - 1e-9:
                dx = 0.0
                dy = MAXD
        else:
            dy = float(np.clip(gy - y, -MAXD, MAXD))
        ymax = WORLD_Y[1] - r['R'] - 1e-3
        if y + dy > ymax:
            dy = max(0.0, ymax - y)
        return dx, dy

    def _action(self, dx=0.0, dy=0.0, darm=0.0, vac=0.0):
        a = np.array([dx, dy, 0.0, darm, vac], dtype=np.float32)
        return np.clip(a, self.low, self.high)

    # ------------------------------------------------------------------- act
    def get_action(self, state):
        self.t += 1
        r, rects = self._parse(state)
        self.r = r
        darm = float(np.clip(ARM_MAX - r['aj'], 0, 0.1))
        dth = 0.0
        # keep theta pointing down
        if abs(r['theta'] + np.pi / 2) > 1e-3:
            dth = float(np.clip(-np.pi / 2 - r['theta'], -0.19, 0.19))

        if self.phase == 'plan':
            self.task = self._plan(rects)
            self.phase = 'to_grasp'
            self.held = None
            self.stuck = 0

        task = self.task
        o = rects.get(task['obj'])

        if self.phase == 'to_grasp':
            # recompute grasp height from current object
            gy = o['y1'] + r['aj'] + r['gw'] + self.grasp_eps
            if r['aj'] < ARM_MAX - 1e-6:
                gy = max(gy, r['y'])  # wait for arm to extend before going down much
            if abs(r['x'] - task['gx']) < 1e-4 and abs(r['y'] - gy) < 1e-4 and r['aj'] >= ARM_MAX - 1e-6:
                self.phase = 'grasp'
                self.grasp_pose = (r['x'], r['y'], o['x'], o['y'])
                return self._action(0, 0, 0, 1.0)
            dx, dy = self._move_toward(task['gx'], gy, rects, None)
            # allow reaching the grasp contact height (target object excluded margin)
            if abs(r['x'] - task['gx']) < 1e-6:
                dy = float(np.clip(gy - r['y'], -MAXD, MAXD))
            vac = 0.0
            if (EARLY and abs(r['x'] + dx - task['gx']) < 1e-6 and abs(r['y'] + dy - gy) < 1e-6
                    and r['aj'] + darm >= ARM_MAX - 1e-6):
                vac = 1.0
                self.phase = 'grasp'
            a = self._action(dx, dy, darm, vac)
            a[2] = dth
            return self._check_stuck(a, r)

        if self.phase == 'grasp':
            self.phase = 'lift'
            self.lift_start = (o['x'], o['y'])
            self.held = self._held_info(o, r)
            self.lift_steps = 0

        if self.phase == 'lift' or self.phase == 'carry':
            held = self.held
            # verify object moves with robot
            ex_y = r['y'] + held['dy0']
            if abs(o['y0'] - ex_y) > 0.01 or abs(o['x0'] - (r['x'] + held['dx0'])) > 0.01:
                # grasp failed
                self.fail_count[task['obj']] = self.fail_count.get(task['obj'], 0) + 1
                self.grasp_eps = max(0.0, self.grasp_eps - 0.001)
                self.phase = 'plan'
                return self._action(0, MAXD, darm, 0.0)
            self.held = held = self._held_info(o, r)
            px, py = task['px'], task['py']
            if abs(r['x'] - px) < 1e-4 and abs(r['y'] - py) < 1e-4:
                self.phase = 'release'
            else:
                dx, dy = self._move_toward(px, py, rects, held)
                if abs(r['x'] - px) < 1e-6:
                    dy = float(np.clip(py - r['y'], -MAXD, MAXD))
                vac = 1.0
                if (EARLY and task['kind'] == 'obst' and abs(r['x'] + dx - px) < 1e-6
                        and abs(r['y'] + dy - py) < 1e-6):
                    vac = 0.0
                    self.phase = 'after_release'
                a = self._action(dx, dy, darm, vac)
                a[2] = dth
                res = self._check_stuck(a, r)
                if self.stuck > 4 and self.task['kind'] == 'obst' and r['x'] == px:
                    self.phase = 'release'
                else:
                    return res

        if self.phase == 'release':
            self.phase = 'after_release'
            self.rel_steps = 0
            return self._action(0, 0, 0, 0.0)

        if self.phase == 'after_release':
            self.phase = 'plan'
            self.held = None
            return self.get_action_replan(state)

        return self._action(0, 0, darm, 0.0)

    def get_action_replan(self, state):
        self.t -= 1
        return self.get_action(state)

    def _check_stuck(self, a, r):
        pos = (round(r['x'], 5), round(r['y'], 5))
        if self.last_pos == pos:
            self.stuck += 1
        else:
            self.stuck = 0
        self.last_pos = pos
        if self.stuck > 3:
            # jiggle upward
            a[0] = 0.0
            a[1] = MAXD * 0.5
        return a
