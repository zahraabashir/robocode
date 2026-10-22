import json, numpy as np, collections
res=json.load(open('cor2_data.json'))
d=collections.defaultdict(list)
for r in res: d[r['name']].append(r)
for nm,rs in d.items():
    C=[];G=[];rate=[];drift=[];fails=0;cnt=[]
    for r in rs:
        cnt.append(r['contact'])
        if len(r['cors'])<3: fails+=1; continue
        c=np.median(np.array(r['cors']),0); C.append(c); G.append((r['Lh'],r['Lv'],r['w']))
        rate.append(r['dth']/max(r['travel'],1e-6))
        rl=np.array(r['rl']); t=np.array([-r['n'][1],r['n'][0]])
        drift.append((rl[-1]-rl[1])@t)
    C=np.array(C);G=np.array(G)
    if len(C)<3: print(nm,len(rs),'fails',fails); continue
    med=np.median(C,0); iqr=np.percentile(C,75,0)-np.percentile(C,25,0)
    A=np.c_[G,np.ones(len(G))]
    fit=[];r2=[]
    for k in range(2):
        co,*_=np.linalg.lstsq(A,C[:,k],rcond=None); pr=A@co
        r2.append(1-np.var(C[:,k]-pr)/max(np.var(C[:,k]),1e-9)); fit.append(co)
    print(f"{nm:7s} n={len(C):2d}/{len(rs)} fail={fails} COR med=({med[0]:+.3f},{med[1]:+.3f}) iqr=({iqr[0]:.3f},{iqr[1]:.3f}) rate={np.median(rate):+.2f} (iqr {np.percentile(rate,75)-np.percentile(rate,25):.2f}) drift={np.median(drift):+.3f} [{np.percentile(drift,25):+.3f},{np.percentile(drift,75):+.3f}] contact={np.median(cnt)}")
    for k,lab in enumerate('xy'):
        print(f"     c{lab} ~ {fit[k][0]:+.2f}Lh {fit[k][1]:+.2f}Lv {fit[k][2]:+.2f}w {fit[k][3]:+.3f}  R2={r2[k]:.2f}")
