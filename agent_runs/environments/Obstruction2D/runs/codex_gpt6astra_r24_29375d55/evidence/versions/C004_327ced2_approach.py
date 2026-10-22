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

    def select(self,s):
        bx,by,bw,bh=self.rect(s,self.block)
        sx,sy,sw,sh=self.rect(s,self.surface)
        obs=self.obstacles(s)
        lo,hi=sx+.002,sx+sw-bw-.002
        candidates=[lo,hi,(lo+hi)/2]
        for o in obs:
            x,y,w,h=self.rect(s,o)
            candidates += [max(lo,min(hi,x-bw-.006)),max(lo,min(hi,x+w+.006))]
        def blockers(x):
            return [o for o in obs if self.rect(s,o)[0]<x+bw+.004 and self.rect(s,o)[0]+self.rect(s,o)[2]>x-.004 and self.rect(s,o)[1]<sy+sh+bh+.01]
        gx=min(candidates,key=lambda x:(len(blockers(x)),abs(x-bx)))
        self.goal=(gx,sy+sh+.005)
        blocking=blockers(gx)
        if blocking:
            o=max(blocking,key=lambda o:self.rect(s,o)[1]+self.rect(s,o)[3])
            x,y,w,h=self.rect(s,o)
            occupied=[self.rect(s,p) for p in obs+[self.block] if p!=o]
            occupied.append([gx,sy+sh,bw,bh])
            places=[]
            for px in np.linspace(.11,1.50-w,90):
                py=.105
                for qx,qy,qw,qh in occupied:
                    if px<qx+qw+.018 and px+w>qx-.018:
                        py=max(py,qy+qh+.02)
                if py+h<.48 and not (px<gx+bw+.12 and px+w>gx-.12):
                    places.append((py*8+abs(px-x),float(px),py))
            if not places:
                for px in np.linspace(.11,1.50-w,90):
                    if px<gx+bw+.04 and px+w>gx-.04: continue
                    py=max([.105]+[qy+qh+.02 for qx,qy,qw,qh in occupied if px<qx+qw+.01 and px+w>qx-.01])
                    places.append((py*8+abs(px-x),float(px),py))
            if places:
                _,px,py=min(places)
                self.dest=(px,py)
            else:self.dest=(max(.01,gx-w-.05),.35)
        else:
            o=self.block
            self.dest=self.goal
        self.task=o
        x,y,w,h=self.rect(s,o)
        lower=max(.1002-x,.1002-self.dest[0],-.025)
        upper=min(1.5178-x,1.5178-self.dest[0],w+.025)
        offset=max(lower,min(upper,w/2))
        self.pickx=max(.1002,min(1.5178,x+offset))
        self.offsetx=self.pickx-x
        self.picktop=y+h
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
            ty=.86
            if abs(ry-ty)<.002:
                tx=self.pickx
                if abs(rx-tx)<.002:self.phase='down'
        if self.phase=='down':
            tx=self.pickx;ty=self.picktop+.215;vac=1.
            if (abs(rx-tx)<.002 and abs(ry-ty)<.002) or self.stuck>=2:
                self.phase='lift';self.before_y=y
        elif self.phase=='lift':
            vac=1.;ty=.86
            if y>self.before_y+.025:
                self.offsetx=rx-x;self.offsety=ry-y
            if abs(ry-ty)<.002:
                if y<self.before_y+.025:
                    self.phase='down';self.picktop-=.005
                else:self.phase='carry'
        elif self.phase=='carry':
            vac=1.;ty=.86;tx=self.dest[0]+self.offsetx
            if abs(rx-tx)<.002:self.phase='place'
        elif self.phase=='place':
            vac=1.;tx=self.dest[0]+self.offsetx;ty=self.dest[1]+self.offsety
            if abs(rx-tx)<.002 and abs(ry-ty)<.002:self.phase='release'
        elif self.phase=='release':
            vac=0.;self.phase='retreat'
        elif self.phase=='retreat':
            ty=.86
            if abs(ry-ty)<.002:self.phase='choose'
        delta=np.array([tx-rx,ty-ry,(-math.pi/2-theta+math.pi)%(2*math.pi)-math.pi,.2-arm,vac])
        return np.clip(delta,self.action_space.low,self.action_space.high).astype(np.float32)
