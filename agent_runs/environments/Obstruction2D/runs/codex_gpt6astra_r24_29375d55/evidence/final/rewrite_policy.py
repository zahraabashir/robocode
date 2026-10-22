p='approach.py'
s=open(p).read()
a=s.index('    def select(self,s):');b=s.index('    def get_action(self, s):')
s=s[:a]+'''    @staticmethod
    def overlap(a,b,margin=.003):
        return a[0]<b[0]+b[2]+margin and a[0]+a[2]>b[0]-margin and a[1]<b[1]+b[3]+margin and a[1]+a[3]>b[1]-margin

    def conflicts(self,s,obj,x,y,offset,others):
        _,_,w,h=self.rect(s,obj)
        rx=x+offset;ry=y+h+.215
        gripper=(rx-.035,ry-.21,.07,.01)
        arm=(rx-.008,ry-.2,.016,.2)
        bad=[]
        for o in others:
            q=self.rect(s,o)
            dx=max(q[0]-rx,0,rx-q[0]-q[2])
            dy=max(q[1]-ry,0,ry-q[1]-q[3])
            if self.overlap((x,y,w,h),q) or self.overlap(gripper,q) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:
                bad.append(o)
        return bad

    def offsets(self,x,px,w):
        low=max(.1002-x,.1002-px,-.022)
        high=min(1.5178-x,1.5178-px,w+.022)
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
                bad=set(self.conflicts(s,self.block,gx,sy+sh+.005,offset,obs)+self.conflicts(s,self.block,bx,by,offset,obs))
                plans.append(((len(bad),abs(offset-bw/2)*.2+abs(gx-bx)*.01),gx,offset,bad))
        if not plans:
            gx=(lo+hi)/2;offset=max(.1002-bx,min(1.5178-gx,bw/2))
            plans=[((len(obs),0),gx,offset,set(obs))]
        _,gx,offset,bad=min(plans,key=lambda p:p[0])
        self.goal=(gx,sy+sh+.005)
        if not bad:
            o=self.block;self.dest=self.goal
        else:
            o=max(bad,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
            # A taller neighbour may block the selected object's top grasp.
            for _ in range(len(obs)+1):
                x,y,w,h=self.rect(s,o)
                others=[p for p in obs+[self.block] if p!=o]
                grasps=[]
                for off in self.offsets(x,x,w):
                    blocking=self.conflicts(s,o,x,y,off,others)
                    grasps.append((len(blocking),abs(off-w/2),off,blocking))
                best=min(grasps,key=lambda z:z[:2])
                if not best[0]:break
                taller=[p for p in best[3] if self.rect(s,p)[1]+self.rect(s,p)[3]>y+h+.001 and p!=self.block]
                if not taller:break
                o=max(taller,key=lambda p:self.rect(s,p)[1]+self.rect(s,p)[3])
            x,y,w,h=self.rect(s,o)
            others=[p for p in obs+[self.block] if p!=o]
            occupied=[self.rect(s,p) for p in others]
            places=[]
            for px in np.linspace(.105,1.513-w,75):
                if px<gx+bw+.13 and px+w>gx-.13:continue
                py=max([.105]+[qy+qh+.022 for qx,qy,qw,qh in occupied if px<qx+qw+.025 and px+w>qx-.025])
                if py+h>.43:continue
                for off in self.offsets(x,px,w):
                    blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
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
                    py=max([.105]+[qy+qh+.025 for qx,qy,qw,qh in occupied if px<qx+qw+.04 and px+w>qx-.04])
                    for off in self.offsets(x,px,w):
                        blockers=self.conflicts(s,o,x,y,off,others)+self.conflicts(s,o,px,py,off,others)
                        fallback.append((len(blockers),py*8+abs(px-x),float(px),py,off))
                _,_,px,py,offset=min(fallback)
                self.dest=(px,py)
        self.task=o
        x,y,w,h=self.rect(s,o)
        self.pickx=max(.1002,min(1.5178,x+offset))
        self.offsetx=self.pickx-x
        self.picktop=y+h
        self.phase='above'
        self.stuck=0

'''+s[b:]
# Delay vacuum until final descent, avoiding early grasp and floor collision.
s=s.replace("tx=self.pickx;ty=self.picktop+.215;vac=1.","tx=self.pickx;ty=self.picktop+.215;vac=0.")
s=s.replace("self.phase='lift';self.before_y=y","self.phase='lift';self.before_y=y;vac=1.")
open(p,'w').write(s)
