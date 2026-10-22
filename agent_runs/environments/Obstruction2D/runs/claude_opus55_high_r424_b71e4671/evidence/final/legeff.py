import sys, math
from env_client import make_env
from approach import GeneratedApproach
env = make_env(); tot_a=tot_i=0
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed); ap.reset(obs, info)
    r=obs.get_object_from_name('robot')
    pos=(float(obs.get(r,'x')),float(obs.get(r,'y')))
    ideal=[]
    for L in ap.legs:
        t = L[3] if L[0]=='pick' else L[2]
        ideal.append(math.ceil(max(abs(t[0]-pos[0]),abs(t[1]-pos[1]))/0.05-1e-6)); pos=t
    counts=[0]*len(ap.legs)
    for _ in range(1000):
        li=min(ap.leg,len(counts)-1); a=ap.get_action(obs); counts[li]+=1
        obs,rr,te,tr,_=env.step(a)
        if te: break
    tot_a+=sum(counts); tot_i+=sum(ideal)
    print(seed, "actual", counts, "ideal", ideal, flush=True)
print("total actual", tot_a, "ideal", tot_i)
