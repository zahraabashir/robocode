# Shared example from the planning-explanations write-up: Appendix A.5, with its dependencies dense_planner.py (A.6) and pose_planner.py (A.7).
# Transcribed from the PDF; only quotes and line wraps were normalised.
import math
import heapq
import numpy as np
from scipy.ndimage import distance_transform_cdt
from dense_planner import DensePlanner
from pose_planner import PosePlanner


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.space = observation_space

    def reset(self, state, info):
        self.robot = next(iter(state.get_objects(self.space.get_type('crv_robot'))))
        targets = list(state.get_objects(self.space.get_type('target_region')))
        self.target = targets[0]
        self.obstacles = []
        for obj in state.get_objects(self.space.get_type('rectangle')):
            if obj in targets:
                continue
            x,y,w,h,t = (state.get(obj, f) for f in ('x', 'y', 'width', 'height', 'theta'))
            c,s = math.cos(t),math.sin(t)
            self.obstacles.append((x+min(w,0)*c-min(h,0)*s,y+min(w,0)*s+min(h,0)*c,abs(w),abs(h),t))
        self.radius = max(state.get(self.robot, 'base_radius'), math.hypot(state.get(self.robot, 'arm_joint') + state.get(self.robot, 'gripper_width')/2, state.get(self.robot, 'gripper_height')/2)) + 0.001
        self.target_data = tuple(state.get(self.target, f) for f in ('x', 'y', 'width', 'height', 'theta'))
        self.path = []
        self.last = None
        self.stuck = 0
        self.h = 0.01
        self.fallback = None
        self.plan(state)
        if not self.solved_plan:
            self.precise_plan(state)

    def precise_plan(self, state):
        self.fallback = DensePlanner(self.action_space, self.space, {})
        self.fallback.reset(state, {})
        if not self.fallback.solved_plan:
            self.fallback = PosePlanner(self.action_space, self.space, {})
            self.fallback.reset(state, {})

    def clear(self, points, radius=None):
        p = np.asarray(points).reshape(-1, 2)
        r = self.radius if radius is None else radius
        good = (p[:, 0] >= r) & (p[:, 0] <= 2.5-r) & (p[:, 1] >= r) & (p[:, 1] <= 2.5-r)
        for x, y, w, h, t in self.obstacles:
            c, s = math.cos(t), math.sin(t)
            dx, dy = p[:, 0]-x, p[:, 1]-y
            u, v = c*dx+s*dy, -s*dx+c*dy
            ex = np.maximum(np.maximum(-u, u-w), 0)
            ey = np.maximum(np.maximum(-v, v-h), 0)
            good &= ex*ex+ey*ey > r*r
        return good

    def segment_clear(self, a, b):
        n = max(2, int(np.max(np.abs(b-a))/0.004)+2)
        return bool(np.all(self.clear(np.linspace(a, b, n))))

    def plan(self, state):
        self.solved_plan = False
        pos = np.array([state.get(self.robot, 'x'), state.get(self.robot, 'y')])
        h = self.h
        self.n = n = int(round(2.5/h))+1
        axes = np.arange(n)*h
        xx, yy = np.meshgrid(axes, axes, indexing='ij')
        pts = np.stack((xx.ravel(), yy.ravel()), axis=-1)
        free = self.clear(pts).reshape(n, n)
        x, y, w, ht, t = self.target_data
        c, s = math.cos(t), math.sin(t)
        u = c*(xx-x)+s*(yy-y)
        v = -s*(xx-x)+c*(yy-y)
        goal = free & (u>0.002) & (u<w-0.002) & (v>0.002) & (v<ht-0.002)
        goals = np.argwhere(goal)
        if not len(goals):
            self.path = [np.array([x+w/2, y+ht/2])]
            return
        start = tuple(np.rint(pos/h).astype(int).clip(0,n-1))
        free[start] = True
        goal_distance = distance_transform_cdt(~goal, metric="chessboard")
        distances = np.full((n,n), np.inf)
        parents = np.full((n,n), -1, dtype=np.int32)
        distances[start] = 0
        heap = [(float(goal_distance[start]),0,start[0],start[1])]
        moves = [(a,b,max(abs(a),abs(b))) for a in (-1,0,1) for b in (-1,0,1) if a or b]
        end = None
        while heap:
            _, negative_d, i, j = heapq.heappop(heap)
            d = -negative_d
            if d > distances[i,j]+1e-8:
                continue
            if goal[i,j]:
                end = (i,j)
                break
            for a,b,cost in moves:
                ni,nj = i+a,j+b
                if not(0<=ni<n and 0<=nj<n) or not free[ni,nj]:
                    continue
                if a and b and not(free[i,nj] and free[ni,j]):
                    continue
                nd = d+cost
                if nd < distances[ni,nj]:
                    distances[ni,nj] = nd
                    parents[ni,nj] = i*n+j
                    heapq.heappush(heap,(nd+goal_distance[ni,nj],-nd,ni,nj))
        if end is None:
            self.path = [goals[np.argmin(np.sum((goals*h-pos)**2,axis=1))]*h]
            return
        rev = []
        while end != start:
            rev.append(np.array(end)*h)
            idx = int(parents[end])
            end = (idx//n, idx%n)
        self.solved_plan = True
        raw_path = list(reversed(rev))
        self.path = []
        anchor = pos
        begin = 0
        while begin < len(raw_path):
            chosen = begin
            for k in range(len(raw_path)-1, begin-1, -1):
                if self.segment_clear(anchor, raw_path[k]):
                    chosen = k
                    break
            self.path.append(raw_path[chosen])
            anchor = raw_path[chosen]
            begin = chosen+1

    def get_action(self, state):
        if self.fallback is not None:
            return self.fallback.get_action(state)
        pos = np.array([state.get(self.robot, 'x'), state.get(self.robot, 'y')])
        if self.last is not None and np.max(np.abs(pos-self.last)) < 1e-7:
            self.stuck += 1
        else:
            self.stuck = 0
        self.last = pos.copy()
        if self.stuck in (3, 8):
            self.radius += 0.002
            self.plan(state)
            if not self.solved_plan:
                self.precise_plan(state)
                return self.fallback.get_action(state)
        while self.path and np.max(np.abs(self.path[0]-pos)) < 0.002:
            self.path.pop(0)
        if not self.path:
            x,y,w,h,t = self.target_data
            self.path = [np.array([x+w/2,y+h/2])]
        choice = 0
        # The furthest visible waypoint gives a continuous, smoothed path.
        for k in range(len(self.path)-1,-1,-1):
            if self.segment_clear(pos,self.path[k]):
                choice = k
                break
        if choice:
            self.path = self.path[choice:]
        delta = self.path[0]-pos
        delta *= min(1.,0.05/max(1e-10,float(np.max(np.abs(delta)))))
        theta = state.get(self.robot, 'theta')
        turn = (0.-theta+math.pi)%(2*math.pi)-math.pi
        return np.array([delta[0],delta[1],np.clip(turn,-0.19634954,0.19634954),-0.1,0],dtype=np.float32)
