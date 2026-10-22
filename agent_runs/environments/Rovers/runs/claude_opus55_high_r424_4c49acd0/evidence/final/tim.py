import json, time, sys
from offline import FakeState
from approach import GeneratedApproach
S=json.load(open('states_0_200.json'))
for sd in sys.argv[1:]:
    st=S[sd] if isinstance(S,dict) else S[int(sd)]
    ap=GeneratedApproach(None,None,None)
    t=time.time(); ap.reset(FakeState(st['objs']), st['info']); print(sd,'time',round(time.time()-t,2), ap.plan_cost, flush=True)
