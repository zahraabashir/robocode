import math, json, sys
seed=int(sys.argv[1]); out=[]
for b,Dfar,Dnear in [(0,1.6,0.75),(15,1.65,0.75),(30,1.85,0.8),(45,2.3,0.75),(60,3.2,0.6),(75,3.9,0.55),(90,4.0,0.5),(105,2.0,0.55),(120,0.9,0.6)]:
    c,s=math.cos(math.radians(b)),math.sin(math.radians(b))
    # rover centre such that camera(theta=0) on ray: camera = rover + (-0.0866,-0.0122)
    f=lambda D:[round(-1.9+D*c+0.0866,3),round(-2.0+D*s+0.0122,3)]
    out.append({"seed":seed,"rover":"rover1","path":[f(Dfar),f(Dnear)],"park":[1.5,0.3],"h":0.1,"pre":[[-0.6,-1.0],[f(Dfar)[0],-1.0]]})
print('\n'.join(json.dumps(o) for o in out))
