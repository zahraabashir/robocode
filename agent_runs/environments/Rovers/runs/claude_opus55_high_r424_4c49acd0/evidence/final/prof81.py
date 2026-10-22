import json, cProfile, pstats, time
from offline import FakeState
from approach import GeneratedApproach
S=json.load(open('states_0_200.json'))
import sys; sd=sys.argv[1] if len(sys.argv)>1 else '81'; st=S[sd] if isinstance(S,dict) else S[int(sd)]
ap=GeneratedApproach(None,None,None)
t=time.time()
cProfile.run("ap.reset(FakeState(st['objs']), st['info'])",'p.out')
print('time',time.time()-t)
pstats.Stats('p.out').sort_stats('cumtime').print_stats(14)
