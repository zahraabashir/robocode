from probe_ops_lib import *
for seed in range(30):
    reset(seed)
    pil=[get(n) for n in names('obstacle') if get(n)[3]<0.1]
    for on in names('objective'):
        ox,oy=get(on)[:2]
        for p in pil:
            dd=math.hypot(p[0]-ox,p[1]-oy)
            if 0.5<dd<1.3 and p[0]*ox>0:
                ux,uy=(p[0]-ox)/dd,(p[1]-oy)/dd
                tx,ty=ox+1.8*ux,oy+1.8*uy
                if abs(tx)>0.4 and tx*ox>0 and abs(ty)<2.2 and abs(tx)<2.2:
                    print(seed,on,(round(ox,2),round(oy,2)),'pillar',(round(p[0],2),round(p[1],2)),'d',round(dd,2),'target',(round(tx,2),round(ty,2)))
