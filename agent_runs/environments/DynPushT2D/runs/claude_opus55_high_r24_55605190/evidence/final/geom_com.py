from geom_lib import *
P=Prober()
for seed in [12,24]:
    o=P.reset(seed); w,Lh,Lv=o[12:15]
    Ab,As=Lh*w,w*Lv; yc=(Ab*(-w/2)+As*(-w-Lv/2))/(Ab+As)
    print('seed',seed,'area centroid y=%.4f'%yc, 'bar-center y=%.4f'%(-w/2), 'stem-mid y=%.4f'%(-w-Lv/2))
    for y in [-0.05,-0.15,-0.25,-0.3,-0.35,-0.4,-0.45,-0.55,-0.7]:
        sx = -1.0 if y<-w else -0.9
        P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
        P.nav(c+M@np.array([sx,y]))
        d=M@np.array([1.0,0])
        for k in range(int((abs(sx)+0.15)/0.005)): P.step(d*0.005)
        db=P.obs[0:3]-P.b0
        print('  push y=%.2f dtheta=%+.5f dpos_body=%s'%(y,db[2],np.round(M.T@db[:2],4)))
