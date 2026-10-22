import json
from offline import FakeState
import approach, numpy as np
S=json.load(open('states_0_200.json')); st=S['0']
ap=approach.GeneratedApproach(None,None,{})
ap.reset(FakeState(st['objs']), st['info'])
for r in ap.rovers:
    G=ap.fields[r]['G']; i,j=approach.to_cell(*ap.home[r][:2])
    for L in sorted(G): print(r, L, G[L][i,j], (G[L]<1e8).sum())
    break
