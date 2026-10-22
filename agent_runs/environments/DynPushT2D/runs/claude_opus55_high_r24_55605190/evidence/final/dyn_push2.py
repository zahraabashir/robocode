from dyn_push import *
print('--- side push +x on stem left face (x=-w/2) at various y')
for y in [-0.2,-0.5,-0.8,-1.1]:
    out,e=push(0,[-0.8,y],[1,0],0.01,8)
    cb,tw=out[5]
    icr=np.array([-tw[1]/tw[2], tw[0]/tw[2]]) if abs(tw[2])>1e-9 else None
    print(f'y={y} pusher_b={cb} twist={tw} icr={icr}', 'c2=',None if icr is None else -icr[1]*cb[1])
print('--- side push on bar end (x=+L/2) moving -x at y=-0.065')
out,e=push(0,[1.0,-0.065],[-1,0],0.01,8)
cb,tw=out[5]; print(cb,tw)
print('--- oblique push at top center, angle a from normal')
for a in [10,20,30,45,60]:
    ar=np.radians(a)
    out,e=push(0,[0.0,0.6],[np.sin(ar),-np.cos(ar)],0.01,10)
    cb0=out[1][0]; cb1=out[-1][0]
    tws=np.array([t for _,t in out[1:]])
    print(f'a={a} pusher body x drift {cb1[0]-cb0[0]:.4f} over {len(out)-2} steps; mean twist {tws.mean(0)}')
