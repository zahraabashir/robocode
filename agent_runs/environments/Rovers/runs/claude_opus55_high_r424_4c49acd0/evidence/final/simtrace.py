import json, sys
from offline import FakeState
import approach
from approach import parse
S=json.load(open('states_0_200.json'))
seed=sys.argv[1]; st=S[seed]
ap=approach.GeneratedApproach(None,None,{})
ap.reset(FakeState(st['objs']), st['info'])
print(ap.orders, ap.plan_cost)
d=parse(FakeState(st['objs'])); ap._pred_cache=None
names={-5/6:'sample',-0.5:'cal',-1/6:'img',0:'-',0.5:'send',5/6:'drop'}
for t in range(int(sys.argv[2]) if len(sys.argv)>2 else 40):
    a=ap._policy(d)
    line=[]
    for k,r in enumerate(ap.rovers):
        ro=d['rover'][r]
        op=min(names.items(), key=lambda kv: abs(kv[0]-a[4*k+3]))[1]
        line.append(f"{r}({ro['x']:.2f},{ro['y']:.2f})+({a[4*k]:.2f},{a[4*k+1]:.2f}) {op} c{int(ro['calibrated'])}s{int(ro['store_full'])}h{int(ro['at_home'])}")
    print(t,' | '.join(line))
    d=ap._model_step(d,a); d['_t']=t+1
    if ap._goal(d): print('GOAL', t+1); break
