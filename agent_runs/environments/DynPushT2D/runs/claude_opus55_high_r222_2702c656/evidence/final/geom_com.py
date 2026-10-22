from geom_probe import *
for s in [12,19,24]:
    o,_=env.reset(seed=s); w,Lh,Lv=o[12:15]
    yc=(Lh*(-w/2)+Lv*(-w-Lv/2))/(Lh+Lv)
    out=[]
    for y in np.linspace(yc-0.06,yc+0.06,7):
        loc,res=probe(s,(0.5,y),(-1,0))
        out.append((round(y-yc,3),float(np.sign(res[2])) if loc is not None else res))
    print(s,"centroid y",round(yc,4),out)
