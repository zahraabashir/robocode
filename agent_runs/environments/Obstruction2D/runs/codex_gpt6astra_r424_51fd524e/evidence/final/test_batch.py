from env_client import make_env
from approach import GeneratedApproach
import sys,time,json,concurrent.futures
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
n=int(sys.argv[2]) if len(sys.argv)>2 else 100
count=int(sys.argv[3]) if len(sys.argv)>3 else None

def run(seed):
 e=make_env()
 try:
  s,i=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
  p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
  st=time.time();trace=[];policy_seconds=0.0
  for t in range(e.max_steps):
   tick=time.perf_counter();a=p.get_action(s);policy_seconds+=time.perf_counter()-tick
   s,r,d,tr,i=e.step(a)
   if t%40==0:trace.append([t,p.phase,p.obj.name if p.obj else '',round(s.get(p.robot,'x'),4),round(s.get(p.robot,'y'),4)])
   if d or tr:break
  out=dict(seed=seed,count=count,done=d,steps=t+1,seconds=round(time.time()-st,3),policy_seconds=round(policy_seconds,4))
  if not d:out['trace']=trace[-4:];out['state']={o.name:{f:s.get(o,f) for f in ('x','y','width','height')} for o in s.get_objects(p.ot)}
  print(seed, "OK" if d else "FAIL", t+1, flush=True)
  if not d:print(out,flush=True)
  return out
 except Exception as ex:return dict(seed=seed,count=count,error=str(ex))
 finally:e.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 results=list(ex.map(run,range(start,start+n)))
for r in results:
 if not r.get('done'):print(r)
print('SUMMARY',len(results),'success',sum(r.get('done',False) for r in results),'mean_steps',round(sum(r.get('steps',0) for r in results)/len(results),2),'max_time',max(r.get('seconds',0) for r in results),flush=True)
json.dump(results,open('results_%s_%s_%s.json'%(start,n,count),'w'))
