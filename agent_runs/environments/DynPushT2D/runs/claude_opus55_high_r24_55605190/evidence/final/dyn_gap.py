from dyn_lib import *
for s in [0.005,0.02,0.035,0.049]:
    e=E(0); e.goto_safe([0,0.1+s*3.5+1e-4]); o0=e.obs.copy(); dw=R(o0[2])@np.array([0,-1.0])
    rows=[]
    for k in range(8):
        ob=e.obs.copy(); o=e.step(dw*s)
        rows.append((to_body(ob,ob[16:18])[1]-0.1, R(ob[2]).T@(o[0:2]-ob[0:2])))
    print('step',s,' '.join(f'[gap {g:.4f} dy {d[1]:.4f}]' for g,d in rows))
    # then change step size to s/2 and 0
    for s2 in [s/2,0.0,s]:
        ob=e.obs.copy(); o=e.step(dw*s2); print('   next step',s2,'dy',(R(ob[2]).T@(o[0:2]-ob[0:2]))[1].round(5),'gap after',(to_body(o,o[16:18])[1]-0.1).round(5))
