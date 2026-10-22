import json,sys
S=int(sys.argv[1])
for x,y in [(0.4,-0.3),(1.0,0.0),(0.5,0.5),(1.5,-0.6),(0.8,1.0),(1.6,0.2)]:
    print(json.dumps({"seed":S,"rover":"rover0","path":[[x,y],[x+0.01,y]],"park":[-0.6,0.3],"h":0.01,"pre":[[1.0,-1.0],[x,-1.0]]}))
for x,y in [(-1.65,0.5),(-1.7,-0.5),(-2.05,-1.0),(-2.3,-1.2)]:
    print(json.dumps({"seed":S,"rover":"rover1","path":[[x,y],[x+0.01,y]],"park":[1.5,0.3],"h":0.01,"pre":[[-0.6,-1.0],[-0.6,y]]}))
