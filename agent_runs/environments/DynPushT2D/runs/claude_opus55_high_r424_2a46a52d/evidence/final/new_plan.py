    def _rollout(self, pos0, th0, rob0, steps_opts=None):
        """Evaluate all candidate pushes from block pose (pos0, th0), robot rob0.
        Returns dict of arrays over (candidate x stepsize): score, start, a, k, pos, th, rob, cost."""
        m = self.model
        c, s = math.cos(th0), math.sin(th0)
        Rm = np.array([[c, -s], [s, c]])
        r = m.r
        pw = self.c_pts @ Rm.T + pos0
        nw = self.c_nrm @ Rm.T
        start = pw + nw * (r + 0.03)
        ca, sa = np.cos(self.c_ang), np.sin(self.c_ang)
        nin = -nw
        dirs = np.stack([ca * nin[:, 0] - sa * nin[:, 1], sa * nin[:, 0] + ca * nin[:, 1]], 1)
        cur_d = np.linspace(-np.pi, np.pi, 24, endpoint=False)
        cstart = np.repeat(rob0[None], len(cur_d), 0)
        cdirs = np.stack([np.cos(cur_d), np.sin(cur_d)], 1)
        starts = np.concatenate([start, cstart])
        dirs = np.concatenate([dirs, cdirs])
        ok = (starts[:, 0] >= LO + 0.01) & (starts[:, 0] <= HI - 0.01) & \
             (starts[:, 1] >= LO + 0.01) & (starts[:, 1] <= HI - 0.01)
        dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
        ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
        starts, dirs = starts[ok], dirs[ok]
        nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
        nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
        steps_opts = steps_opts or [AMAX, 0.02, 0.008]
        N = len(starts)
        S = len(steps_opts)
        out_score = np.full((S, N), np.inf)
        out_k = np.zeros((S, N), int)
        out_pos = np.zeros((S, N, 2))
        out_th = np.zeros((S, N))
        out_rob = np.zeros((S, N, 2))
        out_cost = np.zeros((S, N))
        out_a = np.zeros((S, N, 2))
        for si, ss in enumerate(steps_opts):
            pos = np.repeat(pos0[None], N, 0)
            th = np.full(N, th0)
            rob = starts.copy()
            a = dirs * ss
            out_a[si] = a
            alive = np.ones(N, bool)
            for k in range(1, self.KMAX + 1):
                nrob = rob + a
                inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
                alive &= inb
                pos_n, th_n = m.step(pos, th, rob, a)
                pos = np.where(alive[:, None], pos_n, pos)
                th = np.where(alive, th_n, th)
                rob = np.where(alive[:, None], nrob, rob)
                cc, sc = np.cos(th), np.sin(th)
                cx = pos[:, 0:1] + cc[:, None] * m.corners[None, :, 0] - sc[:, None] * m.corners[None, :, 1]
                cy = pos[:, 1:2] + sc[:, None] * m.corners[None, :, 0] + cc[:, None] * m.corners[None, :, 1]
                wall = (cx.min(1) < 0.02) | (cx.max(1) > 4.98) | (cy.min(1) < 0.02) | (cy.max(1) > 4.98)
                alive &= ~wall
                cst = self._cost(pos, th)
                tc = self._cost_tight(pos, th)
                total = nav + k
                score = cst + self.STEP_PEN * total
                score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
                score = np.where(alive, score, np.inf)
                better = score < out_score[si]
                if better.any():
                    out_score[si] = np.where(better, score, out_score[si])
                    out_k[si] = np.where(better, k, out_k[si])
                    out_pos[si] = np.where(better[:, None], pos, out_pos[si])
                    out_th[si] = np.where(better, th, out_th[si])
                    out_rob[si] = np.where(better[:, None], rob, out_rob[si])
                    out_cost[si] = np.where(better, cst, out_cost[si])
                if not alive.any():
                    break
        return dict(score=out_score.ravel(), k=out_k.ravel(), pos=out_pos.reshape(-1, 2),
                    th=out_th.ravel(), rob=out_rob.reshape(-1, 2), cost=out_cost.ravel(),
                    a=out_a.reshape(-1, 2), start=np.tile(starts, (S, 1)),
                    nav=np.tile(nav, S))

    def _plan_push(self, obs):
        pos0 = np.array(obs[0:2], float)
        th0 = float(obs[2])
        rob0 = np.array(obs[16:18], float)
        cost0 = float(self._cost(pos0, th0))
        R1 = self._rollout(pos0, th0, rob0)
        order = np.argsort(R1["score"])
        i0 = int(order[0])
        best_i = i0
        if R1["score"][i0] > -5 and self.LOOK > 0:
            # two-stage lookahead over top-M first pushes (distinct-ish)
            cand = []
            for i in order:
                if not np.isfinite(R1["score"][i]):
                    break
                if all(np.abs(R1["pos"][i] - R1["pos"][j]).max() > 0.01 or
                       abs(R1["th"][i] - R1["th"][j]) > 0.02 for j in cand):
                    cand.append(int(i))
                if len(cand) >= self.LOOK:
                    break
            best_tot = np.inf
            for i in cand:
                steps1 = R1["nav"][i] + R1["k"][i]
                R2 = self._rollout(R1["pos"][i], float(R1["th"][i]), R1["rob"][i], [AMAX, 0.02])
                s2 = min(float(R2["score"].min()), R1["score"][i] - self.STEP_PEN * steps1)
                tot = s2 + self.STEP_PEN * steps1
                if tot < best_tot:
                    best_tot, best_i = tot, i
        i = best_i
        best = (float(R1["score"][i]), R1["start"][i].copy(), R1["a"][i].copy(), int(R1["k"][i]),
                float(R1["cost"][i]))
        return best, cost0
