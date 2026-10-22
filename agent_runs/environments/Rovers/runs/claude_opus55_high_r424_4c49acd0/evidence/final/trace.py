import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach, parse
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
print('orders', ap.orders, 'plan', ap.plan_cost)
names={-5/6:'sample',-0.5:'cal',-1/6:'img',0:'-',0.5:'send',5/6:'drop'}
def opn(v): return min(names.items(), key=lambda kv: abs(kv[0]-v))[1]
for k in range(200):
    d=parse(obs)
    a = ap.get_action(obs)
    obs, r, te, tr, info = env.step(a)
    d2=parse(obs)
    line=[]
    for i,rv in enumerate(['rover0','rover1']):
        p=d['rover'][rv]; q=d2['rover'][rv]
        moved = abs(q['x']-p['x']-a[4*i])<1e-4 and abs(q['y']-p['y']-a[4*i+1])<1e-4
        line.append(f"{rv}({p['x']:.2f},{p['y']:.2f})+({a[4*i]:.2f},{a[4*i+1]:.2f}){'' if moved else 'BLOCK'} {opn(a[4*i+3])} c{int(q['calibrated'])}s{int(q['store_full'])}")
    rec=sum(o['received_image'] for _,o in d2['objective']); ra=sum(s['received_analysis'] for _,s in d2['sample'])
    print(k, ' | '.join(line), f"recImg={rec:.0f} recAn={ra:.0f}")
    if te or tr: break
