from pm_util import *
e=E(); seed=12
for s in [0.002,0.005,0.01,0.02,0.03,0.04,0.049]:
    for y0 in [0.2,0.2+s/3,0.2+2*s/3]:
        mv,obs,act=run_push(e,seed,[0,y0],[0,-1],s,int(0.2/s)+6)
        out=[]
        for i in range(1,len(obs)):
            b0=obs[i-1][0:3]; b1=obs[i][0:3]
            dl=R(b0[2]).T@(b1[0:2]-b0[0:2])
            g0=(R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]))[1]
            g1=(R(b1[2]).T@(obs[i][16:18]-b1[0:2]))[1]
            if g0-s<0.1+s: out.append(f"({g0:.4f}->{g0-s:.4f}: d={-dl[1]:.5f} g1={g1:.5f})")
        print(s, " ".join(out[:5]))
