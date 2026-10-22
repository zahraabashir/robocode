import argparse, importlib, json, time
from env_client import make_env
p=argparse.ArgumentParser();p.add_argument('variant');p.add_argument('--start',type=int,default=0);p.add_argument('--count',type=int,default=20);a=p.parse_args()
Policy=importlib.import_module(a.variant).GeneratedApproach
results=[]
for seed in range(a.start,a.start+a.count):
 env=make_env();s,info=env.reset(seed=seed);policy=Policy(env.action_space,env.observation_space,{});policy.reset(s,info);start=time.monotonic();done=False
 for t in range(env.max_steps):
  s,r,done,trunc,info=env.step(policy.get_action(s))
  if done or trunc:break
 env.close();results.append({'seed':seed,'success':bool(done),'steps':t+1,'time':time.monotonic()-start})
 print(a.variant,seed,done,t+1,flush=True)
with open('results_%s_%s_%s.json'%(a.variant,a.start,a.count),'w') as f:json.dump(results,f)
print('SUMMARY',a.variant,'success',sum(x['success'] for x in results),'mean',sum(x['steps'] for x in results)/len(results),'max',max(x['steps'] for x in results),flush=True)
