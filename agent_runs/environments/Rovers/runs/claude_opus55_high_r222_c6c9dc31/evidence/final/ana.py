import sys, json, math
# summarise: for each run, list last fail & first success positions (post-move camera)
th={'rover0':math.pi,'rover1':0.0}
def cam(r,x,y):
    t=th[r]+math.radians(188); return x+0.0875*math.cos(t), y+0.0875*math.sin(t)
for f in sys.argv[1:]:
    for L in open(f):
        if not L.startswith("{"): continue
        d=json.loads(L); a=d['args']; res=[r for r in d['res'] if r[0]!='start']
        if not res: print(a['seed'],a['rover'],a['path'],'NO SENDS', d['res']); continue
        fails=[r for r in res if r[2] is False]; succ=[r for r in res if r[2] is True]
        def fm(r):
            cx,cy=cam(a['rover'],*r[1]); D=math.hypot(cx+1.9,cy+2.0); b=math.degrees(math.atan2(cy+2.0,cx+1.9))
            return f"pre({r[0][0]:.2f},{r[0][1]:.2f})post({r[1][0]:.2f},{r[1][1]:.2f}) D={D:.2f} brg={b:.1f}"
        print(a['seed'],a['rover'],a['path'],'n=',len(res),'| firstfail',fm(fails[0]) if fails else '-','| lastfail', fm(fails[-1]) if fails else '-', '| succ', fm(succ[0]) if succ else '-')
