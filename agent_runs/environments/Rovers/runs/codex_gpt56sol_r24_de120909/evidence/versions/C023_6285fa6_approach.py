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
        self.extra_rects=[[],[]]
        self.last_motion=[None,None]
        self.radio_choices=[self._radio_points(state,i) for i in range(2)]
        self.radio_idx=[0,0]
        self.last_ops=["noop","noop"]
        # Pick one concrete sample of each required kind and give it to the rover
        # already on that side of the wall.
        self.sample_jobs = [{}, {}]
        for soil in (False, True):
            choices=[]
            land=self._get(state,"lander")[0]
            lq=(state.get(land,"x"),state.get(land,"y"))
            for o in self._get(state,"sample"):
                if bool(state.get(o,"is_soil")>.5) != soil: continue
                x,y=state.get(o,"x"),state.get(o,"y")
                owner=0 if x>=0 else 1
                # Samples squeezed between the large lander and southwest arena
                # corner are not drive-reachable; prefer either of the other two.
                trapped = owner==1 and math.dist((x,y),lq)<.60
                edge = abs(x)>2.20 or abs(y)>2.20
                pillars=self._rects(state)[5:]  # skip wall, four mounds
                pinched=any(math.dist((x,y),(r[0],r[1]))<.34 for r in pillars)
                choices.append((int(trapped or edge or pinched),math.dist(self.home[owner],(x,y)),owner,o.name))
            if choices:
                _,_,owner,name=min(choices)
                self.sample_jobs[owner][soil]=name

    def _radio_points(self,s,i):
        land=self._get(s,"lander")[0]; q=(s.get(land,"x"),s.get(land,"y"))
        if i==0:
            raw=[(x,y) for y in (.25,.45,.65,.85)
                 for x in (.35,.55,.75,.95,1.15,1.35)]
        else:
            raw=[(-1.0,-1.75),(-1.0,-1.45),(-1.3,-1.6),(-1.5,-1.4),(-1.7,-1.2)]
        rects=self._rects(s)[1:] # wall is low enough to radio over from right poses
        free=[]; good=[]
        for p in raw:
            if math.dist(p,q)>=3.9 or not self._free(p,self._rects(s)): continue
            free.append(p)
            if not any(self._seg_rect(p,q,r,.07) for r in rects): good.append(p)
        # Try predicted-clear rays first, but retain every collision-free pose so
        # silent failures can be escaped even when the crude 2-D LOS model is wrong.
        return good+[p for p in free if p not in good]

    def _radio(self,i):
        pts=self.radio_choices[i]
        return pts[self.radio_idx[i] % len(pts)]

    def _rects(self, s):
        # The central wall is a fixed part of the arena but is intentionally not
        # listed among observation objects.  Its narrow ends leave routes around
        # it at the north and south edges.
        ans = [(0.0, 0.0, .03, 2.50)]
        for o in self._get(s, "obstacle"):
            ans.append((s.get(o,"x"), s.get(o,"y"), s.get(o,"half_x"), s.get(o,"half_y")))
        # Lander is a physical obstacle; use a conservative footprint.
        for o in self._get(s, "lander"):
            # Its collision body is compact (rover1 starts only .25 m north of it).
            ans.append((s.get(o,"x"), s.get(o,"y"), .04, .04))
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

    def _free(self, p, rects, pad=.20):
        if p[0] < -2.27 or p[0] > 2.27 or p[1] < -2.27 or p[1] > 2.27:
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

    def _astar(self, start, goals, rects, tolerance=.18):
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
            if any((p[0]-q[0])**2+(p[1]-q[1])**2 <= tolerance**2 for q in goals):
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
        endpos=pos(end)
        ks=[]
        while end != (0,0): ks.append(end); end=parent[end]
        ks.reverse()
        path=[pos(k) for k in ks]
        final=min(goals,key=lambda q:math.dist(endpos,q))
        if self._free(final,rects) and math.dist(endpos,final)>.025:
            path.append(final)
        return path

    def _candidates(self, s, q, radius, require_los=True):
        rects=self._rects(s); out=[]
        # Fine angular rings give plenty of robust visibility choices.
        rings=[min(radius*.72,1.55), min(radius*.88,1.68), radius*.55]
        if radius<.5: rings.insert(0,radius*.98)
        for rad in rings:
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
            pending_analysis = any(s.get(o,"analyzed_rover%d"%i)>.5 and
                                   s.get(o,"received_analysis")<.5
                                   for o in self._get(s,"sample"))
            if not pending_analysis:
                return ("drop",pos)
            q=self._radio(i)
            return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
        # Each rover handles objectives on its own side of the short south wall.
        need=[]
        for j,o in enumerate(self._get(s,"objective")):
            owner=0 if s.get(o,"x")>=0 else 1
            if owner==i and s.get(o,"received_image") < .5:
                q=(s.get(o,"x"),s.get(o,"y")); need.append((o,q))
        if need:
            # If we have an unsent image and can see lander, send opportunistically.
            if any(s.get(o,"have_image_rover%d"%i)>.5 and s.get(o,"received_image")<.5
                   for o in self._get(s,"objective")):
                q=self._radio(i)
                return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
            best=None
            for o,q in need:
                # Already photographed by this rover: only needs sending.
                if s.get(o,"have_image_rover%d"%i)>.5: continue
                if math.dist(pos,q)<=1.72 and self._los(pos,q,rects):
                    return (("image" if s.get(r,"calibrated")>.5 else "calibrate"),pos)
                cs=self._candidates(s,q,1.9,True)
                if cs:
                    p=min(cs,key=lambda x:math.dist(pos,x)); val=math.dist(pos,p)
                    if best is None or val<best[0]: best=(val,p)
            if best: return ("nav_image",best[1])
            # All local images taken: go radio.
            return ("nav_send",self._radio(i))
        # Execute the preassigned one-stone/one-soil jobs (possibly both on one rover).
        soil=None
        chosen_name=None
        for kind,name in sorted(self.sample_jobs[i].items()):
            matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==kind]
            if not any(s.get(o,"received_analysis")>.5 for o in matching):
                soil=kind; chosen_name=name; break
        if soil is None: return ("home",self.home[i])
        matching=[o for o in self._get(s,"sample") if bool(s.get(o,"is_soil")>.5)==soil]
        samples=[s.get_object_from_name(chosen_name)]
        if samples:
            candidates=[]
            for o in samples:
                q=(s.get(o,"x"),s.get(o,"y"))
                if s.get(o,"analyzed_rover%d"%i)>.5:
                    q=self._radio(i)
                    return ("send",pos) if math.dist(pos,q)<.16 else ("nav_send",q)
                q=(s.get(o,"x"),s.get(o,"y"))
                candidates.append((math.dist(pos,q),q))
            q=min(candidates)[1]
            # Aim well inside the inclusive .25 m server cutoff; stopping near its
            # floating-point boundary proved brittle on diagonals.
            if math.dist(pos,q)<=.18: return ("sample",pos)
            return ("nav_sample",q)
        # No pending work of our nominal class: help with anything globally missing.
        return ("home",self.home[i])

    def get_action(self, state):
        a=np.zeros(8,dtype=np.float32)
        base_rects=self._rects(state)
        for i in range(2):
            r=state.get_object_from_name(self.names[i]); pos=(state.get(r,"x"),state.get(r,"y"))
            if self.last_motion[i] is not None and math.dist(pos,self.lastpos[i])<.0005:
                bx,by=self.last_motion[i]
                if not any(math.dist((bx,by),(r[0],r[1]))<.08 for r in self.extra_rects[i]):
                    self.extra_rects[i].append((bx,by,.07,.07))
                    self.extra_rects[i]=self.extra_rects[i][-12:]
                self.paths[i]=[]; self.targets[i]=None
            rects=base_rects+self.extra_rects[i]
            if self.last_ops[i]=="send":
                pending_img=any(state.get(o,"have_image_rover%d"%i)>.5 and state.get(o,"received_image")<.5
                                for o in self._get(state,"objective"))
                pending_ana=any(state.get(o,"analyzed_rover%d"%i)>.5 and state.get(o,"received_analysis")<.5
                                for o in self._get(state,"sample"))
                if pending_img or pending_ana:
                    self.radio_idx[i]+=1; self.paths[i]=[]; self.targets[i]=None
            task,target=self._choose_task(state,i,pos)
            op=task if task in self.OPS else "noop"
            if task=="nav_sample" and math.dist(pos,target)<.34:
                # Nudge into the exact pickup disk while attempting the operator;
                # this is especially important for samples beside the divider.
                op="sample"
                a[4*i]=max(-.04,min(.04,target[0]-pos[0]))
                a[4*i+1]=max(-.04,min(.04,target[1]-pos[1]))
                task="near_sample"
            if task.startswith("nav") or task=="home":
                key=(task,round(target[0],2),round(target[1],2))
                if self.targets[i]!=key or not self.paths[i] or self.stalls[i]>=2:
                    if task=="nav_sample":
                        goals=self._candidates(state,target,.24,False)+[target]; tolerance=.09
                    else:
                        goals=[target]; tolerance=.15
                    self.paths[i]=self._astar(pos,goals,rects,tolerance)
                    self.targets[i]=key; self.stalls[i]=0
                    if not self.paths[i] and task!="nav_sample" and self._free(target,rects):
                        self.paths[i]=[target]
                while self.paths[i] and math.dist(pos,self.paths[i][0])<.05: self.paths[i].pop(0)
                if self.paths[i]:
                    wp=self.paths[i][0]
                    a[4*i]=max(-.2,min(.2,wp[0]-pos[0])); a[4*i+1]=max(-.2,min(.2,wp[1]-pos[1]))
            a[4*i+3]=self.OPS[op]
            moved=math.dist(pos,self.lastpos[i])>.03
            self.stalls[i]=0 if moved or (abs(a[4*i])+abs(a[4*i+1])<.01) else self.stalls[i]+1
            self.lastpos[i]=pos
            self.last_ops[i]=op
            self.last_motion[i]=(pos[0]+float(a[4*i]),pos[1]+float(a[4*i+1])) if abs(a[4*i])+abs(a[4*i+1])>.01 else None
        return a
