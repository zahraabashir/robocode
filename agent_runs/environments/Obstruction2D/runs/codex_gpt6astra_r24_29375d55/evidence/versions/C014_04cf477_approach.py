import math
import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.types = {t.name: t for t in observation_space.types}

    def reset(self, state, info):
        self.robot = next(iter(state.get_objects(self.types['crv_robot'])))
        self.block = next(iter(state.get_objects(self.types['target_block'])))
        self.surface = next(iter(state.get_objects(self.types['target_surface'])))
        self.phase = 'choose'
        self.task = None
        self.steps = 0
        self.stuck = 0
        self.last = None

    def rect(self, s, o):
        return [float(s.get(o,f)) for f in ('x','y','width','height')]

    def obstacles(self,s):
        return [o for o in s.get_objects(self.types['rectangle']) if o != self.surface and o != self.block and not s.get(o,'static')]

    @staticmethod
    def overlap(a,b,margin=.003):
        return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin

    def hits_configuration(self,q,x,y,w,h,offset,body_margin=.003):
        rx=x+offset;ry=y+h+.215
        dx=max(q[0]-rx,0,rx-q[0]-q[2])
        dy=max(q[1]-ry,0,ry-q[1]-q[3])
        return (self.overlap((x,y,w,h),q,margin=body_margin)
                or self.overlap((rx-.035,ry-.21,.07,.01),q,margin=.014)
                or self.overlap((rx-.008,ry-.2,.016,.2),q)
                or dx*dx+dy*dy<.103**2)

    def conflicts(self,s,obj,x,y,offset,others,pickup=False):
        _,_,w,h=self.rect(s,obj)
        bad=[]
        for o in others:
            q=self.rect(s,o)
            overhead=pickup and q[1]>=y+h-.001 and q[0]<x+w+.001 and q[0]+q[2]>x-.001
            if overhead or self.hits_configuration(q,x,y,w,h,offset,body_margin=.00001 if pickup else .003):
                bad.append(o)
        return bad

    def offsets(self,x,px,w):
        low=max(.1002-x,.1002-px,-.034)
        high=min(1.5178-x,1.5178-px,w+.034)
        if low>high:return []
        return sorted(set([max(low,min(high,w/2))]+[float(z) for z in np.linspace(low,high,7)]),key=lambda z:abs(z-w/2))

    def select(self,s):
        bx,by,bw,bh=self.rect(s,self.block)
        sx,sy,sw,sh=self.rect(s,self.surface)
        obs=self.obstacles(s)
        lo,hi=sx+.002,sx+sw-bw-.002
        candidates=[lo,hi,(lo+hi)/2]
        for o in obs:
            x,y,w,h=self.rect(s,o)
            candidates += [max(lo,min(hi,x-bw-.007)),max(lo,min(hi,x+w+.007))]
        plans=[]
        for gx in candidates:
            for offset in self.offsets(bx,gx,bw):
                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs,True))
                plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
        if not plans:
            gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
            plans=[((len(obs),0),gx,offset,set(obs))]
        _,gx,offset,bad=min(plans,key=lambda p:p[0])
        self.goal=(gx,sy+sh+.005)
        keep_pick=(bx,by,bw,bh,offset)
        keep_place=(gx,sy+sh+.005,bw,bh,offset)
        if not bad:
            o=self.block;self.dest=self.goal
        else:
            o=max(bad,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
            # Clear dependencies of an exclusive vacuum grasp, including shorter
            # neighbours. Track visited tasks to avoid dependency cycles.
            visited=set()
            for _ in range(len(obs)+2):
                visited.add(o)
                x,y,w,h=self.rect(s,o)
                others=[p for p in obs+[self.block] if p!=o]
                grasps=[]
                for off in self.offsets(x,x,w):
                    blocking=self.conflicts(s,o,x,y,off,others,True)
                    grasps.append((len(blocking),abs(off-w/2),off,blocking))
                best=min(grasps,key=lambda z:z[:2])
                if not best[0]:break
                dependencies=set(p for grasp in grasps for p in grasp[3] if p not in visited)
                if not dependencies:break
                def access_cost(p):
                    qx,qy,qw,qh=self.rect(s,p)
                    rest=[q for q in obs+[self.block] if q!=p]
                    scores=[len(self.conflicts(s,p,qx,qy,z,rest,True)) for z in self.offsets(qx,qx,qw)]
                    return (min(scores) if scores else 999,p==self.block,-qy-qh)
                o=min(dependencies,key=access_cost)
            x,y,w,h=self.rect(s,o)
            others=[p for p in obs+[self.block] if p!=o]
            occupied=[self.rect(s,p) for p in others]
            places=[]
            for px in np.linspace(.105,1.513-w,75):
                if px<gx+bw+.13 and px+w>gx-.13:continue
                if px<bx+bw+.008 and px+w>bx-.008:continue
                py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
                if py+h>.43:continue
                if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
                for off in self.offsets(x,px,w):
                    blockers=self.conflicts(s,o,x,y,off,others,True)+self.conflicts(s,o,px,py,off,others)
                    if not blockers:
                        places.append((py*8+abs(px-x)+abs(off-w/2)*.2,float(px),py,off))
            if places:
                _,px,py,offset=min(places)
                self.dest=(px,py)
            else:
                # If floor space is scarce, park above the lowest nearby stack.
                fallback=[]
                for px in np.linspace(.105,1.513-w,75):
                    if px<gx+bw+.07 and px+w>gx-.07:continue
                    if px<bx+bw+.008 and px+w>bx-.008:continue
                    py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
                    if self.hits_configuration((px,py,w,h),*keep_pick) or self.hits_configuration((px,py,w,h),*keep_place):continue
                    for off in self.offsets(x,px,w):
                        blockers=self.conflicts(s,o,x,y,off,others,True)+self.conflicts(s,o,px,py,off,others)
                        fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
                _,_,px,py,offset=min(fallback)
                self.dest=(px,py)
        self.task=o
        x,y,w,h=self.rect(s,o)
        self.pickx=max(.1002,min(1.5178,x+offset))
        self.offsetx=self.pickx-x
        self.picktop=y+h
        rx=float(s.get(self.robot,'x'))
        self.empty_cruise=max([.34]+[qy+qh+.235 for p in obs+[self.block] for qx,qy,qw,qh in [self.rect(s,p)] if qx<max(rx,self.pickx)+.11 and qx+qw>min(rx,self.pickx)-.11])
        self.empty_cruise=min(.86,self.empty_cruise)
        self.carry_cruise=.86
        self.phase='above'
        self.stuck=0

    def get_action(self, s):
        self.steps+=1
        r=self.robot
        rx,ry=float(s.get(r,'x')),float(s.get(r,'y'))
        theta=float(s.get(r,'theta'))
        arm=float(s.get(r,'arm_joint'))
        pose=(rx,ry)
        oldphase=self.phase
        self.stuck=self.stuck+1 if self.last==(pose,oldphase) else 0
        self.last=(pose,oldphase)
        if self.phase=='choose':self.select(s)
        x,y,w,h=self.rect(s,self.task)
        vac=0.
        tx,ty=rx,ry
        if self.phase=='above':
            ty=self.empty_cruise
            if ry>=ty-.002:
                tx=self.pickx
                if abs(rx-tx)<.002:self.phase='down'
        if self.phase=='down':
            tx=self.pickx;ty=self.picktop+.215;vac=0.
            if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
                self.phase='lift';self.before_y=y;vac=1.
                self.offsety=ry-y;self.offsetx=rx-x
                left=min(x,self.dest[0])-.11;right=max(x+w,self.dest[0]+w)+.11
                tops=[qy+qh for p in self.obstacles(s)+[self.block] if p!=self.task for qx,qy,qw,qh in [self.rect(s,p)] if qx<right and qx+qw>left]
                self.carry_cruise=min(.88,max([y+.06]+tops)+self.offsety+.026)
        elif self.phase=='lift':
            vac=1.;ty=self.carry_cruise
            if y>self.before_y+.025:
                self.offsetx=rx-x;self.offsety=ry-y
            if abs(ry-ty)<.002:
                if y<self.before_y+.025:
                    self.phase='down';self.picktop-=.005
                else:self.phase='carry'
        elif self.phase=='carry':
            vac=1.;ty=self.carry_cruise;tx=self.dest[0]+self.offsetx
            if abs(rx-tx)<.002:self.phase='place'
        elif self.phase=='place':
            vac=1.;tx=self.dest[0]+self.offsetx;ty=self.dest[1]+self.offsety
            if abs(rx-tx)<.002 and abs(ry-ty)<.002:self.phase='release'
        elif self.phase=='release':
            vac=0.;self.phase='choose'
        elif self.phase=='retreat':
            ty=.86
            if abs(ry-ty)<.002:self.phase='choose'
        delta=np.array([tx-rx,ty-ry,(-math.pi/2-theta+math.pi)%(2*math.pi)-math.pi,.2-arm,vac])
        return np.clip(delta,self.action_space.low,self.action_space.high).astype(np.float32)
