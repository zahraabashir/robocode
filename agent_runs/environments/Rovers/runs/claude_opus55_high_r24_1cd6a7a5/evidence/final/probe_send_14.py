exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
def one(p, th, r1=None):
    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
    if r1: goto(1,*r1)
    turn_to(0,th); goto(0,*p,tol=0.002); step(0,op='send')
    q=pos(0); dl=math.hypot(q[0]+1.9,q[1]+2.0); rel=(math.degrees(q[2]-math.atan2(-2-q[1],-1.9-q[0]))+180)%360-180
    print(np.round(q[:3],3),'dist',round(dl,3),'rel',round(rel),'recv',dump('sample')['sample3'][-1])
for th in [0.0, math.pi, math.pi/2]:
    one((1.0,-1.75),th); one((0.3,1.0),th); one((0.3,0.0),th); one((2.08,-1.5),th,(-1,-1)); one((1.5,1.2),th)
