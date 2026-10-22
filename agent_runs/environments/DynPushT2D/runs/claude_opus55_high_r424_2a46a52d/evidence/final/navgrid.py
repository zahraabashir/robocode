"""Grid shortest-path distances around the T-block (scipy csgraph Dijkstra)."""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

LO, HI = 0.1, 4.9
RES = 0.05
NG = int(round((HI - LO) / RES)) + 1
_xs = LO + np.arange(NG) * RES
_X, _Y = np.meshgrid(_xs, _xs, indexing="ij")
PTS = np.stack([_X.ravel(), _Y.ravel()], 1)
_idx = np.arange(NG * NG).reshape(NG, NG)
_E = []
for di, dj, w in [(1, 0, 1.0), (0, 1, 1.0), (1, 1, 2 ** 0.5), (1, -1, 2 ** 0.5)]:
    a = _idx[max(0, -di):NG - max(0, di), max(0, -dj):NG - max(0, dj)]
    b = _idx[max(0, di):NG - max(0, -di) if max(0, -di) else NG, max(0, dj):NG - max(0, -dj) if max(0, -dj) else NG]
    _E.append((a.ravel(), b.ravel(), w))
EA = np.concatenate([e[0] for e in _E])
EB = np.concatenate([e[1] for e in _E])
EW = np.concatenate([np.full(len(e[0]), e[2]) for e in _E]) * RES


def cell_of(p):
    i = np.clip(np.round((np.asarray(p)[..., 0] - LO) / RES).astype(int), 0, NG - 1)
    j = np.clip(np.round((np.asarray(p)[..., 1] - LO) / RES).astype(int), 0, NG - 1)
    return i * NG + j


class NavGrid:
    def __init__(self, model, pos, th, clear):
        d = model.world_dist(np.repeat(np.asarray(pos)[None], len(PTS), 0), np.full(len(PTS), th), PTS)
        self.free = d >= clear
        m = self.free[EA] & self.free[EB]
        a, b, w = EA[m], EB[m], EW[m]
        self.G = csr_matrix((np.concatenate([w, w]), (np.concatenate([a, b]), np.concatenate([b, a]))),
                            shape=(NG * NG, NG * NG))

    def nearest_free(self, p):
        c = int(cell_of(p))
        if self.free[c]:
            return c
        fi = np.flatnonzero(self.free)
        dd = ((PTS[fi] - np.asarray(p)) ** 2).sum(1)
        return int(fi[np.argmin(dd)])

    def from_source(self, p):
        src = self.nearest_free(p)
        dist, pred = dijkstra(self.G, directed=False, indices=src, return_predecessors=True)
        return src, dist, pred

    def dist_to(self, dist, pts, src_p):
        """path length estimates from source to each of pts (N,2)."""
        c = cell_of(pts)
        base = dist[c]
        # fallback: pts in non-free cells -> look at 3x3 neighbourhood
        bad = ~np.isfinite(base) | ~self.free[c]
        if bad.any():
            ci, cj = c // NG, c % NG
            best = np.full(len(c), np.inf)
            for di in (-2, -1, 0, 1, 2):
                for dj in (-2, -1, 0, 1, 2):
                    ii = np.clip(ci + di, 0, NG - 1)
                    jj = np.clip(cj + dj, 0, NG - 1)
                    cc = ii * NG + jj
                    val = np.where(self.free[cc], dist[cc] + np.linalg.norm(PTS[cc] - pts, axis=1), np.inf)
                    best = np.minimum(best, val)
            base = np.where(bad, best, base)
        return base + np.linalg.norm(pts - PTS[c], axis=1) * 0.0

    def path(self, pred, src, dst):
        cells = [dst]
        while cells[-1] != src and cells[-1] >= 0:
            cells.append(pred[cells[-1]])
        if cells[-1] != src:
            return None
        return PTS[np.array(cells[::-1])]
