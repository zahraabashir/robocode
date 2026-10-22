from geom_lib import *
P=Prober()
for seed in [22,16]:
    o=P.reset(seed); th=P.b0[2]; M=rot(th); c=P.b0[:2]
    print('seed',seed,'theta0',th)
    P.nav(c+M@np.array([0.45,-0.5]))
    ths=[]
    for k in range(200):
        P.step(M@np.array([0,1.0])*0.005); ths.append(P.obs[2])
    print('  theta traj', np.round(ths[40::8],4))
