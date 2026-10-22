"""Geometry-aware policy for the black-box Rovers environment."""
import math
import heapq
import numpy as np


class GeneratedApproach:
    # Centres of sample, calibrate, image, noop, send, drop selector bands.
    OPS = {"sample": -5/6, "calibrate": -1/2, "image": -1/6,
           "noop": 1/6, "send": 1/2, "drop": 5/6}

    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.space = observation_space
        self.types = {t.name: t for t in observation_space.types}

    def _get(self, s, typ):
        return s.get_objects(self.types[typ])

    def reset(self, state, info):
        self.names = [[o.name for o in self._get(state, "rover")][i] for i in range(2)]
        self.home = []
        for n in self.names:
            r = state.get_object_from_name(n)
            self.home.append((state.get(r, "x"), state.get(r, "y")))
        self.phase = ["work", "work"]
        self.paths = [[], []]
        self.targets = [None, None]
        self.stalls = [0, 0]
        self.lastpos = list(self.home)

    def _rects(self, s):
        ans = []
        for o in self._get(s, "obstacle"):
            ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
        # Lander is a physical obstacle; use a conservative footprint.
        for o in self._get(s, "lander"):
            ans.append((s.get(o,"x"), s.get(o,"y"), .32, .32))
        return ans

    @staticmethod
    def _seg_rect(a, b, rect, pad=0.0):
        # Slab intersection, including boundaries.
        x, y, hx, hy = rect
        lo, hi = 0.0, 1.0
        for p, q, mn, mx in ((a[0], b[0], x-hx-pad, x+hx+pad),
                             (a[1], b[1], y-hy-pad, y+hy+pad)):
            d = q-p
            if abs(d) < 1e-9:
                if p < mn or p > mx: return False
            else:
                u, v = (mn-p)/d, (mx-p)/d
                if u > v: u, v = v, u
                lo, hi = max(lo,u), min(hi,v)
                if lo > hi: return False
        return True

    def _free(self, p, rects, pad=.24):
        if p[0] < -2.30 or p[0] > 2.30 or p[1] < -2.30 or p[1] > 2.30:
            return False
        return not any(abs(p[0]-x) <= hx+pad and abs(p[1]-y) <= hy+pad
                       for x,y,hx,hy in rects)

    def _los(self, p, q, rects):
        # Ignore an obstacle containing the target (objective's own mound).
        for rect in rects:
            x,y,hx,hy = rect
            if abs(q[0]-x) <= hx+1e-5 and abs(q[1]-y) <= hy+1e-5:
                continue
            if self._seg_rect(p, q, rect, .01): return False
        return True

    def _astar(self, start, goals, rects):
        if not goals: return []
        step = .20
        # Lattice anchored at current location, keeping actions exactly feasible.
        def pos(k): return (start[0]+k[0]*step, start[1]+k[1]*step)
        goal = min(goals, key=lambda g: (g[0]-start[0])**2+(g[1]-start[1])**2)
        def h(k):
            p=pos(k); return max(abs(p[0]-goal[0]),abs(p[1]-goal[1]))/step
        openq=[(h((0,0)),0,(0,0))]; parent={}; cost={(0,0):0}
        end=None
        for _ in range(12000):
            if not openq: break
            _,g,k=heapq.heappop(openq)
            if g != cost.get(k): continue
            p=pos(k)
            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= .10**2 for q in goals):
                end=k; break
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                nk=(k[0]+dx,k[1]+dy); np_=pos(nk)
                if not self._free(np_,rects): continue
                # Endpoint checking suffices for convex inflated rectangles at this resolution,
                # except diagonal corner cutting.
                if not self._free((p[0]+dx*step,p[1]),rects) and dx and dy: continue
                if not self._free((p[0],p[1]+dy*step),rects) and dx and dy: continue
                ng=g+1
                if ng < cost.get(nk,10**9):
                    cost[nk]=ng; parent[nk]=k; heapq.heappush(openq,(ng+h(nk),ng,nk))
        if end is None: return []
        ks=[]
        while end != (0,0): ks.append(end); end=parent[end]
        ks.reverse()
        return [pos(k) for k in ks]

    def _candidates(self, s, q, radius, require_los=True):
        rects=self._rects(s); out=[]
        # Fine angular rings give plenty of robust visibility choices.
        for rad in (min(radius*.72,1.55), min(radius*.88,1.82), radius*.55):
            for j in range(32):
                a=2*math.pi*j/32
                p=(q[0]+rad*math.cos(a),q[1]+rad*math.sin(a))
                if self._free(p,rects) and (not require_los or self._los(p,q,rects)):
                    out.append(p)
        return out

    def _choose_task(self, s, i, pos):
        r=s.get_object_from_name(self.names[i])
        rects=self._rects(s)
        # Finish any held sample result, then empty store.
        if s.get(r,"store_full") > .5:
            land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
            if math.dist(pos,q) <= 3.85 and self._los(pos,q,rects): return ("send",pos)
            cs=self._candidates(s,q,3.8,True); return ("nav_send", min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
        # Split objectives deterministically between the rovers.
        need=[]
        for j,o in enumerate(self._get(s,"objective")):
            if j%2==i and s.get(o,"received_image") < .5:
                q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
        if need:
            # If we have an unsent image and can see lander, send opportunistically.
            land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
            if any(s.get(o,"have_image_rover%d"%i)>.5 for o in self._get(s,"objective")):
                if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
            best=None
            for o,q in need:
                # Already photographed by this rover: only needs sending.
                if s.get(o,"have_image_rover%d"%i)>.5: continue
                if math.dist(pos,q)<=1.90 and self._los(pos,q,rects):
                    return (("image" if s.get(r,"calibrated")>.5 else "calibrate"),pos)
                cs=self._candidates(s,q,1.9,True)
                if cs:
                    p=min(cs,key=lambda x:math.dist(pos,x)); val=math.dist(pos,p)
                    if best is None or val<best[0]: best=(val,p)
            if best: return ("nav_image",best[1])
            # All local images taken: go radio.
            cs=self._candidates(s,lq,3.8,True); return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
        # One rover takes stone, the other soil, choosing nearest unreceived sample.
        soil=bool(i)
        samples=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil and s.get(o,"received_analysis")<.5]
        if samples:
            candidates=[]
            for o in samples:
                q=(s.get(o,"x"),s.get(o,"y"))
                if s.get(o,"analyzed_rover%d"%i)>.5:
                    land=self._get(s,"lander")[0]; lq=(s.get(land,"x"),s.get(land,"y"))
                    if math.dist(pos,lq)<=3.85 and self._los(pos,lq,rects): return ("send",pos)
                    cs=self._candidates(s,lq,3.8,True)
                    return ("nav_send",min(cs,key=lambda p:math.dist(pos,p)) if cs else self.home[i])
                q=(s.get(o,"x"),s.get(o,"y"))
                candidates.append((math.dist(pos,q),q))
            q=min(candidates)[1]
            if math.dist(pos,q)<=.24: return ("sample",pos)
            return ("nav_sample",q)
        # No pending work of our nominal class: help with anything globally missing.
        return ("home",self.home[i])

    def get_action(self, state):
        a=np.zeros(8,dtype=np.float32)
        rects=self._rects(state)
        for i in range(2):
            r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
            task,target=self._choose_task(state,i,pos)
            op=task if task in self.OPS else "noop"
            if task.startswith("nav") or task=="home":
                key=(task,round(target[0],2),round(target[1],2))
                if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
                    radius=.24 if task=="nav_sample" else .12
                    goals=[target] if radius<.2 else self._candidates(state,target,radius,False)+[target]
                    self.paths[i]=self._astar(pos,goals,rects)
                    self.targets[i]=key; self.stalls[i]=0
                while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
                if self.paths[i]:
                    wp=self.paths[i][0]
                    a[4*i]=max(-.2,min(.2,wp[0]-pos)); a[4*i+1]=max(-.2,min(.2,wp[1]-pos))
            a[4*i+3]=self.OPS[op]
            moved=math.dist(pos,self.lastpos[i])>.03
            self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
            self.lastpos[i]=pos
        return a
