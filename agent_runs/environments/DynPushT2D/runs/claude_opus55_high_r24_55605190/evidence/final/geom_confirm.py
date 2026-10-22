from geom_lib import *
import sys
P=Prober()
for seed in [20,31,24]:
    o=P.reset(seed); w,Lh,Lv=o[12:15]; r=o[28]
    print('seed',seed,'w %.4f Lh %.4f Lv %.4f'%(w,Lh,Lv))
    probes={'top(y=0)':((0.2,1.0),(0,-1),1,0.0),
            'bar_bottom(y=-w)':((0.35,-1.0),(0,1),1,-w),
            'bar_end_right(x=Lh/2)':((1.2,-w/2),(-1,0),0,Lh/2),
            'bar_end_left(x=-Lh/2)':((-1.2,-w/2),(1,0),0,-Lh/2),
            'stem_right(x=w/2)':((1.0,-0.7),(-1,0),0,w/2),
            'stem_left(x=-w/2)':((-1.0,-0.7),(1,0),0,-w/2),
            'stem_tip(y=-w-Lv)':((0.0,-1.55),(0,1),1,-w-Lv)}
    for name,(s,d,ax,pred) in probes.items():
        res,msg=P.probe(seed,np.array(s),np.array(d,float))
        if res is None: print(name,msg); continue
        surf=res[1][ax]-r*np.array(d)[ax]
        print('  %-24s surface=%.4f predicted=%.4f err=%.5f'%(name,surf,pred,surf-pred))
