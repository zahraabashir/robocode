from plib import *
np.set_printoptions(precision=4, suppress=True, linewidth=200)
env=make_env()
res=[]
for seed in range(12):
    for name,start,dirn in [('bartop',(0,0.45),(0,-1)),('stemend',(0,-1.7),(0,1)),('barbot',(0.35,-0.5),(0,1)),
                            ('barend',(0.95,0),(-1,0)),('stemside',(0.45,-0.8),(-1,0)),('barbotL',(-0.35,-0.5),(0,1))]:
        obs,_=env.reset(seed=seed)
        pose=obs[0:3].copy(); w,Lh,Lv=obs[12:15]
        st=np.array(start,float)
        if name=='barend': st[0]=Lh/2+0.35
        if name=='stemend': st[1]=-Lv-0.5
        sw=to_world(pose,st)
        if sw.min()<0.15 or sw.max()>4.85: continue
        obs,ok=navigate(env,obs,sw)
        if not ok: print(seed,name,'nav fail'); continue
        dw=rot(pose[2])@np.array(dirn,float)
        c=None
        for k in range(300):
            prev=obs[16:18].copy()
            obs,*_=env.step(dw*0.002)
            if np.abs(obs[0:3]-pose).max()>1e-7:
                c=to_local(pose,prev); c2=to_local(pose,obs[16:18]); break
        if c is None: print(seed,name,'no contact'); continue
        print(seed,name,'w=%.4f Lh=%.4f Lv=%.4f'%(w,Lh,Lv),'contact local prev',c,'after',c2)
        res.append((seed,name,w,Lh,Lv,*c,*c2))
np.save('geom_res.npy',np.array([r[2:] for r in res]))
import json; json.dump([list(map(lambda x: x if isinstance(x,str) else float(x),r)) for r in res],open('geom_res.json','w'))
env.close()
